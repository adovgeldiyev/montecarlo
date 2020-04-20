# Azat Dovgeldiyev
#03/05/2020
#I have not given or received any unauthorized assistance on this assignment.   

from Ellipse import ClsEllipse
from Ellipse import ClsPoint
import random

#Following code to test the Point Class
p1 = ClsPoint(20,20)
p2 = ClsPoint(10,20)
print('p1 X ' + str(p1.get_xord())+ ' p1 y ' + str(p1.get_yord()))
print('p2 X ' + str(p2.get_xord())+ ' p2 y ' + str(p2.get_yord()))
print('Distance between P1 and P2  ' + str(p1.distance_bet_points(p2)))

#Ellipse Class Testing

e1 = ClsEllipse(1,1,2,2,4)
print('Area of Ellipse is ' + str(e1.get_Area()))
print('Circumference of Ellipse is ' + str(e1.get_Circum()))

#Program To Test 

def testAndCompute(): 
    print('Overlap area of 2 ellipses - Using Monte Carlo Simulation')
    print("First ! You prompted to create 2 ellipses.")
    print("Before entering numbers please read instuctions.")
    print("To avoid ValueError, make sure that the width must be greater than\
the largest distance on x or y axis")  
    
    x1, y1, x2, y2, w = input('Enter  5 numbers for Ellipse 1 here with \nspace only not punctuation: ').split()
    e1 = ClsEllipse(float(x1),float(y1),float(x2),float(y2),float(w))
    x1, y1, x2, y2, w = input('Enter  5 numbers for Ellipse 2 here with \nspace only not punctuation: ').split()
    e2 = ClsEllipse(float(x1),float(y1),float(x2),float(y2),float(w))
   
    x1, y1, x2, y2, x3, y3, x4, y4 = getBox(e1,e2)
    area = doSimulation(e1,e2,x1,y1,x2,y2,x3,y3,x4,y4)
    DisplayResult(area)


def doSimulation(e1, e2, bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy):
    #box-lower right(x),upper right(y),lowerleft(x),lowerleft(y),upperleft(x),upperleft(y)
    #get each coordinate point of the box that surrounds the 2 ellipses    
    #bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy = getBox(ellipse1, ellipse2)
    
    #create the 4 points of the box
    LR = ClsPoint(bLRx, bLRy)
    UR = ClsPoint(bURx, bURy)
    LL = ClsPoint(bLLx, bLLy)
    UL = ClsPoint(bULx, bULy)
    
    #calculate the length of the sides
    lenSide1 = LR.distance_bet_points(UR)
    lenSide2 = LR.distance_bet_points(LL)
    
    areaSquare = lenSide1*lenSide2  #calculate the area of the square surround the 2 ellipses
    
    #run the Monte Carlo doSimulation and get result
    percOverlap = simulate(e1,e2,bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy)
    
    areaOverlap = areaSquare*percOverlap 
    
    return areaOverlap #returns areaOverlap

def getBox(e1, e2):
    #creating box to capture both ellipses
    w1 = e1.get_w()
    w2 = e2.get_w()   
        
    if  w1 > w2 : # half the width to use as buffer
        wbuff = w1
    else:
        wbuff = w2
    #coordinating lower right box
    bLRx = max(e1.x1,e1.x2,e2.x1, e2.x2) + 0.5*wbuff
    bLRy = min(e1.y1,e1.y2,e2.y1, e2.y2) - 0.5*wbuff
    
    #coordinating upper right box
    bURx = max(e1.x1,e1.x2,e2.x1, e2.x2) + 0.5*wbuff
    bURy = max(e1.y1,e1.y2,e2.y1, e2.y2) + 0.5*wbuff
    
    #coordinating lower left box
    bLLx = min(e1.x1,e1.x2,e2.x1, e2.x2) - 0.5*wbuff
    bLLy = min(e1.y1,e1.y2,e2.y1, e2.y2) - 0.5*wbuff
    
    #coordinating upper left box
    bULx = min(e1.x1,e1.x2,e2.x1, e2.x2) - 0.5*wbuff
    bULy = max(e1.y1,e1.y2,e2.y1, e2.y2) + 0.5*wbuff
    #print(' bullx ' + str(bULx))  
    return bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy  #coordinates for 4 corners of bx

def simulate(e1, e2, bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy):
        
    count = 0
    n = 8000
    
    startX = int(min(bLRx, bURx, bLLx, bULx))
    endX = int(max(bLRx, bURx, bLLx, bULx))
    startY = int(min(bLRy, bURy, bLLy, bULy))
    endY = int(max(bLRy, bURy, bLLy, bULy))
    i = 0
    while(i <= n):
        x = random.uniform(startX, endX)
        y = random.uniform(startY, endY)
        
        point = ClsPoint(x,y)
        
        if simulateOnce(e1, e2, point) == True:
            count += 1
        i+=1  
            
    print("Count is {}, number of random points is {}".format(count,n))        
    return count/n

def simulateOnce(e1, e2, point):
    #if point is in both ellipse 1 and ellipse 2, then it returns True runing dosimulation'
    
    if e1.isPointInside(point) == True and e2.isPointInside(point) == True:
        return True

def DisplayResult(areaOverlap):
    
    print('The area of overlap of the Two Ellipses is: ', areaOverlap)    

testAndCompute()


