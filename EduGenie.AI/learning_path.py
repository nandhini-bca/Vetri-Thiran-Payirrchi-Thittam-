def get_learning_recommendations(topic: str, level: str = "beginner"):
    """Return a simple learning path for a topic."""
    cleaned_topic = (topic or '').strip()
    if not cleaned_topic:
        return []

    normalized_level = (level or 'beginner').strip().lower() or 'beginner'

    return [
        {
            "step": 1,
            "title": f"Learn the foundations of {cleaned_topic}",
            "description": f"Start with the basic definitions, key terms, and the overall purpose of {cleaned_topic}.",
            "difficulty": normalized_level
        },
        {
            "step": 2,
            "title": "Study examples and applications",
            "description": "Look at examples, diagrams, or short case studies to see how the idea is used in practice.",
            "difficulty": normalized_level
        },
        {
            "step": 3,
            "title": "Practice with exercises",
            "description": "Solve practice questions and attempt to explain the concept in your own words.",
            "difficulty": normalized_level
        }
    ]
