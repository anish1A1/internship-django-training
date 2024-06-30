# class Animal:
#     def Sound(self,name):
#         print(name)
        

# animal = Animal()
# animal.Sound("Dog")        


#Encapsulation
class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def Sound(self):
        print(self.name) 
        print(self.age)  
        
    def con(self):
       print("asd")     

anima = Animal("Dog", 14)       
anima.Sound()   
anima.con()      

print("\n")

#Inheritance
class Food(Animal):
    def __init__ (self, name , age, food):
        self.food = food
        super().__init__( name, age)
        
        
    def Cheese(self):
        super().Sound()
        print("Super class Soundmethod is been called")
        
        
food = Food("Don", 14, "Pizza")
food.Cheese()
            