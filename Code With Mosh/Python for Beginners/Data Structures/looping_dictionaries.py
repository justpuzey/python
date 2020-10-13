user={
    'username' : 'jpuzey',
    'first':'justin',
    'last':'puzey',
}

for key,value in user.items():
    print(f"key: {key}")
    print(f"value: {value}\n")


favorite_languages = {
    'justin' : 'Python',
    'Taylor' : 'Ruby',
    'Brinley' : 'C#',
    'Cameron' : 'Javascript',
    'Ashlyn' : 'Python',
    'Devin' : 'HTML',
}

daughters = ['Brinley','Ashlyn']

for kid in favorite_languages.keys():
    print(kid.title())

    if kid in daughters:
        print(f"Hey {kid.title()} I understand that your favorite language is {favorite_languages[kid]}")

print(f"\nThe languages mentioned by your kids are:")
for language in set(favorite_languages.values()): #the 'set' function creates a set of unique values
    print(language.title())


