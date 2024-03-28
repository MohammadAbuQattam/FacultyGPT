import os
import sys

sys.path.append('../')
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from utils import load_file, split_file, save_to_database, create_path
from constants import (COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY,
                       KNOWLEDGE_FILES_DIRECTORY)


def get_list_of_files(directory):
    """
    Retrieves a list of all files in the specified directory.

    Parameters:
    - directory (str): The directory from which to list files.

    Returns:
    - A list of filenames (str) found in the specified directory.
    """
    return os.listdir(directory)


def process_file(directory, file_name):
    try:
        file_path = create_path(directory, file_name)
        file_docs = load_file(file_path)
        documents = split_file(file_docs)
        embedding = OpenAIEmbeddings()
        save_to_database(documents, embedding, COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if not load_dotenv(find_dotenv()):
    print("Failed to load .env file.")
    sys.exit(1)

try:
    knowledge_files = get_list_of_files(KNOWLEDGE_FILES_DIRECTORY)
    for file in knowledge_files:
        process_file(KNOWLEDGE_FILES_DIRECTORY, file)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
