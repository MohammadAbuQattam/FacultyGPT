import sys

sys.path.append('../')
from manager.chat_manager import ChatManager
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    if not load_dotenv(find_dotenv()):
        print("Failed to load .env file.")
        sys.exit(1)

    chat_manager = ChatManager()
    while True:
        user_input = input("Enter a string (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break

        answer = chat_manager.chain({"question": user_input.lower()})['answer']
        print(f"Question: {user_input}\nAnswer: {answer}")
