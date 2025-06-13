from stats import count_words, count_letters, sort_by_value
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(filepath)  # Use the filepath from sys.argv
    word_count = count_words(contents)
    letter_count = count_letters(contents)
    descending = sort_by_value(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter, count in descending.items():
        print(f"{letter}: {count}")
    print("============= END ===============")


main()

