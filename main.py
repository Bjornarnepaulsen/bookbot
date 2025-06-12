from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main():
    contents = get_book_text('books/frankenstein.txt')
    word_count= (count_words(contents))
    letter_count = count_letters(contents)
    decending = sorted(letter_count)

    #print(f"{word_count} words found in the document")
    #print(f"{letter_count} letters found in the document")
    #print(decending)


main()

