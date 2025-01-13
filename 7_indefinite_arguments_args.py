# args = allows you to pass multiple non-key arguments
# kwargs = allows you to pass multiple keyword-arguments 
#           unpaking operator
#           1. positional 2. default 3. keyword 4. ARBITRARY

# Arbitrary and random amount of arguments 
# def add(a, b):
#     return a + b
# print(add(1, 2, 3))
#  no work cuz too many arguments

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3))

# star matters not word in parameter

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ") #puts a space
    
# display_name( "Dr.","Spongebob","Harold","Squarepants", "III")

# kwargs

# only prints the actual element 

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# print_address(street="123 Cookie Rd.", 
#               city="Chicago", 
#               state="IL", 
#               zip="252323")

# does both elements

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Cookie Rd.", 
#               city="Chicago", 
#               state="IL", 
#               zip="252323")

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
