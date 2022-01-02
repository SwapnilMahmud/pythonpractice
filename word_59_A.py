sentence=input()
upper = 0
lower = 0
for i in sentence:
    if i >='A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1
print("Upper case: " + str(upper))
print("Lower case: " + str(lower))

if upper==lower:
    sentence=sentence.lower()
    
elif lower>upper:
    sentence=sentence.lower()

elif upper>lower:
    sentence=sentence.upper()
print(sentence)
    
