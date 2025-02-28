class father():

    age = 41
    role = "father"
    def __init__(self):
        print(f"role: {self.role}")
        print(f"age: {self.age}")


class mother():

    role = "mother"
    age= 37
    def __init__(self):
        print("Name: ", self.role)
        print(f"age: {self.age}")

class child(father,mother):

    def __init__(self, name, age):
        mother().__init__()
        super().__init__()
        
        print(f"name : {name}")
        print(f"child age: {age}")
        

obj = child("mudit", 18)
