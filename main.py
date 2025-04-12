from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    message = f"{count_words(text)} words found in the document"
    print(message)
    
main()