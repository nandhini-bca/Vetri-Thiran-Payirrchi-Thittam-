def summarize_text(text: str) -> str:
    """Return a concise summary of the supplied text."""
    cleaned = (text or '').strip()
    if not cleaned:
        return "Please provide text to summarize."

    words = cleaned.split()
    if len(words) <= 30:
        return cleaned

    snippet = " ".join(words[:30])
    return snippet + "... (summary truncated for brevity)"
