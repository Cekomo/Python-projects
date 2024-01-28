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
    def gather_random_dataset(whole_df, train_sample_count):
        selected_indices = set()
        train_df = pd.DataFrame()
        for _ in range(0, train_sample_count):
            break_point = 0
            # it is a problem if training dataset entity reaches..
            #.. the number of whole dataset
            while True and break_point < 1000:
                break_point += 1
                index = whole_df.sample().index[0]
                if index not in selected_indices:
                    selected_indices.add(index)
                    train_df = train_df._append(whole_df.loc[index])
                    break
        return train_df


    @staticmethod
    def get_test_sample(whole_df, train_df):
        break_point = 0
        while True and break_point < 1000:
            selected_index = whole_df.sample().index[0]
            if selected_index not in train_df.index:
                return whole_df.loc[selected_index]
            break_point += 1
            
        raise ValueError("Unable to find a test sample", 
                         " not present in the training dataset.")
    

    @staticmethod
    def get_df_record(df, row_title, row_title_value):
        return df[df[row_title] == row_title_value].iloc[:, 1:]
    

    @staticmethod
    def form_dict_from_df(train_df):
        years = train_df.columns.astype(int)
        values = train_df.values.flatten()
        return {key: value for key, value in zip(years, values)}
    

    @staticmethod
    def check_if_titles_valid(df, record_name, record_value):
        if record_name not in df.columns:
            raise KeyError(f"'{record_name}' is not valid header in dataframe.")
        elif df[df[record_name] == record_value].empty:
            raise KeyError(f"'{record_value}' is not valid identifier in dataframe.")
        
    
    @staticmethod
    def check_if_dependent_value_valid(dependent_value):
        if (type(dependent_value) != int or type(dependent_value) != float):
            raise TypeError(f"Independent value parameter must be a number.")
