"Napisz program, który wypisze na ekranie wszystkie liczby pierwsze z zadanego zakresu."

# # #_______________________Program [ONE LOOP] - Print list with prime numbers 
# lower = 0
# upper = 0

# # Create a list in a range of a to b
# my_list = list(range(lower, upper+1))
# print(f'My list: {my_list}')

# #  Empty list with prime numbers
# prime_list = []

# # Add prime numbers to prime list
# for num in range(lower, upper + 1):
#     # all prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             prime_list.append(num)

# print(f'Prime number list: {prime_list}')


#_______________________Create cases

range_one = (1,30)
result_one = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
case_one = (range_one, result_one)

range_two = (0,15)
result_two = [2, 3, 5, 7, 11, 13]
case_two = (range_two, result_two)


range_three = (0,0)
result_three = []
case_three = (range_three, result_three)

range_four = (100,200)
result_four = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
case_four = (range_four, result_four)

cases = [case_one, case_two, case_three, case_four]

#______________________Check cases
for case in cases:
    print(f"Case: {case}")

    # Get values for cases. Get lower range and uppper range.
    range_case = case[0]
    lower = range_case[0]
    upper = range_case[1]

    # Expected results:
    result_case = case[1]

    # # List with range (lower-upper)
    case_list = list(range(lower, upper+1))

    #  Empty list with prime numbers
    prime_list = []

    # Add prime numbers to prime list
    # for num in range(lower, upper + 1):
    for num in case_list:
        # all prime numbers are greater than 1
        if num > 1:
            # Check if num can be divison by other number in range - if is = not prime number
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)

    result_creation = prime_list

    # Check if result from creation is the same as the result in case
    if result_case == result_creation:
        result = True
    else: 
        result = False

    print(case, ": ", result, "\n")
    

