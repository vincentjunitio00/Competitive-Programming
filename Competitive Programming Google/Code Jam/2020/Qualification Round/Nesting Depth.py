T = int(input())


def printA(n):
    string = ''
    for i in range(0, n):
        string += '('
    return string


def printB(n):
    string = ''
    for i in range(0, n):
        string += ')'
    return string


for x in range(T):
    word = input()
    string = ''
    i = 0
    checkA = int(len(word[i]))
    checkB = 0
    while (i < len(word)):
        if(i+1 == len(word)):
            # if(len(word)==1):
            #     string += printA(checkA)
            #     string += word[i]
            #     string += printB(checkA)
            # else:
                string+= printA(checkA)
                string+= word[i]
                string+= printB(checkA)
        else:
            string+=printA(checkA)
            string+=word[i]
            checkB -= checkA
            if(checkB < 0):
                if((i+1)<i):
                    checkB=int(word[i])-int(word[i+1])
                    string+=printB(checkB)
            checkA = checkA-checkB
        i+=1

    print('Case #{}: {}'.format(x + 1, string))

    # print('Case #{}: {}'.format(x+1,string))