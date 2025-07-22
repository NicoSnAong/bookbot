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

def create_report(char_dict):
    report=1
    return report