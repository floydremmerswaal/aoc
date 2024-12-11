example = [125, 17]
input = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]

TARGET = input

def update_list(lst):
    new_lst = []
    for no in lst:
        if no == 0:
            new_lst.append(1)
        elif len(str(no)) % 2 == 0:
            string = str(no)
            new_lst.append(int(string[:len(string)//2]))
            new_lst.append(int(string[len(string)//2:]))
        else:
            new_lst.append(no * 2024)
    return new_lst


def iterate(lst: list, no: int):
    for _ in range(no):
        lst = update_list(lst)
    return lst

def update_dict_part2(dct):
    new_dct = {}
    for no, count in dct.items():
        if no == 0:
            new_dct[1] = new_dct.get(1, 0) + count
        elif len(str(no)) % 2 == 0:
            string = str(no)
            new_dct[int(string[:len(string)//2])] = new_dct.get(int(string[:len(string)//2]), 0) + count
            new_dct[int(string[len(string)//2:])] = new_dct.get(int(string[len(string)//2:]), 0) + count
        else:
            new_dct[no * 2024] = new_dct.get(no * 2024, 0) + count
    return new_dct

def iterate_part2(lst: list, iter: int) -> dict:
    dct = {}
    for no in lst:
        dct[no] = dct.get(no, 0) + 1
    for _ in range(iter):
        print(dct)
        dct = update_dict_part2(dct)
    return dct    

def count_part2(dct: dict) -> int:
    return sum(dct.values())

part1 = iterate(TARGET, 25)
part2 = iterate_part2(TARGET, 75)

print("Part 1:", len(part1))
print("Part 2:", count_part2(part2))