def longest_consec(strarr, k):
    if(len(strarr) == 0 or k > len(strarr) or k <= 0):
        return ''
    toReturn =  [(''.join(strarr[x[0]:x[0] + k])) for x in enumerate(strarr)]
    maxElement = [len(toReturn[0]), toReturn[0]]
    for x in toReturn[1:]:
        temp = len(x)
        if temp > maxElement[0] :
            maxElement[0] = temp
            maxElement[1] = x

    return maxElement[1]
