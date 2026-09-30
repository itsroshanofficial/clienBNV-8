from ai.model_manager import generate

def translate(text, target_language):
    return generate(
        f"Translate the following business message to {target_language}. "
        f"Preserve meaning and professional tone:\n{text}"
    )
