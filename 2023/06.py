from numpy import prod

def part1(game_info) -> int:
    total_winnings = []
    for time, distance in game_info:
        winnings = 0
        for charge_time in range(time + 1):
            if charge_time * (time - charge_time) > distance:
                winnings += 1
        total_winnings.append(winnings)
    return prod(total_winnings)

def part2(game_info) -> int:
    total_winnings = []
    for time, distance in game_info:
        winnings = 0
        for charge_time in range(time + 1):
            if charge_time * (time - charge_time) > distance:
                winnings += 1
        total_winnings.append(winnings)
    return total_winnings[0]

def solve_puzzle(use_example_data: bool = False) -> None:

    # game_info = [(time, distance)]

    if use_example_data:
        game_info = [(7, 9), (15, 40), (30, 200)]
        game_info_part2 = [(71530, 940200)]
    else:
        game_info = [(48, 255), (87, 1288), (69, 1117), (81, 1623)]
        game_info_part2 = [(48876981, 255128811171623)]

    print(f'Part 1: {part1(game_info)}')
    print(f'Part 2: {part2(game_info_part2)}')


if __name__ == '__main__':

    solve_puzzle(use_example_data=False)
