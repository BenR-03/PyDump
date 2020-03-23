array = ["4", "7", "hello", "2.6"]
password = ''.join(array)
print(int(array[0]) + int(array[1]))
print(array[2])
print(password)
array[1] = "9"
array.pop(3)
array.append("goodbye")
