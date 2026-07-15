from pathlib import Path


class PromptManager:
    """
    Loads prompt templates from disk.
    """

    def __init__(self, folder="prompts"):

        self.folder = Path(folder)

    # -------------------------

    def load(self, name):

        file = self.folder / f"{name}.txt"

        if not file.exists():

            raise FileNotFoundError(file)

        return file.read_text(
            encoding="utf-8"
        )

    # -------------------------

    def exists(self, name):

        return (
            self.folder /
            f"{name}.txt"
        ).exists()

    # -------------------------

    def list(self):

        return sorted(
            file.stem
            for file in self.folder.glob("*.txt")
        )