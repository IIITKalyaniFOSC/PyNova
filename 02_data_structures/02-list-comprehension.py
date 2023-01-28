numbers = range(100)    #creating a list of numbers 1..100

#filtering evens
evens = [e for e in numbers if e % 2 == 0]
#filtering odds
odds = [o for o in numbers if o % 2 == 1]

print(evens)
print(odds)

