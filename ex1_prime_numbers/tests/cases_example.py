cases = ((1, True), (2, False), (13, False), (64, True), (997, False), (1001*1001, True))

# ================
for case in cases:
    N = case[0]# dana wejściowa np 64
    result = False
    i = 0

    # sprawdzamy czy 64 jest kwadratem jakiejś liczby
    while i <= N and not result:
        if i*i == N: # 8*8 = 64
            result = True
        i += 1

    print(case, ": ", result == case[1])