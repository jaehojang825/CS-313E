#File: TestCipher.py

#Description: representation of substitution cipher and transposition cipher

#Student's Name: Jaeho Jang

#Student's UT EID: jj36386

#Course Name: CS 313E

#Unique Number: 50300

#Date Created: 2/7/20

#Date Last Modified: 2/9/20

abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng,key):
    strng_list=list(strng)
    print(strng_list)
    matrix=[]
    for i in range(key):
        row=[]
        for j in range(len(strng)):
            row.append('-')
        matrix.append(row)
    print(matrix)
    dir=True
    x=0
    y=0
    for i in range(len(strng)):
        if x==0:
            dir=True
        if x==(key - 1):
            dir=False
        matrix[x][i]=strng_list[y]
        y+=1

        if dir is False:
            x-=1
        else:
            x+=1

    encode=[]
    for i in range(key):
        for j in range(len(strng)):
            if matrix[i][j]!='-':
                encode.append(matrix[i][j])
    encode=''.join(encode)

    return encode

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng,key):
    strng_list=list(strng)

    matrix=[]
    for i in range(key):
        row = []
        for j in range(len(strng)):
            row.append('-')
        matrix.append(row)

    dir=True
    x=0
    for i in range(len(strng)):
        if x==0:
            dir=True
        if x==(key-1):
            dir=False
        matrix[x][i]='+'
        if dir is False:
            x-=1
        else:
            x+=1

    y=0
    for i in range(key):
        for j in range(len(strng)):
            if matrix[i][j] == '+':
                matrix[i][j] = strng_list[y]
                y += 1

    dir=True
    decode=[]
    for i in range(key):
        for j in range(len(strng)):
            if i==(key-1):
                dir = True
            elif i==0:
                dir=False
            decode.append(matrix[i][j])
            if dir is True:
                i-=1
            else:
                i+=1
    decode=''.join(decode[:len(strng)])

    return decode

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    fStrng=''
    for i in strng:
        if ord(i)>=97 and ord(i)<=122:
            fStrng += i

    return fStrng

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p,s):
    i=ord(p)-ord('a')
    j=ord(s)-ord('a')
    m=i+j
    if m>26:
        m=m-26
    elif m==26:
        m=0
    encoded=abc[m]

    return encoded

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p,s):
    x=ord(p)-ord('a')
    y=ord(s)-ord('a')
    z=y-x
    decoded = abc[z]

    return decoded

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vignere_encode(strng,p):
    encoded=''
    for i in range(len(strng)):
        x=(encode_character(p[i],strng[i]))
        encoded+=x
    return encoded

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vignere_decode(strng,p):
    decoded=''
    for i in range(len(strng)):
        x=(decode_character(p[i],strng[i]))
        decoded+=x
    return decoded

def main():
    print('Rail Fence Cipher')
    print('')

    # prompt the user to enter plain text
    txt=input('Enter Plain Text to be Encoded:')
    # prompt the user to enter the key
    key = int(input('Enter Key:'))
    # prompt the user to enter encoded text
    print('Encoded Text:',
          rail_fence_encode(txt,key))
    print('')

    eTxt = input('Enter Encoded Text to be Decoded:')
    # prompt the user to enter the key
    dKey = int(input('Enter Key:'))
    # decrypt and print the encoded text using rail fence cipher
    print('Decoded Plain Text:',
          rail_fence_decode(eTxt,dKey))
    print('')

    print('Vigenere Cipher')
    print('')

    # prompt the user to enter plain text
    txt=input('Enter Plain Text to be Encoded:')
    txt=txt.lower()
    fTxt=filter_string(txt)

    # prompt the user to enter pass phrase
    pass_phrase=input('Enter Pass Phrase (no spaces allowed):')
    pass_phrase=pass_phrase.lower()
    x=len(fTxt)-len(pass_phrase)
    # encrypt and print the plain text using Vigenere cipher
    for i in range(len(fTxt)):
        if x!=0:
            pass_phrase+=pass_phrase[i]
            x-=1

    # prompt the user to enter encoded text
    print('Encoded Text:',
          vignere_encode(fTxt, pass_phrase))
    print('')

    # prompt the user to enter pass phrase
    vig_eTxt=input('Enter Encoded Text to be Decoded:')
    pass_phrase=input('Enter Pass Phrase (no spaces allowed):')
    pass_phrase=pass_phrase.lower()
    x=len(vig_eTxt)-len(pass_phrase)
    for i in range(len(vig_eTxt)):
            pass_phrase+=pass_phrase[i]
            x -= 1

    # decrypt and print the encoded text using Vigenere cipher
    print('Decoded Plain Text:',
          vignere_decode(vig_eTxt, pass_phrase))

if __name__ == "__main__":
    main()