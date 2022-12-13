#NOTE: Before running this code on your pycharm you have to install fontstyle module. 
import random

import fontstyle



up=0
cp=0

print('*='*175)
print('*='*175)


str=fontstyle.apply('Hello user!!MIE welcomes you to play S.W.G!!','Italic/black/BLUE_BG')
str1=fontstyle.apply('Snake-Water-Gun','Italic/red')
str2='*'*17
str3=fontstyle.apply('Be ready to play with Dinku!!Game starts in 3 2 1!!','Italic/BLACK/YELLOW_BG')
print()
str4=fontstyle.apply("Let's Start!!",'Italic/Bold/green')
str5=fontstyle.apply("For Snake enter 's'",'Italic/yellow')
str6=fontstyle.apply("For Water enter 'w'",'Italic/yellow')
str7=fontstyle.apply("For Gun enter 'g'",'Italic/yellow')
str8=fontstyle.apply("Hurray!!You have got the point!",'Italic/green')
str9=fontstyle.apply("Oh No!!Dinku got the point!",'Italic/red')
str10=fontstyle.apply("Dinku made it!!Better luck next time!",'Italic/red')
str11=fontstyle.apply("Congrats!!You won the game",'Italic/green')
str12=fontstyle.apply("Its a Tie!",'Italic/blue')
str13=fontstyle.apply("ONLY CHOOSE 's' OR 'w' OR 'g'!!!",'Italic/black/RED_BG')
print()
print()
print(str.center(180))
print()
print()
print(str2.center(164))
print(str1.center(175))
print(str2.center(164))
print()
print()
print('*='*175)
print('=*'*175)

print()

print(str3.center(175))

print(str4.center(175))
print(str5.center(175))
print(str6.center(175))
print(str7.center(175))
rounds=int(input('How many rounds you want to play:'))
choices=['s','w','g']
usern=input('Enter your name:')
while rounds>=1:
    compc = random.choice(choices)
    userc = input('Now its Your turn\nEnter your choice:')

    fontstyle.apply(print(usern,"'s choice is ",userc,' and Dinku choice is ',compc,sep=''),'Italic/red')
    if userc!='s'and userc!='g' and userc!='w':
        print(str13.center(175))
    if compc=='s':
        if userc=='w':
            print(str9.center(175))
            cp=cp+1
        elif userc=='g':
            print(str8.center(175))
            up=up+1
    if compc=='w':
        if userc=='g':
            print(str9.center(175))
            cp =cp+ 1
        elif userc=='s':
            print(str8.center(175))
            up =up+ 1
    if compc=='g':
        if userc=='s':
            print(str9.center(175))
            cp =cp+ 1
        elif userc=='w':
            print(str8.center(175))
            up =up+ 1
    if compc==userc:
        print(str12.center(175))
    rounds=rounds-1
print('your score is',up,'comp score is',cp)
print('='*175)
print()
print()
print(str2.center(164))

if cp>up:
    print(str10.center(175))
elif up>cp:
    print(str11.center(175))
else:
    print(str12.center(175))
print(str2.center(164))
print()
print()
print('='*175)
