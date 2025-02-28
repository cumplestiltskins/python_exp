marks=0
marksList = []
nameList = []
rollList = []
info = []

print("starting! type exit to exit")

while True:

    marksList = []
    nameList = []
    inp = int(input("continue? or exit(0)"))
    if inp == 0:
        break

    name = input("enter the name of the student")
    roll = int(input("enter roll number"))
    year = input("enter year")
    nameList.append(name)

    for i in range(0,3):
        marks = input("Enter marks")
        marksList.append(marks)

    nameList.append(tuple(marksList))
    info.append(tuple(nameList))

choice = int(input("enter your choice"))

while choice !=0:
    choice = int(input("enter your choice"))

    print("1. add student\n2.find by name")
    if 



info = tuple(info)
print(info)
search = input("enter name to find ")
k=0

def find_name(info):
    for i in range(len(info)):
        if search in info[i]:
            return i
            
find = (find_name(info))

final = {

    f"{info[find][0]}": info[find]

}

print(final)