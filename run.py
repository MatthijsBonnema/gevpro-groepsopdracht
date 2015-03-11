#!/usr/bin/python3
# File: run.py.py
# Author: Matthijs Bonnema
# Date: 3/11/15
# Info: 

import sys
import room_generator
import hero


def main():
    name = input("What is your name?\n")

    hunter = hero.Hero(name)
    print(hunter)


if __name__ == "__main__":
    main()