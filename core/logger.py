from datetime import datetime


class Logger:

    @staticmethod
    def _log(level, message):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(
            f"[{timestamp}] "
            f"[{level}] "
            f"{message}"
        )

    # -------------------------------------

    @staticmethod
    def info(message):

        Logger._log(
            "INFO",
            message
        )

    # -------------------------------------

    @staticmethod
    def warning(message):

        Logger._log(
            "WARNING",
            message
        )

    # -------------------------------------

    @staticmethod
    def error(message):

        Logger._log(
            "ERROR",
            message
        )

    # -------------------------------------

    @staticmethod
    def debug(message):

        Logger._log(
            "DEBUG",
            message
        )