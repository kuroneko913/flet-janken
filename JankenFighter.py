import numpy as np
from jankenHand import Hand
import pickle
import pathlib

class JankenFighter:
    PROP_FILE_NAME = 'janken_prop.bin'

    def __init__(self):
        self.probabillity = [1/3, 1/3, 1/3]
        self.count = {
            Hand.ROCK.value:1, 
            Hand.SCISSORS.value:1, 
            Hand.PAPER.value:1
        }
        if (pathlib.Path(self.PROP_FILE_NAME).exists()):
            self.load_prop()
        
    def doJanken(self, target_hand):
        print(self.probabillity)
        result = np.random.choice([Hand.ROCK, Hand.SCISSORS, Hand.PAPER], p=self.probabillity)
        self.update_probabillity(target_hand)
        return result

    def update_probabillity(self, target_hand:Hand):
        self.count[target_hand.value] += 1
        self.probabillity = list(map(lambda x:x/sum(self.count.values()), self.count.values()))
        self.probabillity = [self.probabillity[1], self.probabillity[2], self.probabillity[0]]
        with open('janken_prop.bin', 'wb')as f:
            pickle.dump(self.count, f)
        
    def load_prop(self):
        with open('janken_prop.bin', 'rb') as f:
            self.count = pickle.load(f)
        self.probabillity = list(map(lambda x:x/sum(self.count.values()), self.count.values()))
        self.probabillity = [self.probabillity[1], self.probabillity[2], self.probabillity[0]]