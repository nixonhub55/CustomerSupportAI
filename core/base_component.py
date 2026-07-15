class BaseComponent:
    """
    Base class for all framework components.
    """

    AUTO_REGISTER = False

    NAME = ""

    DISPLAY_NAME = ""

    DESCRIPTION = ""

    CATEGORY = ""

    VERSION = "1.0.0"

    AUTHOR = ""

    TAGS = []

    def metadata(self):

        return {
            "name": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "description": self.DESCRIPTION,
            "version": self.VERSION,
            "author": self.AUTHOR,
            "category": self.CATEGORY,
            "tags": self.TAGS,
            "type": self.__class__.__name__
        }