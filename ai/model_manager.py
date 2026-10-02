import os
import streamlit as st
import json
import urllib.request
import urllib.error

def local_model_available():
    """Checks if Google Gemini API key is configured."""
    try:
        return bool(st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY"))
    except Exception:
        return bool(os.getenv("GEMINI_API_KEY"))

def generate(prompt, system="You are a helpful business assistant."):
    """
    Generates a response with automatic model fallback to handle high demand (503).
    """
    try:
        api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    except Exception:
        api_key = os.getenv("GEMINI_API_KEY")
        
    if not api_key:
        return (
            "Error: GEMINI_API_KEY is not configured in .streamlit/secrets.toml. "
            "Please add your API key to enable AI features."
        )
    
    # Models ki list jo try ki jaye gi agar aik busy ho
    models_to_try = ["gemini-1.5-flash", "gemini-pro", "gemini-3.8-flash"]
    
    full_text = f"{system}\n\n{prompt}"
    payload = {
        "contents": [{
            "parts": [{"text": full_text}]
        }]
    }
    data = json.dumps(payload).encode("utf-8")
    
    last_error = ""
    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
        
        try:
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                candidate = res_data.get("candidates", [])[0]
                content = candidate.get("content", {})
                parts = content.get("parts", [])[0]
                return parts.get("text", "No response text found.")
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            last_error = f"HTTP {e.code}: {error_body}"
            continue  # Agla model try karega agar yeh busy hua
        except Exception as e:
            last_error = str(e)
            continue
            
    return f"AI Generation Error: All models are currently busy or unavailable. Details: {last_error}"
