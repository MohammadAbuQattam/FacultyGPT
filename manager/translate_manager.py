from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from constants import LLM_NAME


class TranslateManager:
    def __init__(self, source_language, target_language):
        load_dotenv(find_dotenv())
        self.source_language = source_language
        self.target_language = target_language
        self.client = OpenAI()

    def translate(self, text_to_translate):
        prompt = (f"Translate the given text from {self.source_language} to {self.target_language} only provide"
                  f" the translation: {text_to_translate}")
        completion = self.client.chat.completions.create(
            model=LLM_NAME,
            messages=[
                {"role": "system", "content": "Please assist with the following translation task."},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
