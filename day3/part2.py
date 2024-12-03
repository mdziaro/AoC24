import re

### input
file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
data = ''.join(data)


### scan for dos and dont's
def find_dos(data):
    pattern1 = "do\(\)"
    dos = []
    dos = [m.span()[0] for m in re.finditer(pattern1, data)]

    return dos
def find_donts(data):
    pattern2 = "don't\(\)"
    donts = []
    donts = [m.span()[0] for m in re.finditer(pattern2, data)]

    return donts

def find_subsets(good, bad, length):
    subs = [(0, bad[0])]
    for i in range(len(good)):
        if good[i] > max(bad):
            subs.append((good[i], length))
            break
        for j in range(len(bad)):
            if good[i] < bad[j]:
                if bad[j] == subs[-1][1]:
                    break
                subs.append((good[i], bad[j]))
                break
    return subs


pattern3 = "mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)"
answer = []
#print(data[i])
ranges = find_subsets(find_dos(data), find_donts(data), len(data))
#print(find_dos(data))
#print(find_donts(data))
print(ranges)
for j in range(len(ranges)):
    answer.append(re.findall(pattern3, data[ranges[j][0]:ranges[j][1]]))
    
#print(answer)
count = 0
for i in range(len(answer)):
    for j in range(len(answer[i])):
        count += int(answer[i][j][0]) * int(answer[i][j][1])
print(count)