import re
import sys

# Implement me.
def histogram(s):
    words = {}
    longest_word = 0
    s_arr = re.split('[\s":;,.\-+=/\\\|[\]{}()*^&]+', s.lower())
    for word in s_arr:
        if len(word) == 0:
            # Empty string, skiip it
            continue

        # Update the longest word count
        longest_word = max(longest_word, len(word))

        # If our word is in our cache, add 1.
        # If not, create it in our cache as 1.
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    words = list(words.items())
    words.sort(key=lambda x: x[1], reverse=True)

    final_string = ""
    for word_tuple in words:
        final_string += word_tuple[0].ljust(longest_word) + \
            "#" * word_tuple[1] + "\n"

    return final_string



if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        with open(filepath, 'r') as file:
            print(histogram(file.read()))
    except Exception as e:
        print()
        print(e)
        print("Please call this script with a file to read.")
        print("Example:  py histo.py robin.txt")
        exit()