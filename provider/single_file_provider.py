import sys

sys.path.append('../')

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from constants import (DATABASE_METADATA_DIRECTORY,
                       SEPERATED_DATABASE_KNOWLEDGE_FILES_DIRECTORY,
                       METADATA_FILE_DESCRIPTION,
                       METADATA_FIELD_INFO,
                       FILE_DETERMINER_LLM_NAME,
                       LLM_NAME)
from langchain.retrievers.self_query.base import SelfQueryRetriever
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from utils import create_path
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

NUMBER_OF_SIMILAR_DOCS = 1  # used to determine the number of splits to pass


def get_retriever(vectordb):
    llm = OpenAI(model=FILE_DETERMINER_LLM_NAME, temperature=0)
    return SelfQueryRetriever.from_llm(
        llm,
        vectordb,
        METADATA_FILE_DESCRIPTION,
        METADATA_FIELD_INFO,
        verbose=True
    )


def get_chain(vectordb):
    llm = ChatOpenAI(model_name=LLM_NAME, temperature=0)
    return RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
    )


def get_chosen_files(question, persist_directory, embedding):
    try:
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
        print(vectordb._collection.count())
        retriever = get_retriever(vectordb)
        return retriever.get_relevant_documents(question)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def get_vectordb(chosen_files, embedding):
    chosen_file = chosen_files[0]
    file_name = chosen_file.metadata['Header 1'] + '.txt'
    persist_directory = create_path(SEPERATED_DATABASE_KNOWLEDGE_FILES_DIRECTORY, file_name)
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)


def get_answer(question):
    embedding = OpenAIEmbeddings()
    chosen_files = get_chosen_files(question, DATABASE_METADATA_DIRECTORY, embedding)
    if len(chosen_files) == 0:
        return None
    else:
        vectordb = get_vectordb(chosen_files, embedding)
        qa_chain = get_chain(vectordb)
        return qa_chain({"query": question})


if not load_dotenv(find_dotenv()):
    print("Failed to load .env file.")
    sys.exit(1)

result = get_answer("Is the given context text data?")
print(result["result"])
