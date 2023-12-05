'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

from typing import List


def read_map(indices: List[int], mapv: str):
    mapv = mapv.split(":\n")[1].splitlines()
    true_map = [tuple(map(int, x.split())) for x in mapv]
    out = []
    
    for ind in indices:
        val = None
        
        for l, r, mod in true_map:
            diff= ind - r
            if mod > diff >= 0: 
                val = l + diff
                break
        
        if val == None: out.append(ind)
        else: out.append(val)
    
    return out

with open("input5.txt") as f:
    seed, soil, fertilizer, water, light, temp, humidity, location = f.read().split('\n\n')
    seeds = [int(x) for x in seed.split(': ')[1].split(' ')]
    soils = read_map(seeds, soil)
    fertilizers = read_map(soils, fertilizer)
    waters = read_map(fertilizers, water)
    lights = read_map(waters, light)
    temps = read_map(lights, temp)
    hums = read_map(temps, humidity)
    locs = read_map(hums, location)
    
    # print(seeds)
    # print(soils)
    # print(fertilizers)
    # print(waters)
    # print(lights)
    # print(temps)
    # print(hums)
    # print(locs)
    # print()
    
    print(min(locs))

## part two
def zip_array(array, n):
    return [tuple(array[ind: ind + n]) for ind in range(0, len(array), n)]

def read_map_ranges(ranges, mapv):
    mapv = mapv.split(":\n")[1].splitlines()
    # (out_start, in_start, len)
    true_map = sorted((tuple(map(int, x.split())) for x in mapv), key = lambda a: a[1])
    out = []
    
    # ranges_v = 
    print(ranges)
    
    for start, max_count in ranges:
        left = start
        ind = 0
        while ind < len(true_map):
            print(left, max_count, true_map[ind]) 
            if left < true_map[ind][1]:
                print("less")
                range_count = min(true_map[ind][1] - left, max_count)
                out.append((left, range_count))
                max_count -= range_count
                left += range_count
            elif true_map[ind][1] + true_map[ind][2] > left >= true_map[ind][1]:
                print("in")
                range_count = min(true_map[ind][1] + true_map[ind][2] - left, max_count)
                out.append((true_map[ind][0] - true_map[ind][1] + left, range_count))
                max_count -= range_count
                left += range_count
            else: 
                print("next")
                ind += 1    
            
            if max_count == 0: break
        print("end")
        if max_count!= 0:
            out.append((left, max_count))
            
            
    return out

with open("input5.txt") as f:
    seed, soil, fertilizer, water, light, temp, humidity, location = f.read().split('\n\n')
    seeds = zip_array([int(x) for x in seed.split(': ')[1].split(' ')], 2)
    soils = read_map_ranges(seeds, soil)
    fertilizers = read_map_ranges(soils, fertilizer)
    waters = read_map_ranges(fertilizers, water)
    lights = read_map_ranges(waters, light)
    temps = read_map_ranges(lights, temp)
    hums = read_map_ranges(temps, humidity)
    locs = read_map_ranges(hums, location)
    
    print(seeds)
    print(soils)
    print(fertilizers)
    print(waters)
    print(lights)
    print(temps)
    print(hums)
    print(locs)
    print()
    
    # first element of the tuple is the smallest start of the range which is also the number we seek
    print(min(locs))