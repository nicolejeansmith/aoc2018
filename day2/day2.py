from collections import Counter

with open('./input.txt') as file:
    input = [line.strip() for line in file.readlines()]
# Day 2 Part 1
def calc_checksum(iter):
    two_count = sum([2 in Counter(id).values() for id in iter])
    three_count = sum([3 in Counter(id).values() for id in iter])
    return two_count * three_count

def test1():
    example = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    assert calc_checksum(example) == 12

test1()

print(calc_checksum(input))