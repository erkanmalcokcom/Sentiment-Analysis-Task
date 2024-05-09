from mistralai.client import MistralClient as MistralAPIClient
from mistralai.models.chat_completion import ChatMessage

import os

class MyMistralClient:
    def __init__(self):
        self.client = MistralAPIClient(api_key=os.getenv("MISTRAL_API_KEY"))
    
    def analyze_sentiment_mistral(self, text):
        try:
            prompt = "Analyze the sentiment of the text. Respond with POSITIVE, NEGATIVE, NEUTRAL or MIXED in all caps."
            chat_response = self.client.chat(
                model="mistral-large-latest",
                messages=[
                    ChatMessage(role="user", content=f"{prompt} {text}")
                ]
            )
            return chat_response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "Unable to analyze sentiment."
