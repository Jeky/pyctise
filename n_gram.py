#
# N-gram model is widely used in NLP (natural language processing).
# If we have a sentence: 'This is a good day'
# 1-gram (unigram) model list will be: ['this', 'is', 'a', 'good', 'day']
# 2-gram (bigram) model list will be : ['this is', 'is a', 'a good', 'good day']
# 3-gram (trigram) model list will be: ['this is a', 'is a good', 'a good day']
# ... (usually 3-gram is enough for training)
#

from count_words import filter_str
from typing import List


def split_words(sentence: str) -> List[str]:
    """Split sentence into words
    """
    filtered_sentence = filter_str(sentence)
    return [word.lower() for word in filtered_sentence.split(' ') if word != '']
    # the last line is LIST COMPREHENSION
    # equals to:
    #
    # words = []
    # for word in filtered_sentence.split(' '):
    #     if word != '':
    #         words.append(word.lower())
    # return words
    #


def generate_gram_model(words: List[str], gram_len: int = 2) -> List[str]:
    """Generate gram model using words
    """
    grams = []
    for i in range(0, len(words) - gram_len + 1):
        grams.append(' '.join(words[i:i+gram_len]))
    return grams

if __name__ == '__main__':
    sentence = 'This is a good day'
    words = split_words(sentence)
    print(generate_gram_model(words, 1))
    print(generate_gram_model(words, 2))
    print(generate_gram_model(words, 3))