# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------
# Two types of functions
# 1- Functions that perform a task
# 2- Functions that return a value

# ----------------------------------------------------------
# Perform a task
def greet(first_name, last_name):  # two parameters
    print(f"Hell0 {first_name} {last_name}")
    print("This is my Function")


# two attributes are passed to the function when called
greet("Justin", "Puzey")


# ----------------------------------------------------------
# Function that returns a value
def get_name(first_name, last_name):  # two parameters
    return f"Greetings. My first name is: {first_name} , and my last name is: {last_name}"


# Function is called and passes attributes. formatted message is returned and stored in variable
message = get_name("Justin", "Puzey")
print(message)


# ----------------------------------------------------------
# Make code more readable using KEYWORD ARGUMENTS
def increment(number, by):
    return number + by


# passes attributes to 'increment' function and stores result in variable 'result'
result = increment(3, 2)
print(result)


# Make code more readable using KEYWORD ARGUMENTS
def increment_by(number, by):
    return number + by


# function is nested within print rather than stored in variable, since varable is not used anywhere else
# make arguments more readable by adding Keyword Argueements
print(increment_by(number=3, by=4))

# ----------------------------------------------------------
# Optional parameters


def increment_default(number, by=1):  # assign defalut value
    return number + by


# make arguments more readable by adding Keyword Argueements
# no attribute passed for the second parameter,which will use the default
print(increment_default(number=3))

# ----------------------------------------------------------
# PASSING A VARIABLE NUMBER OF ARGUMENTS
print(f"\nReults from xargs and xxargs")


# xargs
def multiply(*numbers):  # single '*' allows passing multiple arguments to create a 'Tuple' (similar to list or array) that can be iterated over
    total = 1
    for number in numbers:
        # augmented assignment operator. (same as total = total * number).
        total *= number
    return total


# calls 'multiply' function and passes multiple arguments
print(multiply(4, 8, 1, 5))


# xxargs - allows the passing of variable number of keyword arguments output is a dictionary object
def create_user(**user):
    print(user)
    print(user["name"])


create_user(id=1, name="justin", age=40)
