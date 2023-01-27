a = [1, 2, 6, 3, 0]

print(type(a))

#lists are mutable(can be changed)
a[3] = 10
#swapping places
a[0], a[1], a[1], a[0]
print(a)

metals = ["sodium", "calcium", "magnesium", "chlorine"]
#removing elements
metals.remove("chlorine")
#adding elements
metals.append("potassium")
print(metals)

#iterating through a list
for ele in metals:
    print(ele, end=" ")
print('\n')
#clearing the list
a.clear()
print(a)

metals.sort()
print(metals)
metals.reverse()
print(metals)





