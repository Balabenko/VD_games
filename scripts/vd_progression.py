from VD_games.engine import run_game
from VD_games.games import progression

def main():
    description = "What number is missing in the progression?"
    run_game(progression, description)

if __name__ == "__main__":
    main()
