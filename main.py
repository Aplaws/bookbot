def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    bookpath = "./books/frankenstein.txt"
    text = get_book_text(bookpath)
    print(text)

main()
