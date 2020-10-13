# --------------------------------------------------------------------
# Pass a list to a Function
# --------------------------------------------------------------------

def greet_users(names):
    """Print a simple greeting to each user in the list. """
    for name in names:
        msg = f"Hello {name.title()} !"
        print(msg)


usernames = ['leslie', 'taylor', 'brinley', 'devin']
greet_users(usernames)


#
def build_person(first_name, last_name, middle_name='', age=''):
    """ Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


family_member = build_person('justin', 'puzey', middle_name='T', age=40)
print(family_member)
