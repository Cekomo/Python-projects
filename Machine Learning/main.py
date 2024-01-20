import time
from knn_algorithm import KNearestAlgorithm

def predict_sample_knn(k_number, total_iteration):
    correct_count = 0
    k_nearest_algorithm = KNearestAlgorithm()
    for i in range(0, total_iteration):
        selected_sample = k_nearest_algorithm.whole_df.sample(n=1)
        distance_dict = k_nearest_algorithm.calculate_euclidean_distance(
            selected_sample)
        distance_dict_processed = k_nearest_algorithm.define_knn_samples(
            distance_dict, k_number)
        selected_sample_ind = selected_sample.index.values[0]
        category_occ_dict = k_nearest_algorithm.determine_sample_type(
            selected_sample_ind, distance_dict_processed)
        correct_count = k_nearest_algorithm.control_prediction_output(
            selected_sample, category_occ_dict, correct_count)
    
    print(f"Success ratio: {round(correct_count/total_iteration*100, 1)}%")
    k_nearest_algorithm.plot_height_weight()


start_time = time.time()

k_number = 3
iteration_count = 1000
predict_sample_knn(k_number, iteration_count)

end_time = time.time()
print(f"Time taken: {end_time - start_time}")