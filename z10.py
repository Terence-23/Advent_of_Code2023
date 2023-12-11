
from queue import Queue
from typing import List, Tuple


pipe_type ={
    # letter: (N, W, S, E)
    '|' : (1, 0, 1, 0),
    '-' : (0, 1, 0, 1),
    "L" : (1, 0, 0, 1),
    'J' : (1, 1, 0, 0),
    '7' : (0, 1, 1, 0),
    "F" : (0, 0, 1, 1),
    '.' : (0, 0, 0, 0),
    
}


class Node: 
    type = (0, 0, 0, 0)
    distance: int = -1
    
    def __init__(self, ch) -> None:
        self.type = pipe_type.get(ch, (-1, -1, -1, -1))
   
def bfs(maze: List[List[Node]], start: Tuple[int, int]):
    x, y = start
    maze[y][x].distance = 0
    
    node_que = Queue()
    
    if y > 0 and maze[y-1][x].type[2]:
        node_que.put((x, y-1))
        maze[y-1][x].distance = 1
    if x < len(maze[y]) - 1 and maze[y][x+1].type[1]:
        node_que.put((x+1, y))
        maze[y][x+1].distance = 1
    if y < len(maze) and maze[y+1][x].type[0]:
        node_que.put((x, y+1))
        maze[y+1][x].distance = 1
    if x > 0 and maze[y][x-1].type[3]:
        maze[y][x-1].distance = 1
        node_que.put((x-1, y))
    
    last_xy = x, y
    
    while not node_que.empty():
        x, y = node_que.get()
        steps = maze[y][x].distance
        node_type = maze[y][x].type
        
        if y > 0 and node_type[0] and maze[y-1][x].distance == -1:
            maze[y-1][x].distance = steps + 1
            node_que.put((x, y -1))
        if x > 0 and node_type[1] and maze[y][x-1].distance == -1:
            maze[y][x-1].distance = steps + 1
            node_que.put((x - 1, y))
        if y < len(maze) and node_type[2] and maze[y+1][x].distance == -1:
            maze[y+1][x].distance = steps + 1
            node_que.put((x, y + 1))
        if x < len(maze[y]) and node_type[3] and maze[y][x+1].distance == -1:
            maze[y][x+1].distance = steps + 1
            node_que.put((x + 1, y))
            
        last_xy = x, y
    
    for line in maze:
        for node in line:
            print(node.distance if node.distance != -1 else ' ', end=' ')
        print()
    
    return last_xy
        
        
        
with open('input10.txt') as f:
    text = f.read().splitlines()
    start_pos= (0, 0)
    for y, l in enumerate(text):
        for x, ch in enumerate(l):
            if ch == 'S':
                start_pos = x, y
                break
            
    
    maze = [[Node(ch) for ch in l] for l in text]
    
    last_xy = bfs(maze, start_pos)
    print(last_xy)
    
    x, y = last_xy
    print(maze[y][x].distance)
    
## part two

def dfs(maze: List[List[Node]], start: Tuple[int, int]):
    
    x, y = start
    side = False
    count = 0
    visited_stack = [start]
    
    node_stack = []
    if x == 0 or \
        y == 0 or \
        x == len(maze[y])-1 or \
        y == len(maze)-1 :
        side = True
    if maze[y][x].distance == -1: count += 1
    maze[y][x].distance = -6
    
    if y > 0 and maze[y-1][x].distance < 0:
        node_stack.append((x, y-1))
        maze[y-1][x].distance = -6
    if x < len(maze[y]) - 1 and maze[y][x+1].distance < 0:
        node_stack.append((x+1, y))
        maze[y][x+1].distance = -6
    if y < len(maze)-1 and maze[y+1][x].distance < 0:
        node_stack.append((x, y+1))
        maze[y+1][x].distance = -6
    if x > 0 and maze[y][x-1].distance < 0:
        maze[y][x-1].distance = -6
        node_stack.append((x-1, y))

    
    while len(node_stack):
        x, y = node_stack.pop()
        visited_stack.append((x, y))
        
        side = side or maze[y][x].__dict__.get('notisolated', False)
        
        if (x == 0 or y == 0 or 
            x == len(maze[y])-1 or 
            y == len(maze)-1 ):
            side = True
        if maze[y][x].distance == -1: count += 1
        
        if y > 0 and (maze[y-1][x].distance == -1 or maze[y-1][x].distance == -2):
            if maze[y-1][x].distance == -1:
                count += 1
            maze[y-1][x].distance = -6
            node_stack.append((x, y -1))
            
        if x > 0 and (maze[y][x-1].distance == -1 or maze[y][x-1].distance == -2):
            if maze[y][x-1].distance == -1:
                count += 1
            maze[y][x-1].distance = -6
            node_stack.append((x - 1, y))
            
        if y < len(maze) -1 and (maze[y+1][x].distance == -1 or maze[y+1][x].distance == -2):
            if maze[y+1][x].distance == -1:
                count += 1
            maze[y+1][x].distance = -6
            node_stack.append((x, y + 1))
            
        if x < len(maze[y]) -1 and (maze[y][x+1].distance == -1 or maze[y][x+1].distance == -2):
            if maze[y][x+1].distance == -1:
                count += 1
            maze[y][x+1].distance = -6
            node_stack.append((x + 1, y))
            

    for i in visited_stack:
        x, y = i
        maze[y][x].notisolated = side
    
    
    # for line in maze:
    #     for node in line:
    #         print(node.distance if node.distance < 0 else '.' if node.distance == -1 else '@' if node.distance == -2 else '*', end=' ')
    #     print()
        
    if not side:
        return count
    
    return 0


with open('input10.txt') as f:
    text = f.read().splitlines()
    start_pos= (0, 0)
    for y, l in enumerate(text):
        for x, ch in enumerate(l):
            if ch == 'S':
                start_pos = x, y
                break
    
    maze = [[Node(ch) for ch in l] for l in text]
    
    ## find the loop
    last_xy = bfs(maze, start_pos)
    print(last_xy)
    
    x, y = last_xy
    print(maze[y][x].distance)
    
    ## extend
    side_maze = []
    for line in maze:
        added = []
        for l, r in zip(line[:-1], line[1:]):
            mind = min(l.distance, r.distance)
            newNode = Node(' ')
            if mind == -1 or l.distance + r.distance - 2* mind != 1:
                newNode.distance = -2
            else:
                newNode.distance = mind
            added.append(newNode)
        new_line = [line[x >>1] if (x & 1) == 0 else added[x>>1] for x in range(len(line) + len(added))]
        # print(new_line)
        side_maze.append(new_line)
    
    new_maze = []
    for u, d in zip(side_maze[:-1], side_maze[1:]):
        added = []
        for l, r in zip(u, d):
            mind = min(l.distance, r.distance)
            newNode = Node(' ')
            if mind < 0 or l.distance + r.distance - 2* mind != 1:
                newNode.distance = -2
            else:
                newNode.distance = mind
            # print(mind, newNode.distance)
            added.append(newNode)
        
        new_maze.append(u)
        new_maze.append(added)
    new_maze.append(side_maze[-1])
    ## count 
    
    for line in new_maze:
        for node in line:
            s = str(node.distance) if node.distance >= 0 else '.' if node.distance == -1 else '@' if node.distance == -2 else '*'
            if len(s) < 2:
                s += ' '
            print(s, end=' ')
        print()
    
    print('\n')
    
    good_count = 0
    
    for y in range(len(new_maze)):
        for x in range(len(new_maze[y])):
            if new_maze[y][x].distance == -1 or \
                new_maze[y][x].distance == -2:
                    good_count += dfs(new_maze, (x, y))

    for line in new_maze:
        for node in line:
            s = str(node.distance) if node.distance >= 0 else '.' if node.distance == -1 else '@' if node.distance == -2 else '*'
            if len(s) < 2:
                s += ' '
            print(s, end=' ')
        print()
    print(good_count)   