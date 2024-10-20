"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
words.sort()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

max_length = max([len(word) for word in words])
for word in word_to_count:
    print(f'{word:{max_length}} : {word_to_count[word]}')
