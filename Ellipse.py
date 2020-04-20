# Azat Dovgeldiyev
#03/05/2020
#I have not given or received any unauthorized assistance on this assignment.

import math


class ClsEllipse:
    #creating Ellipse class defining essential variables
    def __init__(self,x1 = 0, y1 = 0, x2 = 0, y2 = 0, w = 1):
        self.x1 = x1 #for any given string values will be raised error.
        if type(self.x1)==str:
            raise TypeError("Please use integer or float only")
        self.y1 = y1
        if type(self.y1)==str:
            raise TypeError("Please use integer or float only")
        self.x2 = x2
        if type(self.x2)==str:
            raise TypeError("Please use integer or float only")
        self.y2 = y2
        
        self.w = w  # width must me greater than the max values on x and y axis
        if self.w < max ( abs(self.x1 - self.x2), abs(self.y1 - self.y2) ):
            raise ValueError("Width must be greater than the largest distance on x or y axis.")
        #as well as defining focus points or Foci lie on the major axis.
        self.F1 = ClsPoint(self.x1,self.y1)
        self.F2 = ClsPoint(self.x2,self.y2)
        
    
        
    def set_x1(self, x1):
        #set x coordinate of point to xcoordinate
        self.x1 = x1
        
    # getter method 
    def get_x1(self): 
        return self.x1
    
    
    def set_x2(self, x2):
        #set x coordinate of point to xcoordinate
        self.x2 = x2
        
    # getter method 
    def get_x2(self): 
        return self.x2
    
    def set_w(self, w):
        self.w = w
        
    # getter method 
    def get_w(self): 
        return self.w
    
    def set_F1(self):
        self.F1 = ClsPoint(self.x1,self.y1)
        
    def set_F2(self):
        self.F2 = ClsPoint(self.x2,self.y2)
        
    def get_F1(self):
        return self.F1
    
    def get_F2(self):
        return self.F2
    
    def get_SemiMajor(self):
        #getting the longest diameter of an ellipse, major
        self.semiMajor = self.F1.distance_bet_points(self.F2)*.5 + (self.w - self.F1.distance_bet_points(self.F2))*.5 
        #half the d between F1F2 plus half w-d
        return self.semiMajor
    
    def get_SemiMinor(self):
        #getting the shortest diameter of an ellipse
        self.semiMinor = ( (0.5*self.w)**2 - ( (0.5*self.F1.distance_bet_points(self.F2) )**2) )**0.5 
        #using geometry to solve for semiminor
        return self.semiMinor
    
    def isPointInside(self, other):
        #using focus points determine whether given points are inside of an ellipse or not
        #if sum of given distances are less than width, it is inside
        if self.F1.distance_bet_points(other) + self.F2.distance_bet_points(other) < self.w:
         
            return True
        else:
            return False

    def get_Area(self):
        #calculating area of an ellipse using math formula
        semiMajor = self.get_SemiMajor()
        semiMinor = self.get_SemiMinor()
         
        return math.pi*semiMajor*semiMinor
    
    
    def get_Circum(self):
        #calculating circumference
        semiMajor = self.get_SemiMajor()
        semiMinor = self.get_SemiMinor()
         
        return math.pi*( 3*(semiMajor + semiMinor) - ( (3*semiMajor + semiMinor) *(semiMajor + 3*semiMinor) )**0.5)
     
    def checkForBoundary(self, oXord, oYord):    
        'determines is a given point is on the edge of the ellipse'
 
        oPoint = ClsPoint(oXord,oYord)
        
        if self.F1.distance_bet_points(oPoint) + self.F2.distance_bet_points(oPoint) == self.w: #uses definition to determine if on boundary    
            return True
        else:
            return False
    def __repr__(self):
        return "Foci:({},{}) and Width:{}".format(self.F1,self.F2,self.w)
  #creating child class for parent      
class ClsPoint:
    #two different x and y coords
    def __init__(self, xord = 0, yord = 0):
        self.xord = xord
        self.yord = yord
        self.p = (xord,yord)
        
            
    def set_xord(self, xord):
        #set x coordinate of point to xcoordinate
        self.xord = xord

    def set_yord(self, yord):
        #set y coordinate of point to ycoordinate
        self.yord = yord   
        
    # getter method 
    def get_xord(self): 
        return self.xord
    
     
    def get_yord(self): 
        return self.yord 
    
    def get_Pair(self):
        #return coordinates of the point as a tuple
        return (self.xord, self.yord) 
    
    def distance_bet_points(self, point):
        #Distance between two points
        xpart = point.get_xord() - self.get_xord()
        ypart = point.get_yord() - self.get_yord()

        dist = (xpart**2 + ypart**2)**0.5 
        return dist
     
    def __repr__(self):
        
        return 'Point({}, {})'.format(self.xord, self.yord)     
