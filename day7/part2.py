file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
    data[i] = data[i].split(":")
    data[i][1] = data[i][1][1:].split(" ")
    data[i][0] = int(data[i][0])
    data[i][1] = list(map(int, data[i][1]))

def add_one(num: str):
    length = len(num)
    num = bin(int(num, 2) + 1)[2:]
    return num.zfill(length)

result_sum = 0
not_found = []
for i in range(len(data)):
    target = data[i][0]
    numbers = data[i][1]
    string = "0" * (len(numbers) - 1)
    found = False
    while string != "1" * (len(numbers) - 1):
        result = numbers[0]
        for j in range(len(string)):
            if string[j] == "0":
                result += numbers[j + 1]
            else:
                result *= numbers[j + 1]
        if result == target:
            result_sum += target
            found = True
            break
        string = add_one(string)
    if not found:
        result = numbers[0]
        for j in range(len(string)):
            if string[j] == "0":
                result += numbers[j + 1]
            else:
                result *= numbers[j + 1]
        if result == target:
            found = True
            result_sum += target
        if not found:
            not_found.append(data[i])
            

# Part 2
import numpy as np

def add_one_ternary(num: str):
    length = len(num)
    num = int(num, 3) + 1
    num = np.base_repr(num, base=3)
    return num.zfill(length)       
for i in range(len(not_found)):
    target = not_found[i][0]
    numbers = not_found[i][1]
    
    string = "0" * (len(numbers) - 1)
    found = False
    
    while string != "2" * (len(numbers) - 1):
        result = numbers[0]
        for j in range(len(string)):
            if string[j] == "0":
                result += numbers[j + 1]
            elif string[j] == "1":
                result *= numbers[j + 1]
            elif string[j] == "2":
                result = int(str(result) + str(numbers[j + 1]))
        if result == target:
            result_sum += target
            found = True
            break
        string = add_one_ternary(string)
    if not found:
        result = numbers[0]
        for j in range(len(string)):
            if string[j] == "0":
                result += numbers[j + 1]
            elif string[j] == "1":
                result *= numbers[j + 1]
            elif string[j] == "2":
                result = int(str(result) + str(numbers[j + 1]))
        if result == target:
            result_sum += target

print(result_sum)
