from sys import argv  # Import argv module

# -------------------------------------------------------------------------
# CAPTURING USER INPUT
# -------------------------------------------------------------------------
# user input is always a string
x = input("Type a number: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# TYPE CONVERSION
# int(x)
# float(x)
# bool(x)
# str(x)

# FALSEY VALVUES
# ""
# 0
# none
print(bool(0))

# -------------------------------------------------------------------------
# COMPARISON OPERATORS
# -------------------------------------------------------------------------
10 > 3
10 >= 3  # Evaluates values (greater-than or equal to)
10 == 10  # Evaluates values to determine if they are equal
9 != 10  # Evaluates values to determine if they are not equal

# -------------------------------------------------------------------------
# CONDITIONAL STATEMENTS
# -------------------------------------------------------------------------
temperature = y
if temperature > 30:
    print("it's warm")
else:
    print("it's not warm")

    # TERNARY OPERATOR | alternate conditional statement structure
message = "it's warm" if temperature > 30 else "it's not warm"
print(message)

# -------------------------------------------------------------------------
# LOGICAL OPERATORS
# -------------------------------------------------------------------------
# and
# or
# not

high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:  # no need to add '== True' to condition
    print("eligible for loan")
else:
    print("not eligible")

# Short Circuit | Python interpreter will stop evaluating the expression as soon as one of the arguements evaluates to False

# Chaining Comparison Operators
age = y
if 18 <= age < 65:  # expression is formatted similar to a mathmatecal expression
    print(age)
else:
    print("ineligible age")

# -------------------------------------------------------------------------
# LOOPS
# -------------------------------------------------------------------------
print(f"\nfor Loops")  # Just here as a heading
# for loop
# range() goes from first number to the second number, but does not include that number (1,2,3)
for number in range(1, 4):
    print("Iteration #:", number, number * ".")

for character in "String":  # strings are iterable and can be looped through
    print(character)

for item in ["iterate", "through", "Object", "List"]:
    print(item)

# for...else (early termination)
successful = 0
for number in range(3):
    print("Iteration #:", number)
    successful += 1
    if successful > 2:
        print("successful after", number, "attempts")
        break  # terminates loop
else:
    # this line only executes if early termination is not executed
    print("Attempted 3 times and failed")


# nested for loops
print(f"\nNested Loops")  # Just here as a heading

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# While loops
print(f"\nWhile Loops")  # Just here as a heading

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO:", command)
