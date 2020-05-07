import re

def word_count(s):
    words = {}
    s_arr = re.split('[\s":;,.\-+=/\\\|[\]{}()*^&]+', s.lower())
    for word in s_arr:
        if len(word) == 0:
            continue
        if words.get(word):
            words[word] += 1
        else:
            words[word] = 1
    print(words)
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))