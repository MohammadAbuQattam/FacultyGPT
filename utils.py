import os
import sys
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import Chroma
from constants import HEADERS_TO_SPLIT_ON


def load_file(file_path):
    """
    Loads the content of a file using the TextLoader.

    Parameters:
    - file_path (str): The path to the file to be loaded.

    Returns:
    - The content of the file as loaded by the TextLoader.

    Raises:
    - Exception: If the file could not be loaded for any reason.
    """
    loader = TextLoader(file_path)
    try:
        return loader.load()
    except Exception as e:
        print(f"Failed to load file: {e}")
        sys.exit(1)


def split_file(file_docs):
    """
    Splits file documents based on specified markdown headers.

    Parameters:
    - file_docs (list): A list of file documents to be split.

    Returns:
    - A list of split documents.

    Notes:
    - The headers used for splitting are defined in the HEADERS_TO_SPLIT_ON constant.
    """
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON,
                                                   strip_headers=False,
                                                   return_each_line=False)
    splits = []
    for doc in file_docs:
        splits.extend(markdown_splitter.split_text(doc.page_content))
    return splits


def save_to_database(documents, embedding, directory):
    """
    Saves a list of documents to a Chroma vector store.

    Parameters:
    - documents (list): The documents to be saved.
    - embedding: The embedding model to be used.
    - directory (str): The directory path where the vector store will persist.

    Returns:
    - The Chroma vector store instance created from the documents.

    Raises:
    - Exception: If the documents could not be saved for any reason.
    """
    try:
        return Chroma.from_documents(
            documents=documents,
            embedding=embedding,
            persist_directory=directory
        )
    except Exception as e:
        print(f"Failed to save to database: {e}")
        sys.exit(1)


def create_path(directory, filename):
    """
    Constructs a file path by joining a directory path with a filename.

    Parameters:
    - directory (str): The directory path.
    - filename (str): The filename.

    Returns:
    - A string representing the full path to the file.
    """
    return os.path.join(directory, filename)


def get_api_key():
    """
    Retrieves the OpenAI API key from environment variables.

    Returns:
    - The OpenAI API key as a string, or None if not found.
    """
    return os.getenv('OPENAI_API_KEY')
