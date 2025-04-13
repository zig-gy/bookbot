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


def sort_on(dic):
    return dic["num"]


def sort_letters(letters):
    sorted_letters = []
    for k, v in letters.items():
        letter = {"char": k, "num": v}
        sorted_letters.append(letter)
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
