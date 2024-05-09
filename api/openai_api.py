from openai import OpenAI
import os

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_sentiment_gpt3(self, text):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "ONLY ONE WORD ALLOWED. You are a helpful assistant, and once you read the text, please provide the sentiment of the text."},
                    {"role": "system", "content": "Respond with 'positive', 'negative', 'mixed', or 'neutral' to indicate the sentiment of the following text."},
                    {"role": "user", "content": text}
                ],
            )
            return response.choices[0].message.content.upper()
        except Exception as e:
            print(f"Error: {e}")
            return "API_ERROR"
