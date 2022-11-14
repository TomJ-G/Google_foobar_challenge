def solution(dimensions, your_position, trainer_position, distance):

    """
    This can be solved with crystallographic theory of 2D groups.
    I treat the Room, Me and Trainer as Assymetric Unit of a lattice.
    This setting would be 2D space group "Pmm": no centering and two mirror planes under 90 deg.
    By constructing such crystal lattice, I can use symmetry to bypass calculation of reflected beams,
    and use straight lines instead (all other trainer positions are symmetrically equivalent).
    
    The problem with determination of which beam hits the target and which can hit me,
    can be solved by calculating all potential beams, between my position and all generated
    trainer positions, but also between me and all my mirror positions.
    Next I'll group values by the unique angles and select the one with the shortest distance.
    In the last step I need to check if the target is the trainer of me. 
    """
    
    from math import sqrt, atan2, pi
   
    def mirror_V(val,dim,i):
        """
        Flip positions vertically and add translation
        :param val: list(int), value to be flipped,
        :param dim: list, dimensions of the cell,
        :param i: int, number of the cell,
        :return: int, mirrored value of x.
        """       
        if i%2==1:
            yp_m = dim[0] - val[0] +(i*dim[0])
        else:
            yp_m = val[0] +(i*dim[0])
        return(yp_m)
    
    def mirror_H(val,dim,i):
        """
        Flip positions horizontally and add translation
        :param val: list(int), value to be flipped,
        :param dim: list, dimensions of the cell,
        :param i: int, number of the cell,
        :return: int, mirrored value of y.
        """
        if i%2==1:
            yp_m = dim[1] - val[1]+(i*dim[1])
        else:
            yp_m = val[1]+(i*dim[1])
        return(yp_m)
    
    def dist(P1,P2):
        """
        Calculate distance between two points
        :param P1, P2: list(int,int), point on x, y plane.
        :return: float, distance between P1 and P2.
        """
        return(sqrt((P1[0]-P2[0])**2+(P1[1]-P2[1])**2))
    
    def ProduceSymm(val):
        return([[x,y] for xi, yi in val for x, y in [(xi,yi),(-xi,yi),(-xi,-yi),(xi,-yi)] ])
    
    def group_and_select(a,b):
        """
        Group by angle and select the value with shortest distance.
        :param a: list, [angle,point,distance] - all possible beams.
        :param b: list, all mirrored points of me
        :return: list, [angle,point,distance] - possible trainer hits.
        """
        unique =[]
        selected =[]
        #Select unique values
        for i in a:
            if i[0] not in unique:
                unique.append(i[0])
        #Filter values among uniques
        for u in unique:
            d = 10**309
            temp = [i for i in a if i[0] == u]
            #Find the shortest distance
            for t in temp:
                if t[2]<d:
                    d = t[2]
                    s = t
            #Do not include beams that hit me.
            if s[1] not in b:
                selected.append(s)
        return(selected)
    
    me_list = []
    target_list = []
    tmp1,tmp2 = [],[]
    yps = your_position
    #Calculate how many repeated cells are needed in X and Y dimensions.
    rep = [(distance // dimensions[0]) + 2, (distance // dimensions[1]) + 2]

    #Each cell undergoes two operations: translation and mirror symmetry
    for j in range(rep[1]):
        YP = your_position
        TP = trainer_position

        YP_y = mirror_H(YP,dimensions,j)
        TP_y = mirror_H(TP,dimensions,j)

        for i in range(rep[0]):
            YP_x = mirror_V(YP,dimensions,i)
            TP_x = mirror_V(TP,dimensions,i)
            
            #Apply also parts mirrored by X and Y axis
            tmp1 += ProduceSymm([[YP_x,YP_y]])
            tmp2 += ProduceSymm([[TP_x,TP_y]])
            
    for i in range(len(tmp1)):    
        #Only if distance is shorter than laser range, point should be included
        if dist(yps,tmp1[i]) <= distance:
            me_list.append(tmp1[i])
        if dist(yps,tmp2[i]) <= distance:
            target_list.append(tmp2[i])
    ALL = me_list + target_list
    #Calculate angles, except for my own position (angle would=0 and dist=0!)
    ang = [[atan2(i[1]-yps[1],i[0]-yps[0])* (180/pi),i,dist(i,yps)] for i in ALL if i!=yps]
    
    count = len(group_and_select(ang,me_list))
            
    return(count)