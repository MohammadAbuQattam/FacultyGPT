import os
import sys
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from utils import load_file, split_file, save_to_database, create_file_path
from constants import DATABASE_KNOWLEDGE_FILES_DIRECTORY, KNOWLEDGE_FILES_DIRECTORY

sys.path.append('../..')


def get_list_of_files(directory):
    """
    Retrieves a list of all files in the specified directory.

    Parameters:
    - directory (str): The directory from which to list files.

    Returns:
    - A list of filenames (str) found in the specified directory.
    """
    return os.listdir(directory)


def process_file(file_path):
    """
    Processes a single file by loading, splitting, embedding, and saving its content.

    Parameters:
    - file_path (str): The path to the file to be processed.

    Raises:
    - Exception: If any step in the process fails, an exception is raised.
    """
    try:
        # Load the file's content, split based on markdown headers, embed using OpenAI, and save to DB.
        file_docs = load_file(file_path)
        documents = split_file(file_docs)
        embedding = OpenAIEmbeddings()
        vectordb = save_to_database(documents, embedding, DATABASE_KNOWLEDGE_FILES_DIRECTORY)
        print(vectordb._collection.count())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if not load_dotenv(find_dotenv()):
    print("Failed to load .env file.")
    sys.exit(1)

try:
    knowledge_files = get_list_of_files(KNOWLEDGE_FILES_DIRECTORY)
    for file in knowledge_files:
        process_file(create_file_path(KNOWLEDGE_FILES_DIRECTORY, file))
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
