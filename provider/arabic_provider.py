import sys

from manager.translate_manager import TranslateManager

sys.path.append('../')
from manager.chat_manager import ChatManager
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    if not load_dotenv(find_dotenv()):
        print("Failed to load .env file.")
        sys.exit(1)

    chat_manager = ChatManager()
    arabic_translate_manager = TranslateManager(source_language="Arabic", target_language="English")
    english_translate_manager = TranslateManager(source_language="English", target_language="Arabic")
    while True:
        user_input = input("Enter a string (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break
        question = arabic_translate_manager.translate(user_input)
        answer = chat_manager.chain({"question": question})['answer']
        answer = english_translate_manager.translate(answer)
        print(f"Question: {user_input}\nAnswer: {answer}")