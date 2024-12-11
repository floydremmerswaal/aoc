#INPUT = "C:\\Users\\floyd\\aoc\\2024\\day7\\example.txt"
INPUT = "C:\\Users\\floyd\\aoc\\2024\\day7\\input.txt"

class Line:
    def __init__(self, line):
        # line example
        # 190: 10 19
        self.target = int(line.split(':')[0])
        self.inputs = line.split(':')[1].strip().split(' ')
        self.inputs = [int(i) for i in self.inputs]

def can_reach(target, inputs, acc = 0):
    if len(inputs) == 0:
        return target == acc
    else:
        return can_reach(target, inputs[1:], acc + inputs[0]) or can_reach(target, inputs[1:], acc * inputs[0])

def can_reach_part2(target: int, inputs: list[int], acc: int = 0, stack: list[str] = []) -> bool:
    if len(inputs) == 0:
        return target == acc
    else:
        plus = can_reach_part2(target, inputs[1:], acc + inputs[0], stack + ["+"]) 
        times = can_reach_part2(target, inputs[1:], acc * inputs[0], stack + ["*"])
        concat = can_reach_part2(target, inputs[1:], int(f"{acc}{inputs[0]}"), stack + ["||"])
        return plus or times or concat

with open(INPUT) as f:
    inputlines = f.readlines()

    lines = [Line(l) for l in inputlines]
    total = 0
    total2 = 0
    for l in lines:
        if can_reach(l.target, l.inputs):
            total += l.target
        # issue was that I started the acc on 0 
        # meaning the search could multiply the first number by 0
        if can_reach_part2(l.target, l.inputs[1:], l.inputs[0]):
            total2 += l.target

    print("Part 1: ", total)
    print("Part 2: ", total2)
