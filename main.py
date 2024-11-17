def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_book_count(book_text)
    print(book_text, word_count)
    character_count = get_character_count(book_text)
    print(character_count)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_book_count(text):
    words = text.split()
    return len(words)


def get_character_count(words):
    characters = {}
    lowercase_words = words.lower()
    split_words = lowercase_words.split()
    for words in split_words:
        for char in words:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters


main()
