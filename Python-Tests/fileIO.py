

import os



# Create an absolute file path to a specific document using Python

# Assign file name
fName = 'Hello.txt'
#Assign file path
# To avoid Python ignoring the \ in your path, you must use a double \\
fPath = 'C:\\A\\'



abPath = os.path.join(fPath, fName)
print(abPath)
