
#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#Lists are created using square brackets:


thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.append("raspberry")

print(thislist)

thislist.insert(2, "orange")
print(thislist)

thislist.remove("banana")
print(thislist)
del thislist[2]
print(thislist)

#Loop through list
for x in thislist:
    print(x)