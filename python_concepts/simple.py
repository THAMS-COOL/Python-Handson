class PlayerCharacter():
    membership = True
    def __init__(self, name, age):
        # if(self.membership): # PlayerCharacter.membership
            self.name = name 
            self.age = age
    
    # def run(self):
    #     print("run")
    #     return "done"

    def shout(self): # Instance Method
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2

    @classmethod
    def m1(cls):
        return cls.__name__

player1 = PlayerCharacter("Thams", 23)
player2 = PlayerCharacter("Rahul", 23)

# player3 = PlayerCharacter.adding_things(2,3)
# print(player3.age)

#print(player1.run())
print(player2.shout())
print(player1.adding_things(3,4))
print(player1.age)
player4 = PlayerCharacter.m1()
print(player4)

# Dunder Methods



