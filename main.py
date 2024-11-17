def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_book_count(book_text)
    print(book_text, word_count)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_book_count(text):
    words = text.split()
    return len(words)


main()
