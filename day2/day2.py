from collections import Counter
from itertools import combinations

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

# Day 2 Part 2

# First determine which are the two correct boxes
# Having looked up string metrics and discovered the hamming distance
def find_common_letters(iter):
    pairs = [c for c in combinations(iter, 2)]
    def hamming_distance(s1, s2):
        return sum(char1 != char2 for char1, char2 in zip(s1, s2))
    final_pair = False
    index = 0
    while not final_pair:
        pair = pairs[index]
        index += 1
        dist = hamming_distance(pair[0], pair[1])
        if dist == 1:
            final_pair = True
    result = ''.join([char1 for char1, char2 in zip(pair[0], pair[1]) if char1 == char2])
    return(result)


def test2():
    example = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    assert find_common_letters(example) == 'fgij'

print(find_common_letters(input))