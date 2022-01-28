import sys
from datetime import datetime
from random import randrange

class colors:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

def binaryguess():
    with open("data.txt",'a',encoding = 'utf-8') as f:
        guess = randrange(32)
        guess2 = guess
        s = ''
        while guess != 0:
            if guess % 2 == 0:
                s += '0'
            else:
                s += '1'
            guess//=2
        #print(guess2)
        s = s[::-1]
        print(s)

        res = 1
        if int(input("Enter your value: ")) != guess2:
            print('\033[31m','wrong','anwser -> ', guess2)
            res = 0
        else:
            print('\033[32m','right!')

        f.write(str(res) + ' ')
        f.write(str(guess2) + ' ')
        f.write(datetime.today().strftime('%Y-%m-%d') + '\n')

binaryguess()

#print(colors.orange,'test',colors.yellow,'et ici?')
