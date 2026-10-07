def collatz_sequence(n):
    sequence = [n]
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps


def main():
    start = 27
    sequence, steps = collatz_sequence(start)
    print(", ".join(str(n) for n in sequence))
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
