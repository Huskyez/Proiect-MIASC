import numpy as np
from pre_steps import predictions_csv, lat_long_csv, region_country_file, read_countries_excel, position_maps
import pandas as pd
from pre_steps import get_processed_data

def print_predicted_data(x_test,y_test,y_pred):
    for point, true, pred in zip(x_test, y_test, y_pred):
        print(str(point) + ": " + str(true) + " --- "  + str(pred))




def make_1980_2030_data(region_pos_map):
    # new_x = []
    # x_del = np.delete(x, 0, 1)
    # x_del = np.unique(x_del,axis=0)
    # for entry in x_del:
    #     for i in range(1980,2031):
    #         new_x.append([i,entry[0],entry[1]])
    # return new_x

    # points to predict
    X_predict = []
    # a list of regions corresponding to X_predict
    # i.e. if X_predict[i] corresponds to region 'A' then regions_to_predictions[i] = 'A'
    regions_to_predictions = [] 
    for region in region_pos_map.keys():
        print(region_pos_map[region][0], region_pos_map[region][1])
        for year in range(1980, 2031):
            X_predict.append(np.array([year, region_pos_map[region][0], region_pos_map[region][1]]))
            regions_to_predictions.append(region)

    return X_predict, regions_to_predictions

def get_country_from_lat_long():
    country_region_map, regions = read_countries_excel(region_country_file)
    region_pos_map, country_pos_map = position_maps(lat_long_csv, country_region_map)
    predictions_df = pd.read_csv(predictions_csv)
    predictions=predictions_df.values.tolist()
    list=[]
    list_to_unscale=[]
    x, y, scaler = get_processed_data()
    for prediction in predictions:
        list_to_unscale.append(prediction[3])
    list_to_unscale=np.array(list_to_unscale)
    list_to_unscale=list_to_unscale.reshape(-1,1)
    list_to_unscale=scaler.inverse_transform(list_to_unscale)
    list_to_unscale=list_to_unscale.reshape(len(list_to_unscale))
    for prediction in predictions:
        for country in country_pos_map:
            if country_pos_map[country][0]== prediction[1] and country_pos_map[country][1]== prediction[2]:
                try:
                    list.append([country,prediction[0],prediction[1],prediction[2]])
                except:
                    continue
    for el in range(len(list)):
        list[el].append(list_to_unscale[el])
    return list


def save_predictions_country(x, y, file_name):
    file=open(file_name,'w')
    text=''
    text=text+'year,'+'lat,'+'long,'+'net_forest_conversion\n'
    for i in range(len(x)):
        text=text+str(x[i][0])+","+str(x[i][1])+","+str(x[i][2])+","+str(y[i])+'\n'
    file.write(text)

def get_regions_dict_lat_long():
    country_region_map, regions = read_countries_excel(region_country_file)
    region_pos_map, country_pos_map = position_maps(lat_long_csv, country_region_map)

    regions_dict = {}
    for region in regions:
        regions_dict[region]=[]

    for country in country_region_map:
        try:
            regions_dict[country_region_map[country]].append(country_pos_map[country])
        except:
            continue

    return regions_dict


def compute_mean_predicted_region(regions_dict):
    predictions_df = pd.read_csv(predictions_csv)
    country_region_map, regions=read_countries_excel(region_country_file)
    region_pos_map, country_pos_map=position_maps(lat_long_csv,country_region_map)
    print(predictions_df)
    predictions=predictions_df.values.tolist()
    regions_values={}
    for region in regions_dict:
        regions_values[region]=[]
        for i in range(1980,2031):
            try:
                lat=region_pos_map[region][0]
                long=region_pos_map[region][1]
                regions_values[region].append([i,lat,long])
            except:
                continue

    # print(list)
    print(regions_dict)
    print(country_pos_map)
    for region in regions_dict:
        for i in range(1980,2031):
            avg=0
            k=0
            for prediction in predictions:
                if [prediction[1],prediction[2]] in regions_dict[region] and prediction[0]==i:
                    avg=avg+prediction[3]
                    k=k+1
            try:
                avg=avg/k
                regions_values[region][i-1980].append(avg)
            except:
                continue

    return regions_values


# def save_predictions_regions(regions, filename):
#     file=open(filename,'w')
#     text=''
#     text=text+'region,'+'year,'+'lat,'+'long,'+'net_forest_conversion\n'
#     for region in regions:
#         for i in regions[region]:
#             try:
#                 text=text+str(region)+","+str(i[0])+","+str(i[1])+\
#                      ","+str(i[2])+","+str(i[3])+'\n'
#             except:
#                 continue
#     file.write(text)


def save_predictions_regions(filename, regions, points, predictions):
    with open(filename, 'w') as f:
        f.write("region,year,lat,long,net_forest_conversion\n")

        for i in range(len(regions)):
            f.write(regions[i] + "," \
                + str(points[i][0]) + "," + str(points[i][1]) + "," + str(points[i][2]) + "," \
                + str(predictions[i]) + "\n")


def save_predictions_country(filename,content):
    f=open(filename,'w')
    f.write("country,year,lat,long,net_forest_conversion\n")

    for i in range(len(content)):
        f.write(content[i][0] + "," \
                + str(content[i][1]) + "," + str(content[i][2]) + "," + str(content[i][3]) + "," \
                + str(content[i][4]) + "\n")

# regions_dict=get_regions_dict_lat_long()
# regions_values=compute_mean_predicted_region(regions_dict)
# save_predictions_regions(regions_values,"1980-2030 predictions region.csv")

list=get_country_from_lat_long()
save_predictions_country(predictions_csv,list)
