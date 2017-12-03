import sys

def first_december(input):
    sum = 0;
    for a in range(len(input)):
        if a+1 != len(input) and input[a] == input[a+1]:
            sum += int(input[a])
        if a+1 == len(input):
            if input[0] == input[-1]:
                sum += int(input[a])
    print sum


def main(input):
    first_december(input)

if __name__ == "__main__":
    main(sys.argv[1])
