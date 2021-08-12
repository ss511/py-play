import random


if __name__ == "__main__":
    rolls = int(input("Number of rolls"))
    while rolls:
        print(random.randint(1, 6))
        rolls -= 1
