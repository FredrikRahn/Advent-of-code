import sys

def inverse_captcha(input):
    sum = 0;
    step = 1

    for a in range(len(input)):
        next_index = (a + step) % len(input)
        if input[a] == input[next_index]:
            sum += int(input[a])
    print sum


def main(input):
    inverse_captcha(input)

if __name__ == "__main__":
    main(sys.argv[1])
