import random

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    correct_answer = calculate_gcd(num1, num2)
    question = f"{num1} {num2}"
    
    return question, str(correct_answer)
