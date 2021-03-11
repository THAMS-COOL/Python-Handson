class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    def my_decorator(func):
        def wrapper():
            print('Wrapper inside function')
            func()
            print('Function Called ')
    
    def say_whee():
        print('Wheel')
    
    say_whee = my_decorator(say_whee)
    

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.my_decorator(say_whee))




