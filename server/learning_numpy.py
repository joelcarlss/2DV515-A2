import numpy as np

# Array with zeros(floats)
z = np.zeros(10)

print(z)
z.shape = (10, 1)
print(z.shape)

# Array with ones
o = np.ones(1)

# Array from 2 - 10 with five elements
li = np.linspace(2, 10, 5)

# from list to np array
n_list = [1, 2, 3]
np_array_list = np.array(list)
print(np_array_list)

# Random array
rand = np.random.randint(10, size=6)

# Check if values in array are greater than three
print(rand > 3)

# Get numbers that are greater than three
print(rand[rand > 3])

# Where value is higher than hundred, replace with 255, else replace with 0
replaced = np.where(rand > 100, 255, 0)


a = np.linspace(2, 10, 5)
b = np.linspace(2, 10, 5)

print("a: ", a)
print("b: ", b)
# Add every index in a with the right index in b
print("a + b", a + b)

# Add 30 to each element of A
print("a + 30:", a + 30)

# Multiply by each element with two
print("a * 2:", a * 2)

# Multiply every index in a with the right index in b
print("a * b", a * b)

# This does.... (gives dot product?)
print(a@b)


# Sort
np.sort(rand)

# This accesses all in the column 0 in a multidimensional array
# multi_dim_array[:,0]
