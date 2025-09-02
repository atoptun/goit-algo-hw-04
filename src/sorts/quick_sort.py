def quick_sort(lst):
    result = lst[:]
    if len(result) <= 1:
        return result
    pivot = result[len(result) // 2]
    left = [x for x in result if x < pivot]
    middle = [x for x in result if x == pivot]
    right = [x for x in result if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 2]
    # numbers = [2, 3, 4, 5, 8]
    s_nums = quick_sort(numbers)
    print(numbers)
    print(s_nums)
