import os
import streamlit as st
import google.generativeai as genai

def local_model_available():
    """Checks if Google Gemini API key is configured."""
    try:
        return bool(st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY"))
    except Exception:
        return bool(os.getenv("GEMINI_API_KEY"))

def generate(prompt, system="You are a helpful business assistant."):
    """
    Generates a response using Google Gemini.
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
    
    try:
        genai.configure(api_key=api_key)
        
        # Yahan hum gemini-1.5-flash ya gemini-1.5-pro try karte hain
        for m_name in ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']:
            try:
                model = genai.GenerativeModel(m_name)
                full_prompt = f"{system}\n\n{prompt}"
                response = model.generate_content(full_prompt)
                if response and response.text:
                    return response.text
            except Exception:
                continue
                
        return "AI Generation Error: Could not connect with available models using this API key."
    except Exception as e:
        return f"AI Generation Error: {str(e)}"
