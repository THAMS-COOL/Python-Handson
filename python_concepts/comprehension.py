
# normal for loop

output = []

for i in range(3):
    # print(i)
    for j in range(3):
        # print(j)
        output.append(i+j)

print(output)


# list comprehension

output = [i+j for i in range(3) for j in range(3)]

print(output)

# List set dictionery comprehensive

#example 1

square = dict()
for num in range(1,11):
    square[num] = num* num
print(square)

square_dict = {num: num*num for num in range(1, 11)}
print(f'Dict Comprehension\n{square_dict}')

# Hands on needed

#example 2

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76

new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(f'Dict Comprehension2\n{new_price}')

new_prices = dict()
for items, value in old_price.items():
    new_price = value * dollar_to_pound
    new_prices = {items:new_price}
print(new_prices.items())

# tuple comprehension

power = tuple(num**num for num in (1,2,3))
print(power)

print(tuple())