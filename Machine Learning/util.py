import numpy as np
import pandas as pd

class UtilityClass():

    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)


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
    
    
    @staticmethod
    def gather_random_dataset(whole_df, train_df, sample_amount):
        selected_indices = set()
        for _ in range(0, sample_amount):
            break_point = 0
            # it is a problem if training dataset entity reaches..
            #.. the number of whole dataset
            while True and break_point < 1000:
                break_point += 1
                index = whole_df.sample().index[0]
                if index not in selected_indices:
                    selected_indices.add(index)
                    train_df.loc[index]
                    break
        return train_df
