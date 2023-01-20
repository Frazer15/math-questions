# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math_input
import problemGenerator


def math_answers(c,d):
    try:
        if int(d) == c:
            print("you are correct good job")
        else:
            print("so close, the answer was " + str(c))
    except:
        print("that is not an integer")
def main():
    math_type = input("what kind of math would you like to work on, (+,-,*,/)")
    math_hardness = input("how difficult would you like the math to be, (easy, medium, hard )")
    algebra = input("would you like some algebra to be involved, (yes,no)")
    if math_type == "*" or math_type == "multiplication":
        if math_hardness == "easy":
            if algebra == "yes":
                while "true":
                    chance, total, l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is x if, " + str(l1st["b"]) + " * x = " + str(total))
                        math_answers(l1st["a"],d)
                    else:
                        d = input("what is x if " + str(l1st["b"]) + " * " + str(l1st["c"]) + " * x = " + str(total))
                        math_answers(l1st["a"], d)

            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]))
                        math_answers(total,d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]) + " * " + str(l1st["c"]))
                        math_answers(total, d)
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.multiply_or_divide()
                    if chance == 2:
                        d = input("what is x if , " + str(l1st["a"]) + " * x = " + str(total))
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if , " + str(l1st["c"])+ " * "+ str(l1st["a"]) + " * x = " + str(total))
                        math_answers(l1st["b"],d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.multiply_or_divide()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]))
                        math_answers(total, d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]) + " * " + str(l1st["c"]))
                        math_answers(total,d)
        elif math_hardness == "hard":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.multiply_or_divide()
                    if chance == 2:
                        d = input("what is x if , " + str(l1st["a"]) + " * x = " + str(total))
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if , " + str(l1st["c"])+ " * "+ str(l1st["a"]) + " * x = " + str(total))
                        math_answers(l1st["b"],d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.multiply_or_divide()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]))
                        math_answers(total, d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " * " + str(l1st["b"]) + " * " + str(l1st["c"]))
                        math_answers(total,d)
        else:
            pass
    elif math_type == "+" or math_type == "addition":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    chance, total, l1st= problemGenerator.problem_generator.basic.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if,  " + str(total) + " = " + str(l1st["a"]) + " + x")
                        math_answers(l1st["b"],d)
                    else:
                        d = input("what is x if,  " + str(total) + " = " + str(l1st["a"]) + " + " + str(l1st["b"]) + " + " + " x")
                        math_answers(l1st["c"],d)
            elif algebra == "no":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]))
                        math_answers(total,d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]) + " + " + str(l1st["c"]))
                        math_answers(total, d)
            else:
                pass
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if , " + str(l1st["a"]) + " +  x  = " + str(total))
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if , " + str(l1st["a"]) + " + " + str(l1st["c"]) +" +  x  = " + str(total))
                        math_answers(l1st["b"], d)
            elif algebra == "no":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]))
                        math_answers(total, d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]) + " + " + str(l1st["c"]))
                        math_answers(total, d)
            else:
                pass
        elif math_hardness == "hard":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if , " + str(l1st["a"]) + " +  x  = " + str(total))
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if , " + str(l1st["a"]) + " + " + str(l1st["c"]) +" +  x  = " + str(total))
                        math_answers(l1st["b"], d)
            elif algebra == "no":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]))
                        math_answers(total, d)
                    else:
                        d = input("what is " + str(l1st["a"]) + " + " + str(l1st["b"]) + " + " + str(l1st["c"]))
                        math_answers(total, d)
        else:
            pass
    elif  math_type == "-" or math_type == "subtraction":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - x")
                        math_answers(l1st["b"],d)
                    else:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - " +str(l1st["c"]) + " - x")
                        math_answers(l1st["b"], d)
            elif algebra == "no":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]))
                        math_answers(l1st["a"],d)
                    else:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]) + " - " + str(l1st["c"]))
                        math_answers(l1st["a"], d)
            else:
                pass
        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - x" )
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - " + str(l1st["c"]) + " - x")
                        math_answers(l1st["b"], d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]))
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]) + " - " + str(l1st["c"]))
                        math_answers(l1st["a"], d)
        elif math_hardness == "hard":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.add_or_subtract()
                    if chance == 2:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - x" )
                        math_answers(l1st["b"], d)
                    else:
                        d = input("what is x if, " + str(l1st["a"]) + " = " + str(total) + " - " + str(l1st["c"]) + " - x")
                        math_answers(l1st["b"], d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.add_or_subtract()
                    if chance == 2:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]))
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is " + str(total) + " - " + str(l1st["b"]) + " - " + str(l1st["c"]))
                        math_answers(l1st["a"], d)
        else:
            pass
    elif  math_type == "/" or math_type == "division":
        if math_hardness == "easy":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is x if , " + str(l1st["a"]) + " = " + str(total) + " / x")
                        math_answers(l1st["b"],d)
                    else:
                        d = input("what is x if , " + str(l1st["a"]) + " = " + str(total) + " / " + str(l1st["c"])  +" / x")
                        math_answers(l1st["ab"],d)
            elif algebra == "no":
                while True:
                    chance, total,l1st = problemGenerator.problem_generator.basic.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is " + str(total) + " /  " + str(l1st["b"]))
                        math_answers(l1st["a"],d)
                    else:
                        d = input("what is " + str(total) + " / " + str(l1st["b"]) + " / " + l1st["c"])
                        math_answers(l1st["a"],d)
            else:
                pass

        elif math_hardness == "medium":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is x if, " + str(l1st["b"]) + " = " + str(total) + " / x")
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is x if, " + str(l1st["c"]) + " = " + str(total) + " / " + str(l1st["b"]) + " / x")
                        math_answers(l1st["a"],d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.intermediate.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is " + str(total) + " / " + str(l1st["b"]))
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is " + str(total) + " / " + str(l1st["b"]) + " / " + str(l1st["c"]))
                        math_answers(l1st["a"],d)
        elif math_hardness == "hard":
            if algebra == "yes":
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is x if, " + str(l1st["b"]) + " = " + str(total) + " / x")
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is x if, " + str(l1st["c"]) + " = " + str(total) + " / " + str(l1st["b"]) + " / x")
                        math_answers(l1st["a"],d)
            else:
                while True:
                    chance, total, l1st = problemGenerator.problem_generator.hard.multiply_or_divide()
                    if int(chance) == 2:
                        d = input("what is " + str(total) + " / " + str(l1st["b"]))
                        math_answers(l1st["a"], d)
                    else:
                        d = input("what is " + str(total) + " / " + str(l1st["b"]) + " / " + str(l1st["c"]))
                        math_answers(l1st["a"],d)
        else:
            pass
    else:
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
