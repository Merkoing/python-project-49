#!/usr/bin/env python3


from brain_games.games.games_engine import play
from brain_games.games import gcd_game


def main():
    play(gcd_game)


if __name__ == '__main__':
    main()