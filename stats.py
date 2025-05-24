def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    char_list = list(text) 

    for char in char_list:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def get_sorted_count(char_count):
    list_of_dicts = []

    for char in char_count:
        if char.isalpha():
            list_of_dicts.append({
                "char": char,
                "num": char_count[char]
            })

    def sort_on(dict):
        return dict['num']

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts 
