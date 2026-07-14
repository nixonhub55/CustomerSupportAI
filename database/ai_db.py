import mariadb


def connect():

    return mariadb.connect(
        host="localhost",
        user="root",
        password="PfNgB@y@n",
        database="ai_db"
    )


def search_knowledge(category=None):

    conn = connect()

    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT
            knowledge_id,
            category,
            title,
            keywords,
            content
        FROM knowledge
        WHERE is_active = 1
    """

    params = []

    if category:
        sql += " AND category=?"
        params.append(category)

    sql += " ORDER BY priority DESC"

    cursor.execute(sql, params)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def search_knowledge_by_keywords(keywords):

    conn = connect()

    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT
            knowledge_id,
            title,
            content,
            keywords,
            category
        FROM knowledge
        WHERE is_active = 1
    """

    cursor.execute(sql)

    articles = cursor.fetchall()

    cursor.close()
    conn.close()

    results = []

    for article in articles:

        score = 0

        db_keywords = article["keywords"].lower().split(",")

        for keyword in keywords:

            if keyword.lower() in db_keywords:
                score += 1

        if score > 0:

            article["score"] = score

            results.append(article)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results

