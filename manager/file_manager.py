import os
import sys
from constants import (COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY,
                       KNOWLEDGE_FILES_DIRECTORY)
from manager.database_manager import DatabaseManager
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

from constants import HEADERS_TO_SPLIT_ON
from manager.path_manager import PathManager


class FileManager:
    def __init__(self):
        """
        Initializes the FileManager class by setting up directories and initializing
        DatabaseManager.
        """
        self.directory = KNOWLEDGE_FILES_DIRECTORY
        self.database_manager = DatabaseManager()
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=HEADERS_TO_SPLIT_ON,
            strip_headers=False,
            return_each_line=False
        )

    def load_file(self, file_path):
        """
        Loads the content of a file using a TextLoader, handling markdown or plain text.

        Args:
            file_path (str): The path to the file to be loaded.

        Returns:
            list: A list of loaded document contents.

        Raises:
            SystemExit: If there is an issue with loading the file, the system will exit.
        """
        try:
            loader = TextLoader(file_path)
            return loader.load()
        except Exception as e:
            print(f"Failed to load file: {e}")
            sys.exit(1)

    def split_file(self, file_docs):
        """
        Splits a list of loaded document contents into segments based on markdown headers.

        Args:
            file_docs (list): A list of document content objects, each potentially containing multiple pages.

        Returns:
            list: A list of document segments split according to markdown headers.
        """
        splits = []
        for doc in file_docs:
            splits.extend(self.markdown_splitter.split_text(doc.page_content))
        return splits

    def process_files(self):
        """
        processing knowledge files located in a predefined directory.The method checks if the database directory already
        exists to avoid duplicate processing.If not, it processes each file: reads, splits,
        and stores its contents into the database.
        """
        if not os.path.exists(COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY):
            try:
                knowledge_files = PathManager.get_list_of_files(self.directory)
                for file_name in knowledge_files:
                    file_path = PathManager.create_path(self.directory, file_name)
                    print(file_name)
                    loaded_file = self.load_file(file_path)
                    print(file_path)
                    documents = self.split_file(loaded_file)
                    print(documents)
                    self.database_manager.save_to_database(documents, COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY)
            except Exception as e:
                print(f"An error occurred while creating the database: {e}")
                sys.exit(1)
        else:
            print(
                f"Directory already exists, skipping database creation"
                f" and file processing: {COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY}")
