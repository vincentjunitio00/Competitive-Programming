T = int(input())

for i in range(0,T):
    N = int(input())
    H = list(map(int,input().split()))

    count = 0
    j=1
    while(j<(N-1)):
        if((H[j]>H[j-1])):
            if(H[j]>H[j+1]):
                count+=1
            j+=1
        else:
            j+=1
    
    print("Case #{}: {}".format((i+1),count))