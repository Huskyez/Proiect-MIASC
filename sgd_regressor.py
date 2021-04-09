import os
import sys

import numpy as np
import pandas as pd

from sklearn.linear_model import SGDRegressor 
from sklearn.preprocessing import StandardScaler


region_country_file = "List.excel.xlsx"
change_forest_csv = "annual-change-forest-area.csv"


country_region_map = {}


if __name__ == "__main__":

	countries_excel = pd.read_excel(region_country_file, engine="openpyxl", names=["REGION", "COUNTRY"])
	countries_excel.dropna(inplace=True)

	# print(data_frame["Europa de nord"])

	# print(type(data_frame.iloc[2]["REGION"]))
	# print(data_frame["REGION"])	

	# map each country to its corresponding region
	for i, row in countries_excel.iterrows():
		# print(row)
		region = row["REGION"]
		countries_str = row["COUNTRY"].strip()
		
		# remove spaces
		countries_str = countries_str.replace(", ", ",")
		countries_str = countries_str.replace(",  ", ",")
		country_list = countries_str.split(',')
		# print(country_list)
		for country in country_list:
			country_region_map[country] = region

		# region_country_map[region] = country_list


	print(country_region_map)

	# change_df = pd.read_csv(change_forest_csv)

	# print(change_df)
