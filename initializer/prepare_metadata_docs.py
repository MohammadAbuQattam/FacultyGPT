import sys
sys.path.append('../')
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from utils import load_file, split_file, save_to_database, create_path
from constants import (METADATA_DIRECTORY, DATABASE_METADATA_DIRECTORY, FILES_INFO)


if not load_dotenv(find_dotenv()):
    print("Failed to load .env file.")
    sys.exit(1)

try:
    file_docs = load_file(create_path(METADATA_DIRECTORY, FILES_INFO))
    documents = split_file(file_docs)
    embedding = OpenAIEmbeddings()
    vectordb = save_to_database(documents, embedding, DATABASE_METADATA_DIRECTORY)
    print(vectordb._collection.count())
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
