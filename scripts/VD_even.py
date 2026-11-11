import random

def welcome_user():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def play_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()
        
        # Определяем правильный ответ
        correct_answer = "yes" if number % 2 == 0 else "no"
        
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при ошибке
            
    print(f"Congratulations, {name}!")

def main():
    play_even_game()

if __name__ == "__main__":
    main()
