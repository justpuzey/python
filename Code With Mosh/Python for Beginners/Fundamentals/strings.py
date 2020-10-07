# pull substring
string = "This is a string"
print(string[0:4])  # returns 1st through 5th characters
print(string[-1])  # returns last character
print(string[:3])  # returns 1st through 4th characters

# Escaping
# escape sequence quotes to be included as part of string
escape_string = "Python \"Programming\""
# adds return which moves second half of string to a new line
escape_return = "return \nnew line"
print(escape_string)
print(escape_return)
# add a tab with \t
print("\tThis line has been \"tabbed\" using \\t")
# add text over multiple lines using """
print("""\nWith the three double-qotes,
we will be able to add as much 
text as we would like\n""")

# FORMATTED STRINGS
first = "Justin"
last = "Puzey"
full_concat = first + last
full_formated = f"{first} {last}"  # replaces text in {} at runtime
print(full_concat)
print(full_formated)

# another method of formatting strings using .format()
formatter = "{} {} {} {}"
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "or a song"
))


# STRING METHODS
string = "This is a string "
print(f"{first} {last}".upper())
print(string.title())  # Capitalizes the first letter of each word in a string
print(string.strip())  # Trims blank space from ends of strings
print(string.find("is"))  # Returns index of substring if found in String
print(string.replace("a", "not a"))
# Returns boolean value rather than index if substring is found in string
print("is" in string)
print("is" not in string)
