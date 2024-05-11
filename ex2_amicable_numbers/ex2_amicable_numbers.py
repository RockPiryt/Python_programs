"""Liczby zaprzyjaźnione to dwie liczby naturalne, 
gdzie każda z nich jest równa sumie dzielników właściwych drugiej liczby. 
Napisz program wypisujący liczby zaprzyjaźnione z zadanego zakresu."""

#_______________________Create cases
cases = [(220, 284), (1184, 1210), 
        (2620, 2924), (5020, 5564), 
        (6232, 6368), (10744, 10856), 
        (12285, 14595), (17296, 18416), 
        (63020, 76084), (66928, 66992), 
        (777, 888), (0,1), (100,101)]

#______________________Check cases  
number_case = 1

for num_one, num_two in cases:
    # Print case values
    print(f"Case number: {number_case}")
    print(f"Number one {num_one}")
    print(f"Number two {num_two}")
    
    # Create variable for sum
    sum_div_one_num = 0
    sum_div_two_num = 0

    # Add num_one's divisiors to sum variable 
    for num in range(1, num_one):
        #If first number is divided by num (without rest)
        if(num_one % num == 0):
            sum_div_one_num += num 

    # Add num_one's divisiors to sum variable 
    for num in range(1, num_two):
        #If second number is divided by num (without rest)
        if(num_two % num == 0):
            sum_div_two_num += num 

    # Print sum of diviors of num_one and num_two
    print(f"Sum of divisors number one: {sum_div_one_num}")
    print(f"Sum of divisors number two: {sum_div_two_num}")

    # Check if num_one's sum of diviors is the same as num_two and opposite situation
    if sum_div_one_num == num_two and sum_div_two_num == num_one:
        result = True
    else:
       result = False

    print(f"Numbers {num_one} and {num_two} are amicable? {result}")
    print(f"Test result of case {number_case}: {result}\n")
    number_case += 1
#_______________________Program [ONE LOOP]

# amicable_pairs= [(220, 284), (1184, 1210), 
#                  (2620, 2924), (5020, 5564), 
#                  (6232, 6368), (10744, 10856), 
#                  (12285, 14595), (17296, 18416), 
#                  (63020, 76084), (66928, 66992)]

# first_num = 220
# second_num = 284

# sum_div_first_num = 0
# sum_div_second_num = 0

# for num in range(1, first_num):
#     #If fist number is divided by num
#     if(first_num % num == 0):
#         sum_div_first_num += num 

# for num in range(1, second_num):
#     #If fist number is divided by num
#     if(second_num % num == 0):
#         sum_div_second_num += num 

# print(sum_div_first_num)

# print(sum_div_second_num)
# if sum_div_first_num == second_num and sum_div_second_num == first_num:
#     print("Numbers are amicable")
       
#______________________Check cases  

# #Print tuples from list
# for case in cases:
#     # print(type(case))
      # print(case)
      # (220, 284)
      # (1184, 1210)