T = int(input())

for i in range(T):
    N = int(input())
    way = input()
    answer = ""
    for j in range(0, len(way)):
        if( way[j] == "S"):
            answer += "E"
        else:
            answer += "S"
    
    print("Case #{}: {}".format((i+1),answer))