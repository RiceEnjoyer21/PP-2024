import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.findall(r"ab{2,3}", text)

print(x)

