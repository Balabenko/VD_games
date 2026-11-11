import random

def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    match operator:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2
        case _:
            raise ValueError("Неизвестный оператор")
            
    question = f"{num1} {operator} {num2}"
    return question, str(correct_answer)
