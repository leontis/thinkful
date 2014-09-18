my_file = open("File_IO.py","r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

with open("text.txt", "w") as textfile:
	textfile.write("Success!")
