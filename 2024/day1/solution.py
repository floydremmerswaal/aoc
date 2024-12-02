
left = []
right = []

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        strings = line.split()
        left.append(int(strings[0]))
        right.append(int(strings[1]))

    left.sort()
    right.sort()

# solution 1
diff = 0
for i in range(len(left)):
    diff += abs(left[i] - right[i])
print(diff)

# solution 2

# preprocess right array and build a dictionary
right_dict = {}
for i in range(len(right)):
    if right[i] in right_dict:
        right_dict[right[i]] += 1
    else:
        right_dict[right[i]] = 1

total = 0
for i in range(len(left)):
    right_occurence = right_dict.get(left[i], 0)
    total += left[i] * right_occurence

print(total)
