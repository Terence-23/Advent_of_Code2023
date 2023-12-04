import re

nums = {
    "one" : 1, 
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine" : 9
}


sum = 0
with open("input1.txt") as f:
    for line in f.readlines():
        p = re.compile("(\d|one|two|three|four|five|six|seven|eight|nine)")
        val = p.search(line).group()
        num1 = int(nums.get(val, val))
        p = re.compile("(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)")
        val =p.search(line[::-1]).group()
        num2 = int(nums.get(val[::-1], val))
        print(line, num1 * 10 + num2)
        sum += num1 * 10 + num2
print(sum)        