from VD_games.engine import run_game
from VD_games.games import calc

def main():
    description = "What is the result of the expression?"
    run_game(calc, description)

if __name__ == "__main__":
    main()
