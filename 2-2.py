def solution(x,y):
    """
    Instead of looking at rows and columns look at the diagonals.
    For example (1,1) is on 1st level diagonal.
    (2,1);(1,2) are on 2nd level diagonal, (3,1);(2,2);(1,3) are on 3rd level diagonal...
    The number of elements in each diagonal equals to diagonal level.
    To get the answer we need to sum up all diagonal levels below last one,
    and check which element in diagonal are our coordinates.
    It can be done easily by checking value of y.
    """
    level = x+y-1
    sum = 0
    for i in range(0,level):
        sum += i
    return(sum+level-y+1)