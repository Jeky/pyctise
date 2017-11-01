#
# Count the words in a string. Usually we use regular expression to do this kind of string related works. 
#
from typing import Dict


def filter_str(sentence: str) -> str:
    """Filter a sentence, replacing every the non-alphabet character with a space.
    """
    chars = list(sentence)
    for i in range(len(chars)):
        if not chars[i].isalpha():
            chars[i] = ' '

    # join them together
    return ''.join(chars)


def count_words(sentence: str) -> Dict[str, int]:
    """Count words in sentence. Return a dictionary mapping from word to frequency
    """
    counter = {}

    filtered_sentence = filter_str(sentence)
    words = filtered_sentence.split(' ')
    for word in words:
        if word != '': # only care about non-empty strings
            lower_case_word = word.lower()
            if lower_case_word not in counter:
                counter[lower_case_word] = 0

            counter[lower_case_word] += 1

    return counter


if __name__ == '__main__':
    sentence = 'This is a good day!Hello world!!! There are some words that are repeated repeated repeated....'
    print(count_words(sentence))