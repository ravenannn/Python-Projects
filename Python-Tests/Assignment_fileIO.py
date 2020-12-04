

import os


# set file path, use \\ to avoid escape
fpath = 'C:\\python_projects'

files = os.listdir(fpath)
filesText = [i for i in files if i.endswith('.txt')]
print("\nThe text files are: \n{}. \n\nThey were last modified: \n".format(filesText))        

for file in os.listdir(fpath):
    if file.endswith(".txt"):
        print(os.path.getmtime(os.path.join(fpath, file)))
        



      



