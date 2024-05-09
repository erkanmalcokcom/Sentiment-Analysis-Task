from transformers import pipeline


class TransformersClient:
    def __init__(self):
        pass

    @staticmethod # This method is static because it doesn't need to access any class attributes
    def analyze_sentiment_bert(text):
        sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", revision="af0f99b")
        result = sentiment_analyzer(text)
        return result.pop()["label"]

