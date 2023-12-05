import re


num_regex = re.compile("[\d]+")
card_sum = 0

with open("input4.txt") as f:
    for line in f.read().splitlines():
        id, data = line.split(':')
        id = int(num_regex.search(id).group())
        winning, yours = data.split(' | ')
        winning = set(int(s.group()) for s in num_regex.finditer(winning))
        yours = set(int(s.group()) for s in num_regex.finditer(yours))
        
        winning_count = len(winning) + len(yours) - len(winning.union(yours))
        # print(winning_count, len(winning) + len(yours), len(winning.union(yours)))
        card_sum +=  (1 << winning_count-1) if winning_count > 0 else (0)
        print(f"id {id}: {(1 << winning_count-1) if winning_count > 0 else (0)}")
        
print(card_sum)
        
        
## part two


with open("input4.txt") as f:
    line_list = f.read().splitlines()
    card_num = len(line_list)
    cards = [1 for _ in range(len(line_list))]
    
    for ind, line in enumerate(line_list):
        id, data = line.split(':')
        id = int(num_regex.search(id).group())
        winning, yours = data.split(' | ')
        
        winning = set(int(s.group()) for s in num_regex.finditer(winning))
        
        yours = set(int(s.group()) for s in num_regex.finditer(yours))
        winning_count = len(winning) + len(yours) - len(winning.union(yours))
        for i in range(ind + 1, min(ind + 1 + winning_count, len(cards))):
            cards[i] += cards[ind]

print(cards)
print(sum(cards))