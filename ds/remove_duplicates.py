if __name__ == "__main__":
    input_numbers = input("Enter integers with space separation: ")
    numbers = list(map(int, input_numbers.split()))

    print("Input numbers are: ", numbers)

    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    print("Unique numbers are: ", unique_numbers)
    print("Max number is: ", max(unique_numbers))
