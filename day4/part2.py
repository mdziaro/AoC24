file = open("input.txt")
data = file.read()
 
def add_padding(data, padding_size=4):
    rows = data.splitlines()
 
    row_length = len(rows[0])
    padding_row = '.' * (row_length + 2 * padding_size)
 
    # Add the padding on top and bottom
    padded_data = [padding_row] * padding_size  # Top padding
    for row in rows:
        padded_data.append('.' * padding_size + row + '.' * padding_size)  # Left and right padding on each row
    padded_data.extend([padding_row] * padding_size)  # Bottom padding
 
    return padded_data
 
data = add_padding(data)
 
count = 0
for i in range(4,len(data)-4):
    for j in range(4,len(data[i])-4):
        if data[i][j] == "M" and data[i][j+2] == "M" and data[i+1][j+1] == "A" and data[i+2][j] == "S" and data[i+2][j+2] == "S":
            count += 1
        if data[i][j] == "S" and data[i][j+2] == "S" and data[i+1][j+1] == "A" and data[i+2][j] == "M" and data[i+2][j+2] == "M":
            count += 1
        if data[i][j] == "M" and data[i][j+2] == "S" and data[i+1][j+1] == "A" and data[i+2][j] == "M" and data[i+2][j+2] == "S":
            count += 1
        if data[i][j] == "S" and data[i][j+2] == "M" and data[i+1][j+1] == "A" and data[i+2][j] == "S" and data[i+2][j+2] == "M":
            count += 1
print(count)