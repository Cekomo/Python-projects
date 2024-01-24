import numpy as np
import pandas as pd

class LinearRegression():
    def __init__(self) -> None:
        pass

    def calculate_axis_median(self, axis_coordinates):
        total_sum = sum(axis_coordinates)
        return total_sum / len(axis_coordinates)
    
