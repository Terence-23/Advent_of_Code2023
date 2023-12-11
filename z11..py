class Galaxy:
    x = 0
    y = 0
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
    
    def distance(self, oth):
        if not isinstance(oth, Galaxy): return 0
        x_dif = self.x - oth.x
        y_dif = self.y - oth.y
        distance = x_dif.__abs__()+ y_dif.__abs__()
        return distance
    
    def expanded_distance(self, oth, mul, expanded_y, expanded_x):
        if not isinstance(oth, Galaxy): return 0
        x_dif = sum([1 if expanded_x[x] == 0 else mul for x in range(min(self.x, oth.x), max(self.x, oth.x))])
        y_dif = sum([1 if expanded_y[y] == 0 else mul for y in range(min(self.y, oth.y), max(self.y, oth.y))])
        distance = x_dif+ y_dif
        return distance
    
        
with open("input11.txt") as f:
    sky = [[x for x in line] for line in f.read().splitlines()]
    
    ## expand
    expanded_r = []
    for ind, r in enumerate(sky):
        if r.count('#') == 0:
            expanded_r.append(ind)
    
    for i in expanded_r[::-1]:
        sky.insert(i, sky[i][:])
    
    expanded_c = []
    for ind, c in enumerate(zip(*sky)):
        if c.count('#') == 0:
            expanded_c.append(ind)
    
    
    for i in expanded_c[::-1]:
        for x in range(len(sky)):
            sky[x].insert(i, '.')
    print(sky)
    
    ## find galaxies
    galaxies = []
    for y in range(len(sky)):
        for x in range(len(sky[y])):
            if sky[y][x] == '#': galaxies.append(Galaxy(x, y))
            
    galaxy_pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            galaxy_pairs.append((galaxies[i], galaxies[j]))
    
    distance = 0
    for l,r in galaxy_pairs:
        distance += l.distance(r)
        
    print(distance)
        

## part two

with open("input11.txt") as f:
    sky = [[x for x in line] for line in f.read().splitlines()]
    
    ## expand
    expanded_r = []
    for ind, r in enumerate(sky):
        if r.count('#') == 0:
            expanded_r.append(1)
        else:
            expanded_r.append(0)
        
    
    expanded_c = []
    for ind, c in enumerate(zip(*sky)):
        if c.count('#') == 0:
            expanded_c.append(1)
        else:
            expanded_c.append(0)

    print(sky)
    print(expanded_c)
    print(expanded_r)
    
    ## find galaxies
    galaxies = []
    for y in range(len(sky)):
        for x in range(len(sky[y])):
            if sky[y][x] == '#': galaxies.append(Galaxy(x, y))
            
    galaxy_pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            galaxy_pairs.append((galaxies[i], galaxies[j]))
    
    distance = 0
    for l,r in galaxy_pairs:
        distance += l.expanded_distance(r, 1_000_000, expanded_r, expanded_c)
        
    print(distance)
        
    
    