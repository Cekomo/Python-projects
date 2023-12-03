import numpy as np
"""
Create a program that takes user input to create two matrices and performs basic operations such as addition, subtraction, and multiplication using NumPy. Ensure that your program handles input validation. (Valid operators: '+', '-', '*', '/', '.')
"""

class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.input = user_input
        super().__init__(self.message)


class NumpyController():
    def __init__(self):
        self.first_array = []
        self.second_array = []
        self.operator = ""

    def process_input(self, equation):
        input_array = equation.split()
        self.operator = input_array[1]
        self.first_array = np.append(self.first_array, eval(input_array[0]))
        self.second_array = np.append(self.second_array, eval(input_array[2]))

        if len(input_array) > 3:
            raise CustomException("There must be two arrays and single operator.")

    def execute_operation(self):
        if self.operator == '+':
            return self.first_array + self.second_array
        elif self.operator == '-':
            return self.first_array - self.second_array
        elif self.operator == '*':
            return self.first_array * self.second_array
        elif self.operator == '.':
            return np.dot(self.first_array, self.second_array)
        elif self.operator == '/':
            return self.first_array / self.second_array
        else:
            raise CustomException("Operator cannot be a character than those: '+', '-', '*', '/', '.'.")

numpy_controller = NumpyController()

while True:
    user_input = input("Please provide equation in this format: [x,y,z] * [a,b,c]. Matrice size, operator and variables can be changed arbitrarily:\n")
    if user_input == "q":
        break
    try:
        numpy_controller.process_input(user_input)
        print(numpy_controller.execute_operation())
    except CustomException as ce:
        print(f"Error: {ce.message}\nInput: {ce.input}")
    except NameError:
        print("Invalid input is provided.")
    except TypeError:
        print("There must be blanks left in between array and operator.")
    except IndexError:
        print(f"Invalid number of elements is typed.")
    except SyntaxError:
        print("Invalid array syntax formation.")
    except ValueError:
        print("Dimension of matrixes must be the same.")

# [3,4,7] * [5,6,2]
