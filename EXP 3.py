

class employee:

    def __init__(self, name,age,address):
        name = "default"
        age = 0
        address = "default"
        

    def personal(self):
        self.name = name
        self.age = age
        self.address = address

        print(f"name: {name}\nage: {age}\naddress:{address}")
    
    @staticmethod
    def incSalary(sal):
        inc = int(input("salary increment: "))
        sal = sal + inc
        return sal


name = input("name: ")
age = int(input("enter age: "))
address = input("enter address")
obj = employee(name,age,address)
obj.personal()
print(f"salary: {obj.incSalary(30000)}")
