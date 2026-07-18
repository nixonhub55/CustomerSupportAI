from core.logger import Logger


class ContextManager:

    def __init__(self, context):

        self.context = context

    def merge(self, entities):

        Logger.debug(
            "Merging conversation context..."
        )

        merged = dict(entities)

        for key, value in self.context.data.items():

            if key not in merged:

                merged[key] = value

        Logger.debug(
            f"Merged entities: {merged}"
        )

        return merged

    def update(self, entities):

        Logger.debug(
            "Updating conversation context..."
        )

        for key, value in entities.items():

            if value is not None:

                self.context.set(key, value)

        Logger.debug(
            f"Current Context: {self.context.data}"
        )

    def clear(self):

        self.context.clear()