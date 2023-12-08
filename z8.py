import itertools as it
import operator
from typing import List
from math import gcd, lcm


with open("test.txt") as f:
    lines = f.read().splitlines()
    seq = lines[0]
    travel_map = {}
    
    for k,v in map(lambda s: s.split(' = '), lines[2:]):
        travel = (v.split(', ')[0][1:], v.split(', ')[1][:-1])
        print(travel)
        travel_map[k] = travel

    pos = 'AAA'
    for ind, v in enumerate(it.cycle(seq), 1):
        pos = travel_map[pos][0 if v == "L" else 1]
        if pos == 'ZZZ':
            print(ind)
            break
         
    



with open("input8.txt") as f:
    lines = f.read().splitlines()
    seq = lines[0]
    travel_map = {}
    
    for k,v in map(lambda s: s.split(' = '), lines[2:]):
        travel = (v.split(', ')[0][1:], v.split(', ')[1][:-1])
        # print(travel)
        travel_map[k] = travel
        
    
    nodes: List[str] = list(filter(lambda s: s[-1] == 'A', travel_map.keys())) 
    times = []
    print(nodes)
    for pos in nodes:
        for ind, v in enumerate(it.cycle(seq), 1):
            pos = travel_map[pos][0 if v == "L" else 1]
            
            if pos[-1] == 'Z':
                print(ind)
                times.append(ind)
                break
    
    print(times)
    for lcm_v in it.accumulate(times, lcm):
        print(lcm_v)
    
         
    
