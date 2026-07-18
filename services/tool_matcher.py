from core.logger import Logger


class ToolMatcher:

    def __init__(self, registry):
        self.registry = registry

    # -------------------------------------------------

    def match(self, question):

        question = question.lower()

        matched = []

        for metadata in self.registry.metadata():

            keywords = metadata.get("keywords", [])

            for keyword in keywords:

                if keyword.lower() in question:

                    Logger.debug(
                        f"Matched tool '{metadata['name']}' "
                        f"using keyword '{keyword}'"
                    )

                    matched.append(metadata["name"])

                    break

        return matched