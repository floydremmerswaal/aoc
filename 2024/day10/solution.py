INPUT = "C:\\Users\\floyd\\aoc\\2024\\day10\\input.txt"

height_map: list[list[int]] = []

def trailheads(height_map: list[list[int]]) -> list[tuple[int, int]]:
    trailheads = []
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.append((i, j))
    return trailheads

def find_number_of_trails(height_map: list[list[int]], trailheads: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    trailhead_reach = {}

    for trailhead in trailheads:
        cur_height = 0
        possible_locations = {trailhead}
        next_possible_locations = set()
        reached_nines = set()

        while cur_height < 9:
            for loc in possible_locations:
                for direction in directions:
                    new_loc = (loc[0] + direction[0], loc[1] + direction[1])
                    if new_loc[0] >= 0 and new_loc[0] < len(height_map) and new_loc[1] >= 0 and new_loc[1] < len(height_map[0]):
                        if height_map[new_loc[0]][new_loc[1]] == cur_height + 1:
                            next_possible_locations.add(new_loc)
                            if height_map[new_loc[0]][new_loc[1]] == 9:
                                reached_nines.add(new_loc)
            
            possible_locations = next_possible_locations
            next_possible_locations = set()
            cur_height += 1

        trailhead_reach[trailhead] = len(reached_nines)

    return trailhead_reach

def count_paths(height_map: list[list[int]], loc: tuple[int, int], cur_height: int, visited: set) -> int:
    if height_map[loc[0]][loc[1]] == 9:
        return 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    path_count = 0

    for direction in directions:
        new_loc = (loc[0] + direction[0], loc[1] + direction[1])
        if new_loc[0] >= 0 and new_loc[0] < len(height_map) and new_loc[1] >= 0 and new_loc[1] < len(height_map[0]):
            if height_map[new_loc[0]][new_loc[1]] == cur_height + 1 and new_loc not in visited:
                visited.add(new_loc)
                path_count += count_paths(height_map, new_loc, cur_height + 1, visited)
                visited.remove(new_loc)

    return path_count

def find_number_of_paths(height_map: list[list[int]], trailheads: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    trailhead_paths = {}
    for trailhead in trailheads:
        visited = set()
        visited.add(trailhead)
        path_count = count_paths(height_map, trailhead, 0, visited)
        trailhead_paths[trailhead] = path_count

    return trailhead_paths

with open(INPUT, "r") as f:
    data = f.read().splitlines()
    for line in data:
        height_map.append([int(x) for x in line])
    trailheadlist = trailheads(height_map)
    trailhead_reach = find_number_of_trails(height_map, trailheadlist)
    trailhead_paths = find_number_of_paths(height_map, trailheadlist)
    print("Sum of all reach counts:", sum(trailhead_reach.values()))
    print("Sum of all path counts:", sum(trailhead_paths.values()))