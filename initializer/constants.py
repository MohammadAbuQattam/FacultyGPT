import os

# Directories
KNOWLEDGE_FILES_DIRECTORY = os.path.join('..', 'docs', 'knowledge_files')
METADATA_DIRECTORY = os.path.join('..', 'docs', 'metadata_files')
DATABASE_KNOWLEDGE_FILES_DIRECTORY = os.path.join('../docs', 'chroma', 'knowledge_files')
DATABASE_METADATA_DIRECTORY = os.path.join('../docs', 'chroma', 'metadata_files')

# File
FILES_INFO = 'files_info.txt'

# Headers to split on
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
