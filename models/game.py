class Game:

    def __init__(self, winner):
        self.winner = winner

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
