from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read() 

def main():
    book_text = get_book_text("./books/frankenstein.txt")

    word_count = get_word_count(book_text) 
    char_count = get_char_count(book_text)
    sorted_count = get_sorted_count(char_count)

    print(f"{word_count} words found in the document")
    print(sorted_count)

main()
