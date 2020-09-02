testcases = int(input())

for i in range(0,testcases):
    count = 0
    score = []
    nums,money = map(int,input().split(" "))
    score = list(map(int,input().split(" ")))
    score.sort()

    for j in range(0,nums):
        money-=int(score[j])
        if(money>=0):
            count+=1
        else:
            break

    print("Case #{}: {}".format((i+1),count))
