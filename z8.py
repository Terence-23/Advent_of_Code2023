import itertools as it


with open("input8.txt") as f:
    lines = f.read().splitlines()
    seq = lines[0]
    travel_map = {}
    
    for k,v in map(lambda s: s.split(' = '), lines[2:]):
        travel = (v.split(', ')[0][1:], v.split(', ')[1][:-1])
        print(travel)
        travel_map[k] = travel

    pos = 'AAA'
    for ind, v in enumerate(it.cycle(seq)):
        pos = travel_map[pos][0 if v == "L" else 1]
        if pos == 'ZZZ':
            print(ind)
            break
         
    
