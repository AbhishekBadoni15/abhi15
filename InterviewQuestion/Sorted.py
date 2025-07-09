def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

print(is_sorted([1, 2, 3, 4])) 
print(is_sorted([4, 3, 2, 1]))    
print(is_sorted([1, 3, 2]))       
