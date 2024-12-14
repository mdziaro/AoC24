import re

file = open("input.txt")
data = file.readlines()
file.close()

for i in range(len(data)):
    data[i] = re.findall(r"(-?\d+,-?\d+)", data[i]) 
    data[i][0] = list(map(int, data[i][0].split(",")))
    data[i][1] = list(map(int, data[i][1].split(",")))

width = 101
height = 103

fin_pos = []

for i in range(len(data)):
    pos = data[i][0]
    v = data[i][1]
    pos[0] = (pos[0] + v[0] * 100) % width
    pos[1] = (pos[1] + v[1] * 100) % height
    fin_pos.append((pos[0], pos[1]))

results = [0, 0, 0, 0]

for i in range(len(fin_pos)):
    if fin_pos[i][0] < width // 2 and fin_pos[i][1] < height // 2:
        results[0] += 1
    elif fin_pos[i][0] > width // 2 and fin_pos[i][1] < height // 2:
        results[1] += 1
    elif fin_pos[i][0] < width // 2 and fin_pos[i][1] > height // 2:
        results[2] += 1
    elif fin_pos[i][0] > width // 2 and fin_pos[i][1] > height // 2:
        results[3] += 1

print(results)
print(results[0] * results[1] * results[2] * results[3])
