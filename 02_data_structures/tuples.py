a = ("val1", "val2", "val3", "val4")
b = (1, 2, 3, 5)

# accessing a tuple item
print(a[3])
print(b[1])

# updating tuple values
# tuples are immutable, so they need to
# be casted into lists first
c = list(b)
c[2] = 10
b = tuple(c)

# adding elements to the tuple
q = list(b)
q.append(22)
b = tuple(q)

# tuple unpacking
z = (3, 2, 1)
three, two, one = z
print(one, two, three)






