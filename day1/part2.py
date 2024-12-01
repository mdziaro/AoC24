### input
file = open("input.txt", "r")
data = file.readlines()
file.close()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]
    data[i] = data[i].split(" ")
    data[i]= (data[i][0], data[i][3])

### end input

left_list, right_list = [], []
for i in range(len(data)):
    left_list.append(int(data[i][0]))
    right_list.append(int(data[i][1]))

simil = []
for i in range(len(left_list)):
    simil.append(left_list[i]*right_list.count(left_list[i]))
print(sum(simil))