s = 'azcbobobegghakl'

numVowels = 0
substring = s[0]
for i in range(len(s) - 1 ):
    if s[i] <= s[i+1]:
        substring = substring + s[i+1]
    else:
        substring = s[i+1]
print(substring)
