vowel = "AEIOUaeiou"
name = "Muheesh"
count = 0
for i in name:
    print(i)
    for j in vowel:
        if (i == j):
            count = count + 1
print(count)