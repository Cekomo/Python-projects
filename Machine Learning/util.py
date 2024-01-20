import numpy as np

class UtilityClass():

    @staticmethod
    def normalize_data(data, axis_type):
        norms = np.linalg.norm(data, axis=axis_type)
        return data / norms

    
    @staticmethod
    def get_end_points(end_points, new_value):
        if new_value > end_points[1]:
            end_points[1] = new_value
        if new_value < end_points[0]:
            end_points[0] = new_value
        return end_points