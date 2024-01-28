import numpy as np
import pandas as pd

class LinearRegression():
    def __init__(self) -> None:
        pass


    def get_mean(self, axis_coordinates):
        total_sum = np.nansum(list(axis_coordinates))
        return total_sum / len(axis_coordinates)
    

    def calc_diff_btw_median_and_samples(self, the_dict, mean, power):
        return [abs(float(value) - mean)**power for value in the_dict]
    

    def calc_linear_regression_slope(self, dict, x_mean, y_mean):
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in 
                        zip(dict.keys(), dict.values())
                        if not np.isnan((x - x_mean) * (y - y_mean)))
        denominator = sum((x - x_mean)**2 for x in dict.keys()
                          if not np.isnan((x - x_mean)**2))
        return numerator / denominator

    def calc_linear_regression_constant(self, x_mean, y_mean, slope):
        return y_mean - slope * x_mean
    

    def fit_data_to_regression_line(self, x, slope, constant):
        print(f"Predicted output for {x} is: {round(constant + slope * x, 2)}")


    def print_lr_equation(self, slope, constant):
        print(f"Y = {round(constant, 2)} + {round(slope, 2)} * x")
