import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KNearestAlgorithm():
    def __init__(self):
        file_name = 'bmi_dataset.csv'
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        self.df = pd.read_csv(file_path)
        self.gender_color = {'Male': 'blue', 'Female': 'pink'}


    def plot_height_weight(self):
        x_axis = self.df['Weight']
        y_axis = self.df['Height']
        z_axis = self.df['Gender']

        for index, (x, y, gender) in enumerate(zip(x_axis, y_axis, z_axis)):
            plt.scatter(x, y, color=self.gender_color[gender], 
                        label=gender, marker='.')
            plt.text(x, y, str(index), fontsize=8, ha='right')

        plt.xlabel('Weight')
        plt.ylabel('Height')
        plt.title('Individuals\' Physical Appearence')
        plt.show()

    
    def calculate_euclidean_distance(self, selected_sample):
        selected_sample = self.df.sample(n=1)
        distance_dict = {}
        for index, sample in self.df.iterrows():
            weight_distance = abs(sample['Weight'] - selected_sample['Weight'])
            height_distance = abs(sample['Height'] - selected_sample['Height'])
            euclidean_distance = np.sqrt(weight_distance**2 + height_distance**2)
            if index != selected_sample.index[0]:
                distance_dict[index] = [euclidean_distance.item(), sample['Category']]

        return distance_dict
    

    def define_knn_samples(self, distance_dict, sample_size):
        if sample_size >= len(distance_dict):
            print("Sample size is greater than dataset, all dataset is added.")
        distance_dict_processed = dict(sorted(distance_dict.items(), 
            key=lambda item:item[1])[:sample_size])
        
        return distance_dict_processed


    def determine_sample_type(self, selected_sample_ind, distance_dict_processed):
        category_occurence_dict = {}
        for key, value in distance_dict_processed.items():
            if value[1] not in category_occurence_dict:
                category_occurence_dict[value[1]] = 1
            else:
                category_occurence_dict[value[1]] += 1
        # print(f"Output for index {selected_sample_ind}:" 
        #       f" {max(category_occurence_dict.keys())}")
        return category_occurence_dict
        

    def optimise_output_accuracy(self):
        pass
    

    def control_prediction_output(self, the_sample, category_occurence_dict, correct_count):
        the_sample_category = the_sample['Category'].values[0]
        if max(category_occurence_dict.keys()) == the_sample_category:
            # print("Prediction is correct!")
            return correct_count + 1
        else:
            # print(f"Prediction is incorrect, the label was {the_sample_category}")
            return correct_count

