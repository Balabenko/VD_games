import random

def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]

def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    
    progression = generate_progression(start, step, length)
    
    hidden_index = random.randint(0, length - 1)
    
    correct_answer = str(progression[hidden_index])
    
    progression[hidden_index] = ".."
    
    question = " ".join(map(str, progression))
    
    return question, correct_answer
