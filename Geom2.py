#File: Geom.py

#Description: Reads in points,circles,and rectangles to compare size and position on a x-y plane

#Student Name: Jaeho Jang

#Student EID: jj36386

#Course Name: CS 313E

#Unique Number: 50205

#Date Created: 9/18/19

#Dat Last Modified: 9/20/19
import math
e=10

class Point(object):
    #constructor
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def dist(self,other):
    #distance between points
        return math.hypot(self.x-other.x,self.y-other.y)

    def __str__(self):
    #returns formatted (string) output
        return '('+str(self.x)+','+str(self.y)+')'

    def __eq__(self,other):
    #test for point equality
        tol = 1.0*(e^-8)
        return (abs(self.x-other.x)<tol) and (abs(self.y-other.y)<tol)

class Circle(object):
    #constructor
    def __init__(self,radius=1,x=0,y=0):
        self.radius = radius
        self.center = Point(x,y)

    def circumference(self):
        #compute circle circumference
        return 2.0*math.pi*self.radius

    def area(self):
        #compute circle area
        return math.pi*self.radius*self.radius

    def point_inside(self,p):
        #determine if point is strictly inside circle
        return self.center.dist(p)<self.radius

    def circle_inside(self,c):
        #determine if circle is strictly inside circle
        distance = self.center.dist(c.center)
        return (distance+c.radius)<self.radius

    def circle_overlap(self,c):
        #determine if one circle overlaps another
        #when on circle area=other circle
        distance=self.center.dist(c.center)
        return (distance+c.radius)<self.radius+c.radius

    def circle_circumscribe(self,r):
        #determines smallest circle that circumscribes rectangle r
        r.ul.x = self.center.x-self.radius
        r.lr.x = self.center.x+self.radius
        r.ul.y = self.center.y+self.radius
        r.lr.y = self.center.y-self.radius
        return r

    def __str__(self):
        #returns formatted (string) output
        return 'Radius:'+str(self.radius)+', Center:'+str(self.center)

    def __eq__(self,other):
        #tests for equality
        tol = 1.0*(e^-8)
        return abs(self.radius-other.radius)<tol

class Rectangle(object):
    #constructor
    def __init__(self,ul_x=0,ul_y=0,lr_x=1,lr_y=0):
        if(ul_x<lr_x) and (ul_y>lr_y):
            self.ul=Point(ul_x,ul_y)
            self.lr=Point(lr_x,lr_y)
        else:
            self.ul=Point(0,1)
            self.lr=Point(1,0)

    def length(self):
        #determine length of rectangle
        length = self.ul.x-self.lr.x
        return abs(length)

    def width(self):
        #determines width of rectangle
        width = self.ul.y-self.lr.y
        return abs(width)

    def perimeter(self):
        #computes perimeter of rectangle
        return 2*(abs((self.ul.x-self.lr.x))+abs((self.ul.y-self.lr.y)))

    def area(self):
        #computes area of rectangle
        return abs(self.ul.x-self.lr.x)*(self.ul.y-self.lr.y)

    def point_inside(self,p):
        #determine if a point is strictly inside the rectangle
        center = Point(int((self.ul.x + self.lr.x)/2), int((self.ul.y + self.lr.y) / 2))
        return (self.ul.x-self.lr.x)>center.dist(p) and (self.ul.y-self.lr.y)>center.dist(p)

    def rectangle_inside(self,r):
        #determine if another rectangle is strictly inside this rectangle
        return r.ul.x>self.ul.x and r.ul.y<self.ul.y and r.lr.x<self.lr.x and r.lr.y>self.lr.y

    def rectangle_overlap(self,r):
        #determine if two rectangles overlap
        ov1 = r.ul.x < self.lr.x and r.ul.y > self.lr.y
        ov2 = r.ul.x>self.ul.x and r.ul.y<self.ul.y
        ov3=self.ul.x < r.lr.x and self.ul.y > r.lr.y
        ov4=self.ul.x>r.ul.x and self.ul.y<r.ul.y
        return (ov1 and ov2) or (ov3 and ov4)

    def rectangle_circumscribe(self,c):
        #determine smallest rectangle that circumscribes a circle
        c.radius=math.sqrt(((self.length()*self.length())+(self.width()*self.width())))
        center = Point(int((self.ul.x + self.lr.x)/2), int((self.ul.y + self.lr.y)/2))
        c.center.x = center.x
        c.center.y = center.y
        return c

    def __str__(self):
        #returns formatted (string) output
        return 'UL:'+str(self.ul)+', LR:'+str(self.lr)

    def __eq__(self,other):
        #tests for equality
        tol = 1.0*(e^-8)
        return abs(self.length()-other.length())<tol and abs(self.width()-other.width())<tol

def main():
    #opens file and calls class objects to test
    with open('geom.txt','r') as geom_file:
        coord=geom_file.readlines()
    coord=[x.strip() for x in coord]

    coord_list=[]
    for i in coord:
        coord_sp=i.split(' ')
        coord_list.append(coord_sp)

    point_p=Point(float(coord_list[0][0]),float(coord_list[0][1]))
    point_q=Point(float(coord_list[1][0]),float(coord_list[1][1]))
    print('Coordinates of P:',point_p)
    print('Coordinates of Q:',point_q)

    dist_pq = point_p.dist(point_q)
    print('Distance between P and Q:',dist_pq)

    circle_c=Circle(float(coord_list[2][0]),float(coord_list[2][1]),float(coord_list[2][2]))
    circle_d=Circle(float(coord_list[3][0]),float(coord_list[3][1]),float(coord_list[3][2]))
    print('Circle C:',circle_c)
    print('Circle D:',circle_d)
    print('Circumference of C:',circle_c.circumference())
    print('Area of D:',circle_d.area())
    if circle_c.point_inside(point_p) is True:
        print('P is inside C')
    if circle_c.point_inside(point_p) is False:
        print('P is not inside D')
    if circle_d.circle_inside(circle_c) is True:
        print('C is inside D')
    if circle_d.circle_inside(circle_c) is False:
        print('C is not inside D')
    if circle_c.circle_overlap(circle_d) is True:
        print('C does intersect D')
    if circle_c.circle_overlap(circle_d) is False:
        print('C does not intersect D')
    if circle_c.__eq__(circle_d) is True:
        print('C is equal to D')
    if circle_c.__eq__(circle_d) is False:
        print('C is not equal to D')

    rect_g=Rectangle(float(coord_list[4][0]),float(coord_list[4][1]),float(coord_list[4][2]),float(coord_list[4][3]))
    rect_h=Rectangle(float(coord_list[5][0]),float(coord_list[5][1]),float(coord_list[5][2]),float(coord_list[5][3]))
    print('Rectangle G:',rect_g)
    print('Rectangle H:',rect_h)
    print('Length of G:',rect_g.length())
    print('Width of H',rect_h.width())
    print('Perimeter of G:',rect_g.perimeter())
    print('Area of H:',rect_h.area())
    if rect_g.point_inside(point_p) is True:
        print('P is inside G')
    if rect_g.point_inside(point_p) is False:
        print('P is not inside G')
    if rect_h.rectangle_inside(rect_g) is True:
        print('G is inside H')
    if rect_h.rectangle_inside(rect_g) is False:
        print('G is not inside H')
    if rect_h.rectangle_overlap(rect_g) is True:
        print('G does overlap H')
    if rect_h.rectangle_overlap(rect_g) is False:
        print('G does not overlap H')

    print('Circle that circumscribes G:',rect_g.rectangle_circumscribe(Circle()))
    print('Rectangle that circumscribes D:',circle_d.circle_circumscribe(Rectangle()))
    if rect_g.__eq__(rect_h) is True:
        print('Rectangle G is equal to H')
    if rect_g.__eq__(rect_h) is False:
        print('Rectangle G is not equal to H')

    geom_file.close()
if __name__ == '__main__':
    main()