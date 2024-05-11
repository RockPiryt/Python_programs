"""Napisz program, który posortuje n dat. 
Zdefiniuj i wykorzystaj słownik, która będzie posiadał klucze zawierające informacje 
na temat dnia, miesiąca i roku. Następnie posortuje dowolnym algorytmem daty rosnąco.

Uwaga: Napisz algorytm sortujący od podstaw. Nie korzystaj z gotowych rozwiązań dostępnych w Pythonie."""


from random import randint
from datetime import datetime

#_______________________Create use cases
date_num_one = 2
dict_random_dates_one = [{},{}]
# dict_random_length = len(dict_random_dates_one)
case_one = (date_num_one, dict_random_dates_one)


date_num_two = 5
dict_random_dates_two = [{},{},{},{},{}]
case_two = (date_num_two, dict_random_dates_two)

date_num_three = 10
dict_random_dates_three = [{},{},{},{},{},{},{},{},{},{}]
case_three = (date_num_three, dict_random_dates_three)

cases_list = [ case_one, case_two, case_three]

#_______________________Create use cases
for case in range(0, len(cases_list)):
    

    # How many dates will be created
    print(f"Case: {case+1}")
    num_dates = cases_list[case][0]
    print(f"User give number of dates: {num_dates}")

    #__________________Create dict with random dates
    print(f"Create dict with random {num_dates} dates:")

    dict_dates_random = {}
    for i in range(1, num_dates+1):

        current_year = int(datetime.now().date().strftime("%Y"))

        random_year = randint(1900, current_year)
        random_month = randint(1, 12)
        random_day = randint(1, 31)

        dict_dates_random[f"date_{i}"] = {"day": random_day, "month": random_month, "year": random_year}

        print(dict_dates_random[f"date_{i}"])# to genereje poszczególne daty
    # print(dict_dates_random)# to generuje cały słownik z kluczami date_1, date_2


    # _________________Sort dict with dates
    # Copy dict_dates_random to new variable - to do not change original dict_dates_random  
    sort_dict = dict_dates_random

    n = num_dates

    #Use bubble sort algorithm to sort dates
    # Loop through all dates in list
    for i in range(1, n+1): #date_1, date_2, date_n
        # # Loop to compare each 2 pairs (last element is not compare)
        for j in range(1, n):
            # Sort dates 
            if sort_dict[f"date_{j}"]["year"] > sort_dict[f"date_{j+1}"]["year"]:
                # Create temp fo year, mont, day
                temp = sort_dict[f"date_{j}"]["year"]
                temp_two = sort_dict[f"date_{j}"]["month"]
                temp_three = sort_dict[f"date_{j}"]["day"]
                # Swap places if not right order
                sort_dict[f"date_{
                    j}"]["year"] = sort_dict[f"date_{j+1}"]["year"]
                sort_dict[f"date_{
                    j}"]["month"] = sort_dict[f"date_{j+1}"]["month"]
                sort_dict[f"date_{
                    j}"]["day"] = sort_dict[f"date_{j+1}"]["day"]
                # Set temp
                sort_dict[f"date_{j+1}"]["year"] = temp
                sort_dict[f"date_{j+1}"]["month"] = temp_two
                sort_dict[f"date_{j+1}"]["day"] = temp_three

    year_list = []
    month_list = []
    day_list = []
    # Print sorted dict
    print("\nSorted dict with years:")
    for i in range(1, n+1):
        print(sort_dict[f"date_{i}"])
        single_year = sort_dict[f"date_{i}"]["year"]
        single_month = sort_dict[f"date_{i}"]["month"]
        single_day = sort_dict[f"date_{i}"]["day"]
        year_list.append(single_year)
        month_list.append(single_month)
        day_list.append(single_day)
    print("\n")
    # print(year_list)
    # print(month_list)
    # print(day_list)

    # Check order
    for i in range(len(year_list)):
        for j in range(0, len(year_list) - i - 1):
            if year_list[j] < year_list[j+1]:
                result = True
            elif year_list[j] == year_list[j+1]:
                if month_list[j] < month_list[j+1]:
                    result = True
                elif month_list[j] == month_list[j+1]:
                    if day_list[j] <= day_list[j+1]:
                        result = True
                    else:
                        result = False
                else:
                    False
            else:
                result = False

    print(f"Dates are in ascending order? {result}\n\n")

# # _______________________Program [ONE LOOP] - Create dict with random dates
# dict_dates_random = {}

# print("\nCreate dict with random dates:")
# n = 5
# for i in range(1, n+1):

#     current_year = int(datetime.now().date().strftime("%Y"))

#     random_year = randint(2000, current_year)
#     random_month = randint(1, 12)
#     random_day = randint(1, 31)

#     dict_dates_random[f"date_{i}"] = {
#         "day": random_day, "month": random_month, "year": random_year}

#     print(dict_dates_random[f"date_{i}"])

#     # date_year = dict_dates_random[f"date_{i}"]["year"]
#     # print(date_year)

# # _________________Sort dict with dates
# for i in range(1, n+1):
#     for j in range(1, n):
#         # Sort years
#         if dict_dates_random[f"date_{j}"]["year"] > dict_dates_random[f"date_{j+1}"]["year"]:
#             # Create temp fo year, mont, day
#             temp = dict_dates_random[f"date_{j}"]["year"]
#             temp_two = dict_dates_random[f"date_{j}"]["month"]
#             temp_three = dict_dates_random[f"date_{j}"]["day"]
#             # Swap places
#             dict_dates_random[f"date_{
#                 j}"]["year"] = dict_dates_random[f"date_{j+1}"]["year"]
#             dict_dates_random[f"date_{
#                 j}"]["month"] = dict_dates_random[f"date_{j+1}"]["month"]
#             dict_dates_random[f"date_{
#                 j}"]["day"] = dict_dates_random[f"date_{j+1}"]["day"]
#             # Set temp
#             dict_dates_random[f"date_{j+1}"]["year"] = temp
#             dict_dates_random[f"date_{j+1}"]["month"] = temp_two
#             dict_dates_random[f"date_{j+1}"]["day"] = temp_three

# # Print dict
# print("\nSorted dict with years:")
# for i in range(1, n+1):
#     print(dict_dates_random[f"date_{i}"])

