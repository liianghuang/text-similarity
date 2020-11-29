import string
import spacy

nlp = spacy.load('en_core_web_sm')
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
class Doc:
    def __init__(self, stopwords=spacy_stopwords):
        self.exclude = set(string.punctuation)
        self.stopword = stopwords if stopwords is not None else []

    def pre_process(self, doc):
        doc = doc.lower()
        words = [w for w in doc.split(" ") if w not in self.stopword and w not in self.exclude]
        return words