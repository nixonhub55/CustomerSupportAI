from core.logger import Logger


class ToolMatcher:

    def __init__(self, registry):

        self.registry = registry

    # -----------------------------------------------------

    def match(self, question):

        question = question.lower()

        matches = []

        for tool in self.registry.tools.values():

            score = 0

            keywords = getattr(tool, "KEYWORDS", [])

            for keyword in keywords:

                if keyword.lower() in question:

                    score += 1

            if score > 0:

                matches.append({

                    "tool": tool,

                    "score": score

                })

        matches.sort(

            key=lambda item: item["score"],

            reverse=True

        )

        Logger.debug(
            f"ToolMatcher: {[m['tool'].NAME for m in matches]}"
        )

        return matches