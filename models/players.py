import random

class Player:

    def __init__(self, player_name, choice):
        self.player_name = player_name
        self.choice = choice

    def add_computer_player(self):
        self.player_name = "Computer"
        self.player_choice = random.choice(["rock", "scissors", "paper"])
        computer_player = Player(self.player_name, self.player_choice)
        return computer_player