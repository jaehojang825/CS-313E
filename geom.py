#File: Geom.py

#Description: representation of line in geometry

#Student Name: Jaeho Jang

#Student UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/13/20

#Date Last Modified: 2/14/20

import math
e=10
tol=1.0*(e^-6)

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
        return (abs(self.x-other.x)<tol) and (abs(self.y-other.y)<tol)

class Line(object):
    # line is defined by two Point objects p1 and p2
    # constructor assign default values if user does not define
    # the coordinates of p1 and p2 or the two points are the same
    def __init__(self,p1_x=0,p1_y=0,p2_x=1,p2_y=1):
        self.p1=Point(p1_x,p1_y)
        self.p2=Point(p2_x,p2_y)

    # returns True if the line is parallel to the x axis
    # and False otherwise
    def is_parallel_x(self):
        if abs(self.p1.y-self.p2.y<tol):
            return True
        else:
            return False

    # returns True if the line is parallel to the y axis
    # and False otherwise
    def is_parallel_y(self):
        if abs(self.p1.x-self.p2.x<tol):
            return True
        else:
            return False

    # determine slope for the line
    # return float ('inf') if line is parallel to the y-axis
    def slope(self):
        if self.is_parallel_y():
            return float ('inf')
        else:
            slope=(self.p1.y-self.p2.y)/(self.p1.x-self.p2.x)
            return slope

    # determine the y-intercept of the line
    # return None if line is parallel to the y axis
    def y_intercept(self):
        y_int=self.p1.y-self.slope()*self.p1.x
        return y_int

    # determine the x-intercept of the line
    # return None if line is parallel to the x axis
    def x_intercept(self):
        x_int=-1*self.y_intercept()/self.slope()
        return x_int

    # returns True if line is parallel to other and False otherwise
    def is_parallel(self,other):
        return abs(self.slope()-other.slope())<tol

    # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular(self,other):
        return abs(self.slope()-(-1/other.slope())<tol)

    # returns True if Point p is on the line or an extension of it
    # and False otherwise
    def is_on_line(self,p):
        if self.is_parallel_y():
            return abs(p.x-self.x_intercept()<tol)
        else:
            return abs(self.slope()*p.x+self.y_intercept()-p.y)<tol

    # determine the perpendicular distance of Point p to the line
    # return 0 if p is on the line
    def perp_dist(self,p):
        if self.is_parallel_y():
            dist=abs(self.p1.x-p.x)
            return dist
        else:
            p2slope=-1/self.slope()
            p2int=p.y-p2slope*p.x
            x=((p2int-self.y_intercept())/(self.slope()-p2slope))
            y=self.slope()*x+self.y_intercept()
            p2=Point(x,y)
            dist=p.dist(p2)
            return dist

    # returns a Point object which is the intersection point of line
    # and other or None if they are parallel
    def intersection_point(self,other):
        if not self.is_parallel(other):
            x=(other.y_intercept()-self.y_intercept())/(self.slope()-other.slope())
            if x==-0:
                x=abs(x)
            y=self.slope()*x+self.y_intercept()
            return Point(x,y)

    # return True if two points are on the same side of the line
    # and neither points are on the line
    # return False if one or both points are on the line or both
    # are on the same side of the line
    def on_same_side(self,p1,p2):
        s1=self.slope()*p1.x+self.y_intercept()
        s2=self.slope()*p2.x+self.y_intercept()
        if (p1.y>s1 and p2.y>s2) or (p1.y<s1 and p2.y<s2):
            return True
        else:
            return False

    # string representation of the line - one of three cases
    # y = c if parallel to the x axis
    # x = c if parallel to the y axis
    # y = m * x + b
    def __str__(self):
        if self.is_parallel_x():
            return 'y = '+str(self.p1.y)
        elif self.is_parallel_y():
            return 'x = '+str(self.p1.x)
        else:
            return 'y = '+str(self.slope())+'x + '+str(self.y_intercept())

def main():
    # open file "geom.txt" for reading
    with open('geom.txt','r') as geom_file:
        coord=geom_file.readlines()
    coord=[x.strip() for x in coord]

    coord_list=[]
    for i in coord:
        coord_sp=i.split(' ')
        coord_list.append(coord_sp)

    # print the coordinates of points P and Q
    point_p=Point(float(coord_list[0][0]), float(coord_list[0][1]))
    point_q=Point(float(coord_list[1][0]), float(coord_list[1][1]))
    print('Coordinates of P:',point_p)
    print('Coordinates of Q:',point_q)

    # print distance between P and Q
    dist_pq=point_p.dist(point_q)
    dist_pq=format(dist_pq,'.2f')
    print('Distance between P and Q:',dist_pq)

    # print the slope of the line PQ
    line_PQ=Line(point_p.x,point_p.y,point_q.x,point_q.y)
    slope_pq=line_PQ.slope()
    slope_pq=format(slope_pq,'.2f')
    print('Slope of PQ:',slope_pq)

    # print the y-intercept of the line PQ
    y_slope_PQ=line_PQ.y_intercept()
    y_slope_PQ=format(y_slope_PQ,'.2f')
    print('Y-Intercept of PQ:',y_slope_PQ)

    # print the x-intercept of the line PQ
    x_slope_PQ = line_PQ.x_intercept()
    x_slope_PQ = format(x_slope_PQ, '.2f')
    print('Y-Intercept of PQ:', x_slope_PQ)


    point_a = Point(float(coord_list[2][0]), float(coord_list[2][1]))
    point_b = Point(float(coord_list[3][0]), float(coord_list[3][1]))

    # print the string representation of the line AB
    line_AB=Line(point_a.x,point_a.y,point_b.x,point_b.y)
    print('Line AB:',line_AB)

    # print if the lines PQ and AB are parallel or not
    if line_PQ.is_parallel(line_AB) is True:
        print('PQ is parallel to AB')
    else:
        print('PQ is not parallel to AB')

    # print if the lines PQ and AB (or extensions) are perpendicular or not
    if line_PQ.is_perpendicular(line_AB):
        print('PQ is not perpendicular to AB')
    else:
        print('PQ is perpendicular to AB')

    point_g = Point(float(coord_list[4][0]), float(coord_list[4][1]))
    point_h = Point(float(coord_list[5][0]), float(coord_list[5][1]))

    # print coordinates of the intersection point of PQ and AB if not parallel
    intersection_PQAB=line_PQ.intersection_point(line_AB)
    print(intersection_PQAB)

    # print if the the points G and H are on the same side of PQ
    if line_PQ.on_same_side(point_g,point_h):
        print('G and H are on the same side of PQ')
    else:
        print('G and H are not on the same side of PQ')

    # print if the the points G and H are on the same side of AB
    if line_AB.on_same_side(point_g,point_h):
        print('G and H are on the same side of AB')
    else:
        print('G and H are not on the same side of AB')

    # close file "geom.txt"
    geom_file.close()
if __name__ == "__main__":
    main()