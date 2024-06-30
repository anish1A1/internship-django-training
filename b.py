#encapsulation

class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self._balance = balance
    
    def __deposit(self,amount):
        self._balance += amount
        print(f"Deposit successful. New Balance : ${self._balance}")

    def check_balance(self):
        print(f"Current Balance : {self._balance}")
    
    def withdraw(self,amount):
        self._balance -= amount
        print(f"Wdithdraw successful. New Balance : ${self._balance}")

    
account = BankAccount('1234',1000)
# account.deposit(-100)
# account.withdraw(1500)
# account.check_balance()

print(account._account_number)


print("\n")

class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def drive(self):
        print(f" {self.name}  can  drive")
        
    def talk(self):
        print("Father is talking.")
        
                
class Ram(Father):
    def sing(self):
        print("Ram is singing")


class Hari(Father):
    def read(self):
        print("Hari is reading")      
        
        
ram = Ram("Arjun", 38)      
ram.sing()            


hari = Hari("har" , 34)
hari.read()
hari.talk()

print("\n")
class Employee:
    def __init__ (self,name,emp_id,salary=0):
        self._name = name
        self._emp_id = emp_id
        self._salary = salary
        
    def calculate_bonus(self):
        return self._salary * 1.1
    
    
    def display_info(self):
        print(f"Name : {self._name}")
        print(f"Employee ID: ${self._emp_id}")
        print(f"Salary: ${self._salary}")
        
Pre = Employee("Pre", 342, 24000)
Pre.calculate_bonus()
Pre.display_info()        
print("\n")


class Manager(Employee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department = department
        
    def dispaly_info(self):
        super().display_info()
        print(f"Department : {self.department}")
        

class Developer(Employee):
    def __init__(self, name, emp_id, p_lang):
        super().__init__(name, emp_id)
        self.p_lang = p_lang
        
    def display_info(self):
        super().display_info()   
        print(f"Programming Language : {self.p_lang}")     
        

manager = Manager("Anish", 323, 234)
#manager.dispaly_info()        

developer = Developer("Akash", 223, "Python")
developer.display_info()
                
print("\n")        

#polymorphism
class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2
    
    
class Rectangle(Shape):
    def __init__(self, length, width ):
        self.length = length
        self.width = width 
        
    def area(self):
        return self.length * self.width
    

def print_area(shape):
    print("Area :", shape.area()) 
    
reactangle = Rectangle(4,5)
circle = Circle(5)

print_area(reactangle)  



class Animaal:
    def speak(self):
        pass
    
class Dog(Animaal):
    def speak(self):
        return "Bhow Bhow"
    
class Cat(Animaal):
    def speak(self):
        return "Meow Meow"
    

def print_animal(sound):
    print(sound.speak())

# dog = Dog()
# cat = Cat()
    
animal_list = [Dog(), Cat()]     

for animals in animal_list:
    print_animal(animals)     
    

print("\n")

class Employee:
    def __init__ (self, name):
        self.name = name
        
    def calculate_salary(self):
        pass
    

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
    
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 25000
    
    
employee = [FullTimeEmployee("Akash"), PartTimeEmployee("Bob")]



for employees in employee:
    print(f" {employees.name} salary is : {employees.calculate_salary()}")
                        
     
         
  
                 
            