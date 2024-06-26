
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
for chars in char:
    print(chars)   
    
    


