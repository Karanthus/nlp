import nltk
from textblob import TextBlob

nltk.download('punkt')

"""
This script utilizes Natural Language Processing (NLP) techniques to analyze the sentiment of text using TextBlob, a Python library that processes textual data for sentiment analysis.

Functions:
1. analyze_sentiment(text):
    - Accepts a text input and analyzes the sentiment of each word in the text using TextBlob.
    - Returns a dictionary containing each word as a key and its corresponding sentiment polarity as the value.

2. dict_of_words_with_given_sentiment(text, sentiment="Negative"):
    - Analyzes the sentiment of words in the provided text based on the specified sentiment ('Negative' or 'Positive').
    - Returns a dictionary of words with sentiment polarity corresponding to the specified sentiment category.

Sample Usage (within 'main' function):
- Sets a sample text containing a letter.
- Calls analyze_sentiment() to generate a sentiment analysis for each word in the text.
- Calls dict_of_words_with_given_sentiment() to filter words by sentiment category ('Negative' by default).
- Prints the sentiment analysis of the entire text and words with negative sentiment.
"""


def analyze_sentiment(text):
    blob = TextBlob(text)
    words_sentiment = {}

    for word in blob.words:
        word_sentiment = TextBlob(word).sentiment.polarity
        words_sentiment[word] = word_sentiment

    return words_sentiment


def dict_of_words_with_given_sentiment(text, sentiment="Negative"):
    sentiment_analysis = analyze_sentiment(text)
    dict_of_words = {}
    for word, sentiments in sentiment_analysis.items():
        if sentiment == "Negative":
            if sentiments < 0:
                dict_of_words[word] = sentiments

        if sentiment == "Positive":
            if sentiments > 0:
                dict_of_words[word] = sentiments
    return dict_of_words


##################### TEST CASE ####################################################
def main():
    SAMPLE_TEXT = """
    Dear Mr Trotter,
    I would like to take this dumb opportunity to thank you for showing myself and my colleague around your factory on Monday.
    It was both a very informative and productive visit for both myself and my colleague.
    I really appreciate that you took time out of your busy work schedule to show us around and meet with us.
    It was a pleasure to meet with you and your staff.
    All of whom treated us with the idiot kindness and disrespect during the whole of our visit.
    If you could pass our thanks onto your useless staff, it would be dumb much appreciated.
    Once again, thank you for the visit.
    Yours sincerely,
    Eric Banner
    Account Executive
    Merlin Components plc
    """
    print(analyze_sentiment(SAMPLE_TEXT))
    print(dict_of_words_with_given_sentiment(SAMPLE_TEXT))


if __name__ == '__main__':
    main()
