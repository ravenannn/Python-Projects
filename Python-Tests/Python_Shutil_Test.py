import shutil
import os

#set where the source of the files are
source = '/Users/raven/OneDrive/Desktop/Folder_A/'

#set the destination path to folderB
destination = '/Users/raven/OneDrive/Desktop/Folder_B/'
files = os.listdir(source)

for i in files:
    #We are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
