# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150


import random
import time

from bubble_sort import bubble_sort


def merge_sort(lst):
    index_half_list = len(lst) // 2
    sorted_list = list()
    index_1 = 0
    index_2 = index_half_list

    if len(lst) > 2:
        lst = merge_sort(lst[:index_2]) + merge_sort(lst[index_2:])
    if len(lst) != 1:
        while True:
            if lst[index_1] < lst[index_2]:
                sorted_list.append(lst[index_1])
                index_1 += 1
            elif lst[index_1] > lst[index_2]:
                sorted_list.append((lst[index_2]))
                index_2 += 1
            else:
                sorted_list.append(lst[index_1])
                sorted_list.append(lst[index_2])
                index_1 += 1
                index_2 += 1

            if index_1 == index_half_list:
                sorted_list.extend(lst[index_2:])
                break
            elif index_2 == len(lst):
                sorted_list.extend(lst[index_1:index_half_list])
                break
    else:
        sorted_list.append(lst[0])

    return sorted_list


# unsorted_list = list(map(int, input().split(", ")))
# unsorted_list = [1, 40, 20, 27, 3, 1, 4, 2, 12, -1]

is_successfully = True
for n in range(1, 100000):
    unsorted_list = list()
    # n = random.randint(10, 100000)
    for _ in range(n):
        unsorted_list.append(random.randint(-1000000, 1000000))

    begin1 = time.time()
    merge_sorted_list = merge_sort(unsorted_list)
    end1 = time.time()

    begin2 = time.time()
    bubble_sorted_list = bubble_sort(unsorted_list)
    end2 = time.time()

    print(f"merge / bubble sorted: {(end1 - begin1)/(end2 - begin2)},"
          f" \t merge: {(end1 - begin1)} s, "
          f"\t bubble: {(end2 - begin2)} s, n = {n} \n")

    for i in range(len(unsorted_list)):
        if merge_sorted_list[i] != bubble_sorted_list[i]:
            print("NO")
            print("merge: " + str(merge_sorted_list))
            print("bubble: " + str(bubble_sorted_list))
            is_successfully = False
            break
    if not is_successfully:
        print("merge != bubble")
        break
