import random
class problem_generator:
    possible_variables = {0 :"a", 1 : "b", 2 : "c", 3 : "d" }
    class basic:
        def add_or_subtract(self):
            maybe = random.randint(2, 3)
            possible_values = {}
            total = 0
            if maybe == 2:

                for i in range(0, maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(0, 50)
                    total += possible_values[variable]

            else:
                for i in range(0, maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(-50, 50)
                    total += possible_values[variable]
            return maybe, total, possible_values
        def multiply_or_divide(self):
            maybe = random.randint(2,3)
            possible_values = {}
            total = 0

            if maybe == 2:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(1, 12)
                    total *= possible_values[variable]
            else:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(1, 5)
                    total *= possible_values[variable]
            return maybe, possible_values, total
    class intermediate:

        def add_or_subtract(self):
            maybe = random.randint(2,3)
            possible_values = {}
            total = 0
            if maybe == 2:

                for i in range(0,maybe):

                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(-50,50)
                    total += possible_values[variable]
            else:
                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(-25, 25)
                    total += possible_values[variable]
            return maybe, total, possible_values
        def multiply_or_divide(self):
            maybe = random.randint(2,3)
            possible_values = {}
            total = 0

            if maybe == 2:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    num = random.randint(1, 25)
                    if num != 13:
                        num = num - 13
                    else:
                        num = 12
                    possible_values[variable] = num
                    total *= possible_values[variable]
            else:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    num = random.randint(1, 13)
                    if num != 7:
                        num = num - 7
                    else:
                        num = 6
                    possible_values[variable] = num
                    total *= possible_values[variable]
            return maybe, possible_values, total

    class hard:
        def add_or_subtract(self):
            maybe = random.randint(2,3)
            possible_values = {}
            total = 0
            if maybe == 2:

                for i in range(0,maybe):

                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(-500,500)
                    total += possible_values[variable]
            else:
                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    possible_values[variable] = random.randint(-250, 250)
                    total += possible_values[variable]
            return maybe, total, possible_values

        def multiply_or_divide(self,):
            maybe = random.randint(2,3)
            possible_values = {}
            total = 0

            if maybe == 2:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    num = random.randint(1, 41)
                    if num != 21:
                        num = num - 21
                    else:
                        num = 20
                    possible_values[variable] = num
                    total *= possible_values[variable]
            else:

                for i in range(0,maybe):
                    variable = problem_generator.possible_variables[i]
                    num = random.randint(1, 21)
                    if num != 11:
                        num = num - 11
                    else:
                        num = 10
                    possible_values[variable] = num
                    total *= possible_values[variable]
            return maybe, possible_values, total









