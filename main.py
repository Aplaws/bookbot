from stats import count_words, char_count, sort_char  
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    num_words = count_words(text)
    dic_words = char_count(text)
    sort_dic = sort_char(dic_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_dic:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
        else:
            continue
    print("============= END ===============")
   

main()
