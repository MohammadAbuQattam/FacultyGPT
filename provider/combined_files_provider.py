import sys

sys.path.append('../')

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from constants import (COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY,
                       LLM_NAME)
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

NUMBER_OF_SIMILAR_DOCS = 3


def get_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )


def get_chain():
    llm = ChatOpenAI(model_name=LLM_NAME, temperature=0)
    embedding = OpenAIEmbeddings()
    vectordb = get_vectordb(embedding)
    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectordb.as_retriever(),
        memory=get_memory()
    )


def get_vectordb(embedding):
    persist_directory = COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)


if not load_dotenv(find_dotenv()):
    print("Failed to load .env file.")
    sys.exit(1)

chain = get_chain()

while True:
    user_input = input("Enter a string (or type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break


    answer = chain({"question": user_input.lower()})['answer']

    print(f"Question: {user_input}\nAnswer: {answer}")
