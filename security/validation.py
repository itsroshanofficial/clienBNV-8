import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def valid_email(value):
    return bool(value and EMAIL_RE.match(value.strip()))

def clean_text(value, max_length=2000):
    value = str(value or "").strip()
    return value[:max_length]

def safe_filename(name):
    return re.sub(r"[^a-zA-Z0-9._-]", "_", str(name))
