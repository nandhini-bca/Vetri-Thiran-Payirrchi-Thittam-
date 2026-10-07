def generate_quiz(text: str):
    """Create a simple quiz from the provided text."""
    cleaned = (text or '').strip()
    if not cleaned:
        return []

    return [
        {
            "question": f"What is the main idea of '{cleaned[:80]}'?",
            "options": [
                "The central concept or theme",
                "A random unrelated detail",
                "A summary of the final answer only",
                "The same information repeated twice"
            ],
            "answer": "The central concept or theme"
        },
        {
            "question": "Which strategy makes a topic easier to learn?",
            "options": [
                "Breaking it into smaller parts",
                "Ignoring examples",
                "Memorizing without understanding",
                "Skipping practice"
            ],
            "answer": "Breaking it into smaller parts"
        },
        {
            "question": "Why are examples useful in learning?",
            "options": [
                "They connect theory to real life",
                "They make the topic harder",
                "They replace the need to study",
                "They are only for entertainment"
            ],
            "answer": "They connect theory to real life"
        }
    ]
