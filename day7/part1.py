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
            result_sum += target
            

print(result_sum)
