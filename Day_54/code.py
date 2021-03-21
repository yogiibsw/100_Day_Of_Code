#define a class which has at least 2 methods:
#.getString: to get a string from console input
#.printString: to print the string in upper case 
#also please include simple test function to test the class methods.

class newclass():
    def __init__(self):
        self.name=""
    def getString(self):
        self.name= input("ENter name: ") 
    def printString(self):
        print(self.name.upper())

final = newclass()
final.getString()
final.printString()