def find_word_lengths(words):
    return {word: len(word) for word in words}

def switch_name_and_id(data):
    return {v: k for k, v in data.items()}

def create_multiplication_table(multiplier, limit):
    if limit == 0:
        return {}
    
    return {num_ele: num_ele * multiplier for num_ele in range(1, limit + 1)}