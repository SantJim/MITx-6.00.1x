substring_len = 0
substring = s[0]
for i in range(len(s) - 1 ):
    if s[i] <= s[i+1]:
        substring = substring + s[i+1]
        if len(substring) > substring_len: 
            tempstring = substring
            substring_len = len(substring)
    else:
        substring = s[i+1]
        
if substring_len == 0:
    substring = s[0]
    print("Longest substring in alphabetical order is: " + substring)
else:
    print("Longest substring in alphabetical order is: " + tempstring)
