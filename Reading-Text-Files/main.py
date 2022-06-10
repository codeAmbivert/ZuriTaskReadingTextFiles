import string
# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as text:
        lines = text.read()
        return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    print(text, '\n')
    word_count = {}
    for character in string.punctuation:
        text = text.replace(character, "")
        # This for loop goes through the whole text and replaces all punctuation with an empty space
    words = text.split()

    for word in words:
        word = word.lower()
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    print(word_count)


read_file_content("./story.txt")
count_words()
