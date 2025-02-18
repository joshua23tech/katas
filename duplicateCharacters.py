"""
    Write a function that accepts a String and returns an Integer value representing the
    number of distinct duplicated characters within the String i.e. the number of characters
    that appear twice or more. 

    Your solution should be able to deal with all alphanumeric and special characters. Your
    solution should be able to treat upper and lower case characters as distinct characters. 

    For example:

    Given 'Aasdefsgh!!!' the expected result would be: '2' ('s' and '!' are duplicated).
"""

def solution(input):
    int_counter = 0 
    set_counted = set()
    int_str_len = len(input)

    while int_counter < (int_str_len - 1):
        if input[int_counter] in input[int_counter + 1:]:
            set_counted.add(input[int_counter])
        int_counter += 1 
    
    int_len_set = len(set_counted)
    return int_len_set

print(solution("Aasdefsgh!!!"))