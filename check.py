import re
s="i love my country +91@India"


result = re.search(r"\bI\w+",s)

print(result)

qwe = re.search(r'[a-z]*[@\w+]',s)
print(qwe)
