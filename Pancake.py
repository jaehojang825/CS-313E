#File: Pancake.py

#Description: representation of the pancake sort

#Student's Name: Jaeho Jang

#Student's UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/21/20

#Date Last Modified: 2/21/20

#finds largest pancake and created index for it
def findLargest(pancake,index):
    largest_pan=pancake[index]
    largest_ind=index

    for i in range(index):
        if pancake[i]>largest_pan:
            largest_pan=pancake[i]
            largest_ind=i

    return largest_ind

#flip pancake at index to flip to top
def flip(pancake,index):
    new_pan=pancake[:(index+1)]
    new_pan.reverse()
    new_pan+=pancake[(index+1):]
    return new_pan

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula
#          this is a list of lists
#          the last item in this list is the sorted stack
def sort_pancakes(pancake):
    every_flip=[]
    for i in reversed(range(len(pancake))):
        pancake=flip(pancake,findLargest(pancake,i))
        pancake=flip(pancake,i)
        every_flip.append(pancake)
    return every_flip

def main():
    #open the file pancakes.txt for reading
    in_file = open ("./pancakes.txt", "r")

    line = in_file.readline()
    line = line.strip()
    line = line.split()
    print (line)
    pancakes = []
    for item in line:
        pancakes.append (int(item))

    # print content of list before flipping
    print ("Initial Order of Pancakes = ", pancakes)

    # call the function to sort the pancakes
    every_flip = sort_pancakes ( pancakes )

    # print the contents of the pancake stack after
    # every flip
    for i in range (len(every_flip)):
        print (every_flip[i])

    # print content of list after all the flipping
    print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
    main()