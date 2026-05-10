# Exercise 13 - Sum & Product


def calculate_sum(numbers):
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]

    for i, n in enumerate(numbers):
        if i == 0:
            continue

        result += n

    return result


def calculate_product(numbers):
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return 1

    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]

    for i, n in enumerate(numbers):
        if i == 0:
            continue

        result *= n

    return result


assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30

assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840
