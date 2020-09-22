def is_isogram(string):
    all_uppercase_alpha = [i.upper() for i in string if i.isalpha()]
    return len(all_uppercase_alpha) == len(set(all_uppercase_alpha))