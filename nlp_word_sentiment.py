import nltk
from textblob import TextBlob

nltk.download('punkt')


def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        words_sentiment = {}

        for word in blob.words:
            word_sentiment = TextBlob(word).sentiment.polarity
            words_sentiment[word] = word_sentiment

        return words_sentiment

    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return None


def dict_of_words_with_given_sentiment(text, sentiment="Negative"):
    try:
        sentiment_analysis = analyze_sentiment(text)
        if sentiment_analysis is None:
            return None

        dict_of_words = {}
        for word, sentiments in sentiment_analysis.items():
            if sentiment == "Negative":
                if sentiments < 0:
                    dict_of_words[word] = sentiments

            if sentiment == "Positive":
                if sentiments > 0:
                    dict_of_words[word] = sentiments
        return dict_of_words

    except Exception as e:
        print(f"Error in creating dictionary of words: {e}")
        return None


##################### TEST CASE ####################################################
def main():
    try:
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
        print(dict_of_words_with_given_sentiment(SAMPLE_TEXT, sentiment="Positive"))

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == '__main__':
    main()
