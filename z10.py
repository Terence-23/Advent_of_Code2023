
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
    maze[x][y].distance = 0
    
    node_que = Queue()
    
    if y > 0 and maze[y-1][x].type[2]:
        node_que.put((x, y-1))
    if x < len(maze[y]) - 1 and maze[y][x+1].type[1]:
        node_que.put((x+1, y))
    if y < len(maze) and maze[y+1][x].type[0]:
        node_que.put((x, y+1))
    if x > 0 and maze[y][x-1].type[3]:
        node_que.put((x-1, y))
    
    last_xy = x, y
    
    while not node_que.empty():
        x, y = node_que.get()
        steps = maze[y][x].distance
        node_type = maze[y][x].type
        
        if y > 0 and node_type[0] and maze[y-1][x].distance == -1:
            maze[y-1][x].distance = steps + 1
            node_que.put((x, y-1))
        if x > 0 and node_type[1] and maze[y][x-1].distance == -1:
            maze[y][x-1].distance = steps + 1
            node_que.put((x- 1, y))
        if y < len(maze) and node_type[2] and maze[y+1][x].distance == -1:
            maze[y+1][x].distance = steps + 1
            node_que.put((x, y + 1))
        if x < len(maze[y]) and node_type[3] and maze[y][x+1].distance == -1:
            maze[y][x+1].distance = steps + 1
            node_que.put((x + 1, y))
            
        last_xy = x, y
    
    for line in maze:
        for node in line:
            print(node.distance, end=' ')
        print()
    
    return last_xy
        
        
        
with open('test.txt') as f:
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
    
    