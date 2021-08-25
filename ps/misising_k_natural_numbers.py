def missing_k_numbers(numbers, k):
    """
    This method finds the first k missing numbers from a list of given numbers.
    :param numbers: the list of numbers.
    :param k: the first k missing natural numbers.
    :return: the list of missing numbers.
    """
    result = []

    list_set = set(numbers)

    i = 1
    counter = 0
    while counter < k:
        if i not in list_set:
            result.append(i)
            counter += 1
        i += 1

    return result


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    missing_numbers = missing_k_numbers(arr, k)

    print(missing_numbers)
