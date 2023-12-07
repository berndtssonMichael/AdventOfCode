"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List
from collections import Counter

"""
My original idea was to assign each type of hand a value as a string (hand_type), '7', '6', etc.
Then replace each card with a string that corresponds to its value (rank_score).
hand_type + rank_score converted to an INT gives a good value to then sort all hands.
"""

CARDS = {
    'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10', '9': '09', '8': '08',
    '7': '07', '6': '06', '5': '05', '4': '04', '3': '03', '2': '02'
}

CARDS_WILDCARD = {
    'A': '14', 'K': '13', 'Q': '12', 'T': '10', '9': '09', '8': '08',
    '7': '07', '6': '06', '5': '05', '4': '04', '3': '03', '2': '02', 'J': '01'
}

HAND_TYPES = {
    'five_of_a_kind': '7',
    'four_of_a_kind': '6',
    'full_house': '5',
    'tree_of_a_kind': '4',
    'two_pairs': '3',
    'one_pair': '2',
    'high_card': '1'
}


class CardHand:
    bid: int                # 765
    cards: str              # '32T3K'
    no_of_jacks: int        # number of jacks in the cards, used for part 2
    total_score: int        # the total_score is used for sorting all hands
    use_wildcards: bool     # True for part 2

    def __init__(self, cards: str, bid: str, use_wildcards: bool = False):
        self.use_wildcards = use_wildcards
        self.bid = int(bid)
        self.cards = cards
        self.no_of_jacks = cards.count('J')
        self.total_score = int(self.get_type_of_hand() + self.get_card_rank())

    def __repr__(self) -> str:
        return f'cards: {self.cards}, bid: {self.bid}, jacks: {self.no_of_jacks}, \
rank_score: {self.get_card_rank()}, hand_type: {self.get_type_of_hand()}, total_score: {self.total_score}'

    def get_type_of_hand(self) -> str:

        # count cards, if we use wildcards, ignore 'J' and update the count
        if self.use_wildcards:
            _cards = Counter(self.cards.replace('J', ''))
            if _cards:
                # update the highest counter with number of jacks
                _cards.update({_cards.most_common(1)[0][0]: self.no_of_jacks})
        else:
            _cards = Counter(self.cards)

        # get the card count, high to low
        # will be empty if all cards are Jacks
        card_count = sorted(Counter(_cards).values(), reverse=True)

        if self.no_of_jacks == 5 or card_count[0] == 5:
            return HAND_TYPES['five_of_a_kind']
        elif card_count[0] == 4:
            return HAND_TYPES['four_of_a_kind']
        elif card_count[0] == 3 and card_count[1] == 2:
            return HAND_TYPES['full_house']
        elif card_count[0] == 3:
            return HAND_TYPES['tree_of_a_kind']
        elif card_count[0] == 2 and card_count[1] == 2:
            return HAND_TYPES['two_pairs']
        elif card_count[0] == 2:
            return HAND_TYPES['one_pair']
        else:
            return HAND_TYPES['high_card']

    def get_card_rank(self) -> str:
        # get correct score
        points = CARDS_WILDCARD if self.use_wildcards else CARDS

        return ''.join([points[c] for c in self.cards])

def parse_data(input_data) -> List[str]:
    values = [v for v in input_data.split('\n')]
    return values

def get_winnings(input_data: List[str], use_wildcards: bool = False) -> int:

    cards: List[CardHand] = []
    for line in input_data:
        cards.append(CardHand(*line.split(), use_wildcards))

    ranked_cards = sorted(cards, key=lambda card_hand: card_hand.total_score)

    # debug
    # for i, card in enumerate(cards, 1):
    #     print(i, card)

    return sum([card.bid * i for i, card in enumerate(ranked_cards, 1)])

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {get_winnings(input_data)}')
    print(f'Part 2: {get_winnings(input_data, True)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=7, use_example_data=False)
