def get_num_words(text):
    words = text.split()
    return len(words)

repeated = {}

def get_char_count (text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count [char] += 1
        else:
            char_count [char] = 1

    return char_count

def sort_on(item):
    return item ["num"]

def sort_char_count (char_count):
    sorted_list = []
    
    for char in char_count:
        if char.isalpha ():
            sorted_list.append ({"char": char, "num": char_count[char]})

    sorted_list.sort (reverse=True, key=sort_on)
    
    return sorted_list