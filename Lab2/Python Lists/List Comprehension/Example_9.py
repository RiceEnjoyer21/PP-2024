fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "bannana" else "orange" for x in fruits]

print(newlist)