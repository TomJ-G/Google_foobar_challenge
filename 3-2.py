def solution(x, y):

    """
    To solve this problem, we must understand 4 facts:
       
        1) M can never be equal to F, except initial (1,1).
           Because replication equation is either M=M+F or F=F+M,
           then if M=F at any point, either M or F should be 0 at previous step.
           Impossible situation!
           
        2) Larger of (M,F) is the one which was replicated in previous cycle.
           Examples:
           If (M,F) = (10,9), then in the last cycle: (1,9) M->F (10,9).
           If (M,F) = (3,8) then in the last cycle: (3,5) F->M (3,8).
       
        3) The same step can be consecutively selected multiple number of times.
           Instead of iterating, calculate how many times it can be repeated.
           
        4) If initial (M,F) = (1,1) then every possible scenario can be traced back to (1,1)!
   
    Knowing this, instead of looking forward from (1,1) to (x,y),
    we should trace from (x,y) to (1,1).
   
    """
    from math import ceil
   
    gen = 0
    possible = True
    M,F = int(x),int(y)
   
    #Two edge cases:
    #Initial values means gen = 0
    if (M==1) and (F==1):
        return(str(0))
    #When (M,F) = (N,N-1) or (N-1,N), gen = N-1..
    #Because we can always do ...->(1,N-1)->(N,N-1). It will always take N-1 steps.
    if (M==F-1) or (F==M-1):
        return(str(min(F,M)))
       
    #Run the loop until (1,1) is reached
    #or impossible situation is found
    while possible == True:
        steps = 1
        #Select replication process
        if M > F:
            #Test how many steps are needed
            steps = ceil((M-F)/F)
            M = M-(F*steps)
        elif M < F:
            steps = ceil((F-M)/M)
            F = F-(M*steps)
        gen +=steps
       
        #Check if (1,1) or impossible situation reached.
        if (M == 1) and (F == 1):
            return(str(gen))
        elif (M < 1) or (F < 1):
            return("impossible")
        elif M == F:
            return("impossible")