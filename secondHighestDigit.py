"""
    Write a function that accepts a String and returns the second highest numerical digit in the input as an Integer. 
    The following rules should apply:
        1) Inputs with no numerical digits should return -1 
        2) Inputs with only one numerical digit should return -1
        3) Non-numeric characters should be ignored
        4) Each numerical input should be treated individually; this means in the event of a joint highest digit then 
           the second highest digit will also be the highest digit.
    
    For example:
        "acb:1231234" returns 3 
        "123123" returns 3
"""

def solution(input):
    lst_str_chars = list(input)
    lst_str_ints = [str_char for str_char in lst_str_chars if str_char in '0123456789']

    if len(lst_str_ints) < 2:
        return -1 
    
    lst_ints_confirmed = [int(str_int) for str_int in lst_str_ints]
    lst_ints_sorted = sorted(lst_ints_confirmed)

    return lst_ints_sorted[-2]

print(solution("acb:1231234"))
print(solution("123123"))