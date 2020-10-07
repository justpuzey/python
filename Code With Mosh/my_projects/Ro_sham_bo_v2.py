import random


class color:
    MAGENTA = '\u001b[35m'  # Colors are set using ANSI codes
    YELLOW = '\u001b[33m'
    ENDC = '\u001b[0m'


player = input("Ro-Sham-Bo: ").lower()
computer_index = random.randrange(0, 3)
computer_array = ["rock", "paper", "scissors"]
computer_selection = computer_array[computer_index]

WIN_COMBOS = [
    ["rock", "scissors"],
    ["scissors", "paper"],
    ["paper", "rock"]
]

if player == computer_selection:
    result = "It's a draw!"
elif [player, computer_selection] == WIN_COMBOS[0] or [player, computer_selection] == WIN_COMBOS[1] or [player, computer_selection] == WIN_COMBOS[2]:
    result = f"Player Wins! {player.capitalize()} beats {computer_selection} every time."
else:
    result = f"Sorry, computer wins. {computer_selection.capitalize()} beats {player}"

print(f"Player: {color.YELLOW}{player}{color.ENDC} Computer: {color.YELLOW}{computer_selection}{color.ENDC}")
print(f"Result: {color.MAGENTA}{result}{color.ENDC}")
