#!/usr/bin/python3
import sys
import time


def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = file.readlines()
    except FileNotFoundError:
        print("File not found")
        exit(1)

    start_time = time.time()
    for number in numbers:
        number = int(number)
        factors = factorize(number)
        if factors:
            print(f"{number}={factors[1]}*{factors[0]}")
        if time.time() - start_time > 5:
            print("Time limit exceeded")
            exit(1)


if __name__ == "__main__":
    main()
