import os
import webbrowser

with open("webpage.html", "w") as f:
    f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t  Stay tuned for our amazing summer sale!\n\t\t</h1>\n\t</body>\n</html>")
    f.close()

def openPage():
    webbrowser.open_new_tab("webpage.html")




        
if __name__ ==  "__main__":
    openPage()
