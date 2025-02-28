class Gfather():

    grole = "grandfather"
    gage = 72
    def __init__(self):
        print("role: ",self.grole)
        print("age: ", self.gage)

class Gmother():

    role = "grandmother"
    age = 69
    def __init__(self):
        print("role: ",self.role)
        print("age: ", self.age)
        
class parent(Gfather, Gmother):
    role = "parent"
    age = 45
    def __init__(self):
        print(f"role: {self.role}, age: {self.age}")
        super().__init__()
        

class child1(parent):
    def __init__(self, name, age, address, grade):
        print(f"name: {name}, age: {age}, address: {address}, grade:{grade}")
        super().__init__()

class child2(parent):
    def __init__(self, name, age, address, grade):
        print(f"name: {name}, age: {age}, address: {address}, grade:{grade}")
        super().__init__()

obj1 = child1("mudit", 19, "bablapur", "9th")
#obj2 = child2("prajwal", 24, "bablapur", "12th")
