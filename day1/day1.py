def official_input():
    file = open("input.txt")

    output = []

    for line in file.readlines():
        output.append((line[0], int(line[1:])))

    file.close()

    return output


def example_input():
    file = open("example_input.txt")

    output = []

    for line in file.readlines():
        output.append((line[0], int(line[1:])))

    return output


def calculate_zeroes(actions):
    prev = 50
    current = 50
    num_zeroes = 0

    for action in actions:
        prev = current
        if action[0] == "L":
            current -= action[1]
        elif action[0] == "R":
            current += action[1]

        # Number of times the dial points to zero
        if current == 0:
            num_zeroes += 1

        # Number of times the dial crossed zero
        num_zeroes += abs(current // 100)

        if prev == 0 and current < 0:
            num_zeroes -= 1
        elif current % 100 == 0 and current < 0:
            num_zeroes += 1

        current %= 100

    return num_zeroes


def main():
    result = calculate_zeroes(official_input())
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
