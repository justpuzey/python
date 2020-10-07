import random


class color:
    MAGENTA = '\u001b[35m'  # Colors are set using ANSI codes
    YELLOW = '\u001b[33m'
    ENDC = '\u001b[0m'


player = input("Ro-Sham-Bo: ").lower()
computer_index = random.randrange(0, 3)
computer_array = ["rock", "paper", "scissors"]
computer_selection = computer_array[computer_index]


if player == computer_selection:
    result = "Tie!"
elif player == "rock" and computer_selection == "paper":
    result = "Sorry, Computer Wins"
elif player == "scissors" and computer_selection == "paper":
    result = "scissors cut paper, You Win!"
elif player == "scissors" and computer_selection == "rock":
    result = "Sorry, Computer Wins"
elif player == "paper" and computer_selection == "rock":
    result = "Paper covers rock, You Win!"
elif player == "paper" and computer_selection == "scissors":
    result = "Sorry, Computer Wins"
elif player == (player == "rock" or player == "Rock") and computer_selection == "scissors":
    result = "Rock smashes scissors, You Win!"
else:
    result = "To be evaluated"

print(f"Player: {color.YELLOW}{player}{color.ENDC} Computer: {color.YELLOW}{computer_selection}{color.ENDC}")
print(f"Result: {color.MAGENTA}{result}{color.ENDC}")
print(computer_index)
