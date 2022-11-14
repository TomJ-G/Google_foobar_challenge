def solution(x, y):
    summed = x + y
    for i in summed:
        if summed.count(i) == 1:
            return(i)