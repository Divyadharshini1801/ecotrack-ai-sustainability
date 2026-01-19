def get_response(query):
    """
    Simulated RAG-based response system.
    In a real deployment, this would retrieve data from
    municipal waste guidelines and sustainability documents.
    """

    waste_knowledge = {
        "battery": "Batteries should be disposed of at authorized e-waste collection centers.",
        "plastic": "Clean plastic waste should be placed in dry waste recycling bins.",
        "food": "Food waste should be disposed of in biodegradable or compost bins.",
        "electronics": "Electronic waste must be given to certified e-waste recyclers."
    }

    for key in waste_knowledge:
        if key in query.lower():
            return waste_knowledge[key]

    return (
        "Please segregate waste into dry, wet, and hazardous categories. "
        "Refer to local municipal guidelines for detailed disposal instructions."
    )
