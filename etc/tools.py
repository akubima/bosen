def limit_text(text, max_length=30):
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text