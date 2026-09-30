from ai.model_manager import generate

def analyze_business(summary):
    return generate(
        "Analyze this authorized company business summary and give concise "
        "operational insights, risks and next actions:\n" + summary
    )
