from VD_games.engine import run_game
from VD_games.games import prime

def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(prime, description)

if __name__ == "__main__":
    main()
