def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text):
    words = text.split()

def main():
    print(get_book_text("books/frankenstein.txt"))
    
main()