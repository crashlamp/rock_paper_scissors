import random

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        while True:
            move = input("Rock, paper or scissors?")
            if move in moves:
                return move


    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.round = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


    def play_round(self):
        self.round += 1
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = f"* * * PLAYER ONE WINS ROUND {self.round}! * * *\n"
        elif self.beats(move2, move1):
            self.score_p2 += 1
            winner = f"* * * PLAYER TWO WINS ROUND {self.round}! * * *\n"
        else:
            winner = "* * * TIE! * * *\n"
        print(
            f"> You played: {move1}"
            f"\n> Opponent played: {move2}"
            f"\n\n{winner}"
            f"\nThe score is"
            f"\nPlayer One: {self.score_p1}\tPlayer Two: {self.score_p2}"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Starting Game!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        while True:
            if self.score_p1 == self.score_p2:
                print("* * * TIEBREAKER! * * *")
                self.play_round()
            elif self.score_p1 > self.score_p2:
                print("* * * YOU HAVE WON THE GAME! * * *")
                print("Game over!\n\n")
                game.play_game()
            else:
                print("* * * YOU HAVE BEEN DEFEATED! * * *")
                print("Game over!\n\n")
                game.play_game()


if __name__ == '__main__':
    game = Game(Player(), RandomPlayer())
    game.play_game()
