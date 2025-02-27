import random

def random_primer():
    rand = random.randint(-100,100)
    rand2 = random.randint(-100, 100)
    znak = random.choice(('*', '+', '-', '/'))
    return f"{rand} {znak} {rand2}"

def calculate(example):
    splitted_example = example.split(' ')
    first_num = int(splitted_example[0])
    znak = splitted_example[1]
    second_num = int(splitted_example[2])
    if znak == '+':
        correct_answer = first_num + second_num
    elif znak == '*':
        correct_answer = first_num * second_num
    elif znak == '-':
        correct_answer = first_num - second_num
    else:
        correct_answer = round(first_num / second_num, 2)
    return correct_answer

def check_answer(user_answer, correct_answer):
    if round(float(user_answer), 2) == round(correct_answer, 2):
        return True
    else:
        return False


