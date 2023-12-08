
from enum import Enum


class HandTypes(Enum):
    FIVE = 0
    FOUR = 1
    THREE_TWO = 2
    THREE = 3
    TWO_PAIR = 4
    PAIR = 5
    HIGH = 6
    
    
strength_map = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    "8": 6,
    '7': 7,
    "6": 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12
    }

    

class Hand:
    hand_type: HandTypes
    hand: str
    bid: int
    
    def __lt__(self, oth):
        if not isinstance(oth, Hand): return False
        elif self.hand_type.value == oth.hand_type.value:
            for l, r in zip(self.hand, oth.hand):
                if strength_map[l] < strength_map[r]:
                    return True
                elif strength_map[l] > strength_map[r]:
                    return False
                
        elif self.hand_type.value < oth.hand_type.value:
            
            return True
        return False
    
    def __init__(self, hand, bid) -> None:
        self.bid = int(bid)
        self.hand = hand
        
        count = {}
        for c in hand:
            count[c] = count.get(c, 0) + 1
        
        counts = sorted(count.items(), key=lambda x: x[1], reverse=True) 
        if counts[0][1] == 5:
            self.hand_type = HandTypes.FIVE
        elif counts[0][1] == 4:
            self.hand_type = HandTypes.FOUR
        elif counts[0][1] == 3 and counts[1][1] == 2:
            self.hand_type = HandTypes.THREE_TWO
        elif counts[0][1] == 3:
            self.hand_type = HandTypes.THREE
        elif counts[0][1] == 2 and counts[1][1] == 2:
            self.hand_type = HandTypes.TWO_PAIR
        elif counts[0][1] == 2:
            self.hand_type = HandTypes.PAIR      
        else:
            self.hand_type = HandTypes.HIGH
        self.counts = counts    

sumv = 0
with open("input7.txt") as f:
    hands = sorted([Hand(*s.split(' ')) for s in f.read().splitlines()], reverse=True)
    for e, h in enumerate(hands, 1):
        print(h.hand_type, h.hand, h.bid, h.counts)
        sumv += h.bid * e
    
print(sumv)


## part two

strength_map = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 13,
    'T': 4,
    '9': 5,
    "8": 6,
    '7': 7,
    "6": 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12
    }

class Hand2:
    hand_type: HandTypes
    hand: str
    bid: int
    
    def __lt__(self, oth):
        if not isinstance(oth, (Hand2, Hand)): return False
        elif self.hand_type.value == oth.hand_type.value:
            for l, r in zip(self.hand, oth.hand):
                if strength_map[l] < strength_map[r]:
                    return True
                elif strength_map[l] > strength_map[r]:
                    return False
                
        elif self.hand_type.value < oth.hand_type.value:
            
            return True
        return False
    
    def __init__(self, hand, bid) -> None:
        self.bid = int(bid)
        self.hand = hand
        
        count = {}
        for c in hand:
            count[c] = count.get(c, 0) + 1
        
        counts = sorted(count.items(), key=lambda x: x[1], reverse=True) 
        js = count.get("J", 0) 
        print(counts)
        if 5 > js:
            if counts[0][0] == 'J':
                counts[1] = (counts[1][0], counts[1][1] + js)
            else:
                counts[0] = (counts[0][0], counts[0][1] + js)
            
            counts = list(filter(lambda t: t[0] != 'J', counts))
        
        
        print(counts)
        
        if counts[0][1] == 5:
            self.hand_type = HandTypes.FIVE
        elif counts[0][1] == 4:
            self.hand_type = HandTypes.FOUR
        elif counts[0][1] == 3 and counts[1][1] == 2:
            self.hand_type = HandTypes.THREE_TWO
        elif counts[0][1] == 3:
            self.hand_type = HandTypes.THREE
        elif counts[0][1] == 2 and counts[1][1] == 2:
            self.hand_type = HandTypes.TWO_PAIR
        elif counts[0][1] == 2:
            self.hand_type = HandTypes.PAIR      
        else:
            self.hand_type = HandTypes.HIGH
        self.counts = counts 
        
        
sumv = 0
with open("input7.txt") as f:
    hands = sorted([Hand2(*s.split(' ')) for s in f.read().splitlines()], reverse=True)
    for e, h in enumerate(hands, 1):
        print(h.hand_type, h.hand, h.bid, h.counts)
        sumv += h.bid * e
    
print(sumv)