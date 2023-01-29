numbers = range(100)    #creating a list of numbers 1..100

#filtering evens
evens = [e for e in numbers if e % 2 == 0]
#filtering odds
odds = [o for o in numbers if o % 2 == 1]

print(evens)
print(odds)

# know more about the different comprehensions:
# [https://colab.research.google.com/drive/1PygMIKhTAW_Pl5VVk6UkIfC1VoltqJNj?usp=sharing#scrollTo=dGxViJQub8qd]