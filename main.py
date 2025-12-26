def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def main():
    bookpath = "./books/frankenstein.txt"
    text = get_book_text(bookpath)
    count_words(text)

main()
