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
    Dynamically finds an available model and generates a response using Google Gemini REST API.
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
    
    # Step 1: Automatically list models to find a valid one for this key
    list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    available_model = "gemini-1.5-flash"  # default fallback
    
    try:
        req_list = urllib.request.Request(list_url, method="GET")
        with urllib.request.urlopen(req_list) as resp:
            models_data = json.loads(resp.read().decode("utf-8"))
            for m in models_data.get("models", []):
                methods = m.get("supportedGenerationMethods", [])
                if "generateContent" in methods:
                    name = m.get("name", "")
                    if name:
                        available_model = name.replace("models/", "")
                        break
    except Exception:
        pass

    # Step 2: Generate content using the discovered model
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{available_model}:generateContent?key={api_key}"
    
    full_text = f"{system}\n\n{prompt}"
    payload = {
        "contents": [{
            "parts": [{"text": full_text}]
        }]
    }
    
    data = json.dumps(payload).encode("utf-8")
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
        return f"AI Generation Error (HTTP {e.code}): {error_body}"
    except Exception as e:
        return f"AI Generation Error: {str(e)}"
