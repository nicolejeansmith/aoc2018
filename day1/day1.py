def adjust_freq(sequence):
    freq = 0
    for change in sequence:
        freq += change
    return (freq)


def test():
    assert adjust_freq((1, -2, 3, 1)) == 3
    assert adjust_freq((1,1,1)) == 3
    assert adjust_freq((1, 1, -2)) == 0
    assert adjust_freq((-1, -2, -3)) == -6

with open('./input.txt') as file:
    input = [int(line.strip()) for line in file.readlines()]
    print(adjust_freq(input))
