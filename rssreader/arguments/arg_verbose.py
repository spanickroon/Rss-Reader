"""A module which is responsible for the logic of logs"""
import os
import logging


class AppLogging:
    """A class that contains methods responsible for logs""""
    @staticmethod
    def _setup_logs(file_path):
        """
        Method that configures the log config
        storage location, output format
        """
        logging.basicConfig(
                filename=file_path,
                filemode="a",
                format="%(asctime)s - %(levelname)s - %(message)s",
                datefmt='%Y-%m-%d %H:%M:%S',
                level=logging.INFO
            )

    @staticmethod
    def log_setup():
        """
        Method that configures the logs and checks
        whether the application has already been launched
        """
        file_path = "app_logging.log"
        AppLogging._setup_logs(file_path)
        if not os.path.getsize(file_path):
            logging.info("First launch of the application")

    @staticmethod
    def show_logs():
        """Method that returns all the logs"""
        with open("app_logging.log", "r") as fr:
            return "".join([line for line in fr])
