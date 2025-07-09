def count_occurrences(lst):
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    return count

print(count_occurrences([1, 2, 2, 3, 1, 4, 2]))
