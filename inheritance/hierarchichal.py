class parent():

    role = "parent"
    age = 41
    def __init__(self):
        print("role: ",self.role)
        print("age: ", self.age)

class child1(parent):

    def __init__(self, name, age, address):
        print(f"name: {name}, age: {age}, address: {address}")
        super().__init__()
        
class child2(parent):
    def __init__(self, name, age, address):
        print(f"name: {name}, age: {age}, address: {address}")
        super().__init__()



obj1 = child1("mudit", 19, "bablapur")
obj2 = child2("prajwal", 24, "bablapur")
