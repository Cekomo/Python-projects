import numpy as np
"""
Create a program that takes user input to create two matrices and performs basic operations such as addition, subtraction, and multiplication using NumPy. Ensure that your program handles input validation. (Valid operators: '+', '-', '*', '/', '.')
"""

class NumpyController():
    def __init__(self):
        self.first_array = []
        self.second_array = []
        self.operator = ""

    def process_input(self, equation):
        input_array = equation.split()
        self.first_array = np.append(self.first_array, eval(input_array[0]))
        self.second_array = np.append(self.second_array, eval(input_array[2]))
        self.operator = input_array[1]

    
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

numpy_controller = NumpyController()

input = input("Please provide equation in this format: [x,y,z] * [a,b,c]. Matrice size, operator and variables can be changed arbitrarily:\n")
numpy_controller.process_input(input)
print(numpy_controller.execute_operation())

# [3,4,7] / [5,6,2]