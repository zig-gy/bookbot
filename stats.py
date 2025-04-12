def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_text = text.lower()
    letters = {}
    for letter in lower_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters