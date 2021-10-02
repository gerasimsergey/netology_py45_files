from pprint import pprint
import os
# Задача 1
def load_data_from_file(file_name):
    data = dict()
    with open(file_name) as file:
        for line in file:
            temp_list = []
            cook_name = line.strip()
            counter = int(file.readline())

            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                temp_list.append(
                    {'ingrediate_name': ingredient_name.strip(),
                     'quantity': quantity.strip(),
                     'measure': measure.strip()
                     }
                )
                data[cook_name] = temp_list

            file.readline()
    return data


# pprint(load_data_from_file('recipes.txt'))


# Задача 2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

def get_shop_list_by_dishes(dish_list, person_count):
    shop_list = dict()
    cook_book = load_data_from_file('recipes.txt')
    for dish in dish_list:
        ingridients_list = cook_book.get(dish)

        for ingridient in ingridients_list:
            ingr_name = ingridient.get('ingrediate_name')
            measure = ingridient.get('measure')
            qty_for_pers_count = int(ingridient.get('quantity', 0)) * int(person_count)

            ingr_in_list = shop_list.get(ingr_name)
            if ingr_in_list:
                ingr_in_list['quantity'] += qty_for_pers_count
            else:
                shop_list[ingr_name] = {'measure': measure, 'quantity': qty_for_pers_count}
    return  shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(shop_list)

# Задача 3 (усложненная)

# # v2
# arr = os.listdir(path)
# print(arr)

# import glob
# txtfiles = []
# for file in glob.glob(path + "/*.txt"):
# # for file in glob.glob("*.txt"):
#     txtfiles.append(file)
# print(txtfiles)

from os import walk

path = os.getcwd() + '/test_files'
print(path)

# v1
file_list = []
files_dict = {}


for (dirpath, dirnames, filenames) in walk(path):
    file_list.extend(filenames)
    break

for file_name in file_list:
        with open(path + '/' + file_name) as file:
            lines = file.readlines()
            files_dict[file_name] = len(lines)

# for file_name in file_list:
#         f_name = path + '/' + file_name
#         with open(f_name) as file:
#             lines = file.readlines()
#             files_dict[f_name] = len(lines)

sorted_list = list(files_dict.items())
sorted_list.sort(key=lambda i: i[1])
# print(sorted_list)

def file_data(path, file_name):
    lines = []
    with open(path + '/' + file_name) as file:
        lines = file.readlines()
    return lines

temp_list = []

for item in sorted_list:
    temp_list.append(item[0])
    temp_list.append(item[1])
    for file_line in file_data(path, item[0]):
        temp_list.append(file_line)

print(temp_list)

# файл перезаписывается
with open('result.txt', 'w') as file:
    for item in temp_list:
        file.write(str(item) + '\n')


