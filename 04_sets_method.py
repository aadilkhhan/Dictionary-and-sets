# Creating an empty set 
b = set()
print(type(b))


# Adding values to an empty set 
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add(4)
b.add((4 , 5 , 6))
# b.add({4:5}) # Cannot add list or dictionary to sets

print(b)

# Length os the set 
print(len(b)) # Prints the length of the set

# Removal of an items 
b.remove(5) # Remove 5 from the set b
# b.remove(15) # Throws ann error  while trying to remove 15 from the set which is not present in the set.
print(b)

# Delete anyone value from the set randomly.
print(b.pop())
print(b)

