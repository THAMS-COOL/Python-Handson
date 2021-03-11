# print('hello Word');

# for i in range(0,5,3):
#     print(i);

# count = 0
# while (count < 3):  
#     count = count + 1
#     print("Hello Geek")

# print("While loop executed")

# arrays - list
# object - dictionery


list = ['Kohli', 'Sevwag', 'Gambir']



# for i in list:
#     print(i)

# for j in range(2,10,1):
#     print(j)


for i in enumerate(list):   # automatically marks index
    print(i)

# for i in enumerate(list,100):
#     print(i)

# for count,i in enumerate(list,100):
#     print(i)
#     print(count,i)
    
# print(all(['True', 234, 'fgsf', -1])) # All values need to be true

# print(any(['', True, False, 0])) # any one of the values need to be true

# print(bool(None))
               
list = [2,3,4,56,78,89]
      # 0 1 2 3  4  5
print(list[::-1]) # Reverse

# print(list[2:5])

# print(list[2:5:2])

#1 mutable - change
#2 Immutable - not change

dict = {'name': 'Kani', 'age': 49, 'degree': 5 }

# print(dict.keys())

# print(dict.values())

for item in dict.items():
    print(item[0]) # keys
    print(item[1]) # values


