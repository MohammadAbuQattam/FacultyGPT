import os

# Directories
KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'knowledge_files')
COMBINED_DATABASE_KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'chroma', 'combined_knowledge_files')
SEPERATED_DATABASE_KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'chroma', 'seperated_knowledge_files')

LLM_NAME = "gpt-3.5-turbo"

# File
FILES_INFO = 'files_info.txt'

# Headers to split on
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
