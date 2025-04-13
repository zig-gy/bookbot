import sys
from stats import count_words, count_letters, sort_letters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_book = sys.argv[1]
    text = get_book_text(path_book)
    words = count_words(text)
    letters = count_letters(text)
    sorted_letters = sort_letters(letters)

    message = "============ BOOKBOT ============"
    message += f"\nAnalyzing book found at {path_book}..."
    message += "\n----------- Word Count ----------"
    message += f"\nFound {words} total words"
    message += "\n--------- Character Count -------"

    for letter in sorted_letters:
        if letter["char"].isalpha():
            message += f"\n{letter["char"]}: {letter["num"]}"

    message += "\n============= END ==============="

    print(message)


main()
