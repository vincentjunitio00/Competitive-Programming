T = int(input())

for x in range(0,T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    
    count = 0
    i = 0
    while(i<len(A)):
        if(A[i] == K):
            j = K
            i += 1
            while(j>0 and i<len(A)):
                j -= 1
                if(A[i] != j):
                    i += 1
                    break
                else:
                    if(j == 1):
                        count += 1
                        i += 1
                    else:
                        i += 1
        else:
            i += 1
    x += 1
    print("Case #{}: {}".format(x,count))