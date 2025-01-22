import random
import statistics

def random_list(n):
    return [random.randint(0,99) for _ in range(n)]

def find_mean(lst):
    return sum(lst)/len(lst) if lst else float('nan')

def find_median(lst):
    sorted_lst = sorted(lst)
    len_lst = len(lst)
    return sorted_lst[len_lst // 2] if len_lst % 2 != 0 else ((sorted_lst[len_lst // 2 - 1]+ sorted_lst[len_lst // 2])/2)

def find_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = max(frequency.values())
    return [item for item, count in frequency.items() if max_count == count]

def find_range(lst):
    return max(lst) - min(lst)

def find_variance(lst):
    mean = find_mean(lst)
    return sum((item - mean) ** 2 for item in lst) / (len(lst) - 1)

def find_standart_deviation(lst):
    return find_variance(lst) ** 0.5

n = int(input('Enter the array dimension: '))

lst = random_list(n)

print(lst)
print('Mean value: ', find_mean(lst))
print('Statistics Mean value: ', statistics.mean(lst), '\n')
print('Median: ', find_median(lst))
print('Statistics Median: ', statistics.median(lst), '\n')
print('Mode: ', find_mode(lst))
print('Statistics Mode: ', statistics.mode(lst), '\n')
print('Range: ', find_range(lst), '\n')
print('Variance: ', find_variance(lst))
print('Statistics Variance: ', statistics.variance(lst), '\n')
print('Standart Deviation: ', find_standart_deviation(lst))
print('Statistics Standart Deviation: ', statistics.stdev(lst), '\n')
