
def get_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for c in text:
        characters[c] = 1
    return characters