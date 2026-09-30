import os

def local_model_available():
    # This starter does not require a paid API.
    # Add an Ollama/local model integration here when installed.
    return bool(os.getenv("OLLAMA_HOST"))

def generate(prompt, system="You are a helpful business assistant."):
    """
    Local AI adapter placeholder.
    Recommended production pattern:
    Streamlit -> AI service adapter -> local/open-source model.
    """
    return (
        "AI adapter is ready for a local/open-source model. "
        "Connect Ollama or another approved model provider in ai/model_manager.py.\n\n"
        f"Requested task:\n{prompt}"
    )
