import logging


class AppLogging:
    @staticmethod
    def _setup_logs(file_path):
        logging.basicConfig(
                filename=file_path,
                filemode="a",
                format="%(asctime)s - %(levelname)s - %(message)s",
                datefmt='%Y-%m-%d %H:%M:%S',
                level=logging.INFO
            )

    @staticmethod
    def log_setup():
        file_path = "app_logging.log"
        try:
            with open(file_path, "r") as rf:
                pass
        except FileNotFoundError:
            AppLogging._setup_logs(file_path)
            logging.info("First launch of the application")
        finally:
            AppLogging._setup_logs(file_path)

    @staticmethod
    def show_logs():
        logs = []
        with open("app_logging.log", "r") as fr:
            for line in fr:
                logs.append(line)
        return ''.join(logs)

    @staticmethod
    def add_log(message):
        logging.info(message)
