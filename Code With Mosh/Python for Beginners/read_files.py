#from sys import argv

#script, filename = argv

#txt = open(filename)

#print(f"Here's your file {filename}:")
# print(txt.read())

# -------------------------------------------------------------
# Read files by selecting name through input()
# -------------------------------------------------------------
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

close = input("ready to close?: ")

if close:
    txt_again.close
