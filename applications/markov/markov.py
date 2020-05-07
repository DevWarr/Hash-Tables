import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = re.split('\s+', f.read())

# TODO: analyze which words can follow other words
word_and_followers = {}
single_stoppers = [".", "?", "!"]
quote_stoppers = [".\"", "?\"", "!\""]
starters = []
stoppers = []
for i in range(len(words) - 1):
    word = words[i]
    if len(word) == 0:
        continue

    if word not in word_and_followers:
        word_and_followers[word] = []
    word_and_followers[word].append(words[i + 1])

    if word[-1] in single_stoppers or word[-2:] in quote_stoppers:
        stoppers.append(word)

    if word[0] == word[0].upper() or (len(word) >= 2 and word[:2] == f'"{word[1].upper()}'):
        starters.append(word)

# print(word_and_followers)
# print("starters", starters)
# print("stoppers", stoppers)

# TODO: construct 5 random sentences
final_story = ""
for i in range(5):
    starter = random.choice(starters)
    final_story += starter + " "
    prev_word = starter
    while True:
        word = random.choice(word_and_followers[prev_word])
        final_story += word + " "
        prev_word = word
        if prev_word in stoppers:
            break

print(final_story)
