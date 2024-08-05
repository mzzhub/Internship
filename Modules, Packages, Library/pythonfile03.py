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