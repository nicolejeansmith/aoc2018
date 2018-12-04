# Part One
def adjust_freq(sequence):
    freq = 0
    for change in sequence:
        freq += change
    return (freq)


def test1():
    assert adjust_freq((1, -2, 3, 1)) == 3
    assert adjust_freq((1, 1, 1)) == 3
    assert adjust_freq((1, 1, -2)) == 0
    assert adjust_freq((-1, -2, -3)) == -6

test1()

with open('./input.txt') as file:
    input = [int(line.strip()) for line in file.readlines()]

print(adjust_freq(input))

# Part Two
def find_first_dupe(sequence):
    freq = 0
    display = set([0])
    index = 0
    size = len(sequence)
    while len(display) == index + 1:
        freq += sequence[index % size]
        display.add(freq)
        index += 1
    return(freq)

def test2():
    assert find_first_dupe((1, -2, 3, 1)) == 2
    assert find_first_dupe((1, -1)) == 0
    assert find_first_dupe((3, 3, 4, -2, -4)) == 10
    assert find_first_dupe((-6, 3, 8, 5, -6)) == 5
    assert find_first_dupe((7, 7, -2, -7, -4)) == 14

test2()

print(find_first_dupe(input))