from concurrent.futures import ThreadPoolExecutor, Future

tp = ThreadPoolExecutor(max_workers=10)


def merge_fn(array_1, array_2):
    result = []
    i, j = 0, 0

    while (i < len(array_1)) and (j < len(array_2)):
        if array_1[i] < array_2[j]:
            result.append(array_1[i])
            i += 1
        else:
            result.append(array_2[j])
            j += 1

    while i < len(array_1):
        result.append(array_1[i])
        i += 1

    while j < len(array_2):
        result.append(array_2[j])
        j += 1

    return result


def merge_sort(arr: list, threadpool: ThreadPoolExecutor):
    if len(arr) < 2:
        return arr

    mid_idx = len(arr) // 2
    left_future: Future = threadpool.submit(merge_sort, arr[:mid_idx], threadpool)
    right_future: Future = threadpool.submit(merge_sort, arr[mid_idx:], threadpool)

    left = left_future.result()
    right = right_future.result()

    return merge_fn(left, right)


data = [1, 10, 90, 4, 5, 8, 92, 4]

sorted_arr_future = tp.submit(merge_sort, data, tp)
print(sorted_arr_future.result())
