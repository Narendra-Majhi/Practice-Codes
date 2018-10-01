Str = input()
lis = [0]

switch = {
        '[' : 1,
        ']' : 8,
        '{' : 2,
        '}' : 7,
        '(' : 3,
        ')' : 6,
        '<' : 4,
        '>' : 5
        }

for i in Str:
    val = switch.get(i)
    su = val + lis[-1]
    if(0 in lis):
        lis.remove(0)
    if(su == 9):
        lis.pop()
        if(lis == []):
            lis.append(0)
    else:
        lis.append(val)
    
if(lis == [0]):
    print("Balanced")
else:
    print("Unbalanced")
    
    
    

