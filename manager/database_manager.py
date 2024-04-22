import sys

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class DatabaseManager:
    def __init__(self):
        """
        Initializes the DatabaseManager class by setting up the OpenAI embeddings.
        This embedding will be used to create vector representations of documents for the database.
        """
        self.embedding = OpenAIEmbeddings()

    def save_to_database(self, documents, directory):
        """
        Saves a list of documents into a vector database using the configured embeddings.
        This method creates a Chroma vectorstore from the given documents.

        Args:
            documents (list): A list of document texts to be stored.
            directory (str): The directory where the vector database will be persisted.

        Returns:
            Chroma: A vectorstore instance containing the indexed documents.

        Raises:
            SystemExit: If there's an exception during the database creation, the system will exit.
        """
        try:
            return Chroma.from_documents(
                documents=documents,
                embedding=self.embedding,
                persist_directory=directory
            )
        except Exception as e:
            print(f"Failed to save to database: {e}")
            sys.exit(1)
