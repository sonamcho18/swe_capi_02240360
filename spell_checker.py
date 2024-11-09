import re
def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return set(words)

def read_words_from_file(filename):
    with open(filename, encoding="utf-8") as file:
        content = file.read()
    return extract_words(content)

def spell_checker(text_file, dictionary_file):
    text_words = read_words_from_file(text_file)
    dictionary_words = read_words_from_file(dictionary_file)

    incorrect_words = text_words.difference(dictionary_words)

    for word in incorrect_words:
        print(f"The word '{word}' is incorrect.")

text_file = "360.txt"  # The file to check for spelling
dictionary_file = "clean.txt"  # A file containing correctly spelled words

spell_checker(text_file, dictionary_file)

