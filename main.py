import random

def random_list(n):
    return [random.randint(0,99) for _ in range(n)]

def mean(lst):
    return sum(lst)/len(lst) if lst else float('nan')

def median(lst):
    len_lst = len(lst)
    return lst[len_lst // 2] if len_lst % 2 != 0 else ((lst[len_lst // 2 - 1]+ lst[len_lst // 2])/2)

def mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    return [item for item, count in frequency.items() if max_count == count]

n = int(input('Enter the array dimension: '))

lst = random_list(n)

print(lst)
print('Mean value: ', mean(lst))
print('Median: ', median(lst))
print('Mode: ', mode(lst))