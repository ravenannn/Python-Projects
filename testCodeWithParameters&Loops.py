

mySentence = "loves the color"

colorList = ["red", "blue", "pink", "teal", "black"]

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst



def getName():
    go = True
    while go:
        name = input("What is your name? ")
        if name == "":
            print("You need to provide your name!")
        elif name == "Sally":
            print("Sally, you may not use this software.")
        else:
            go = False
    lst = colorFunction(name)
    for i in lst:
        print(i)


getName()
