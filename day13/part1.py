import re

file = open("input.txt")
data = file.readlines()
file.close()

pattern = r"[-+]?\d+"

results = []

for line in data:
    numbers = re.findall(pattern, line)
    if numbers:
        results.append([int(num) for num in numbers])

print(results)
equations = []

for i in range(0,len(results),3):
    equations.append([results[i][0], results[i+1][0], results[i+2][0]])
    equations.append([results[i][1], results[i+1][1], results[i+2][1]])

sum = 0

for i in range(0, len(equations), 2):
    a1, b1, c1 = equations[i]
    a2, b2, c2 = equations[i+1]

    det = a1 * b2 - a2 * b1
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1

    x = det_x / det
    y = det_y / det

    if (x - x // 1 == 0) and (y - y // 1 == 0):
        sum += x*3 + y
print(sum)