

class Protected:
    def __init__(self):
        self._protectedVar = "This variable is protected"


    def __init__(self):
        self.__privateVar = "This variable is private."

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private





if __name__ == "__main__":
    obj = Protected()
    obj._protectedVar = "This protected variable has been changed!"
    print(obj._protectedVar)

    obj = Protected()
    obj.getPrivate()
    obj.setPrivate("This private variable has been changed!")
    obj.getPrivate()


