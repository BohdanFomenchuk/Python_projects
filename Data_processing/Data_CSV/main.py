# Script to get the number of squirrels of each color and write it to a new csv file

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

new_data = {"gray": 0, "red": 0, "black": 0}

for squirrel in data["Primary Fur Color"]:
    if squirrel == "Gray":
        new_data["gray"] += 1
    elif squirrel == "Cinnamon":
        new_data["red"] += 1
    if squirrel == "Black":
        new_data["black"] += 1

df = pandas.DataFrame.from_dict(new_data, orient='index')
df.to_csv("squirrel_by_color")
