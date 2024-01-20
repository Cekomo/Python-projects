import numpy as np

class UtilityClass():

    @staticmethod
    def normalize_data(data, axis_type):
        norms = np.linalg.norm(data, axis=axis_type)
        return data / norms

    
    @staticmethod
    def get_end_points(data_frame, field):
        end_points = [1000, 0]
        for index, sample in data_frame.iterrows():
            if sample[field] > end_points[1]:
                end_points[1] = sample[field]
            if sample[field] < end_points[0]:
                end_points[0] = sample[field]
        return end_points