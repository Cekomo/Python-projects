import time
import os
from knn_algorithm import KNearestAlgorithm
from linear_regression import LinearRegression
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


def predict_sample_lr(file_path, record_name, record_value, predicted_year):
    lr = LinearRegression()
    gdp_df = util.read_csv(file_path)
    util.check_if_titles_valid(gdp_df, record_name, record_value)
    util.check_if_dependent_value_valid(predicted_year)
    country_gdp_df = util.get_df_record(gdp_df, record_name, record_value)
    country_gdp_dict = util.form_dict_from_df(country_gdp_df)
    visual.plot_linear_regression(country_gdp_dict, record_value)

    x_values = country_gdp_dict.keys()
    y_values = country_gdp_dict.values()
    x_mean = lr.get_mean(x_values)
    y_mean = lr.get_mean(y_values)
    slope = lr.calc_linear_regression_slope(country_gdp_dict, x_mean, y_mean)
    constant = lr.calc_linear_regression_constant(x_mean, y_mean, slope)
    lr.print_lr_equation(slope, constant)
    lr.fit_data_to_regression_line(predicted_year, slope, constant)

    year_list = list(country_gdp_dict.keys())
    lr.calc_mean_squared_error(x_values, y_values, slope, constant)
    visual.plot_regression_line(year_list, slope, constant)


start_time = time.time()

# KNN -----
# k_number = 4
# iteration_count = 1
# predict_sample_knn(k_number, iteration_count)
# KNN -----

# file_path = 'country_citizens_gdp.csv'
file_path = os.path.join(
            os.path.dirname(__file__), 'country_citizens_gdp.csv')
predict_sample_lr(file_path, 'Country Name', 'Barbados', 2030)


end_time = time.time()
print(f"Time taken: {end_time - start_time}")