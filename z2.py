
max_map ={
    "red" : 12,
    "green": 13,
    "blue" : 14,
}

valid = []
valid_sum = 0



def rate_game(game_data):
    
    return True

with open("input2.txt") as f:
    for line in map(str.strip, f.readlines()):
        game_id, game_data, *_ = line.split(": ")
        game_id = int(game_id[5:])
        if rate_game(game_data):
            valid += [game_id]
            valid_sum += game_id
                
print (valid)
print(sum(valid), valid_sum)

## part two

game_powers = []
power_sum = 0

with open("input2.txt") as f:
    for line in map(str.strip, f.readlines()):
        # print("\n\ngame_start\n\n")
        game_map = {}
        game_id, game_data, *_ = line.split(": ")
        game_id = int(game_id[5:])
        # print(game_map)
        for draw in game_data.split("; "):
            for val ,col in map(lambda s: s.split(" "), draw.split(", ")):
                # print(game_map)
                game_map[col] = max(game_map.get(col, 0), int(val))
                # print(val, col, game_map.get(col, 0), int(val))
                # print(game_map)
        # print()
        game_power = 1
        for v in game_map.values():
            # print(v)
            game_power *= v
        
        game_powers.append(game_power)
        power_sum += game_power

print(game_powers)
print(power_sum)
