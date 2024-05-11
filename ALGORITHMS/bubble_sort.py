# ALGORITHM Bubble sort on list
num_list = [6, 5, 4, 9, 2, 1, 3, 8, 7, 0]

# Loop througt all elemets list
for i in range(len(num_list)):

    # Loop to compare each 2 pairs (last element is not compare)
    # last_index = len(num_list) - i - 1 # max index 9, and we dont compre last number
    for j in range(0, len(num_list) - i - 1):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp

# print(num_list)
