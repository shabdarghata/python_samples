#https://www.w3schools.com/python/python_tuples_join.asp
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

mytuple = ("one","two","five")
print(mytuple)
print(mytuple[1])

#loop through tuple
for x in mytuple:
    print(x)

#Joing 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)