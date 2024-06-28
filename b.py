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
                
        
        