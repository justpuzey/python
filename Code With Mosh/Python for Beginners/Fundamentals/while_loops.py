# Moving items from one list to another with while loop
unconfirmed_users = ['alice', 'brian', 'candace', 'justin', 'leslie']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of a specific value from a list
pet_types = ['dog', 'cat', 'fish', 'rabbit', 'dog', 'cat',
             'fish', 'rabbit', 'dog', 'cat', 'fish', 'rabbit']
print(pet_types)

while 'cat' in pet_types:
    pet_types.remove('cat')

print(pet_types)


# --------------------------------------------------------------------
# Filling a Dictionary with User Input
# --------------------------------------------------------------------

responses = {}
# Set a flag to indicate that the polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input(f"\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input(f"would  you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print(f"\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

print(responses)
