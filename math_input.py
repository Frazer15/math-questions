class inputs:
    class addition2:
        def addition_norm(self,a,b):
            inn = input("what is " + str(a) + " plus " + str(b))
            return inn

        def addition_alge(self,a,b):
            inn = input(str(a) + " plus what equals " + str(b))
            return inn

    class addition3:
        def addition_norm(self,a,b,c):
            inn = input("what is " + str(a) + " plus  " + str(b) + " plus " + str(c))
            return inn

        def addition_alge(self,a,b,c):
            inn = input(str(a) + " plus " + str(b) + " plus what equals " + str(c))
            return inn

    class subtraction2:
        def subtraction_norm(self,a,b):
            inn = input(str(a) " minus " + str(b) + " equals what")
            return inn

        def subtraction_alge(self,a,b):
            inn = input(str(a) + " minus what equals " + str(b))
            return inn

    class subtraction3:
        def subtraction_norm(self,a,b,c):
            inn = input(str(a) + " minus " + str(b) + " minus " + str(c) + "equals what")
            return inn

        def subtraction_alge(self,a,b,c):
            inn = input(str(a) + " minus " + str(b) + " minus what equals " + str(c))
            return inn

    class multiplication2:
        def multiplication_norm(self,a,b):
            inn = input("what is " + str(a) + " times " + str(b))
            return inn

        def multiplication_alge(self,a,b):
            inn = input(str(a) + " times what equals " + str(b))
            return inn

    class multiplication3:
        def multiplication_norm(self,a,b,c):
            inn = input("what is " + str(a) + " times " + str(b) + " times " + str(c))
            return inn

        def multiplication_alge(self,a,b,c):
            inn = input(str(a) + " times " + str(b) + " times what equals " + str(c))
            return inn

    class division2:
        def division_norm(self,a,b):
            inn = input(str(a) + " divided by " + str(b) + " equals what ")
            return inn

        def division_alge(self,a,b):
            inn = input(str(a) + " is divided by what equals " + str(b))
            return inn

    class division3:
        def division_norm(self,a,b,c):
            inn = input(str(a) + " divided by " + str(b) + " and divided" + str(c) + "equals ")
            return inn

        def division_alge(self,a,b,c):
            inn = input(str(a) + " divided by " + str(b) + " and divided by what equals " + str(c))
            return inn