from pre_steps import *
from models import *
from utils import *



if __name__ == '__main__':

	x, y, scaler = get_processed_data()
	x_train, x_test, y_train, y_test = split_data(x, y)
	regressor = get_SVMRegressor()
	fit(regressor, x_train, y_train)
	# y_pred=get_predictions(regressor,x_test)
	# error=get_error(y_test,y_pred)
	# gl_error=error
	# print("error: "+str(error))
	# print_predicted_data(x_test,y_test,y_pred)

	country_region_map, _ = read_countries_excel(region_country_file)
	region_pos_map, country_pos_map = position_maps(lat_long_csv, country_region_map)

	# X_predict = []
	x_1980_2030, regions = make_1980_2030_data(region_pos_map)



	# x_1980_2030 = make_1980_2030_data(x)
	# print(x)
	y_1980_2030 = get_predictions(regressor, x_1980_2030)

	# print(y_1980_2030)
	y_1980_2030 = y_1980_2030.reshape(-1, 1)
	unscaled = scaler.inverse_transform(y_1980_2030)
	unscaled = unscaled.reshape(len(unscaled))
	# print(len(unscaled))
	# print(unscaled)

	save_predictions_regions(predictions_csv, regions, x_1980_2030, unscaled)
