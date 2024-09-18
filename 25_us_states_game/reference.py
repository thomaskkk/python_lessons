# # import csv

# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)

# #     temp = []
# #     for row in data:
# #         for cell in row:
# #             if row.index(cell) == 1 and cell != "temp":
# #                 temp.append(int(cell))


# # print(temp)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # temp_list = data['temp'].to_list()
# # average = sum(temp_list) / len(temp_list)

# # print(average)

# # average2 = data['temp'].mean()

# # print(average2)

# # max = data['temp'].max()

# # print(max)

# # sc

# #print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * (9/5)+32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240916.csv")

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [
        len(data[data["Primary Fur Color"] == "Gray"]),
        len(data[data["Primary Fur Color"] == "Cinnamon"]),
        len(data[data["Primary Fur Color"] == "Black"]),
    ]
}

csv = pandas.DataFrame(data_dict)
csv.to_csv("new_data.csv")