# --------------------------------------------------------
# CREATING A LIST
# --------------------------------------------------------
list1 = ["One", 1, "Two", True]
print(list1)  # displays all items in list
dir(list1)  # use to display actions that can be taken using the specified object

# ACCESSING LISTS ________________________________________
print(list1[0])  # access list item at specified location 0...
# access range of list items (will include items up to, but not including the last number)
print(list1[:2])
# access list items beginning at the end of the list and working back to beginning
print(f"Print second to last item in list: {list1[-2]}")

# Creating list using ranges
numbers = list(range(20))  # creates list of numbers 0-19
# prints all items in list by steps of 2 (every-other number)
print(numbers[::2])
print(f" sorted numbers: {numbers.sort(reverse=True)}")
print(sorted(numbers))

# --------------------------------------------------------
# PACKING/UNPACKING A LIST
# --------------------------------------------------------
list_elements = [1, 2, 3, 4, 5, 6, 7]
# Assigns each element in the list to a corresponding variable
# Using the '*' allow you to 'pack' all of the remaining elements into one variable
first_variable, second_variable, third_variable, *other_variable = list_elements
print(third_variable)
print(
    f"These are the elements that are packed into the 'other variable': {other_variable}")


# --------------------------------------------------------
# MODIFYING A LIST
# --------------------------------------------------------
# append(): Adds a new entry to the end of the list
# clear(): Removes all entries from the list
# copy(): Creates a copy of the current list and places it in a new list
# count(): Returns the number of instances that an element appears in a list
# extend(): Adds items from an existing list and into the current list
# index():
# insert(): Adds a new entry to the position specified in the list
# pop(): Removes an entry from the end of the list
# remove(): Removes an entry from the specified position in the list
# reverse(): Sorts list in reverse order
# sort():
list2 = []
print(
    f"\nMODIFYING A LIST: \nThis list currently contains {len(list2)} number of items")
list2.append("Appended Item")
print(f"same list with appended item added: {list2}")
list2.insert(0, "inserted element")
print(f"same list with item inserted at specific location: {list2}")
list3 = list2.copy()
print(
    f"this is a copy of list2. Commonly used to store temporary changes: {list3}")
list3.extend(["Extended", "List", "Elements"])
print(f"list3 has been extended with new elements: {list3}")
print(f"list2 has not: {list2}")

list4 = ["Create"] + ["Lists"] + ["Using"] + ["Concatenation"] + ["!"]*4
print(
    f"Use concatenation and multiplication operators to create lists: {list4}")

# --------------------------------------------------------
# ITERATING THROUGH A LIST
# --------------------------------------------------------
family = ["Justin",
          "Leslie",
          ["Taylor", "Giselle"],
          ["Chance", "Brinley"],
          "Cameron",
          "Ashlyn",
          'Devin']

for each_member in family:
    if isinstance(each_member, list):
        for child_family_member in each_member:
            print(child_family_member)
    else:
        print(each_member)

# using 'enumerate'_____________________________________________________________
letters = ["a", "b", "c"]

# 'enumerate function creates index for each of the items iterated through
for index, letter in enumerate(letters):
    print(index, letter)

# Recursive function to perform same operation
print("\n Extended Family")
extended_family = ["Justin",
                   "Leslie",
                   ["Taylor", "Giselle", ["Grandkid1", "Grandkid Spouse"], ["Baby2"]],
                   ["Chance", "Brinley", ["Baby3"]],
                   "Cameron",
                   "Ashlyn",
                   'Devin']


def print_list(parameter_list):
    for each_list_item in parameter_list:
        if isinstance(each_list_item, list):
            print_list(each_list_item)
        else:
            print(each_list_item)


print_list(extended_family)
print(extended_family[2][2][0])


# --------------------------------------------------------
# SEARCHING THROUGH A LIST
# --------------------------------------------------------


colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
print(colors)

color_select = ""

while str.upper(color_select) != "QUIT":
    color_select = input("Type a color: ")
    if (colors.count(color_select) >= 1):
        print(f"The color exists in the list!")
    elif (str.upper(color_select) != "QUIT"):
        print("The list doesn't contain the color.")
