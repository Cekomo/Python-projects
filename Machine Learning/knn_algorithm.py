import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

class KNearestAlgorithm():
    def __init__(self):
        self.df = pd.read_csv('bmi_dataset.csv')
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
        # plt.show()

    
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
    
    def control_prediction_output(self, selected_sample, category_occurence_dict):
        the_sample_category = selected_sample['Category'].values[0]
        if max(category_occurence_dict.keys()) == the_sample_category:
            # print("Prediction is correct!")
            return correct_count + 1
        else:
            # print(f"Prediction is incorrect, the label was {the_sample_category}")
            return correct_count

start_time = time.time()
correct_count = 0
total_iteration = 100
k_nearest_algorithm = KNearestAlgorithm()
for i in range(0, total_iteration):
    selected_sample = k_nearest_algorithm.df.sample(n=1)
    k_nearest_algorithm.plot_height_weight()
    distance_dict = k_nearest_algorithm.calculate_euclidean_distance(selected_sample)
    distance_dict_processed = k_nearest_algorithm.define_knn_samples(distance_dict, 5)
    selected_sample_ind = selected_sample.index.values[0]
    category_occ_dict = k_nearest_algorithm.determine_sample_type(selected_sample_ind, distance_dict_processed)
    correct_count = k_nearest_algorithm.control_prediction_output(selected_sample, category_occ_dict)

print(f"Success ratio: {round(correct_count/total_iteration*100, 1)}%")
print(f"Time taken: {time.time() - start_time}")
