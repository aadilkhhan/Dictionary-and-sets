myDict = {
    "Pankha" : "Fan",
    "Vastu" : "Item",
    "Dabba" : "Box"
}

print("Options are " , myDict.keys())
a = input("Enter the Hindi word : ")
# print("The meaning of your word is " , myDict[a])
print("The meaning of your word is " , myDict.get(a)) # To avoid error if the key is not present in the dictionary

