class person():
    name = "default"
    age = 0
    add = "default"
    def __init__(self,name,age,add):
        self.name = name
        

class emp(person):
    def __init__(self, name, age, add):
        super().__init__(name, age, add)
        print("Name: ", self.name)


obj = emp("mudit", 18, "bablapur")
