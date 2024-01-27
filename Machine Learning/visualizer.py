import matplotlib.pyplot as plt

class Visualizer():
    def __init__(self) -> None:
        pass

    
    @staticmethod
    def plot_train_df_knn(train_df, test_sample, bmi_color, used_samples):
        # it is better to eliminate label dependency
        x_axis = train_df['Weight']
        y_axis = train_df['Height']
        z_axis = train_df['Category']

        for index, (x, y, bmi) in zip(train_df.index, zip(x_axis, y_axis, z_axis)):
            sample_marker = '.'
            if index in used_samples:
                sample_marker = 'o'
            plt.scatter(x, y, color=bmi_color[bmi], 
                        label=bmi, marker=sample_marker)
            plt.text(x, y, str(index), fontsize=8, ha='right')

        plt.scatter(test_sample['Weight'], test_sample['Height'], 
                    color='turquoise', marker='*')
        plt.text(test_sample['Weight'], test_sample['Height'], 
                str(test_sample.values[0]), fontsize=8, ha='right')

        plt.xlabel('Weight')
        plt.ylabel('Height')
        plt.title('Individuals\' Physical Appearence')
        marker_note = """'*' marker represents train sample while 'o' """
        marker_note += """markers represent the \n """
        marker_note += """samples used to determine sample's label."""
        plt.figtext(0.01, 0.96, marker_note, ha='left', va='center', fontsize=9)

        # plt.legend(self.bmi_color.values(), labels=self.bmi_color.keys())
        plt.show()

    
    @staticmethod
    def plot_linear_regression(train_dict, country_name):
        plt.scatter(train_dict.keys(), train_dict.values(), marker='.')
        plt.title(f'{country_name} - GDP Over the Years')
        plt.xlabel('Year')
        plt.ylabel('GDP Value')
        plt.show()

