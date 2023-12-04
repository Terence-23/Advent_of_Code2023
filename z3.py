
import re

symbol_regexp = re.compile("[^A-Za-z0-9.\s]")

def adjacent_to_symbol(start, finish, line, text):
    for l in text[line-1 if line > 0 else 0:line+2]:
        check_str = l[ start - 1 if start > 0 else 0 : finish + 1]
        match = symbol_regexp.search(check_str)
        if match != None: return True
    
    return False

num_regexp = re.compile('\d+')
sumv = 0

with open("input3.txt") as f:
    text = f.read().splitlines()
    for ind, l in enumerate(text):
        i = 0
        num = num_regexp.search(l, i)
        while num != None:
            
            if adjacent_to_symbol(num.start(), num.end(), ind, text):
                # print("increment")
                sumv += int(num.group())
            else: 
                print("num: ", num.group())
                lind = num.start() - 1 if num.start() > 0 else 0
                print([l[ lind :num.end()+1] for l in text[ind-1 if ind > 0 else 0:ind+2]])
            
            i = num.end()
            num = num_regexp.search(l, i)
print(sumv)
# 528819


## part two

asterisk_regexp = re.compile("\*")
pos_map = {}

def find_asterisks(line, start, end, text):
    
    for i, l in enumerate(text[line-1 if line > 0 else 0:line+2]):
        check_str = l[start - 1 if start > 0 else 0 : end + 1]
        for match in asterisk_regexp.finditer(check_str):
            addr = ( i + (line-1 if line > 0 else 0), match.start() + (start - 1 if start > 0 else 0) )
            val = pos_map.get(addr, (1,0))
            pos_map[addr] = (val[0] * int(text[line][start:end]), val[1]+ 1)
        
with open("input3.txt") as f:
    text = f.read().splitlines()
    for ind, l in enumerate(text):
        for num in num_regexp.finditer(l):
            
            print(num.group())
            find_asterisks(ind, num.start(), num.end(), text)
            
            
print(pos_map)          
print(sum((v[0] for _,v in pos_map.items() if v[1] > 1)))