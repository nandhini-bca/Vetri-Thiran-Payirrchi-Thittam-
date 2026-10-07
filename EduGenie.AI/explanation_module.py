def explain_concept(text: str) -> str:
    """Generate a clear explanation for a concept or topic."""
    cleaned = (text or '').strip()
    if not cleaned:
        return "Please provide a concept or topic to explain."

    return (
        f"Here is a simple explanation of '{cleaned}':\n\n"
        "Start with the core idea, then connect it to a real-world example. "
        "Break the topic into smaller parts so each part is easier to understand. "
        "Finally, test yourself by explaining it in your own words and solving a few practice questions."
    )
