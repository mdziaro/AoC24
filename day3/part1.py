import re

### input
file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
print(data)
print(len(data))

pattern = "mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)"
answer = []
for i in range(len(data)):
    #print(data[i])
    answer.append(re.findall(pattern, data[i]))

count = 0
for i in range(len(answer)):
    print(answer[i])
    for j in range(len(answer[i])):
        count += int(answer[i][j][0]) * int(answer[i][j][1])
print(count)