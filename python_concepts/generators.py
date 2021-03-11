#Generators
# A generator-function is defined like a normal function, 
# but whenever it needs to generate a value, 
# it does so with the yield keyword rather than return. 
# If the body of a def contains yield, 
# the function automatically becomes a generator function.


def generator_function(num):
    for i in range(num):
        yield i*2

# for item in generator_function(100):
#     print(item)

g = generator_function(10)
print(next(g)) # 0
print(next(g)) # 2
print(next(g)) # 4
print(next(g)) # 6
print(next(g)) # 8
print(next(g) * next(g))
        # 10