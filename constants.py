import os
from langchain.chains.query_constructor.base import AttributeInfo

# Directories
KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'knowledge_files')
METADATA_DIRECTORY = os.path.join('..', 'docs', 'metadata_files')
COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'chroma', 'combined_knowledge_files')
SEPERATED_DATABASE_KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'chroma', 'seperated_knowledge_files')
DATABASE_METADATA_DIRECTORY = os.path.join('..', 'docs', 'chroma', 'metadata_files')

METADATA_FILE_DESCRIPTION = "Provides information about each Knowledge file."
FILE_DETERMINER_LLM_NAME = "gpt-3.5-turbo-instruct"
LLM_NAME = "gpt-3.5-turbo"

# File
FILES_INFO = 'files_info.txt'

# Headers to split on
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

METADATA_FIELD_INFO = [
    AttributeInfo(
        name="Header 1",
        description="Provides an overview and key details of the subsequent paragraph.",
        type="string",
    )
]


