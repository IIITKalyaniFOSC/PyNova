a = {"name": "Jack", "age": 21, "weight": 62.3}
b = {"first": 1, "second": 2, "third": 3}

#accessing items
name = a["name"]
age = a["age"]
weight = a["weight"]
one = b.get("first")

#get keys
k = a.keys()

#changing values
a["name"] = "Joe"

#adding values
b["fourth"] = 4
b.update({"fifth": 5})


