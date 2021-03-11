# Error Handling
while True:
    try:
        age = int(input('whats your age? '))
        10/age
        print(age)
    except ValueError: 
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else: 
        print('thank you!!!!')
        break

def sum(n1, n2):
    try:
        return n1 + n2
    except TypeError as err:
        print(f'please enter numbers {err}')

print(sum('1', 9))

#------------------------------------------------------------------------------------------

def div(n1, n2):
    try:
        return n1 / n2
        raise Exception('hey cut it out') # You can use for own errors
    except (TypeError, ZeroDivisionError) as err:
        print(err)
print(div('1', 0))

