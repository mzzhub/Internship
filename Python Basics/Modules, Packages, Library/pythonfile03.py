import re
line = "Python is a programming language."
# to check if the string starts with given characters.
print(re.match("Python",line))
print(re.match("is",line)) #None
# to search if the given pattern is in the string
print(re.search("is",line))
a = re.search(("programming language"),line)
if a:
    print("Match found.")
else:
    print("No Match.")

# substitution method
newline = re.sub("programming","high",line)
print(newline)
line1 = "python is simple. python is powerful python is great"
newline1 = re.sub("python","C",line1,count=2)
print(newline1)
line2 = "4253243432 5324 python is 3423324 programming language python is a high level language"

# All numerical characters are selected.
new1line2 = re.sub("\d","X",line2)
print(new1line2)
# All characters except numerical characters are selected.
new2line2 = re.sub("\D","X",line2)
print(new2line2)
# All spaces are selected.
new3line2 = re.sub("\s","X",line2)
print(new3line2)
# All characters except spaces are selected.
new4line2 = re.sub("\S","X",line2)
print(new4line2)

# Excluded substitution
line3 = "56788 ## $$ 8990 python is ...... 88900 @ # a programming $$$ language."
# note the ^ sign. it says "excluding".
print(re.sub("[^a-z,A-Z,0-9,\s]","",line3))

# to split on every given character.
line4 = "Python is a programming language."
print(re.split("\s",line4))
print(re.split("\s",line4,maxsplit=2))

# findall
line3 = "56788 ## $$ 8990 python is ...... 88900 @ # a programming $$$ language."
# single elements.
print(re.findall("\d",line3))
# As a group.
print(re.findall("\d+",line3))
print(re.findall("[a-z]",line3))
print(re.findall("[a-z]+",line3))

line5 = "Python is a +9156342563 programming 7363 338 language +0939847633."
print(re.findall("[+][0-9]+",line5))

line3 = "56788 ## $$ 8990 python is ...... 88900 @ # a programming $$$ language."
print(re.findall("[p]\w+[n]",line3))

line3 = "56788 ## $$ habeel@gmail.com 8990 python is ...... 88900 @haneen7@gmail.com # a programming $$$ language."
print(re.findall("[\w]+[@][\w]+[.]\w+",line3))
print(re.findall("[a-z,A-Z,0-9]+[@][a-z]+[.][a-z]+",line3))