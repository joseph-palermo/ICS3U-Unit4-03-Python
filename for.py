#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program uses a for do while loop to get the factorial of integers


def main():
    # this function uses a for do while loop to get the factorial of integers

    # variables
    counter = 0
    square = 1

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process & output
    for counter in range(integer + 1):
        square = counter**2
        print(counter, "² = {}"
              .format(square))


if __name__ == "__main__":
    main()
