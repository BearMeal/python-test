class Person:
    name = ""
    age = 0
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def showinfo(self):
        print(f"name:{self.name}")
        print(f"age: {self.age}")
        
person1= Person("김찬란",34)
    
person1.showinfo()