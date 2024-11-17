def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)


def get_book_text(book_path):
    with open(book_path) as f:
        file_content = f.read()
        print(file_content)


main()
