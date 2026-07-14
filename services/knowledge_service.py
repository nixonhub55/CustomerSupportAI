from database.repositories.knowledge_repository import KnowledgeRepository


class KnowledgeService:

    def __init__(self):

        self.repo = KnowledgeRepository()

    def search(self, question):

        words = question.lower().split()

        results = []

        seen = set()

        for word in words:

            rows = self.repo.search(word)

            for row in rows:

                if row["knowledge_id"] not in seen:

                    results.append(row)

                    seen.add(row["knowledge_id"])

        return results