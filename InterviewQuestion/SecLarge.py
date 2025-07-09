def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 4, 45, 99, 99]))  
