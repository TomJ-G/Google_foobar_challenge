#I accidentally deleted my final solution for this problem from my drive, 
#so this solution is just copy of other people solutions.

def solution(n):
    
    """
    The quickest way to cut down the number of steps is to divide by 2 whenever possible.
    If n is odd, we must find which of +/-1 enable more divisions.
    For this purpose I'll use helper function which counts bits in number.
    """
    
    def count_bits(n):
        """
        Check rightmost bit, and then shift right.
        """
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count
    
    steps = 0
    n = int(n)
    
    while n > 1:
        if n%2 == 0:
            n >>= 1
        elif((n==3) or count_bits(n-1) < count_bits(n+1)):
            n-=1
        else:
            n+=1
        
        steps+=1
        
    return steps