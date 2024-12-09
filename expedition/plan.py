import numpy as np
#from PIL import Image, ImageShow

def plan(mymap, x, y, width):
    #print((x,y,mymap.shape, width))
    #im = Image.fromarray(mymap)
    #im.show()
    colors = list(np.unique(mymap))
    clear = mymap[x,y] #Assume the robot is not on a wall
    unexplored = mymap[0,0] #Assume the corner is unexplored
    colors.remove(clear)
    colors.remove(unexplored)
    wall = colors[0] #Remaining color must be clear

    #print(f'clear:{clear}, wall:{wall}, unexplored:{unexplored}')

    plan = np.zeros(mymap.shape, dtype=np.uint8) #Could choose uint16 if we need a longer path

    s = 255
    plan[x][y] = s

    def find_unexplored():
        for i in range(1,50): #Repeat until we find our unexplored area
            j = 0
            for x1 in range(max(x-i,1),min(x+i+1,mymap.shape[0])): #Traverse over every column 
                for y1 in range(max(y-i,1),min(y+i+1,mymap.shape[1])): #Traverse over every row
                    #If not touching the wall but next to explored path
                    x2=x1-width
                    x3=x1+width+1
                    y2=y1-width
                    y3=y1+width+1
                    if wall not in mymap[x2:x3,y2:y3] and s+1-i in plan[x2:x3,y2:y3]:
                        if plan[x1][y1] == 0:
                            plan[x1][y1] = s-i #Mark as next step in plan
                            j += 1
                        if mymap[x1][y1] == unexplored:
                            return(x1,y1) #Return the coordinates of the closest unexplored area
            assert j > 0, f'No path found at depth {i}'


    def retrace_steps(x,y):
        p = [(x,y)]
        for i in range(plan[x1,y1],s):
            n = np.argmax(plan[x-width:x+width+1,y-width:y+width+1])
            x = n//3 + x-1
            y = n%3 + y-1
            p.append((x,y))
        return p


    x1, y1 = find_unexplored()
    steps = retrace_steps(x1,y1)
    steps.reverse()
    return steps
