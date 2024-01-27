#Reverse the contents of the file1.txt.
#Open the file for reading
with open('file1.txt', 'r') as file:
    file_contents = file.read()

reversed_contents = file_contents[::-1]

with open('file1.txt', 'w') as file:
    file.write(reversed_contents)

print("Contents of file1.txt have been reversed.")