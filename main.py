import random

def random_list(n):
    return [random.randint(0,99) for _ in range(n)]

def mean(lst):
    return sum(lst)/len(lst) if lst else float('nan')

n = int(input('Enter the array dimension: '))

lst = random_list(n)

print(lst)
print('Mean value: ', mean(lst))