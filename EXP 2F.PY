

expDict = {

    "first" : 1,
    "second" : 2,
    "third" : 3,

}

choice = 9
while choice!=0:
    expDict[f"{input("enter the value")}"] = input("enter the key")
    print(expDict)
    choice = int(input("0 to exit"))
