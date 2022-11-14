def solution(grid):

    """
    The most important thing in this task is to realize two things:
    1) Because height is limited to 9, it is much faster to check every column, not cell or row.
    2) Because cell content can be True=1 and False=0, then we can treat columns as binary strings.
    
    In my solution, first I generate all possible previous step cells for 1 and 0.
    Then dictionary is created for step forward (used in column determination).
    Result of column solution are two columns - each is treated as binary string and changed to int.
    Solution is kept in dictionary. No need to make calculations is same configuration is encountered again.
    
    Column [i] second integer is compared with first integer of column [i+1].
    If there is a match, I increase the count in dictionary.
    Final answer is a sum of values in dictionary.
    """
    
    from itertools import permutations
    
    def get_cell(value):
        if value == True:
            return(TCell)
        else:
            return(FCell)
    
    def get_column(mx,i):
        return([mx[j][i] for j in range(len(mx))])
    
    def Rep(value):
        #Changes column to binary and then to integer representation.
        s = ""
        for i in value:
            s+=str(int(i))
        return(int(s,2))
    
    def solve_column(column):
        #Solves possible column configurations.
        solutions = []
        stack = [[c,0] for c in get_cell(column[0])]

        while stack:            
            node,i = stack.pop(0)
            if i>=len(column)-1:
                solutions.append(node)
            else:
                i+=1
                #If we consider only one row of cell, ther are only 4 variants.
                cells = [[0,0],[0,1],[1,0],[1,1]]
                for cell in cells:
                    if Generate[tuple(node[-1]),tuple(cell)]==column[i]:
                        k = [n for n in node]
                        k.append(cell)
                        stack.append([k,i])
        #Change solution to integer representation
        int_solutions = [[Rep(get_column(x,0)),Rep(get_column(x,1))] for x in solutions]
        return(int_solutions)
                

    TCell = [[[1,0],[0,0]],[[0,1],[0,0]],[[0,0],[1,0]],[[0,0],[0,1]]]
    #Instead of writing possible cells manually I can just use permutations
    #And then use set to get rid of duplicates.
    FCell = []
    for i in [2,3]:
        s = set(permutations([1 if j<i else 0 for j in range(4)]))
        for k in s:
            FCell.append([[k[0],k[1]],[k[2],k[3]]])
    FCell.append([[1,1],[1,1]])
    FCell.append([[0,0],[0,0]])
    
    #Dictionary for generating cell with step forward.
    Generate = {}
    for f in TCell:
        Generate[tuple(f[0]),tuple(f[1])] = True
    for f in FCell:
        Generate[tuple(f[0]),tuple(f[1])] = False
   
    last_column = 0
    cnt = {}
    column_dict = {}
    col = get_column(grid,0)

    int_rep = Rep(col)
    solved_column = solve_column(col)
    column_dict[int_rep] = solved_column

    #Iterate column by column
    for s in solved_column:
        cnt[s[0]] = 1  
    for num in range(len(grid[0])):
        col = get_column(grid,num)
        int_rep = Rep(col)
        if int_rep not in column_dict:
            solved_column = solve_column(col)
            column_dict[int_rep] = solved_column
        else:
            solved_column = column_dict[int_rep]
        
        count = dict()
        for s in solved_column:
            if s[0] not in cnt: cnt[s[0]] = 0
            if s[1] not in count: count[s[1]] = 0
            count[s[1]] += cnt[s[0]]
        cnt = count
       
    return(sum(cnt.values()))