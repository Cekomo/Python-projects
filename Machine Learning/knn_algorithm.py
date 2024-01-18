import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class KNearestAlgorithm():
    def __init__(self):
        self.df = pd.read_csv('dataset.csv')
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
        plt.show()

k_nearest_alorigthm = KNearestAlgorithm()
k_nearest_alorigthm.plot_height_weight()