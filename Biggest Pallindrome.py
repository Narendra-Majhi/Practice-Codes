def pallindrome(word):
    if((len(word)%2) == 0):
        rev = word[len(word)//2:]
        if(word[:len(word)//2] == rev[::-1]):
            return True
        else:
            return False
    else:
        rev = word[(len(word)//2)+1:]
        if(word[:len(word)//2] == rev[::-1]):
            return True
        else:
            return False

T = input()
c = 0

for i in range(len(T)):
    for j in range(i+1):
        plug = pallindrome(T[0+j:len(T)-i+j])
        #print(T[0+j:len(T)-i+j], plug)

        if(plug == True):
            print(T[0+j:len(T)-i+j])
            c = 1
            break
    if(c==1):
        break
