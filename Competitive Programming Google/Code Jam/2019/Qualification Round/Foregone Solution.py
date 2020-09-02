T = int(input())

for i in range(T):
    number = input()
    ans1 = ""
    ans2 = ""

    for j in range(0,len(number)):
        if(number[j] == "4"):
            ans1 += "3"
            ans2 += "1"
        else:
            ans1 += number[j]
            ans2 += "0"

    ans1 = int(ans1)
    ans2 = int(ans2)
    print("Case #{}: {} {}".format((i+1),ans1 ,ans2))