import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler,RobustScaler,normalize
from sklearn.model_selection import train_test_split
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor
from statistics import variance,mean

region_country_file = "List.excel.xlsx"
change_forest_csv = "annual-change-forest-area.csv"
lat_long_csv = "lat-long.csv"
predictions_csv="1980-2030 predictions.csv"

def read_countries_excel(filepath):
    # returns a map with each country belonging to a a region
    # i.e. map['country'] = 'region'

    country_region_map = {}

    regions = []

    countries_excel = pd.read_excel(filepath, engine="openpyxl", names=["REGION", "COUNTRY"])
    countries_excel.dropna(inplace=True)

    # print(data_frame["Europa de nord"])

    # print(type(data_frame.iloc[2]["REGION"]))
    # print(data_frame["REGION"])

    # map each country to its corresponding region
    for i, row in countries_excel.iterrows():
        # print(row)
        region = row["REGION"]
        regions.append(region)

        countries_str = row["COUNTRY"].strip()

        # remove spaces
        countries_str = countries_str.replace(", ", ",")
        countries_str = countries_str.replace(",  ", ",")
        country_list = countries_str.split(',')
        # print(country_list)
        for country in country_list:
            country_region_map[country] = region

    return country_region_map, regions


def position_maps(filepath, country_region_map):

    # maps a country to its corresponding
    # position (lat, long) map['country'] = [lat, long]
    country_pos_map = {}

    # region_pos_map maps a region
    # to its position (lat, long)
    # by taking the average of all positions
    # of the countries in that regions
    # map['region'] = [avg(lat), avg(lon)]
    region_pos_map = {}

    region_count_map = {}

    lat_long_df = pd.read_csv(filepath, header=None)

    for entry in lat_long_df.iterrows():
        country = entry[1][0]
        # print(country)

        position = [float(entry[1][1]), float(entry[1][2])]
        # position = entry[1][2]
        # print(entry[1][1:3])

        country_pos_map[country] = position

        if country in country_region_map:
            region = country_region_map[country]

            if region in region_pos_map:
                region_pos_map[region][0] += position[0]
                region_pos_map[region][1] += position[1]
            else:
                region_pos_map[region] = position

            if region in region_count_map:
                region_count_map[region] += 1
            else:
                region_count_map[region] = 1

    for key in region_pos_map.keys():
        region_pos_map[key][0] /= region_count_map[key]
        region_pos_map[key][1] /= region_count_map[key]


    return region_pos_map, country_pos_map




def get_points_values(filepath, country_pos_map):
    # this function returns numpy array consisting
    # of points: (year, lat, long)
    # and values: net forest change
    # note: values vary a lot and should be scaled
    # filepath is the path to the annual change forest csv


    change_forest_df = pd.read_csv(filepath)# , header=[0, 2, 3]) #, names=["Entity", "Year", "Net forest conversion"])

    points = []
    values = []
    # print(change_forest_df)

    for entry in change_forest_df.iterrows():

        country = entry[1][0]
        year = int(entry[1][2])
        net = float(entry[1][3])

        # country = entry["Entity"]
        # year = int(entry["Year"])
        # net = int(entry["Net forest conversion"])

        if country in country_pos_map:
            lat = country_pos_map[country][0]
            lon = country_pos_map[country][1]

            # print(country, year, lat, lon)
            points.append(np.array([year, lat, lon]))

            values.append(net)

    # print(country, year, net)

    return np.array(points), np.array(values)

def get_raw_data():
    # print(country_region_map)


    # df = pd.read_csv(change_forest_csv)

    # print(len(np.unique(df["Entity"])))

    country_region_map, regions = read_countries_excel(region_country_file)

    # print(len(mapp.keys()))
    region_pos_map, country_pos_map = position_maps(lat_long_csv, country_region_map)
    # print(region_pos_map)


    points, values = get_points_values(change_forest_csv, country_pos_map)

    return points,values

def get_processed_data():
    points,values=get_raw_data()
    values = values.reshape(-1, 1)

    # STANDARD SCALER

    # scaler = StandardScaler()
    # scaler.fit(values)

    # scaled_values = scaler.transform(values)

    # print(values)

    # print(points.shape)
    # print(scaled_values)
    # scaled_values = scaled_values.reshape(1, scaled_values.shape[0])[0]
    # print(scaled_values)


    #ROBUST SCALER
    # robust=RobustScaler()
    #
    # robust.fit(values)
    # values=robust.transform(values)

    # MIN MAX SCALER
    scaler = MinMaxScaler()

    scaler.fit(values)
    scaled_values = scaler.transform(values)

    scaled_values = np.ravel(scaled_values)


    return points,scaled_values

def split_data(x,y,test_size=0.15):
    return train_test_split(x,y,test_size=test_size)



