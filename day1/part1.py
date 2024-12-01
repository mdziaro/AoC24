file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
    data[i] = data[i].split(" ")
    data[i]= (data[i][0], data[i][3])

left_list, right_list, diffs = [], [], []
for i in range(len(data)):
    left_list.append(int(data[i][0]))
    right_list.append(int(data[i][1]))
left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    diffs.append(abs(left_list[i]-right_list[i]))
print(sum(diffs))