# merge sort
import random
import time


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

unsorted_list = list()
n = random.randint(1, 50)
for _ in range(n):
    unsorted_list.append(random.randint(-1000, 1000))


begin = time.time()
sorted_list = merge_sort(unsorted_list)
end = time.time()

print("Unsorted_list: " + str(unsorted_list))
print(f"sorted in {end - begin} seconds, n = {n} \n")
print("Sorted_list: " + str(sorted_list))
