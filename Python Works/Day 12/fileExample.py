'''
Syntax to open a file

file_object = open("file name", "mode")

'r' - read mode
'w' - write mode
'a' - append mode 
'r+' - read/write mode
'''

file = open("PyBatch06.txt", "w")

file.write("Sup\n")
file.write("This my new file\n")
file.write("This is pretty complex\n")
file.write("This is write mode\n")

file.write("\nSup\n")
file.write("This my new file\n")
file.write("This is pretty complex\n")
file.write("This is write mode\n")
file.close() 

#Open a file for read mode

file = open("PyBatch06.txt", "r")
#Read entire file
#print(file.read())
#print(file.read(16))
#print(file.readline()) # readline = reads only the first line
print(file.readlines())
file.close()

file = open("PyBatch06.txt", "r")
s = file.readlines()

for line in s:
    print(line)
file.close()

file = open("PyBatch06.txt", "r")
for line in file:
    print(line)
file.close()

file = open("PyBatch06.txt", "a")

file.write("\nPython...")
file.write(" is HARD af\n")
file.close()

i = 1
file = open("PyBatch06.txt", "r")
for line in file:
    print(i, '.', line)
    i = i + 1
file.close()
