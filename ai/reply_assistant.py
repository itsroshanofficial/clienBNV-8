from ai.model_manager import generate

CATEGORIES = [
    "Interested", "Not Interested", "Meeting Request",
    "More Information Required", "Follow-up Required",
    "Out of Office", "Unsubscribe"
]

def classify_reply(text):
    t = text.lower()
    if "unsubscribe" in t or "remove me" in t:
        return "Unsubscribe"
    if "meeting" in t or "call" in t:
        return "Meeting Request"
    if "interested" in t or "send details" in t:
        return "Interested"
    if "not interested" in t:
        return "Not Interested"
    if "out of office" in t:
        return "Out of Office"
    return "More Information Required"

def draft_reply(thread):
    return generate(
        f"Draft a concise professional reply to this business email thread:\n{thread}"
    )
