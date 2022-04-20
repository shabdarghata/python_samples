#https://www.w3schools.com/python/python_tuples_join.asp
# This program adds two numbers

num1 = 1.5
num2 = 6.3
#Test
# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

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