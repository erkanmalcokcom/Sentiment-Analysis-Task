from api.openai_api import OpenAIClient
from api.transformers_api import TransformersClient  # Assuming this is the class name
from api.mistral_api import MyMistralClient  # Assuming this is the class name
from utils.utilities import Screen

def main():
    screen = Screen()
    screen.welcome_screen()

    # Instantiate API clients
    openai_client = OpenAIClient()
    transformers_client = TransformersClient()  # Assuming an instance is needed
    mistral_client = MyMistralClient()

    sentiment_dict = {
        'POSITIVE': '😄',
        'NEGATIVE': '😞',
        'NEUTRAL': '😐',
        'MIXED': '🤔',
    }

    while True:
        text = input("Please provide a sentence to analyze (or 'q' to quit): ")
        if text.lower() == 'q':
            break

        print("Thank you, we are starting to analyse the text with multi-models. Please wait...")

        gpt3_sentiment = openai_client.analyze_sentiment_gpt3(text)
        bert_sentiment = transformers_client.analyze_sentiment_bert(text)  # Make sure this matches your class and method
        mistral_sentiment = mistral_client.analyze_sentiment_mistral(text)  # Make sure this matches your class and method

        print("\nThe INPUT: ", text, "\n")

        for model, sentiment in zip(['GPT-3', 'BERT', 'Mistral'], [gpt3_sentiment, bert_sentiment, mistral_sentiment]):
            print(f'{model} Sentiment Analysis Result: {sentiment} {sentiment_dict.get(sentiment)}')

        sentiments = [gpt3_sentiment, bert_sentiment, mistral_sentiment]
        most_common_sentiment = max(set(sentiments), key=sentiments.count)
        print(f'\nMajority Vote Result: {most_common_sentiment} {sentiment_dict.get(most_common_sentiment)}')
        print("\n")

if __name__ == "__main__":
    main()
