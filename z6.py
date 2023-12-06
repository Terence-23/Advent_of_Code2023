# v = t
# s = (tc - t)t

# s = tc*t - t*t
# 0 = -t*t + tc*t - s
# 0 = t^2 - tc* t + s

# d = tc^2 - 4 * s
# t = (tc +- sqrt(d)) /2
import re

from math import sqrt, floor, ceil

num_regex = re.compile("[0-9]+")


with open("input6.txt") as f:
    times, dists = f.read().splitlines()
    times = (int(x.group()) for x in num_regex.finditer(times))
    dists = (int(x.group()) for x in num_regex.finditer(dists))
    out = []
    res = 1
    
    for tc, s in zip(times, dists):
        dd = tc*tc - 4*s
        d = sqrt(dd)
        
        tmi = (tc - d) / 2
        tmi = floor(tmi + 1)
        
        tma = (tc + d) / 2
        tma = ceil(tma - 1)
        
        n = tma - tmi + 1
        out.append(n)
        res *= n
        # print(f"t^2 + {tc} * t + {s} : t1: {tmi}, t2: {tma}, dd: {dd}, n: {n}")
 
    print(out)
    print(res)
    
 
## part two   
 
with open("input6.txt") as f:
    times, dists = f.read().splitlines()
    times = int(''.join(num_regex.findall(times)))
    dists = int(''.join(num_regex.findall(dists)))
    print(times, dists)
    out = []
    res = 1
    
    for tc, s in zip([times], [dists]):
        dd = tc*tc - 4*s
        d = sqrt(dd)
        
        tmi = (tc - d) / 2
        tmi = floor(tmi + 1)
        
        tma = (tc + d) / 2
        tma = ceil(tma - 1)
        
        n = tma - tmi + 1
        out.append(n)
        res *= n
        # print(f"t^2 + {tc} * t + {s} : t1: {tmi}, t2: {tma}, dd: {dd}, n: {n}")
 
    print(out)
    print(res)
 