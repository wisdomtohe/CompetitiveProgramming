def sum_two_smallest_numbers(numbers):
    first = numbers.pop(numbers.index(min(numbers)))
    second = numbers.pop(numbers.index(min(numbers)))
    print(first+second)
sum_two_smallest_numbers([5, 8, 12, 18, 22])
