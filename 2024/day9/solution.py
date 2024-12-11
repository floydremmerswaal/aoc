#INPUT = "C:\\Users\\floyd\\aoc\\2024\\day9\\input.txt"
INPUT = "C:\\Users\\floyd\\aoc\\2024\\day9\\example.txt"

# class that holds a value and an id
# id -1 represents empty space

class Block:
    def __init__(self, size: int, id: int):
        self.size = size
        self.id = id
    def __str__(self):
        return f"Block[s:{self.size}, id:{self.id}]"

def is_compact(input: list) -> list:
    # check if the only empty space is at the end
    for i, block in enumerate(input):
        if (block == -1):
            # check if the rest of the list is empty
            for j in range(i, len(input)):
                if (input[j] != -1):
                    return False 
    return True

def compact(input: list) -> list:
    while not is_compact(input):
        # find the first empty space
        first_empty = 0
        for i, block in enumerate(input):
            if (block == -1):
                first_empty = i
                break
        
        # find the rightmost block
        rightmost = 0
        for i, block in reversed(list(enumerate(input))):
            if (block != -1):
                rightmost = i
                break
        
        # move the rightmost block to the first empty space
        input[first_empty] = input[rightmost]
        input[rightmost] = -1
    return input

def compact2(input: list[Block]) -> list[Block]:
    # iterate over the list in reverse
    copy = input.copy()
    for i, block_tomove in reversed(list(enumerate(input))):
        done = False
        print_blocks(input)
        # if the block is empty
        if not block_tomove.id == -1:
            # attempt to place the block in the first empty space
            for j, empty_block in enumerate(copy):
                print("finding empty block of size", block_tomove.size)
                print(empty_block)
                if empty_block.id == -1 and block_tomove.size <= empty_block.size:
                    print("found empty block")
                    leftover_space = empty_block.size - block_tomove.size
                        # if there is leftover space
                        # swap and insert an empty block with the leftover space
                    print("Swapping and inserting")
                    print_blocks(input)
                    temp_size = block_tomove.size
                    temp_id = block_tomove.id
                    copy[i].size = empty_block.size
                    copy[i].id = empty_block.id
                    copy[j].size = temp_size
                    copy[j].id = temp_id
                    if (leftover_space > 0):
                        copy.insert(j+1, Block(leftover_space, -1))  
                    print_blocks(input)
                    done = True
                    break
            if done:
                continue
    return copy
    
def block_list_to_int_list(input: list[Block]) -> list[int]:
    result = []
    for block in input:
        for _ in range(block.size):
            result.append(block.id)
    return result

def calculate_hash2(input: list[Block]) -> int:
    calculate_hash(block_list_to_int_list(input))


def calculate_hash(input: list) -> int:
    total = 0
    for i, block in enumerate(input):
        if (block == -1):
            return total
        total += block * i

    return -1 

def print_blocks(input: list[Block]):
    for block in input:
        for _ in range(block.size):
            if (block.id == -1):
                print(".", end="")
            else:
                print(block.id, end="")
        print("_", end="")
    print()

def print_list(input: list[int]):
    for block in input:
            if (block == -1):
                print(".", end="")
            else:
                print(block, end="")
    print()
        

def main():
    with open(INPUT, 'r') as f:
        blocks: list[int] = []
        input = f.read().strip()
        for i, char in enumerate(input):
            n = int(char)
            if (i % 2 == 0):
                for _ in range(n):
                    blocks.append(round(i/2))
            else:
                for _ in range(n):
                    blocks.append(-1)    
        compacted = compact(blocks)
        print(calculate_hash(compacted))   

def main2():
    with open(INPUT, 'r') as f:
        blocks: list[Block] = []
        input = f.read().strip()
        for i, char in enumerate(input):
            n = int(char)
            if (i % 2 == 0):
                blocks.append(Block(n, round(i/2)))
            else:
                blocks.append(Block(n, -1))
        compacted = compact2(blocks)
        print(calculate_hash2(compacted))
            

if __name__ == '__main__':
    main2()