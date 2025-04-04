
def get_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_count(counts_dict):
    sorted_list = []
    for char, count in counts_dict.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list

def sort_key(item):
    return item["count"]
