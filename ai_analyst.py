def get_ai_insights(findings):
    """Simulates an AI Agent explaining the technical risk."""
    knowledge_base = {
        "HSTS Missing": "AI Analysis: Protocol downgrade risk. Recommendation: Force HTTPS.",
        "X-Frame-Options Missing": "AI Analysis: Clickjacking risk. Recommendation: Set X-Frame-Options to 'DENY'."
    }
    
    return [knowledge_base.get(issue, "Unknown risk.") for issue in findings]