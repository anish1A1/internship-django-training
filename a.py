
def names():
    names = ["John", "Mary", "Jane", "Bob", "Alice"]
    return names

names()


list = [1,2,3,4,54]  


name = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

name["place"] = "Itahari"
print(name)


print(name.get("first_name"))

print("\n")
print(name["last_name"])

print(name.values())

print("\n")

for v in name.values():
    print(f"{v}")

print("\n")    
    
del name["place"]     #to delete a key
print(name)

tup = ("a", 20, True)

print(tup)
print(tup[0])
print("\n")

for keys in name:
    print(keys.title())
    

student = {
    "name" : "Anish",
    "age" : 20,
    "score" : 95,
    "isPass" : True
    
}    

for std in student:
    print(({std},{student["isPass"]} ))

print("\n")    
for stds in student.items():
    print(stds)


char = "This is a message" 


print("\n")
# for chars in char:
#     print(chars)   
    

def sum(a,b):    
    return a + b

sums = sum(4,4)  #when using return statement the function should be stored in a variable and we print that variable.
print(sums)

def addition(a,b):
    sum = a+b
    print(sum)

addition(2,4)


add = lambda a,b : a+b
multiply = lambda x,y : x*y

print(add(3,5))
print(multiply(3,4))

def tests(*a):
    print(a)

print(tests(2,3,4))    


def cal_even(args):
    if args % 2 != 0:
        print(f"{args} is odd")
        
        
cal_even(5)      

value = [2,3,4,5]

def checker(value):  
    for i in value:
        #print("This is a list")
        print(i)
        
        
checker(value)
print("hello")
print("\n")
to_cube = [1,2,3,4,5,6,7]

def cube(to_cube):
    for i in to_cube:
        cubing =  i ** 3
        print(cubing)
        

cube(to_cube)    
# cubes = cube(to_cube)    
# print(cubes)


#class 
print("\n")
class Calculation:
    def add(self, a, b):
        return a + b
    
    def subs(self, a, b):
        return a - b
    
    def mul(self, a , b):
        return a*b    
    
calc = Calculation()
adds = calc.add(2,6)    
print(adds)

subs = calc.subs(5,3)
print(subs)

muls = calc.mul(3,6)
print(muls)    

value = [2,3,4,5]
print("\n")
list = [1,2,3,7,9]

class Bodmas():
    
    
    def cube(self, list):
        for i in list:
            cubing = i**3
            print(cubing)
            
    def lists_calue(self,value):
        for i in value:
            print(i) 
            
            
bodmas = Bodmas()

cubes = bodmas.cube(list)
print(cubes)                    

lists = bodmas.lists_calue(value)    


#next 


class Animal:
    def __init__(self, name):
        print("Constructor invoked")
        self.__name = name        # __ is used to make the attribute private   in other language it uses private
        
    def eat(self):
        print(self.__name)
        print("I can eat")
        
    def sleep(self):
        print("I can Sleep") 
        
        
animal = Animal("Arjun")

#Arjun = animal()
animal.eat()
#print("Arjun")        \\
    
class Dog(Animal):
    def bark(self):
        print("I can bark")
        

dog1 = Dog("German Shephard")
dog1.eat()        



print("\n")


class BankAccount():
    def __init__(self,account_number,balance):
        self._account_number = account_number  # _ one underscore means protected
        self._balance = balance
        
    # def __deposit(self,amount):  # This is private as it has __
    #     self._balance += amount
    #     print(f"Deposit successful. New balance ${self._balance}")
        
        
    def deposit(self,amount):  # This is private as it has __
        self._balance += amount
        print(f"Deposit successful. New balance ${self._balance}")    
        
        
    def check_balance(self):
        print(f"current balance ${self._balance}")
        
    def withdraw(self,amount):
        self._balance -= amount
        print(f"Withdraw successful. New Balance ${self._balance}")
        
        
        
bank = BankAccount("3434", 2000)
bank.deposit(200)

bank.check_balance()

bank.withdraw(3000)
bank.check_balance()        
                        
            
        
        
        
            
               
        
        
        


        
        
        
        



    