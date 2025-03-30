from stats import get_words, count_characters

book = "books/frankenstein.txt"


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return(book_contents)

def main():
    book_text = get_book_text(book)
    book_words = get_words(book_text)
    book_characters = count_characters(book_text)
    print(f"{book_words} words found in the document")
    print(book_characters)

main()