import collections

if __name__ == "__main__":
    """
    Given a list of shoes available with shoe owners and customers buying the shoe.
    Find out the total earning of the seller. 
    Shoes are in limited quantity so make sure to keep the counter of that. 
    """

    shoes_count = int(input())

    shoes_rep = collections.Counter(map(int, input().split()))
    customers_count = int(input())
    earning = 0

    for i in range(customers_count):
        size, price = list(map(int, input().split()))
        if shoes_rep[size]:
            earning += price
            shoes_rep[size] -= 1

    print(earning)
