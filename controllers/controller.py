from flask import render_template
from app import app
from models.players import Player
from models.players_list import players, play_game
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

@app.route("/play")
def computer_play():
    return render_template("computer_play.html", welcome_message="howdy")