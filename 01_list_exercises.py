"""
    The function should accept a list of names and return a list of greetings. It should work in the following way:
        create_greeting_strings('Simon') # [ 'Hello Simon!' ]
        create_greeting_strings('Cat', 'Danika') # [ 'Hello Cat!', 'Hello Danika!' ]
"""
def create_greeting_strings(names):
    return [f"Hello {name}!" for name in names]


"""
    The function should accept a list of numbers and a number to multiply them by. It should work in the following way:
        multiply_by_num([ 1, 2, 3 ], 2) # [ 2, 4, 6 ]
        multiply_by_num([ 5, 10, 20 ], 10) # [ 50, 100, 200 ]
"""
def multiply_by_num(num_list, multiplier):
    return [num_ele * multiplier for num_ele in num_list]


"""
    The function should accept a list of dictionaries. These dictionaries represent an employee and are in the following format:
    It should work in the following way:
    find_github_admins(
  [
    {
      "first_name": 'Joe',
      "last_name": 'Mulvey',
      "location": 'Liverpool-ish',
      "age": 22,
      'favourite_language': 'JavaScript',
      "github_admin": True
    },{
      "first_name": 'Kyle',
      "last_name": 'McPhail',
      "location": 'Manchester',
      "age": 21,
      'favourite_language': 'Python',
      "github_admin": False
    }
  ]
)

### Will return the following output:

[
  {
      "first_name": 'Joe',
      "last_name": 'Mulvey',
      "location": 'Liverpool-ish',
      "age": 22,
      'favourite_language': 'JavaScript',
      "github_admin": True
  }
]
"""
def find_github_admins(users):
    return [user for user in users if user["github_admin"] == True]


"""
    The function should accept a list of numbers. It should increment only the even numbers and return the list with those changes:
        increment_even_numbers([ 2, 4, 6 ]) # [ 3, 5, 7 ]
        increment_even_numbers([ 1, 3, 5 ]) # [ 1, 3, 5 ]
        increment_even_numbers([ 1, 2, 3, 4, 5 ]) # [ 1, 3, 3, 5, 5 ]
"""
def increment_even_numbers(number_list):
    return [num_ele + 1 if num_ele % 2 == 0 else num_ele for num_ele in number_list]


"""
    The function should accept a list of numbers. It should return a list containing only the numbers that are greater than 10 and divisible by 3:
        find_greater_than_ten_divisible_by_three([ 1, 5, 9, 16, 22, 100 ]) # [ ]
        find_greater_than_ten_divisible_by_three([ 15, 21, 60, 120 ]) # [ 15, 21, 60, 120 ]
        find_greater_than_ten_divisible_by_three([ 1, 45, 87, 3, 150, 276, 7155, 230, 1000, 7 ]) # [ 45, 87, 150, 276, 7155 ]
"""
def find_greater_than_ten_divisible_by_three(number_list):
    return [num_ele for num_ele in number_list if num_ele > 0 and num_ele % 3 == 0]


"""
    The function should accept a list of numbers and a single number n. It should return a list containing only the numbers that contain the digit n:
        find_numbers_containing_digit([ 123, 231, 312 ], 5) # [ ]
        find_numbers_containing_digit([ 15, 50, 555 ], 5) # [ 15, 50, 555 ]
        find_numbers_containing_digit([ 13, 72, 932, 127, 7052, 1926, 1027426, 920198382 ], 7) # [ 72, 127, 7052, 1027426 ]
"""
def find_numbers_containing_digit(number_list, digit):
    return [num_ele for num_ele in number_list if str(digit) in str(num_ele)]