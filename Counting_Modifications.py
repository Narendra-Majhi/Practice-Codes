#Counting the number of modifications

Str1 = input()
Str2 = input()

if(len(Str1) < len(Str2)):
    small = Str1
    large = Str2
else:
    small = Str2
    large = Str1

s_length = len(small)
l_length = len(large)
maxi = 0
count = 0

for i in range(l_length - s_length+1):
    word = large[0+i:s_length+i]
    for j in range(s_length):
        if(small[j] == word[j]):
            count = count+1
    if(count > maxi):
        maxi = count
        max_word = word
    count = 0

print(max_word, maxi)
print("Minimum number of modifications : %i"%(l_length-maxi))

        
