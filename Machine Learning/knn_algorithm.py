import numpy as np
import pandas as pd
from util import UtilityClass as util

class KNearestAlgorithm():
    def __init__(self, train_df, test_sample):
        self.train_df = train_df
        self.test_sample = test_sample

    
    def calculate_euclidean_distance(self):
        euc_distance_dict = {}
        x_end_points = util.get_end_points(self.train_df, 'Weight')
        y_end_points = util.get_end_points(self.train_df, 'Height')
        x_axis_range = x_end_points[1] - x_end_points[0]
        y_axis_range = y_end_points[1] - y_end_points[0]
        for index, sample in self.train_df.iterrows():
            if (self.test_sample.index == index).any():
                continue
            weight_distance = abs(sample['Weight'] - self.test_sample['Weight'])
            height_distance = abs(sample['Height'] - self.test_sample['Height'])
            euclidean_distance = np.sqrt(
                (weight_distance/x_axis_range * 100)**2 + 
                (height_distance/y_axis_range * 100)**2)
            euc_distance_dict[index] = [euclidean_distance.item(), sample['Category']]

        return euc_distance_dict
    

    def define_knn_samples(self, distance_dict, sample_size):
        if sample_size >= len(distance_dict):
            print("Sample size is greater than dataset, all dataset is added.")
        distance_dict_processed = dict(sorted(distance_dict.items(), 
            key=lambda item:item[1])[:sample_size])
        
        return distance_dict_processed


    def determine_sample_type(self, distance_dict_processed):
        category_occurrence_dict = {}
        for key, value in distance_dict_processed.items():
            if value[1] not in category_occurrence_dict:
                category_occurrence_dict[value[1]] = 1
            else:
                category_occurrence_dict[value[1]] += 1

        return category_occurrence_dict
    

    def control_prediction_output(self, category_occurrence_dict, correct_count):
        test_sample_category = self.test_sample['Category']
        max_coccurence_key = max(category_occurrence_dict, key=category_occurrence_dict.get)
        if max_coccurence_key == test_sample_category:
            # print("Prediction is correct!")
            return correct_count + 1
        else:
            # print(f"Prediction is incorrect, the label was {test_sample_category}")
            return correct_count

