from enum import Enum

class Hand(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

    def __str__(self):
        japanese_hand_names = {
            'ROCK':'グー',
            'SCISSORS':'チョキ',
            'PAPER': 'パー'
        }
        return japanese_hand_names[self.name]

class JankenHand:
    def __init__(self, janken_hand_name:Hand):
        self.janken_win_hands = {
            Hand.ROCK : Hand.PAPER,
            Hand.SCISSORS : Hand.ROCK,
            Hand.PAPER : Hand.SCISSORS 
        }
        self.janken_hand_name = janken_hand_name
        self.win_hand_name = self.janken_win_hands[self.janken_hand_name]
    
    def fight(self, other_hand_name:Hand):
        if (other_hand_name == self.janken_hand_name):
            return 'draw'
        if (self.win_hand_name == other_hand_name):
            return 'lose'
        return 'win'


