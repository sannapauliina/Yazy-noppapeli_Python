import random
from collections import Counter

def roll_dice(keep=None):
    if keep is None:
        keep = []
    dice = keep + [random.randint(1, 6) for _ in range(5 - len(keep))]
    return sorted(dice)

def calculate_score(dice, category):
    counts = Counter(dice)
    
    if category == "ones":
        return dice.count(1) * 1
    elif category == "twos":
        return dice.count(2) * 2
    elif category == "threes":
        return dice.count(3) * 3
    elif category == "fours":
        return dice.count(4) * 4
    elif category == "fives":
        return dice.count(5) * 5
    elif category == "sixes":
        return dice.count(6) * 6
    elif category == "three of a kind":
        for num, count in counts.items():
            if count >= 3:
                return sum(dice)
        return 0
    elif category == "four of a kind":
        for num, count in counts.items():
            if count >= 4:
                return sum(dice)
        return 0
    elif category == "full house":
        if sorted(counts.values()) == [2, 3]:
            return 25
        return 0
    elif category == "small straight":
        if set([1, 2, 3, 4]).issubset(dice) or set([2, 3, 4, 5]).issubset(dice) or set([3, 4, 5, 6]).issubset(dice):
            return 30
        return 0
    elif category == "large straight":
        if set([1, 2, 3, 4, 5]).issubset(dice) or set([2, 3, 4, 5, 6]).issubset(dice):
            return 40
        return 0
    elif category == "yatzy":
        if len(counts) == 1:
            return 50
        return 0
    elif category == "chance":
        return sum(dice)
    return 0

def player_turn():
    rolls_left = 3
    kept_dice = []

    while rolls_left > 0:
        roll = roll_dice(kept_dice)
        print("You rolled:", roll)

        keep = input("Enter numbers to keep (comma separated), or press Enter to reroll all: ")
        if keep:
            kept_dice = [int(n) for n in keep.split(",") if int(n) in roll]
        else:
            kept_dice = []

        rolls_left -= 1

    print("Final dice:", kept_dice)
    return kept_dice

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = {}
    
    def update_score(self, category, score):
        self.scores[category] = score

def play_yatzy():
    categories = [
        "ones", "twos", "threes", "fours", "fives", "sixes",
        "three of a kind", "four of a kind", "full house",
        "small straight", "large straight", "yatzy", "chance"
    ]

    players = [Player(input("Enter name for player 1: ")), Player(input("Enter name for player 2: "))]
    
    for player in players:
        print(f"\n{player.name}'s turn")
        for category in categories:
            print(f"\nPlaying for category: {category}")
            final_dice = player_turn()
            score = calculate_score(final_dice, category)
            player.update_score(category, score)
            print(f"Score for {category}: {score}")

    print("\nFinal Scores:")
    for player in players:
        print(f"\n{player.name}'s scores:")
        for category, score in player.scores.items():
            print(f"{category}: {score}")
        print("Total Score:", sum(player.scores.values()))

if __name__ == "__main__":
    print("Welcome to Yatzy!")
    play_yatzy()
