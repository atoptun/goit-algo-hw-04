import random
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.shell_sort import shell_sort
from sorts.bubble_sort import bubble_sort
import timeit


def main():
    small_list = [random.randint(0, 100000) for _ in range(1_000)]
    medium_list = [random.randint(0, 100000) for _ in range(10_000)]
    large_list = [random.randint(0, 100000) for _ in range(100_000)]
    huge_list = [random.randint(0, 10000000) for _ in range(1_000_000)]
    n = 5

    small_bubble_res = timeit.timeit(lambda: bubble_sort(small_list), number=n)
    small_insert_res = timeit.timeit(lambda: insertion_sort(small_list), number=n)
    small_merge_res = timeit.timeit(lambda: merge_sort(small_list), number=n)
    small_quick_res = timeit.timeit(lambda: quick_sort(small_list), number=n)
    small_shell_res = timeit.timeit(lambda: shell_sort(small_list), number=n)
    small_sorted_res = timeit.timeit(lambda: sorted(small_list), number=n)
    small_sort_res = timeit.timeit(lambda: small_list.sort(), number=n)

    medium_bubble_res = timeit.timeit(lambda: bubble_sort(medium_list), number=n)
    medium_insert_res = timeit.timeit(lambda: insertion_sort(medium_list), number=n)
    medium_merge_res = timeit.timeit(lambda: merge_sort(medium_list), number=n)
    medium_quick_res = timeit.timeit(lambda: quick_sort(medium_list), number=n)
    medium_shell_res = timeit.timeit(lambda: shell_sort(medium_list), number=n)
    medium_sorted_res = timeit.timeit(lambda: sorted(medium_list), number=n)
    medium_sort_res = timeit.timeit(lambda: medium_list.sort(), number=n)

    large_insert_res = timeit.timeit(lambda: insertion_sort(large_list), number=n)
    large_merge_res = timeit.timeit(lambda: merge_sort(large_list), number=n)
    large_quick_res = timeit.timeit(lambda: quick_sort(large_list), number=n)
    large_shell_res = timeit.timeit(lambda: shell_sort(large_list), number=n)
    large_sorted_res = timeit.timeit(lambda: sorted(large_list), number=n)
    large_sort_res = timeit.timeit(lambda: large_list.sort(), number=n)

    huge_merge_res = timeit.timeit(lambda: merge_sort(huge_list), number=n)
    huge_quick_res = timeit.timeit(lambda: quick_sort(huge_list), number=n)
    huge_shell_res = timeit.timeit(lambda: shell_sort(huge_list), number=n)
    huge_sorted_res = timeit.timeit(lambda: sorted(huge_list), number=n)
    huge_sort_res = timeit.timeit(lambda: huge_list.sort(), number=n)

    print(f'| {"Algorithm":<20} | {"Time small data (1K)":<20} | {"Time medium data (10K)":<20} | {"Time large data (100K)":<20} | {"Time huge data (1M)":<20}')
    print(f'| {"-"*20} | {"-"*20} | {"-"*20} | {"-"*20} | {"-"*20}')
    print(f'| {"Bubble":<20} | {small_bubble_res:<20.5f} | {medium_bubble_res:<20.5f} | {"None":<20} | {"None":<20}')
    print(f'| {"Insertion":<20} | {small_insert_res:<20.5f} | {medium_insert_res:<20.5f} | {large_insert_res:<20.5f} | {"None":<20}')
    print(f'| {"Merge":<20} | {small_merge_res:<20.5f} | {medium_merge_res:<20.5f} | {large_merge_res:<20.5f} | {huge_merge_res:<20.5f}')
    print(f'| {"Quick":<20} | {small_quick_res:<20.5f} | {medium_quick_res:<20.5f} | {large_quick_res:<20.5f} | {huge_quick_res:<20.5f}')
    print(f'| {"Shell":<20} | {small_shell_res:<20.5f} | {medium_shell_res:<20.5f} | {large_shell_res:<20.5f} | {huge_shell_res:<20.5f}')
    print(f'| {"Tim sorted":<20} | {small_sorted_res:<20.5f} | {medium_sorted_res:<20.5f} | {large_sorted_res:<20.5f} | {huge_sorted_res:<20.5f}')
    print(f'| {"Tim sort":<20} | {small_sort_res:<20.5f} | {medium_sort_res:<20.5f} | {large_sort_res:<20.5f} | {huge_sort_res:<20.5f}')


if __name__ == '__main__':
    main()
