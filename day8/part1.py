file = open("input.txt", "r")
data = file.readlines()

for i in range(len(data)):
    if data[i][-1] == "\n":
        data[i] = data[i][:-1]

letters_to_places = {}

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ".":
            pass
        elif letters_to_places.get(data[i][j]) == None:
            letters_to_places[data[i][j]] = [(i, j)]
        else:
            letters_to_places[data[i][j]].append((i,j))
print(letters_to_places)

locations = set()
for key in letters_to_places:
    lista = letters_to_places[key]
    print(lista)
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            diff = (lista[j][0]-lista[i][0], lista[j][1]-lista[i][1])
            locations.add((lista[i][0]-diff[0], lista[i][1]-diff[1]))
            locations.add((lista[j][0]+diff[0], lista[j][1]+diff[1]))

# remove out of bounds
height = len(data)-1
width = len(data[1])-1
right_locations = []
locations = list(locations)
for i in range(len(locations)):
    if locations[i][0] < 0 or locations[i][0] > height or locations[i][1] < 0 or locations[i][1] > width:
        pass
    else:
        right_locations.append(locations[i])

print(len(right_locations))