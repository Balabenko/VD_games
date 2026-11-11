from VD_games.engine import run_game
from VD_games.games import gcd

def main():
    description = "Find the greatest common divisor of given numbers."
    run_game(gcd, description)

if __name__ == "__main__":
    main()
