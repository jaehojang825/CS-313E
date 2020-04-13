#File: Work.py

#Description:

#Student Name: Jaeho Jang

#Student UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/24/2020

#Date Last Modified: 2/24/2020

import time

def fallAsleep(n,k):
    #counts coffee number till Vyasa is done coding
    cof_count=1
    #total amount coded before Vyasa falls asleep
    code_bef_sleep=n
    #loops till 'code' is 'done'
    while k**cof_count<=n:
        code_bef_sleep+=(n//k**cof_count)
        cof_count+=1
    #returns total amount coded before falling asleep
    return code_bef_sleep

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n,k):
    for i in range(n):
        if fallAsleep(i,k)>=n:
            return i
    return -1

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search(n,k):
    low = 0
    high = n
    # middle point
    mid = (high + low) // 2
    # loop for binary search;derived from example in Zybook
    while mid!=low:
        # if larger then minimum code, make high minimum code
        if fallAsleep(mid,k) >= n:
            high=mid
        # if smaller than minimum code, make low maximum code
        elif fallAsleep(mid,k) < n:
            low=mid
        mid=(low+high)//2
    if fallAsleep(mid,k)<n:
        return mid+1
    # returns minimum code found through binary search
    return mid


def main():
    in_file=open('work.txt','r')
    num_cases=int(in_file.readline().strip())

    for i in range(num_cases):
        inp=(in_file.readline().split())
        n=int(inp[0])
        k=int(inp[1])

        start=time.time()
        print('Binary Search: '+str(binary_search(n,k)))
        finish=time.time()
        print('Time: '+str(finish-start))

        print()

        start=time.time()
        print('Linear Search: '+str(linear_search(n,k)))
        finish=time.time()
        print('Time: '+str(finish-start))

        print()
        print()

if __name__ == "__main__":
    main()