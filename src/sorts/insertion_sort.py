def insertion_sort(lst):
    result = lst[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i-1
        while j >=0 and key < result[j] :
            result[j+1] = result[j]
            j -= 1
        result[j+1] = key 
    return result


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 2]
    # numbers = [2, 3, 4, 5, 8]
    s_nums = insertion_sort(numbers)
    print(numbers)
    print(s_nums)
