moveset = [(571, 532, False, 100), (796, 530, True, 0), (573, 646, False, 100), (796, 646, True, 0)]

def check_availability():
    flag = 0
    for current in moveset:
        if current[2] == True and current[3] == 0:
            flag += 1
    return flag != sum(1 for current in moveset if current[2] == True)

for test_current in moveset:
    test_current[3] -= 1
    
print(moveset)

if not check_availability():
    print("Entrou")