def parse_input(input_str):
    blueprints = []
    for line in input_str.strip().split("\n"):
        blueprint = {}
        for i, part in enumerate(line.strip().split(" ")):
            if i % 4 == 0:
                resource = part.strip(":")
                blueprint[resource] = {}
            elif i % 4 == 1:
                blueprint[resource]["ore"] = int(part.strip("ore"))
            elif i % 4 == 3:
                blueprint[resource]["time"] = int(part.strip("minute"))
        blueprints.append(blueprint)
    return blueprints

def simulate(blueprint, minutes):
    ore_count = 0
    clay_count = 0
    obsidian_count = 0
    geode_count = 0
    ore_robots = 0
    clay_robots = 0
    obsidian_robots = 0
    for minute in range(minutes):
        if ore_robots == 0:
            if ore_count >= blueprint["ore robot"]["ore"]:
                ore_count -= blueprint["ore robot"]["ore"]
                ore_robots += 1
        else:
            ore_count += ore_robots
        if clay_robots == 0:
            if ore_count >= blueprint["clay robot"]["ore"]:
                ore_count -= blueprint["clay robot"]["ore"]
                clay_robots += 1
        else:
            clay_count += clay_robots
        if obsidian_robots == 0:
            if ore_count >= blueprint["obsidian robot"]["ore"] and clay_count >= blueprint["obsidian robot"]["clay"]:
                ore_count -= blueprint["obsidian robot"]["ore"]
                clay_count -= blueprint["obsidian robot"]["clay"]
                obsidian_robots += 1
        else:
            obsidian_count += obsidian_robots
        if obsidian_count >= blueprint["geode robot"]["obsidian"] and ore_count >= blueprint["geode robot"]["ore"]:
            obsidian_count -= blueprint["geode robot"]["obsidian"]
            ore_count -= blueprint["geode robot"]["ore"]
            geode_count += 1
    return geode_count

input_str = "Blueprint 1:\n  Each ore robot costs 4 ore.\n  Each clay robot costs 2 ore.\n  Each obsidian robot costs 3 ore and 14 clay.\n  Each geode robot costs 2 ore and 7 obsidian.\n\nBlueprint 2:\n  Each ore robot costs 2 ore.\n  Each clay robot costs 3 ore.\n  Each obsidian robot costs 3 ore and 14 clay.\n  Each geode robot costs 2 ore and 7 obsidian."


bp = parse_input(input_str)
print(bp)
