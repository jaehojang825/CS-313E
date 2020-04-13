#File: Reducible.py

#Description: finds the longest reducible word in dictionary of words

#Student Name: Jaeho Jang

#Student UT EID: jj36386

#Course Name: CS 313E

#Date Created: 04/01/2020

#Date Last Modified: 04/03/2020

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hash_idx = 0
    for i in range(len(s)):
        letter = ord(s[i]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size(s, const):
    hash_val = 0
    key = 1
    for i in range(len(s) - 1, -1, -1):
        letter = ord(s[i]) - 96
        hash_val += key * letter
        key *= 26
    return const - (hash_val % const)

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    hash_idx = hash_word(s, len(hash_table))
    if hash_table[hash_idx] == '':
        hash_table[hash_idx] = s
    step = step_size(s, 13)
    hash_idx = (hash_idx + step) % len(hash_table)
    while hash_table[hash_idx] != '':
        hash_idx = (hash_idx + step) % len(hash_table)
    hash_table[hash_idx] = s

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    word_idx = hash_word(s, len(hash_table))
    if hash_table[word_idx] == s:
        return True
    step = step_size(s, 13)
    while hash_table[word_idx] != '':
        idx = (word_idx + step) % len(hash_table)
        while idx != word_idx:
            if hash_table[idx] == s:
                return True
            elif hash_table[idx] == '':
                return False
            else:
                idx = (idx + step) % len(hash_table)
    return False

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible(s, hash_table, hash_memo):
    if s=='a' or s=='o' or s=='i':
        return True
    if len(s) == 2:
        if 'a' in s or 'i' in s or 'o' in s:
            hash_memo.append(s)
            return True
    word_list=[]
    for i in range(len(s)):
        child = s[:i] + s[i + 1:]
        if find_word(child, hash_table):
            word_list.append(child)
    for i in word_list:
        return is_reducible(i, hash_table, hash_memo)

    return False

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    max_length = len(string_list[0][0])
    for i in string_list:
        max_length = max(max_length, len(i[0]))
    longest_strings = []
    for i in string_list:
        if len(i[0]) == max_length:
            longest_strings.append(i[0])
    longest_strings.sort()
    return longest_strings

def main():
    # create an empty word_list
    word_list = []

    # open the file words.txt
    file = open('words.txt', 'r')

    # read words from words.txt and append to word_list
    for line in file:
        line = line.split()
        word_list.append(line)

    # close file words.txt
    file.close()

    # find length of word_list
    word_list_len = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    n = 2*word_list_len
    while is_prime(n):
        n+=1

    # create and empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range(0, n):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word[0], hash_list)

   # create an empty hash_memo
    hash_memo = []

   # populate the hash_memo with M blank strings
    M = 27000
    while not is_prime(M):
        M += 1
    for i in range(0, M):
        hash_memo.append('')

   # create and empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word[0], hash_list, hash_memo):
            reducible_words.append(word)

   # find words of the maximum length in reducible_words
    max_words = []
    max_words.append(get_longest_words(reducible_words))

    # print the words of maximum length in alphabetical order
    # one word per line
    for words in max_words:
        print(words[0])

if __name__ == "__main__":
    main()