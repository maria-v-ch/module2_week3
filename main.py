from functools import reduce


def process_numbers(numbers):
    positive_numbers = filter(lambda x: x > 0, numbers)
    doubled_numbers = list(map(lambda x: x ** 2, positive_numbers))
    result_of_process = reduce(lambda x, y: x + y, doubled_numbers)
    return result_of_process


numbers = (-1, 2, 5)
print(process_numbers(numbers))


