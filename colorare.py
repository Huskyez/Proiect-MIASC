import csv
from colour import Color

red = Color("blue")
colors = list(red.range_to(Color("red"),48824))
#print(colors[99998])
for i in range(colors.__len__()):
    print(colors[i])

list=[]
with open('1980-2030_region_predictions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[4]}.')
            line_count += 1
        list.append((row[0], row[1], row[2], row[3], row[4]))
    print(f'Processed {line_count} lines.')

i=0
with open('1980-2030_region_predictions_color.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    while i<=1020:
        if i==0:
            writer.writerow([list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], 'color'])
        else:
            index=int(list[i][4].split('.')[0])
            print(str(list[i][4])+" "+str(index)+" "+str(i))
            writer.writerow([list[i][0],list[i][1],list[i][2],list[i][3],list[i][4], colors[index-20000]])
        i+=1