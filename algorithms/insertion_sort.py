def insertion_sort(target: list):
    for i in range(len(target)):
        j = i
        while j > 0 and target[j-1] > target[j]:
            target[j], target[j-1] = target[j-1], target[j]
            j -= 1
