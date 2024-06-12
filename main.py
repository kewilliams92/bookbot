def main():
    path = "books/frankenstein.txt"
    text = get_bookpath(path)
    word_count = count_words(text)
    character_count = count_characters(text)

    report(word_count, character_count)


def count_words(words):
    return len(words.split())


def count_characters(words):
    count_dictionary = {}
    for word in words:
        lowered = word.lower()
        for character in lowered:
            if character.isalpha():  # check if character is alphabetic
                if character in count_dictionary:
                    count_dictionary[character] += 1
                else:
                    count_dictionary[character] = 1
    return count_dictionary


def report(words, characters):
    beginning = "--- Begin report of books/frankenstein.txt---"
    amount_of_words = f"{words} words found in the document\n"
    sorted_characters = sort_characters(characters)

    # formatting the report
    print(beginning)
    print(amount_of_words)
    # looping over each dictionary
    for item in sorted_characters:
        char = item["char"]
        count = item["num"]
        print(f"The '{char}' character was found {count} times")

    print("\n---End report---")


def sort_characters(character_count):
    # formatting the dictionary into a list of dictionaries, each containing a character and its count
    char_list = [
        {"char": char, "num": count} for char, count in character_count.items()
    ]
    # sort list by numbers of occurrences in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list


def get_bookpath(path):
    with open(path) as f:
        return f.read()


main()
