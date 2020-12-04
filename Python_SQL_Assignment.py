
import sqlite3

# Create a db named 
conn = sqlite3.connect('filesTest.db')

# While your session is open, execute the following code
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    # Save your changes
    conn.commit()
# Be sure to close to avoid a memory leak
conn.close()


conn = sqlite3.connect('filesTest.db')

# tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each obj in tuple to find file names that end in 'txt'
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (x,))
            print(x)
# Close connection to avoid memory leak
conn.close()
