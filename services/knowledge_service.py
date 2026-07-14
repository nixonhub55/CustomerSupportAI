from database.ai_db import search_knowledge_by_keywords
from services.search_service import extract_keywords


def get_knowledge(question):

    keywords = extract_keywords(question)

    articles = search_knowledge_by_keywords(keywords)

    knowledge = ""

    for article in articles[:3]:

        knowledge += f"""
Title:
{article['title']}

Content:
{article['content']}

--------------------------------

"""

    return knowledge