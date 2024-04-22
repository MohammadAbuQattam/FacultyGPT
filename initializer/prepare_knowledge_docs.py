import os
import sys
from dotenv import load_dotenv, find_dotenv
from constants import (COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY,
                       KNOWLEDGE_FILES_DIRECTORY)
from manager.database_manager import DatabaseManager
from helper.file_processor import FileProcessor
from manager.path_manager import PathManager


class FileManager:
    def __init__(self):
        """
        Initializes the FileManager class by setting up directories and initializing
        helper classes like FileProcessor and DatabaseManager.
        """
        self.directory = KNOWLEDGE_FILES_DIRECTORY
        self.file_processor = FileProcessor()
        self.database_manager = DatabaseManager()

    def create_database(self):
        """
        Creates a database by processing knowledge files located in a predefined directory.
        The method checks if the database directory already exists to avoid duplicate processing.
        If not, it processes each file: reads, splits, and stores its contents into the database.
        """
        if not os.path.exists(COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY):
            try:
                knowledge_files = PathManager.get_list_of_files(self.directory)
                for file_name in knowledge_files:
                    file_path = PathManager.create_path(self.directory, file_name)
                    file_docs = self.file_processor.load_file(file_path)
                    documents = self.file_processor.split_file(file_docs)
                    self.database_manager.save_to_database(documents, COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY)
            except Exception as e:
                print(f"An error occurred while creating the database: {e}")
                sys.exit(1)
        else:
            print(
                f"Directory already exists, skipping database creation"
                f" and file processing: {COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY}")


if __name__ == "__main__":
    if not load_dotenv(find_dotenv()):
        print("Failed to load .env file.")
        sys.exit(1)

    file_manager = FileManager()
    file_manager.create_database()
