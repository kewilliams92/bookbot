def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_book_count(book_text)
    character_count = get_character_count(book_text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    character_count.sort(reverse=True, key=sort_on)

    for char in character_count:
        print(f"The '{char['letter']}' character was found {char['num']} times")
    print("---End report---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_book_count(text):
    words = text.split()
    return len(words)


def get_character_count(words):
    characters = {}
    lowercase_words = words.lower()
    for char in lowercase_words:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    char_list = [
        {"letter": letter, "num": count} for letter, count in characters.items()
    ]
    return char_list


def sort_on(item):
    return item["num"]


main()
