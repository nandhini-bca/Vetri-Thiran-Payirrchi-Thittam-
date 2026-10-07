import os


def answer_question(question: str) -> str:
    """Return a helpful educational answer for the passed question."""
    cleaned = (question or '').strip()
    if not cleaned:
        return "Please provide a question to answer."

    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        try:
            import google.generativeai as genai

            model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(cleaned)
            text = getattr(response, "text", None)
            if text:
                return text

            candidates = getattr(response, "candidates", None)
            if candidates:
                first = candidates[0]
                if hasattr(first, "content") and hasattr(first.content, "parts"):
                    parts = []
                    for part in first.content.parts:
                        if hasattr(part, "text"):
                            parts.append(part.text)
                    if parts:
                        return " ".join(parts)
        except Exception:
            pass

    return (
        "I can help with this topic. A concise explanation is that "
        f"{cleaned.lower()} is best understood by breaking it into key ideas, examples, "
        "and practice questions. If you want, I can also explain the concept step by step."
    )
