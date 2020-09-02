T = int(input())

for case in range(T):
    N = int(input())
    A = list(map(int, input().split(" ")))

    diff = [A[i]-A[i-1] for i in range(1, N)]
    diff.append(-99999)

    prev_value = diff[0]
    count = 1
    maximum = []
    for i in range(1, len(diff)):
        if diff[i] == prev_value:
            count += 1
        else:
            maximum.append(count)
            count = 1

        if i == len(diff)-1 and len(maximum)==0:
            maximum.append(count)
        prev_value = diff[i]

    answer = max(maximum)+1
    cases = case+1
    print("Case #{}: {}".format( cases,answer))