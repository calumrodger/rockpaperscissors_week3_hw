import unittest
from models.players import Player
from models.game import Game

class TestPlayers(unittest.TestCase):
    def setUp(self):
        self.player_rock = Player("Rock Guy", "rock")
        self.player_scissors = Player("Scissors Guy", "scissors")
        self.player_paper = Player("Paper Guy", "paper")
        self.player_rock_2 = Player("Rock Guy Two", "rock")
        self.game1 = Game(None)

    def test_player_has_name(self):
        self.assertEqual("Rock Guy", self.player_rock.player_name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player_rock.choice)

    def test_play(self):
        self.game1.play_game(self.player_rock, self.player_rock_2)
        self.assertEqual(None, self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_scissors)
        self.assertEqual("Rock Guy", self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_rock_2)
        self.assertEqual(None, self.game1.winner)
        self.game1.play_game(self.player_scissors, self.player_rock)
        self.assertEqual("Rock Guy", self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_paper)
        self.assertEqual("Paper Guy", self.game1.winner)
        self.game1.play_game(self.player_paper, self.player_scissors)
        self.assertEqual("Scissors Guy", self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_rock_2)
        self.assertEqual(None, self.game1.winner)
        self.game1.play_game(self.player_paper, self.player_rock)
        self.assertEqual("Paper Guy", self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_rock_2)
        self.assertEqual(None, self.game1.winner)
        self.game1.play_game(self.player_rock, self.player_paper)
        self.assertEqual("Paper Guy", self.game1.winner)

   