class str:
    def __init__(self):
        self.str1=""
    
    def getstring(self):
        self.str1=input("Enter a string:")
    
    def printstring(self):
        print("The string is:",self.str1.upper())

obj=str()
obj.getstring()
obj.printstring()