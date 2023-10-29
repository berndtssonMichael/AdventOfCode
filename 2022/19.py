import sys
from typing import List, Tuple

def collect_ore(time: int, ore_count: int, blueprints: List[Tuple[Tuple[int, int, int], Tuple[int, int]]]) -> int:
    def cost_of_building_robots(robot_counts: List[int], blueprint: Tuple[Tuple[int, int, int], Tuple[int, int]]) -> int:
        ore_cost = 0
        ore_robot_count, clay_robot_count, obsidian_robot_count = robot_counts
        ore_robot_cost, clay_robot_cost, obsidian_robot_cost = blueprint[0]
        ore_cost += ore_robot_count * ore_robot_cost
        ore_cost += clay_robot_count * clay_robot_cost
        ore_cost += obsidian_robot_count * obsidian_robot_cost
        return ore_cost

    def robots_produced_per_minute(robot_counts: List[int], blueprint: Tuple[Tuple[int, int, int], Tuple[int, int]]) -> List[int]:
        ore_robot_count, clay_robot_count, obsidian_robot_count = robot_counts
        geode_robot_count, _ = blueprint[1]
        ore_robots_produced = ore_robot_count
        clay_robots_produced = min(ore_robot_count, clay_robot_count)
        obsidian_robots_produced = min(clay_robots_produced, obsidian_robot_count)
        geode_robots_produced = min(obsidian_robots_produced, geode_robot_count)
        return [ore_robots_produced, clay_robots_produced, obsidian_robots_produced, geode_robots_produced]

    max_geode_count = -sys.maxsize
    for blueprint in blueprints:
        ore_robot_count = 1
        clay_robot_count = 0
        obsidian_robot_count = 0
        geode_robot_count = 0
        for minute in range(time):
            ore_count -= cost_of_building_robots([ore_robot_count, clay_robot_count, obsidian_robot_count], blueprint)
            if ore_count < 0:
                break
            ore_robot_count, clay_robot_count, obsidian_robot_count, geode_robot_count = robots_produced_per_minute(
                [ore_robot_count, clay_robot_count, obsidian_robot_count, geode_robot_count], blueprint
            )
        max_geode_count = max(max_geode_count, geode_robot_count)
    return max_geode_count

# Example

blueprints = [
    ((4, 2, 3), (2, 7)),
    ((2, 3, 3), (3, 12))
]
time = 24
ore_count = 10
print(collect_ore(time, ore_count,
