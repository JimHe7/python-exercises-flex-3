fileName = input("File Name?")
with open(fileName, 'r') as file_handle:
  contents = file_handle.read()
print(contents)