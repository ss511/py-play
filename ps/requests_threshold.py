"""
The program solves the following problem.
A gateway drops requests based on following rules:
1. At every sec, number of transactions couldn't exceed 3.
2. In 10 sec period, number of transactions couldn't exceed 20.
3. In 60 sec period, number of transactions couldn't exceed 60.
4. Even if a request is dropped it will be calculated for future calculation for rule number 2 and 3.

I/P - [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
O/P - 7
Let's say length here is 27, index is 0 to 26.
1 at index 3 is dropped.
7 at index 20, 21, and 22 is dropped because it breaches rule number 2.
11 at index 24, 25 and 26 is dropped because it breaches rule number 2.
Though the sliding window for 11 is considered from sec 2.
"""


def get_dropped_count(requests):
    size = len(requests)
    dropped_count = 0
    dropped_dict = {}

    for i in range(size):
        if i > 2 and requests[i] == requests[i-3]:
            if requests[i] not in dropped_dict or dropped_dict[requests[i]] != i:
                dropped_dict[requests[i]] = i
                dropped_count += 1
                print(f"Packet {requests[i]} at {i}th index dropped")
        elif i > 19 and requests[i] - requests[i-20] < 10:
            if requests[i] not in dropped_dict or dropped_dict[requests[i]] != i:
                dropped_dict[requests[i]] = i
                dropped_count += 1
                print(f"Packet {requests[i]} at {i}th index dropped")
        elif i > 59 and requests[i] - requests[i-60] < 60:
            if requests[i] not in dropped_dict or dropped_dict[requests[i]] != i:
                dropped_dict[requests[i]] = i
                dropped_count += 1
                print(f"Packet {requests[i]} at {i}th index dropped")

    return dropped_count


if __name__ == "__main__":
    requests_time = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
    print("The number of dropped requests are: ", get_dropped_count(requests_time))