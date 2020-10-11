colors = {"Sam": "Violet", "Amy": "Red", "Sarah": "Yellow"}
print(colors)
print(colors["Sarah"])
print(colors.keys())


def iterate_favs(param):
    for item in colors.keys():
        print(f"{item} likes the color {colors[item]}.")


iterate_favs(colors)

colors["Sam"] = "Blue"  # Changes the value assigned to Item
colors.update({"Harry": "Orange"})  # Adds new item to the dictionary
print(colors)
iterate_favs(colors)


del colors["Amy"]  # Removes item from dictionary
print(colors)
iterate_favs(colors)

len(colors)
print(f"Dictionary currently has {len(colors)} items")
colors.clear()
print(f"Dictionary currently has {len(colors)} items")


# --------------------------------------------------------------
# Switch
# ---------------------------------------------------------------

def PrintBlue():
    print("You chose blue!\r\n")


def PrintRed():
    print("You chose red!\r\n")


def PrintOrange():
    print("You chose orange!\r\n")


def PrintYellow():
    print("You chose yellow!\r\n")


# This is a dictionary that works like a case statement in other languages
ColorSelect = {
    0: PrintBlue,
    1: PrintRed,
    2: PrintOrange,
    3: PrintYellow
}

Selection = 0
while (Selection != 4):
    print("0. Blue")
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Quit")

    Selection = int(input("Select a color option: "))

    if (Selection >= 0) and (Selection < 4):
        ColorSelect[Selection]()

