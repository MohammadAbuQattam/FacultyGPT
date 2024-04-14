import sys

from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

from constants import HEADERS_TO_SPLIT_ON


class FileProcessor:
    def __init__(self):
        """
        Initializes the FileProcessor class by setting up a markdown text splitter
        based on specific headers. This setup allows for segmented processing of
        markdown documents based on their structure.
        """
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
