#File: Boxes.py

#Description: gets largest subset of boxes that nest inside each other starting with most inner box

#Student Name: Jaeho Jang

#Student UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 3/9/20

#Date last Modified: 3/9/20

#gets all subsets of given box
def get_sub_sets(start, box, ind, sub):
    if (ind == len(start)):
        if (is_valid(box)):
            sub.append(box)
    else:
        next_b = box[:]
        box.append(start[ind])
        get_sub_sets(start, box, ind + 1, sub)
        get_sub_sets(start, next_b, ind + 1, sub)

#returns true if box in box list can nest
def is_valid(boxes):
    for i in range(len(boxes) - 1):
        if can_nest(boxes[i], boxes[i + 1]) is False:
            return False
    return True

#returns true if box fits in another
def can_nest(box1, box2):
    if ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])):
        return True
    else:
        return False

def main():
    #read the file
    box_file = open('boxes.txt','r')
    #read the number of boxes
    num_boxes = int(box_file.readline())
    #create an empty list of box and sublist of box
    boxes = []
    sub_list = []
    #reads the files
    for i in range(num_boxes):
        line = box_file.readline().split()
        for j in range(len(line)):
            line[j] = int(line[j])
        line.sort()
        boxes.append(line)
    #sort the box list and get sublist
    boxes.sort()
    get_sub_sets(boxes,[],0,sub_list)

    maxSub=max([len(subset) for subset in sub_list])
    #print the largest subset
    print("")
    print("Largest Subset of Nesting Boxes:")
    for i in sub_list:
        if len(i)==maxSub:
            [print(j) for j in i]
            print()

    if maxSub<2:
        print('No Nesting Boxes')
main()