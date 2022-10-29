# Deal or no deal emmulator
from math import sqrt
import random 
from copy import deepcopy
import sys
import time
from tkinter import *

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./30)

def slowprintl(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./20)

def slowprintll(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./2)

print('WELCOME TO DEAL OR NO DEAL!')
print('---------------------------\n')

cash = [1,2,4,6,12,14,20,24,28,30,34,40,50,60,80,90,100,150,200,400]
cases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cash2 = deepcopy(cash)
d = {0:0}
loop = 0
offer = 0

for i in range(1,21):
    d[i] = random.choice(cash)
    a = cash.index(d[i])
    cash[a] = 0
    while d[i] == 0:
        d[i] = random.choice(cash)
        a = cash.index(d[i])
        cash[a] = 0

def display(cases):
    
    slowprint('-------------------------------------')
    slowprintl('Cases:')
    slowprint('------')
    for i in range(10):
        print(cases[i],' '*(23 - len(str(cases[i]))), cases[i + 10])
    slowprint('-------------------------------------\n')

def displayd(cash2):
    
    slowprint('-------------------------------------')
    slowprintl('Money\'s:')
    slowprint('--------')
    for i in range(10):
        print(cash2[i],'$',' '*(23 - len(str(cash2[i]))), cash2[i + 10],'$')
    slowprint('-------------------------------------')

def rep(luck,cash2,d):
    b = cash2.index(d[luck])
    cash2[b] = ''

def dealer(cases, cash2):
    offer = 0
    casesrem = 0
    for j in cases:
        if j != 'x':
            casesrem += 1
    for i in cash2:
        if i != '':
            offer += i**2 
    offer = offer/(casesrem)
    offer = round(sqrt(offer))
    return offer
            
def banker():
    offer = dealer(cases, cash2)
    slowprint('Bank has an offer:')
    print(offer, '$\n' , sep = '')
    slowprint('Deal or No Deal?')
    print('-----------------')

    def deal():
        print('You took the offer of ', offer, '$', sep='')
        print('Your box contained ',origin1,'$', sep = '')
        quit()

    def nodeal():
        window.destroy()

    window = Tk()

    bdeal,bnodeal = Button(window,text="Deal", command=deal,font=('Comic Sans',30)),Button(window,text="No Deal", command=nodeal,font=('Comic Sans',30))

    bdeal.pack()
    bnodeal.pack()



    window.mainloop()


displayd(cash2)
display(cases)

origin = eval(input('Pick a suit case: '))
cases[origin-1]='*'
origin1 = d[origin]

slowprintl('Choose 5 cases to open:')
print('-----------------------\n')

while loop != 5:
    luck = eval(input('Case: '))
    if luck == origin:
        print('\nYou cant choose this one')
    else:
        if d[luck] >= 80:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '+ u"\U0001F480"
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1
        else:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1

loop = 0
display(cases)
displayd(cash2)
slowprintl('RING! \nRING! \nRING!')
banker()
print('LETS GO!!!\n')
slowprintl('Choose 5 cases:')
print('-----------------------\n')

while loop != 5:
    luck = eval(input('Case: '))
    if luck == origin:
        print('\nYou cant choose this one')
    else:
        if d[luck] >= 80:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '+ u"\U0001F480"
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1
        else:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1

loop = 0 
display(cases)
displayd(cash2)
slowprintl('RING! \nRING! \nRING!')
banker()
print('LETS GO!!!\n')
slowprintl('Choose 3 cases:')
print('-----------------------\n')

while loop != 3:
    luck = eval(input('Case: '))
    if luck == origin:
        print('\nYou cant choose this one')
    else:
        if d[luck] >= 80:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '+ u"\U0001F480"
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1
        else:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1

loop = 0
display(cases)
displayd(cash2)
slowprintl('RING! \nRING! \nRING!')
banker()
print('LETS GO!!!\n')
slowprintl('Choose 5 cases:')
print('-----------------------\n')

while loop != 5:
    luck = eval(input('Case: '))
    if luck == origin:
        print('\nYou cant choose this one')
    else:
        if d[luck] >= 80:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '+ u"\U0001F480"
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1
        else:
            line = 'Case '+ str(luck)+' has: '+ str(d[luck])+'$ '
            slowprint(line)
            print()
            cases[luck-1] = 'x'
            rep(luck,cash2,d)
            loop += 1

loop = 0
display(cases)
displayd(cash2)
slowprintl('RING! \nRING! \nRING!')
banker()

print('Your case has:')
origin = str(origin)
slowprintll(origin)

