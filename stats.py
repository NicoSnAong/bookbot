def count_words(text):
    words=text.split()
    words_count= len(words)
    return words_count

def count_caracters(text):
    text_lower=text.lower()
    char_dict={}
    
    for c in text_lower:
        if c in char_dict :
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def sort_on(item):
    return item["num"]

def dict_to_sorted_list(char_dict):
    """
    Prend le dict {char: count} et renvoie une liste de dicts:
    [{"char": "e", "num": 44538}, ...] triée par 'num' (descendant).
    """
    report = []
    for char, count in char_dict.items():
        report.append({"char": char, "num": count})
    report.sort(reverse=True, key=sort_on)  # plus grand -> plus petit
    return report