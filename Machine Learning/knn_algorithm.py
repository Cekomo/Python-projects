import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util import UtilityClass as util

class KNearestAlgorithm():
    def __init__(self):
        training_file = 'training_bmi_dataset.csv'
        whole_file = 'whole_bmi_dataset.csv'
        training_file_path = os.path.join(os.path.dirname(__file__), training_file)
        whole_file_path = os.path.join(os.path.dirname(__file__), whole_file)
        self.training_df = pd.read_csv(training_file_path)
        self.whole_df = pd.read_csv(whole_file_path)
        self.bmi_color = {'Normal': 'blue', 'Overweight': 'orange',
                          'Underweight': 'black', 'Obese': 'red'}


    def plot_height_weight(self):
        x_axis = self.training_df['Weight']
        y_axis = self.training_df['Height']
        z_axis = self.training_df['Category']

        for index, (x, y, bmi) in enumerate(zip(x_axis, y_axis, z_axis)):
            plt.scatter(x, y, color=self.bmi_color[bmi], 
                        label=bmi, marker='.')
            plt.text(x, y, str(index), fontsize=8, ha='right')

        plt.xlabel('Weight')
        plt.ylabel('Height')
        plt.title('Individuals\' Physical Appearence')
        plt.show()

    
    def calculate_euclidean_distance(self, selected_sample):
        distance_dict = {}
        x_end_points = util.get_end_points(self.training_df, 'Weight')
        y_end_points = util.get_end_points(self.training_df, 'Height')
        x_axis_range = x_end_points[1] - x_end_points[0]
        y_axis_range = y_end_points[1] - y_end_points[0]
        for index, sample in self.training_df.iterrows():
            if selected_sample.index == index:
                continue
            weight_distance = abs(sample['Weight'] - selected_sample['Weight'])
            height_distance = abs(sample['Height'] - selected_sample['Height'])
            euclidean_distance = np.sqrt(
                (weight_distance.values[0]/x_axis_range * 100)**2 + 
                (height_distance.values[0]/y_axis_range * 100)**2)
            distance_dict[index] = [euclidean_distance.item(), sample['Category']]

        return distance_dict
    

    def define_knn_samples(self, distance_dict, sample_size):
        if sample_size >= len(distance_dict):
            print("Sample size is greater than dataset, all dataset is added.")
        distance_dict_processed = dict(sorted(distance_dict.items(), 
            key=lambda item:item[1])[:sample_size])
        return distance_dict_processed


    def determine_sample_type(self, selected_sample_ind, distance_dict_processed):
        category_occurrence_dict = {}
        for key, value in distance_dict_processed.items():
            if value[1] not in category_occurrence_dict:
                category_occurrence_dict[value[1]] = 1
            else:
                category_occurrence_dict[value[1]] += 1
        return category_occurrence_dict
    

    def control_prediction_output(self, the_sample, category_occurrence_dict, correct_count):
        the_sample_category = the_sample['Category'].values[0]
        max_coccurence_key = max(category_occurrence_dict, key=category_occurrence_dict.get)
        if max_coccurence_key == the_sample_category:
            # print("Prediction is correct!")
            return correct_count + 1
        else:
            # print(f"Prediction is incorrect, the label was {the_sample_category}")
            return correct_count

