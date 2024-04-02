"""Napisz program, który posortuje n dat. 
Zdefiniuj i wykorzystaj słownik, która będzie posiadał klucze zawierające informacje 
na temat dnia, miesiąca i roku. Następnie posortuje dowolnym algorytmem daty rosnąco.

Uwaga: Napisz algorytm sortujący od podstaw. Nie korzystaj z gotowych rozwiązań dostępnych w Pythonie."""


from random import randint
from datetime import datetime

#_______________________Program [ONE LOOP] - Create dict with random dates
dict_dates_random = {}

print("\nCreate dict with random dates:")
n = 5
for i in range(1, n+1):

    current_year = int(datetime.now().date().strftime("%Y"))

    random_year = randint(2000, current_year)
    random_month = randint(1, 12)
    random_day = randint(1, 31)

    dict_dates_random[f"date_{i}"] = {
        "day": random_day, "month": random_month, "year": random_year}

    print(dict_dates_random[f"date_{i}"])

    date_year = dict_dates_random[f"date_{i}"]["year"]
    # print(date_year)

# _________________Sort dict with dates
for i in range(1, n+1):
    for j in range(1, n):
        # Sort years
        if dict_dates_random[f"date_{j}"]["year"] > dict_dates_random[f"date_{j+1}"]["year"]:
            # Create temp fo year, mont, day
            temp = dict_dates_random[f"date_{j}"]["year"]
            temp_two = dict_dates_random[f"date_{j}"]["month"]
            temp_three = dict_dates_random[f"date_{j}"]["day"]
            # Swap places
            dict_dates_random[f"date_{
                j}"]["year"] = dict_dates_random[f"date_{j+1}"]["year"]
            dict_dates_random[f"date_{
                j}"]["month"] = dict_dates_random[f"date_{j+1}"]["month"]
            dict_dates_random[f"date_{
                j}"]["day"] = dict_dates_random[f"date_{j+1}"]["day"]
            # Set temp
            dict_dates_random[f"date_{j+1}"]["year"] = temp
            dict_dates_random[f"date_{j+1}"]["month"] = temp_two
            dict_dates_random[f"date_{j+1}"]["day"] = temp_three

# Print dict
print("\nSorted dict with years:")
for i in range(1, n+1):
    print(dict_dates_random[f"date_{i}"])

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
cases_list_length = len(cases_list)

#_______________________Create use cases
for case in range(0, cases_list_length):
    print(f"Case: {case+1}")
    n_dates = cases_list[case][0]
    print(f"Number of dates: {n_dates}")


    # # Check if calculated_result is the same as the result in case
    # if calc_safe_position == safe_postion_result:
    #     result = True
    # else: 
    #     result = False

    # print(f"Case number: {case+1} : {result}\n")
