# Closures 

# Example 1

def make_printer(msg):

    msg = "hi there" # Cannot be modified coz it is local variable

    def printer():
        print(msg)

    return printer


myprinter = make_printer("Hello there")
myprinter()
myprinter()
myprinter()
print('---------------------------------------------------------------------------------')

print(myprinter.__closure__[0].cell_contents) # we can get the closures

print('---------------------------------------------------------------------------------')
# Example 2

def make_counter():

    count = 0 # Local Variable
    def inner():

        nonlocal count  # Changing the variable to nonlocal so it is a free variable we can modify it 
        count += 1
        return count

    return inner


counter = make_counter()

c = counter()
print(c)

c = counter()
print(c)

c = counter()
print(c)



# Example 3


def get_multiplier(a):
    def out(b):
        return a * b
    return out

multiply_by_3 = get_multiplier(3)
print(multiply_by_3)  # It shows where the function is stored in memory
print(multiply_by_3(10))
print(get_multiplier(3)) # It shows where the function is stored in memory
print(get_multiplier(3)(10))

print('---------------------------------------------------------------------------------')

print(multiply_by_3.__closure__[0].cell_contents) 

print('---------------------------------------------------------------------------------')


# Decorators (Closures are extensively used in decorators)
