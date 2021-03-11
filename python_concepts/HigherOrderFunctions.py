# map, filter, zip and reduce 
from functools import reduce

my_list = [1,2,3]
your_list = [10,20,30]
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 !=0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0)) # 0 acc-- initial value

print()

print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item*2, my_list)))

print(list(filter(only_odd, my_list)))

print(list(zip(my_list, your_list)))

