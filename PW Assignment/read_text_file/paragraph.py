import re
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_words(text):
    # Use regex to find words, ignoring punctuation and making all words lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def display_results(word_counts):
    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")

def main():
    file_path = 'paragraph.txt'
    text = read_file(file_path)
    word_counts = count_words(text)
    display_results(word_counts)

if __name__ == "__main__":
    main()
