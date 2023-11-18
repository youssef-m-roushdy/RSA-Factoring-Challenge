#!/usr/bin/python3
import sys

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

    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        number = int(number)
        factors = factorize(number)
        if factors:
            print(f"{number}={factors[1]}*{factors[0]}")

if __name__ == "__main__":
    main()
