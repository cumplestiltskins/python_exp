class person():
    name = "default"
    age = 0
    add = "default"
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add

class emp(person):
    salary = 15000
    type = "employee"
    def __init__(self, name, age, add):
        super().__init__(name, age, add)
        print("Name: ", self.name)

class manager(emp):
    salary = 45000
    position = "manager"
    def __init__(self, name, age, add):
        super().__init__(name, age, add)
        print("salary: ", self.salary)
        print("position: ", self.position)
        print("type: ", self.type)


obj = manager("mudit", 18, "bablapur")
