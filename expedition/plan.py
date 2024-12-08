import numpy as np

def plan(mymyap, pos):
    wall = 0
    clear = 254
    unexplored = 205


    mymap
    plan = np.zeros(mymap.shape, dtype=np.uint8) #Could choose uint16 if we need a longer path

    x = plan.shape[1]//2
    y = plan.shape[0]//2
    s = 255
    plan[x][y] = s

    def find_unexplored():
        for i in range(1,s): #Repeat until we find our unexplored area
            for x1 in range(max(x-i,1),min(x+i+1,x+x)): #Traverse over every column 
                for y1 in range(max(y-i,1),min(x+i+1,x+x)): #Traverse over every row
                    #If not touching the wall but next to explored path
                    x2=x1-1
                    x3=x1+2
                    y2=y1-1
                    y3=y1+2
                    if wall not in mymap[x2:x3,y2:y3] and s+1-i in plan[x2:x3,y2:y3]:
                        if plan[x1][y1] == 0:
                            plan[x1][y1] = s-i #Mark as next step in plan
                        if mymap[x1][y1] == unexplored:
                            return(x1,y1) #Return the coordinates of the closest unexplored area


    def retrace_steps(x,y):
        p = [(x,y)]
        for i in range(plan[x1,y1],s):
            n = np.argmax(plan[x-1:x+2,y-1:y+2])
            x = n//3 + x-1
            y = n%3 + y-1
            p.append((x,y))
        return p


    x1, y1 = find_unexplored()
    steps = retrace_steps(x1,y1)

    plan2= np.zeros(mymap.shape, dtype=np.uint8)
    for i in steps:
        plan2[i] = 128
    return plan2
