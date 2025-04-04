from stats import get_words, count_characters, sort_count

book = "books/frankenstein.txt"


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return(book_contents)

def main():
    book_text = get_book_text(book)
    book_words = get_words(book_text)
    book_characters = count_characters(book_text)
    book_characters_sorted = sort_count(book_characters)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {book_words} total words
--------- Character Count -------""")
    for item in book_characters_sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()
