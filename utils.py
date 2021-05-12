import numpy as np
from pre_steps import predictions_csv,lat_long_csv,region_country_file,read_countries_excel,position_maps
import pandas as pd
def print_predicted_data(x_test,y_test,y_pred):
    for point, true, pred in zip(x_test, y_test, y_pred):
        print(str(point) + ": " + str(true) + " --- "  + str(pred))


def make_1980_2030_data(x):
    new_x=[]
    x_del = np.delete(x, 0, 1)
    x_del=np.unique(x_del,axis=0)
    for entry in x_del:
        for i in range(1980,2031):
            new_x.append([i,entry[0],entry[1]])
    return new_x



def save_predictions_country(x,y,file_name):
    file=open(file_name,'w')
    text=''
    text=text+'year,'+'lat,'+'long,'+'net_forest_conversion\n'
    for i in range(len(x)):
        text=text+str(x[i][0])+","+str(x[i][1])+","+str(x[i][2])+","+str(y[i])+'\n'
    file.write(text)

def get_regions_dict_lat_long():
    country_region_map, regions=read_countries_excel(region_country_file)
    region_pos_map, country_pos_map=position_maps(lat_long_csv,country_region_map)

    regions_dict={}
    for region in regions:
        regions_dict[region]=[]

    for country in country_region_map:
        try:
            regions_dict[country_region_map[country]].append(country_pos_map[country])
        except:
            continue

    return regions_dict


def compute_mean_predicted_region(regions_dict):
    predictions_df=pd.read_csv(predictions_csv)
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


def save_predictions_regions(regions,filename):
    file=open(filename,'w')
    text=''
    text=text+'region,'+'year,'+'lat,'+'long,'+'net_forest_conversion\n'
    for region in regions:
        for i in regions[region]:
            try:
                text=text+str(region)+","+str(i[0])+","+str(i[1])+\
                     ","+str(i[2])+","+str(i[3])+'\n'
            except:
                continue
    file.write(text)




# regions_dict=get_regions_dict_lat_long()
# regions_values=compute_mean_predicted_region(regions_dict)
# save_predictions_regions(regions_values,"1980-2030 predictions region.csv")

