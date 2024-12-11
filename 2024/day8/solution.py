from typing import Dict, Tuple
import math

INPUT = "C:\\Users\\floyd\\aoc\\2024\\day8\\input.txt"

data: list[list[str]] = []

antennas: Dict[str, list[Tuple[int, int]]] = {}

with open(INPUT, 'r') as infile:
    for line in infile:
        data.append(list(line.strip()))

locations = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
locations2 = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            if data[i][j] not in antennas:
                antennas[data[i][j]] = []
            antennas[data[i][j]].append((i, j))
            locations2[i][j] = 1



def is_valid(x: int, y: int) -> bool:
    return x >= 0 and x < len(data) and y >= 0 and y < len(data[0])

# part 1
for key in antennas:
    for i in range(len(antennas[key])):
        for j in range(i+1, len(antennas[key])):
            x1, y1 = antennas[key][i]
            x2, y2 = antennas[key][j]
            dx, dy = x2 - x1, y2 - y1
            
            points_left = [ x1 - dx, y1 - dy ]
            points_right = [ x2 + dx, y2 + dy ]

            if is_valid(*points_left):
                locations[points_left[0]][points_left[1]] += 1
            if is_valid(*points_right):
                locations[points_right[0]][points_right[1]] += 1

# part 2
for key in antennas:
    for i in range(len(antennas[key])):
        for j in range(i+1, len(antennas[key])):
            x1, y1 = antennas[key][i]
            x2, y2 = antennas[key][j]
            dx, dy = x2 - x1, y2 - y1

            points_left = [ x1 - dx, y1 - dy ]
            points_right = [ x2 + dx, y2 + dy ]

            if is_valid(*points_left):
                locations2[points_left[0]][points_left[1]] += 1
            if is_valid(*points_right):
                locations2[points_right[0]][points_right[1]] += 1

            # simplify the direction vector
            gcd = math.gcd(dx, dy)
            dx //= gcd
            dy //= gcd

            k = 1
            left_valid = True
            right_valid = True
            while (left_valid or right_valid):
                k += 1
                points_left = [ x1 - k*dx, y1 - k*dy ]
                points_right = [ x1 + k*dx, y1 + k*dy ]
                if is_valid(*points_left):
                    locations2[points_left[0]][points_left[1]] += 1
                else:
                    left_valid = False
                if is_valid(*points_right):
                    locations2[points_right[0]][points_right[1]] += 1
                else:
                    right_valid = False

count = 0
count2 = 0
for i in range(len(locations)):
    for j in range(len(locations[i])):
        if locations[i][j] != 0:
            count += 1
        if locations2[i][j] != 0:
            count2 += 1

print("Part 1:", count)
print("Part 2:", count2)