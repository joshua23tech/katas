# This function that accepts a string of any length, and replaces each letter
#  within each word with the corresponding index that that letter has in the
#  alphabet.
# You must have a space between each index number, and do NOT need to account
#  extra for spaces between words.


def alphabet_replace(sample_string):
    lst_response_indices = [str(i) for str_char in sample_string for i, L in enumerate('abcdefghijklmnopqrstuvwxyz', 1) if str_char == L.lower() or str_char == L.upper()]
    str_response_indices = " ".join(lst_response_indices)
    return str_response_indices