import numpy as np
import nltk                                      #tool kit
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()               #types of stemmer


def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]        #sentance
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)        #np.zeros [0,0,0,0]
    for idx, w in enumerate(words):         #index value
        if w in sentence_words:             #hi compare with sentance
            bag[idx] = 1

    return bag
