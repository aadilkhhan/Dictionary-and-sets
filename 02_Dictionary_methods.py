myDict = {
    "fast" : "In a quick manner",
    "Harry" : "A Coder",
    "Marks" : [1 ,2 , 4],
    "anotherdict" : {"harry": "player"},
    1 : 2
}

# Dictionary Methods
print(list(myDict.keys())) # Print the keys of the dictionary
print(list(myDict.values())) # Print the values of the dictionary
print(myDict.items()) # Print the keys,value for all contains of the dictionary


print(myDict)

updateDict = {
    "Lovish" : "Friend",
    "Diksha" : "Friend",
    "Rohan" : "Friend",
    "Harry" : "A dancer"
}
myDict.update(updateDict) # Update the dictionary by adding keys and values pairs from updateDict
print(myDict)


# The differnce between .get and [] syntax in Dictionaries.
print(myDict.get("Harry2")) #Returns None as harry 2 is not present in the dictionary.
print(myDict["Harry2"]) # Throws an error hence harry 2 is not present in the dictionary.