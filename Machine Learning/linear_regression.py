import numpy as np
import pandas as pd

class LinearRegression():
    def __init__(self) -> None:
        pass

    def get_median(self, axis_coordinates):
        total_sum = sum(axis_coordinates)
        return total_sum / len(axis_coordinates)
    

    def calc_diff_btw_median_and_samples(self, the_dict, mean, power):
        return [abs(float(value) - mean)**power for value in the_dict]
    

    def calc_linear_regression_slope(self, dict, x_mean, y_mean):
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in 
                        zip(dict.keys(), dict.values()))
        denominator = sum((x - x_mean)**2 for x in dict.keys())
        return numerator / denominator
    

    def calc_linear_regression_constant(self, x_mean, y_mean, slope):
        return y_mean - slope * x_mean
    

    def fit_data_to_regression_line(self, x, slope, constant):
        print(constant + slope * x)

