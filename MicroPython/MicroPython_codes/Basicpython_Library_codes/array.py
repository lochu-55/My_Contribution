# Create an array with typecode 'i' (signed integer) and initial elements
a = Libraries.array('i', [1, 2, 3, 4, 5])
print("Initial array:", a)

# Append a new element to the array
a.append(6)
print("Array after append:", a)

# Extend the array with another array (not a list)
a.extend(Libraries.array('i', [7, 8, 9]))
print("Array after extend:", a)

# Indexed read (__getitem__)
print("Element at index 2:", a[2])
print("Elements from index 2 to 5:", a[2:6])

# Indexed write (__setitem__)
a[3] = 10
print("Array after setting index 3 to 10:", a)
a[2:4] = Libraries.array('i', [11, 12])
print("Array after setting slice 2:4 to [11, 12]:", a)

# Get the length of the array (__len__)
print("Length of the array:", len(a))

# Concatenate two arrays (__add__)
b = Libraries.array('i', [13, 14, 15])
c = a + b
print("Array after concatenation:", c)

# In-place concatenation (__iadd__)
a += Libraries.array('i', [16, 17])
print("Array after in-place concatenation:", a)

# String representation (__repr__)
print("String representation of the array:", repr(a))

