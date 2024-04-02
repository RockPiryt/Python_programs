"""Problem Józefa Flawiusza.

Wyobraź sobie następującą sytuację: jesteś powstańcem żydowskim podczas oblężenia Jotopaty w 67 roku n.e. 
Zostałeś otoczony wraz z 40 innymi żołnierzami przez legiony rzymskie, ale nie chcecie zostać pojmani. 
Po krótkiej naradzie wymyśliliście rozwiązanie: ustawicie się w kole 
i pierwsza osoba zabije tą znajdującą się bezpośrednio po lewej, 
kolejny żołnierz zabije kompana po swojej lewej, aż do momentu gdy zostanie tylko jeden powstaniec, 
który popełni samobójstwo. Ty jednak nie chcesz zginąć z ręki innego powstańca ani popełniać samobójstwa. 
Gdzie w takim razie ustawić się w tym kręgu, aby uniknąć śmerci? 
Jak opracować uniwersalny sposób na obliczenie bezpiecznego miejsca w kole dla 
dowolnej liczby znajdujących się w nim osób? W opisanej wyżej sytuacji znalazł się Józef Flawiusz, 
rzymsko-żydowski historyk, od którego wzięła się nazwa problemu.

Napisz program rozwiązujący ten problen dla dowolnej liczby żołnierzy."""


# Understand problem 
"""
The Josephus Problem - Numberphile
https://www.youtube.com/watch?v=uCsD3ZGzMgE
"""

# Joseph problem algorithm
"""
If n=2**a (n is a power of 2) safe_postion is 1
If n is not a power of 2 we find highest  power of 2 smaller than or  equal to n.
n = 2**power + r_value
safe_position = r_value * 2 + 1
"""
#__________________________Program [ONE LOOP]
# # Number of soldiers
# n = 77
# print(f"Number of soldiers: {n}")

# # Initial values
# power = 1
# highest_power_two = 2**0 #1

# # Find highest  power of 2 smaller than or  equal to n 
# while highest_power_two * 2 <= n:
#     highest_power_two *= 2
#     power += 1

# print(f"The highest  power of 2 smaller than or  equal to n is: 2^{power} = {highest_power_two }")


# # r value is the remainder
# r_value =  n - highest_power_two 
# print(f"r_value: {r_value}")

# # Calculate Safe position 
# print("Safe position formula - Joseph problem:\n")
# print("f(n) = r_value * 2 + 1")
# safe_position = r_value * 2 + 1
# print(f"The survivor is at position: {safe_position}")


#_______________________Create cases

cases = [(1, 1), (2, 1), (3, 3), (4, 1), (5, 3), (6, 5), (7, 7), (8, 1), (9, 3), (10, 5), (11, 7), (12, 9), (13, 11), (14, 13), (41,19)]
cases_length = len(cases)

print("For loop in cases list:\n")
for case in range(0, cases_length):
    # print(f"Case: {case+1}")

    # Number of soldiers
    n_soldiers = cases[case][0]
    print(f"Number of soldiers: {n_soldiers}")

    # Expected result
    safe_postion_result = cases[case][1]
    # print(f"Expected Safe position: {safe_postion_result}")

    # Initial values
    power = 1
    highest_power_two = 2**0 #1

    # Find highest  power of 2 smaller than or  equal to n 
    while highest_power_two * 2 <= n_soldiers:
        highest_power_two *= 2
        power += 1

    # r value is the remainder
    r_value =  n_soldiers - highest_power_two 

    # Calculate Safe position 
    calc_safe_position = r_value * 2 + 1
    print(f"The survivor is at position: {calc_safe_position}")


    # Check if calculated_result is the same as the result in case
    if calc_safe_position == safe_postion_result:
        result = True
    else: 
        result = False

    print(f"Case number: {case+1} : {result}\n")






