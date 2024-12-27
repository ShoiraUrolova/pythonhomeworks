txt= str(input("enter your string: "))
vowels = "aeiouAEIOU"
counter = 0
result = []
for i in range(len(txt)):
    counter += 1
    result.append(txt[i])
    if i!=len(txt)-1 and counter >= 3 and txt[i] not in vowels:
        vowels += txt[i]
        result.append('_')
        counter = 0

print(''.join(result))