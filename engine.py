def welcome_user():
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def run_game(game_module, game_description):
    name = welcome_user()
    print(game_description)
    
    correct_answers = 0
    max_rounds = 3
    
    while correct_answers < max_rounds:
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f"Congratulations, {name}!")
