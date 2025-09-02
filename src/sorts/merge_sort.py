def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Якщо в лівій або правій половині залишилися елементи, 
	# додайте їх до результату
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 2]
    # numbers = [2, 3, 4, 5, 8]
    s_nums = merge_sort(numbers)
    print(numbers)
    print(s_nums)
    