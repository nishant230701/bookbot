

def get_num_words(contents):
    words = contents.split()
    return len(words)


def get_char_dict(contents):
    dict = {}
    for c in contents:
        if c.lower() in dict:
            dict[c.lower()] += 1
        else:
            dict[c.lower()] = 1
    return dict

def dict_to_arr(dict):
    arr = []
    for k, v in dict.items():
        arr.append({'char': k, 'count': v})
    
    arr.sort(reverse=True, key=sort_on)
    return arr

def sort_on(entry):
    return entry['count']