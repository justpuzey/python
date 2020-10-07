# -------------------------------------------------------------------------
# PASSING ARGUMENTS TO EXTERNAL SCRIPTS (argv)
# -------------------------------------------------------------------------
# argv always passes document(script) name as first argument
# initializes all variable names for arguments passed
#script, two, three, four = argv
#print("Your 1st variable is:", script)
#print("Your second variable is:", two)
#print("Your third variable is:", three)
#print("Your 4th variable is:", four)
# when calling file, you must pass arguments to avoid errors (ex python3 temp.py apple orange grapefruit)
# -------------------------------------------------------------------------
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
