from math import ceil

def binary_search(numbers, target):
    if target < numbers[0] or target > numbers[-1]:
        return False

    middle =  ceil(len(numbers) / 2)
    left = numbers[0:middle]
    right = numbers[middle:]

    if target < right[0]:
        for l in left:
            if l == target:
                return True
    else:
        for r in right:
            if r == target:
                return True

    return False
        