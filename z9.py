def next(seq):
    if max(seq) == 0 and min(seq) == 0:
        print(seq)
        return [0 for _ in seq]
    n_seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    lower_seq = next(n_seq)
    seq += [lower_seq[-1] + seq[-1]]
    # print(seq)
    return seq


with open("input9.txt") as f:
    lines = f.read().splitlines()
    added = []
    
    
    for l in lines:
        v = next(list(map(int, l.split(' '))))
        print(v)
        added.append(v[-1])
        
    print(added)
    print(sum(added))
        
        
#part two

with open("test.txt") as f:
    lines = f.read().splitlines()
    added = []
    
    
    for l in lines:
        v = next(list(map(int, reversed(l.split(' ')))))
        print(v)
        added.append(v[-1])
        
    print(added)
    print(sum(added))