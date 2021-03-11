#Decorators
def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('************')
    return wrap_func

# @my_decorator
def hello():
    print('helloooooooo')

# Similar to 
# hello2 = my_decorator(hello)
# hello2()
# or 
# print(my_decorator(hello)())

# print(hello())
print(my_decorator(hello)())

#-----------------------------------------------

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('************')
    return wrap_func

@my_decorator
def hey(greeting, emoji=':)'):
    print(greeting, emoji)

hey('hiiii')

# Example of Decorators

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn (*args, **kwargs)
        t2 = time()
        print(f'it tool {t2-t1}s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()


#--------------------------------------------------------------------------------------------------------------
# Example

def capitalize_names(func):
    def func_wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return func_wrapper

@capitalize_names
def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)

class Person:
    def __init__(self):
        self.firstname = "John"
        self.lastname = "Doe"

    @capitalize_names
    def get_fullname(self):
        return "{}, {}".format(self.lastname, self.firstname) # or f'{lastname}, {firstname}'

print(get_fullname('Rahman', 'Solanke'))

my_person = Person()
print(my_person.get_fullname())



#---------------------------------------------------------------------------------------------
#multiple decorators


def capitalize_names(func):
    def func_wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return func_wrapper

def lump_names(func):
    def func_wrapper(*args, **kwargs):
        return '@' + func(*args, **kwargs).replace(', ', '')
    return func_wrapper

@lump_names
@capitalize_names
def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)


print(get_fullname(' mv ', 'Thamaraikkannan'))

