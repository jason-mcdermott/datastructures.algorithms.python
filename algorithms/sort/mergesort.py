from math import floor

def sort(numbers):
    if len(numbers) == 1:
        return numbers

    middle =  floor(len(numbers) / 2)
    lh = numbers[0:middle]
    rh = numbers[middle:]

    return merge(sort(lh), sort(rh))



def merge(left, right):
    merged = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        elif len(left) > 0:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    return merged

    

nums = [3, 5, 2, 9, 10, 8, 1, 4, 6, 7 ]
print(sort(nums))