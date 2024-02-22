import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.findall("[А-Я][а-я]+", text)                  #x = re.findall("[A-Z][a-z]+", text) originally

print(x)
