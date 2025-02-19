from src.core import random_primer as rp, check_answer, calculate as calc, Points

def concol_app():
    create_points = Points()

    while True:

        primer = rp()
        print(primer)

        correct_answer = calc(example=primer)
        print(correct_answer)
        answer = float(input('введите ответ - '))
        result = check_answer(user_answer=answer, correct_answer=correct_answer)

        if result == True:
            create_points.plus_points()
        else:
            create_points.minus_points()

        print(f' у вас нищие {create_points.get_points()} очков')
