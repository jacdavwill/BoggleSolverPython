# Name: Jacob Williams
# Date: 1/25/16
# Contact: jacdavwill@gmail.com
# Purpose: The goal of this program is to allow users to solve for all of the words in a Boggle layout.

import random as r

print("Welcome to Boggle Solver!")
print()
print("How to enter your board:")
print("     1) When prompted for your board layout, enter each of the letters on your board without spaces.")
print("     2) Enter the letters from the left to the right, from the top to the bottom. Just like you are reading.")
print("     3) If there is a qu on your board simply type a q.")
print("     4) The board must be a square, but may be of any size.")
print()
print("Example:")
print()
print("     Qu  I   T   H")
print()
print("     P   F   V   E")
print("                       =   qithpfveathuwreo")
print("     A   T   H   U")
print()
print("     W   R   E   O")
print()
print()

input_word = input("Please enter your board layout: ")

def isSquare(num):
    for x in range(1,100):
        if num == (x * x):
            return True

    return False

while not isSquare(len(input_word)):
    print("The board must be a square")
    print()
    input_word = input("Please enter your board layout: ")

myfile = open('/storage/emulated/0/Download/wordsEN.txt','r') # change this to be the location of your dictionary

global row
global ltr_list

dic = []
dic2 = []
box = []
answers = []
row = 4
boxnum = row ** 2
qPos = []

# removes all words from the dictionary that are too big or small
raw_words = myfile.readlines()

for item in raw_words:
    if len(item) >= 4 and len(item) <= boxnum + 1:
        dic.append(item.strip())

myfile.close()

# prints a formatted version of the board
def board():
    print()
    
    sp = '   '
    for item in range(row):
        lin = ''
        print()
        for items in range(row):
            if box[(row*item) + items][2] == 'q':
                lin += box[(row*item) + items][2].upper() + 'u  '
            else:
                lin += box[(row*item) + items][2].upper() + sp
        print(lin)
    
    print()

# returns all of the indexes of a specific letter in a word
def indexof(x,y):
    a = 0
    b = []
    for item in x:
        print(x[a])
        if x[a] == y:
            b.append(a)
            print("true")
        a += 1

    return b

# letters of the alphabet
ltr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ltr_list = []

# places letters in a list    
ltr_list = []
for letter in input_word:
    ltr_list.append(letter)

for x in range(boxnum):
    box[x].append(ltr_list[x])

board()

# takes care of the qu abnormality
for word in dic:
    s = True
    qPos = []
    for num in range(len(word)):
        if word[num] == 'q' and num + 1 != len(word):
            if word[num + 1] == 'u':
                qPos.append(num)
            else:
                s = False
               
        if word[num] not in ltr_list:
            if word[num] == 'u':
                if word[num - 1] == 'q':
                    pass
            else:
                s = False

    if s:
        for item in range(len(qPos),0,-1):
            word = word[:qPos[item - 1] + 1] + word[qPos[item - 1] + 2:]
        dic2.append(word)

qPos = []

# finds all adjacent letters on the board
def adj(a,row):
    ans = []
    pos = [int(a / row), a % row]

    if pos == [0,0]:
        ans.append(a + 1)
        ans.append(a + row)
        ans.append(a + row + 1)

    elif pos == [0,row - 1]:
        ans.append(a - 1)
        ans.append(a + row)
        ans.append(a + row - 1)

    elif pos == [row - 1, 0]:
        ans.append(a + 1)
        ans.append(a - row)
        ans.append(a - row + 1)

    elif pos == [row - 1, row - 1]:
        ans.append(a - 1)
        ans.append(a - row)
        ans.append(a - row - 1)

    elif pos[0] == 0:
        ans.append(a - 1)
        ans.append(a + 1)
        ans.append(a + row)
        ans.append(a + row - 1)
        ans.append(a + row + 1)

    elif pos[0] == row - 1:
        ans.append(a - 1)
        ans.append(a + 1)
        ans.append(a - row)
        ans.append(a - row - 1)
        ans.append(a - row + 1)

    elif pos[1] == 0:
        ans.append(a + row)
        ans.append(a - row)
        ans.append(a + row + 1)
        ans.append(a + 1)
        ans.append(a - row + 1)

    elif pos[1] == row - 1:
        ans.append(a + row)
        ans.append(a - row)
        ans.append(a + row - 1)
        ans.append(a - 1)
        ans.append(a - row - 1)

    else:
        ans.append(a + 1)
        ans.append(a - 1)
        ans.append(a + row)
        ans.append(a + row - 1)
        ans.append(a + row + 1)
        ans.append(a - row)
        ans.append(a - row - 1)
        ans.append(a - row + 1)

    return ans

# recursive function that searches adjacent positions for the next letter in a word
def search(hist, word):
    global ltr_list
    global row

    nex_ltr = word[len(hist)]
    
    for pos in adj(hist[-1],row):
        
        if (ltr_list[pos] == nex_ltr) and (pos not in hist):
            hist.append(pos)
            
            if len(hist) == len(word):
                return True

            else:
                ans = search(hist, word)
                
                if ans:
                    return True
                else:
                    hist.pop(len(hist) - 1)
    
    return False

# checks if any of the words left from the dictionary are found on the board
for word in dic2:
    print(word)
    print(ltr_list)
    print(indexof(ltr_list, word[0]))
    for pos in indexof(ltr_list, word[0]):
        
        ans = search([pos], word)
        
        
        if ans:
            qPos = []
            for num in range(len(word)):
                if word[num] =='q':
                    qPos.append(num)
            for item in range(len(qPos), 0, -1):
                word = word.replace('q','qu')
            answers.append(word)
            break

# prints out all possible words in order of length
def show():

    long = ''
    wordsByLen = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for answer in answers:
        wordsByLen[len(answer) - 3].append(answer)
    
    count = 2
    for item in wordsByLen:
        count += 1
        if len(item) > 0:
            print(str(count) + ".")
            for ans in item:
                print(ans)
            print()
    
    print('Total words: ' + str(len(answers)))

show()       
