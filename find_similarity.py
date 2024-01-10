from fuzzywuzzy import fuzz
import itertools

# pip install fuzzywuzzy python-Levenshtein


accuracy_ratio = 80

word_list_1 = [
    "mercedez",
    "toyota supra",
    "bmw"
]

word_list_2 = [
    "Mercedez benz",
    "supra",
    "bmw"
]


def getComparison():
    for word_1, word_2 in itertools.product(word_list_1, word_list_2):
        ratio = fuzz.partial_ratio(word_1, word_2)
        if ratio > accuracy_ratio:
            print("{} is same/similar to {}".format(word_1, word_2))


if __name__ == "__main__":
    getComparison()
