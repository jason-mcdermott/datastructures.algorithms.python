from math import ceil

def binary_search(numbers, target):
    if target < numbers[0] or target > numbers[-1]:
        return False

    if len(numbers) == 1 and numbers[0] == target:
        return True

    middle =  ceil(len(numbers) / 2)
    left = numbers[0:middle]
    right = numbers[middle:]

    if target < right[0]:
        return binary_search(left, target)
    else:
        return binary_search(right, target)