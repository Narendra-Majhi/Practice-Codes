Arr = list(map(int,input().split(" ")))

maxi_index = Arr.index(max(Arr))
mini_index = Arr.index(min(Arr))

if(maxi_index > mini_index):
    print(min(Arr),max(Arr))
else:
    if(max(Arr)-min(Arr[:maxi_index]) > max(Arr[mini_index:])-min(Arr)):
        print(min(Arr[:maxi_index]),max(Arr))
    else:
        print(min(Arr),max(Arr[mini_index:]))

