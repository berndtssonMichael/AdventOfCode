"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple, Dict

def find_in_map(seed: int, map: List[Tuple[int, int, int]]) -> int:
    # check if seed is in map
    for row in map:
        offset, start_seed, range_len = row
        if start_seed <= seed < start_seed + range_len:
            return seed + offset - start_seed

    return seed

def parse_data(input_data):
    seeds = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    # add data to each list
    current_map = None
    for line in input_data.split('\n'):
        if line:
            if line.startswith("seeds:"):
               seeds += [int(x) for x in line.split() if x.isdigit()]
            elif line.startswith("seed-to-soil map:"):
                current_map = seed_to_soil_map
            elif line.startswith("soil-to-fertilizer map:"):
                current_map = soil_to_fertilizer_map
            elif line.startswith("fertilizer-to-water map:"):
                current_map = fertilizer_to_water_map
            elif line.startswith("water-to-light map:"):
                current_map = water_to_light_map
            elif line.startswith("light-to-temperature map:"):
                current_map = light_to_temperature_map
            elif line.startswith("temperature-to-humidity map:"):
                current_map = temperature_to_humidity_map
            elif line.startswith("humidity-to-location map:"):
                current_map = humidity_to_location_map
            else:
                values = [int(x) for x in line.split()]
                current_map.append(tuple(values))

    return (seeds, [seed_to_soil_map, soil_to_fertilizer_map,
                   fertilizer_to_water_map, water_to_light_map,
                   light_to_temperature_map, temperature_to_humidity_map,
                   humidity_to_location_map])

def part1(seeds, map_info: List[List[Tuple[int, int, int]]]) -> int:
    locations = set()

    for seed in seeds:
        curr_pos = seed
        for map in map_info:
            curr_pos = find_in_map(curr_pos, map)
        locations.add(curr_pos)

    return min(locations)


def part2(seeds, map_info: List[List[Tuple[int, int, int]]]) -> int:
    locations = set()
    ix = 1
    # assume even number of seeds - or this will blow up :)
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            ix += 1
            curr_pos = seed
            for map in map_info:
                curr_pos = find_in_map(curr_pos, map)
            locations.add(curr_pos)

    return min(locations)


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        seeds, map_info = parse_data(puzzle.examples[0].input_data)
    else:
        seeds, map_info = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(seeds, map_info)}')
    #print(f'Part 2: {part2(seeds, map_info)}')

if __name__ == '__main__':

    solve_puzzle(year=2023, day=5, use_example_data=False)
