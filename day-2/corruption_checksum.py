import sys
import itertools

def corruption_checksum_part1(input):
    with open(input + '.txt', 'r') as file:
        matrix = [map(int,line.split()) for line in file]
        print sum([max(row) - min(row) for row in matrix])

def corruption_checksum_part2(input):
    checksum = 0
    with open(input + '.txt', 'r') as file:
        matrix = [map(int,line.split()) for line in file]
        for row in matrix:
            for tuple in itertools.combinations(iter(row),2):
                part_sum = check_division_and_divide(tuple)
                if(part_sum != None):
                    checksum += part_sum
    print checksum

def check_division_and_divide(tuple):
    if int(tuple[0]) % int(tuple[1]) == 0:
        return (tuple[0]/tuple[1])
    if int(tuple[1] % int(tuple[0])) == 0:
        return (tuple[1]/tuple[0])

def main(input):
    corruption_checksum_part2(input)

if __name__ == "__main__":
    main(sys.argv[1])
