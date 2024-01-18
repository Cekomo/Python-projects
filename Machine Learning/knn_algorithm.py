import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KNearestAlgorithm():
    def __init__(self):
        self.df = pd.read_csv('bmi_dataset.csv')
        self.gender_color = {'Male': 'blue', 'Female': 'pink'}

    def plot_height_weight(self):
        x_axis = self.df['Weight']
        y_axis = self.df['Height']
        z_axis = self.df['Gender']

        for x, y, gender in zip(x_axis, y_axis, z_axis):
            plt.scatter(x, y, color=self.gender_color[gender], 
                        label=gender, marker='.')

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
            distance_dict[index] = euclidean_distance.item()

        return distance_dict


k_nearest_alorigthm = KNearestAlgorithm()
selected_sample = k_nearest_alorigthm.df.sample(n=1)
k_nearest_alorigthm.plot_height_weight()
print(k_nearest_alorigthm.calculate_euclidean_distance(selected_sample))