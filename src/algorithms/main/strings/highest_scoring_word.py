"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the 
alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest 
in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    # Code here
    words = x.split(" ")
    results = {"idx": 0, "score": 0}
    for idx, word in enumerate(words):
        word = [str(ord(char) - 96) for char in word.lower() if char.isalpha()]
        score = sum(int(digit) for digit in word)
        if results["score"] < score:
            results["idx"] = idx
            results["score"] = score

    return words[results["idx"]]


def high_extra(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high_extra_two(x):
    words = x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
