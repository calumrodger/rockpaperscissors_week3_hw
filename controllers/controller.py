from flask import render_template, request
from app import app
from models.players import Player
from models.players_list import players
from models.game import Game

@app.route("/")
def index():
    return "jello wrld"

@app.route("/<player1_choice>/<player2_choice>")
def play(player1_choice, player2_choice):
    player1 = Player("P-1", player1_choice)
    player2 = Player("P-2", player2_choice)
    game1 = Game(None)
    winner = game1.play_game(player1, player2)
    return render_template("index.html", welcome_message="howdy", game1=game1, player1=player1, player2=player2, winner=winner)

@app.route("/rules")
def rules():
    return render_template("rules.html", welcome_message="howdy")

@app.route("/play", methods=["POST"])
def computer_play():
    player_name = request.form["player_name"]
    player_choice = request.form["player_choice"]
    player1 = Player(player_name, player_choice)
    computer = Player(None, None)
    computer_choice = computer.add_computer_player()
    game1 = Game(None)
    winner = game1.play_game(player1, computer_choice)
    # new_player_game = Player(player_name, player_choice)
    # play_game_against_computer(new_player_game.player_choice)
    return render_template("computer_play.html", welcome_message="howdy", player_name=player_name, player_choice=player_choice, game1=game1, computer_name=computer_choice.player_name, computer_choice=computer_choice.choice)