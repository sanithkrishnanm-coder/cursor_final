from app.models.base_model import get_collection


def seed_default_careers():
    careers = get_collection("careers")
    if careers.count_documents({}) > 0:
        return
    careers.insert_many(
        [
            {
                "career_title": "Software Engineer",
                "description": "Build scalable software products using modern technologies.",
                "skills": ["Python", "JavaScript", "Data Structures"],
                "roadmap": ["Learn programming basics", "Build projects", "Contribute to open source"],
            },
            {
                "career_title": "Data Analyst",
                "description": "Transform raw data into insights and dashboards.",
                "skills": ["Excel", "SQL", "Data Visualization"],
                "roadmap": ["Statistics fundamentals", "Dashboard tools", "Portfolio projects"],
            },
        ]
    )
