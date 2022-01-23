from models.players import *

player_rock = Player("Rock Guy", "rock")
player_scissors = Player("Scissors Guy", "scissors")
# player_paper = Player("Paper Guy", "paper")
# player_rock_2 = Player("Rocky Pretender", "rock")
players = [player_rock, player_scissors]

def play_game(self, playerA, playerB):
        if playerA.choice == playerB.choice:
            self.winner = None
        elif playerA.choice == "rock" and playerB.choice == "scissors":
            self.winner = playerA.player_name
        elif playerA.choice == "rock" and playerB.choice == "paper":
            self.winner = playerB.player_name
        elif playerA.choice == "paper" and playerB.choice == "rock":
            self.winner = playerA.player_name
        elif playerA.choice == "paper" and playerB.choice == "scissors":
            self.winner = playerB.player_name
        elif playerA.choice == "scissors" and playerB.choice == "paper":
            self.winner = playerA.player_name
        elif playerA.choice == "scissors" and playerB.choice == "rock":
            self.winner = playerB.player_name
            return self.winner 