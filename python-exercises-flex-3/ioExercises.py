#EX1

"""
fileName = input("File Name?")
with open(fileName, 'r') as file_handle:
  contents = file_handle.read()
print(contents)

"""
#EX2
fileName = input("File Name?")
with open(fileName, 'w') as file_handle:
  contents = input("Contents of file?")
  file_handle.write(contents)