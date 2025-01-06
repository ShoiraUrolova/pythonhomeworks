import os
import string
from collections import Counter

def create_sample_file():
    if not os.path.exists("sample.txt"):
        print("File 'sample.txt' does not exist. Create it by typing a paragraph below:")
        content = input("Enter content for 'sample.txt': ")
        with open("sample.txt", "w") as file:
            file.write(content)

def count_word_frequency():
    with open("sample.txt", "r") as file:
        text = file.read().lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
    word_count = Counter(words)
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    create_sample_file()
    count_word_frequency()

main()