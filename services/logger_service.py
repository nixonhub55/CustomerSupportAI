from datetime import datetime


class Logger:

    def __init__(self):
        self.log_file = "logs/ai.log"

    def _write(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}"

        print(line)

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(line + "\n")

    def info(self, message):
        self._write("INFO", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)


logger = Logger()