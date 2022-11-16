def solution(x):
    """To solve this we just need to notice that if amount of negative numbers 
    is odd, we need to discard the smallest negative number. Then it is enough 
    to multiply all other numbers (we ignore '0' values)"""

    pos = [i for i in x if i >0] #By making two lists we discard '0's and
    neg = [i for i in x if i <0] #make it easy to check how many negatives there are
    pos.sort()
    neg.sort(reverse=True) #Sort numbers to ensure the smallest one will be on '0' position.
    if len(neg)%2 != 0:
        neg.pop(0)
    result = 1
    for i in pos:
        result = result*i
    for i in neg:
        result = result*i
    #print(pos,neg)
    return(str(result)) 