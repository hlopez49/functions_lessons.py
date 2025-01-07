from determineEligibility import determinEligibilty_toGraduate, listOfMovies
# functions are way to wrap your code
# into resonable units


# #define a function with def 
# def say_hello():
#       print("Hello!")
#       print("How are you?")
    
# # call the function 
# say_hello()

# #when I pass in a parameter
# # I am passing in a placeholder 
# # for future info


# #define a function with def 
# def say_hello(name,age,address):
#       print(f"Hello! {name}")
#       print(f"How are you? {name}")
#       print(f"{name} are {age} years old")
#       print(f"You live at {address}")
    
# # call the function 
#       #pass in info called an argument
# say_hello("Alice",66, "123 Main St")
# say_hello("Sumire",56, "967 Cookie Rd")



# determinEligibilty_toGraduate("Sumire", 120, 4.0, 1500)
# determinEligibilty_toGraduate("Ryuji", 120, 1.9, 600)

# listOfMovies("Rise_Of_Fhantoms", 20, "action")

# the return statement is
# used to return a value from a function

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
