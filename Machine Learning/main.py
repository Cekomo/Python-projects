import time
import os
from knn_algorithm import KNearestAlgorithm
from util import UtilityClass as util
from visualizer import Visualizer as visual

def predict_sample_knn(k_number, total_iteration):
    correct_count = 0
    whole_file_path = os.path.join(
            os.path.dirname(__file__), 'whole_bmi_dataset.csv')
    whole_df = util.read_csv(whole_file_path)
    
    for i in range(0, total_iteration):
        train_df = util.gather_random_dataset(whole_df, 40)
        test_sample = util.get_test_sample(whole_df, train_df)
        k_nearest_algorithm = KNearestAlgorithm(train_df, test_sample)
        distance_dict = k_nearest_algorithm.calculate_euclidean_distance()
        distance_dict_processed = k_nearest_algorithm.define_knn_samples(
            distance_dict, k_number)
        category_occ_dict = k_nearest_algorithm.determine_sample_type(
            distance_dict_processed)
        correct_count = k_nearest_algorithm.control_prediction_output(
            category_occ_dict, correct_count)
    
    print(f"Success ratio: {round(correct_count/total_iteration*100, 1)}%")
    # execute plot for single iteration count, will execute the latest otherwise
    used_samples_dict = distance_dict_processed.keys()
    bmi_color = {'Normal': 'blue', 'Overweight': 'orange', 
                'Underweight': 'black', 'Obese': 'red'}
    visual.plot_train_df_knn(train_df, test_sample, bmi_color, used_samples_dict)


start_time = time.time()

k_number = 4
iteration_count = 1
predict_sample_knn(k_number, iteration_count)

end_time = time.time()
print(f"Time taken: {end_time - start_time}")