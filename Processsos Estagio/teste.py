import re

string = "hey th~~ere"
char = re.sub('[^a-zA-Z0-9\.]', '', string)

print(char)
print (string)
