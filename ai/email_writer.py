from ai.model_manager import generate

def write_email(context, tone="Professional", language="English"):
    prompt = f"""
Write a business email.

Tone: {tone}
Language: {language}
Context:
{context}

Return:
1. Subject
2. Email body
"""
    return generate(prompt)
