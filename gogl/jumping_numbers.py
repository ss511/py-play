"""
Print all Jumping Numbers smaller than or equal to a given value

A number is called as a Jumping Number if all adjacent digits in it differ by 1.
The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
Given a positive number x, print all Jumping Numbers smaller than or equal to x.
The numbers can be printed in any order.

Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101
"""
from queue import Queue


def fetch_all_jumping_numbers(x):
    jumping_numbers = [0]
    q = Queue()

    for i in range(1, 10):
            q.put(i)

    while not q.empty():
        temp = q.get()
        if temp <= x:
            jumping_numbers.append(temp)
            last_digit = temp % 10
            if last_digit == 0:
                q.put(temp*10 + last_digit+1)
            elif last_digit == 9:
                q.put(temp*10 + last_digit-1)
            else:
                q.put(temp * 10 + last_digit - 1)
                q.put(temp * 10 + last_digit + 1)

    return jumping_numbers


if __name__ == "__main__":
    x = 105
    print(fetch_all_jumping_numbers(x))