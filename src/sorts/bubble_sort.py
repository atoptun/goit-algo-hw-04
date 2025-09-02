def bubble_sort(lst):
    result = lst[:]
    n = len(result)
    for i in range(n-1):
        is_changed = False
        for j in range(0, n-i-1): 
            if result[j] > result[j+1] :
                result[j], result[j+1] = result[j+1], result[j] 
                is_changed = True
        if not is_changed:
            break
    return result


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 2]
    # numbers = [4, 3, 2, 5, 8]
    s_nums = bubble_sort(numbers)
    print(numbers)
    print(s_nums)
