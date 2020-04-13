#File: Nim.py

#Description:

#Student's Name: Jaeho Jang

#Student's UT EID: jj36386

#Course Name: CS 313E

#Unique Number 50300

#Date Created: 1/30/19

#Date Last Modified: 1/31/19

def nim_sum(heaps):
    #returns single integer which is nim_sum
    nim_sum = heaps[0]
    for i in range(1,len(heaps)):
        nim_sum=nim_sum^heaps[i] #xor
    return nim_sum

def find_heap(heaps,nim_sum):
    #returns two integers:first is number of counters that has to be removed and second is
    #number of heap from which counters are removed
    if nim_sum==0:
        print('Lose Game')
    else:
        for i in range(0,len(heaps)):
            count=heaps[i]^nim_sum
            if count<heaps[i]:
                counter=heaps[i]-count
                print('Remove',counter,'counters from Heap',i+1)
                break

def main():
    print('')
    nim_file=open('nim.txt','r')
    #read input from input file
    case_num = int(nim_file.readline())
    for i in range(0, case_num):
        case = nim_file.readline().strip().split(' ')
        case_list = [int(i) for i in case]
        sum_nim=nim_sum(case_list)
        #call function nim_sum() with inputs as given
        find_heap(case_list,sum_nim)
        #call function find_heap() with inputs as given and prints results
if __name__=="__main__":
    main()
