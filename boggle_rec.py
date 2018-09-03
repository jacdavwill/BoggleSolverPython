import random as r

###############################
input_word = "ttmkbgnhnavrnldi"
###############################

myfile = open('/storage/emulated/0/Download/wordsEN.txt','r')

global row
global ltr_list

dic = []
dic2 = []
box = []
answers = []
row = 4
boxnum = row ** 2
qPos = []

raw_words = myfile.readlines()

for item in raw_words:
    if len(item) >= 4 and len(item) <= boxnum + 1:
        dic.append(item.strip())

myfile.close()

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

def indexof(x,y):
    a = 0
    b = []
    for item in x:
        if x[a] == y:
            b.append(a)
        a += 1

    return b

ltr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

scrabble = ['a','a','a','a','a','a','a','a','a','b','b','c','c','d','d','d','d','e','e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','g','h','h','i','i','i','i','i','i','i','i','i','j','k','l','l','l','l','m','m','n','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r','r','r','r','r','r','s','s','s','s','t','t','t','t','t','t','v','v','v','v','w','w','x','y','y','z']

ltr_list = []

for item in range(boxnum):
    b = scrabble[r.randint(0,95)]
    ltr_list.append(b)

for num1 in range(row):
    for num2 in range(row):
        box.append([num1,num2])
     
ltr_list = []
for letter in input_word:
    ltr_list.append(letter)

for x in range(boxnum):
    box[x].append(ltr_list[x])

board()

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

for word in dic2:
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
    






