# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import problemGenerator


def math_answers(c,d):
    if int(d) == c:
        print("you are correct good job")
    else:
        print("so close, the answer was " + str(c))

def main():
    math_type = input("what kind of math would you like to work on, (+,-,*,/)")
    math_hardness = input("how difficult would you like the math to be, (easy, medium, hard )")
    algebra = input("would you like some algebra to be involved, (yes,no)")
    if math_type == "*" or math_type == "multiplication":
        if math_hardness == "easy":
            if algebra == "yes":
                while "true":
                    chance, total, l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    if int(l1st[0]) == 2:
                        d = input("what is x if , " + str(total) + " = " + str(l1st[1]) + " * x")
                        math_answers(l1st[0],d)
                    else:
                        d = input("what is x if , " + str(total) + " = " + str(l1st[1]) + " * " + str(l1st[2]) + " * x")
                        math_answers(l1st[0], d)

            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    d = input("what is " + str(l1st[0]) + " times " + str(l1st[1]))
                    math_answers(total,d)
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    l1st = inter_multiplication()
                    d = input("what is x if , " + str(l1st[0]) + " times x = " + str(l1st[2]))
                    math_answers(l1st[1], d)
            else:
                while True:
                    l1st = inter_multiplication()
                    d = input("what is " + str(l1st[0]) + " times " + str(l1st[1]))
                    math_answers(l1st[2], d)
        else:
            pass
    elif math_type == "+" or math_type == "addition":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    l1st= basic_algebra_addition()
                    d = input("what is x if,  " + str(l1st[1]) + " = " + str(l1st[0]) + " + x")
                    math_answers(l1st[2],d)
            elif algebra == "no":
                while True:
                    l1st = basic_addition()
                    d = input("what is " + str(l1st[0]) + " plus " + str(l1st[1]))
                    math_answers(l1st[2],d)
            else:
                pass
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    l1st = inter_addition()
                    d = input("what is x if , " + str(l1st[0]) + " plus  x  = " + str(l1st[2]))
                    math_answers(l1st[1], d)
            elif algebra == "no":
                while True:
                    l1st = inter_addition()
                    d = input("what is " + str(l1st[0]) + " plus " + str(l1st[1]))
                    math_answers(l1st[2], d)
            else:
                pass

        else:
            pass
    elif  math_type == "-" or math_type == "subtraction":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    l1st = basic_algebra_subtraction()
                    d = input("what is x if, " + str(l1st[1]) + " = " + str(l1st[0]) + " - x")
                    math_answers(l1st[2],d)
            elif algebra == "no":
                while True:
                    l1st = basic_subtraction()
                    d = input("what is " + str(l1st[0]) + " minus " + str(l1st[1]))
                    math_answers(l1st[2],d)
            else:
                pass
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    l1st = inter_subtraction()
                    d = input("what is x if, " + str(l1st[2]) + " = " + str(l1st[0]) + " - x" )
                    math_answers(l1st[1], d)
            else:
                while True:
                    l1st = inter_subtraction()
                    d = input("what is " + str(l1st[0]) + " minus " + str(l1st[1]))
                    math_answers(l1st[2], d)
        else:
            pass
    elif  math_type == "/" or math_type == "division":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    l1st = basic_algebra_division()
                    d = input("what is x if , " + str(l1st[1]) + " = " + str(l1st[0]) + " / x")
                    math_answers(l1st[2],d)
            elif algebra == "no":
                while True:
                    l1st = basic_division()
                    d = input("what is " + str(l1st[0]) + " divided by " + str(l1st[1]))
                    math_answers(l1st[2],d)
            else:
                pass

        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    l1st = inter_division()
                    d = input("what is x if, " + str(l1st[2]) + " = " + str(l1st[1]) + " divided by x")
                    math_answers(l1st[0], d)
            else:
                while True:
                    l1st = inter_division()
                    d = input("what is " + str(l1st[2]) + " divided by " + str(l1st[1]))
                    math_answers(l1st[0], d)
        else:
            pass
    else:
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
