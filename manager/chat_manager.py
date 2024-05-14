import sys

sys.path.append('../')

from manager.file_manager import FileManager
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from constants import COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY, LLM_NAME


class ChatManager:
    def __init__(self):
        """
        Initializes the ChatManager class, setting up necessary components for the chat system.
        This includes creating the database, initializing memory, embeddings, vector database,
        and the conversational retrieval chain.
        """
        self.file_manager = FileManager()
        self.file_manager.process_files()
        self.memory = self.get_memory()
        self.embedding = OpenAIEmbeddings()
        self.vectordb = self.get_vectordb(self.embedding)
        self.chain = self.get_chain()

    def get_memory(self):
        """
        Configures and returns a conversation buffer memory, which stores and retrieves chat history.

        Returns:
            ConversationBufferMemory: An instance configured for storing chat history.
        """
        return ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    def get_vectordb(self, embedding):
        """
        Creates and returns a vector database configured with a persistence directory and an embedding function.

        Args:
            embedding (function): A function to compute embeddings for text input.

        Returns:
            Chroma: An instance of the Chroma vector database using the provided embedding function.
        """
        persist_directory = COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY
        return Chroma(persist_directory=persist_directory, embedding_function=embedding)

    def get_chain(self):
        """
        Creates and returns a conversational retrieval chain configured with a language model,
        a retriever, and memory integration.

        Returns:
            ConversationalRetrievalChain: An instance of the conversational retrieval chain.
        """
        llm = ChatOpenAI(model_name=LLM_NAME, temperature=0.3)
        return ConversationalRetrievalChain.from_llm(
            llm,
            retriever=self.vectordb.as_retriever(),
            memory=self.memory
        )
