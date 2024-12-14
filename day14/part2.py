import re
from PIL import Image, ImageDraw
for seconds in range(0,10000):
    
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
        pos[0] = (pos[0] + v[0] * seconds) % width
        pos[1] = (pos[1] + v[1] * seconds) % height
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

    if max(results) > 200:
        view = [["." for _ in range(width+2)] for _ in range(height+2)]
        for i,j in fin_pos:
            view[i][j] = "#"
        img = Image.new("RGB", (width + 2, height + 2), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        for i in range(height + 2):
            for j in range(width + 2):
                if view[i][j] == "#":
                    draw.point((j, i), fill=(0, 0, 0))

        img.save(f"output_second_{seconds}.png")