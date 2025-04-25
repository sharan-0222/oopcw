class employee:
    def __init__ (self) :
        print("function called")

    def __del__(self) :
        print("destructor called")

def destructor():
    print("function is called")
    obj=employee()
    print("function deleted")
    del obj

destructor()  