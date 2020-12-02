

mySentence = "loves the color"

colorList = ["red", "blue", "pink", "teal", "black"]

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst





lst = colorFunction("Raven")
for i in lst:
    print(i)
