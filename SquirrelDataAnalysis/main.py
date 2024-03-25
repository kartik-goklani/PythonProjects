import pandas

data = pandas.read_csv('squirrel_data.csv')

gray = data[data['Primary Fur Color'] == 'Gray']
cin = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']

gray_count = len(gray)
cin_count = len(cin)
black_count = len(black)

# print(gray_count)
# print(cin_count)
# print(black_count)
#
# print(len(data))

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_count, cin_count, black_count]
}

new_dataframe = pandas.DataFrame(data_dict)

print(new_dataframe)

new_dataframe.to_csv('new_squirrel.csv')
