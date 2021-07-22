import re

text = "man sum mat run manner matt bumat mar"
text.split(' ')

x = re.findall(r"m\w\w\s|\sm\w\w", text)
x = re.findall(r"^m[\w{3}]", "man mun tan monner")
x = re.findall(r"\bm\w\w\b", text)
x = re.findall(r"\bm\w{2}\b", text)
x


txt = "The rain in Spain The trash in Spain"
x = re.findall("^The.*Spain$", txt)
x2 = re.findall("^m*$n", text)
x2
x
print(x)
x.group()

