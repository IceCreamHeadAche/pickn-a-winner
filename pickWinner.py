x = 0

#respList = [] # creates an empty list to hold responders names 
#resp = raw_input('[+] Please <TYPE> a name and press <ENTER> - <TYPE> q and press enter to quit entering names \n') #prompts for a name and collects the input, stores as resp


#print 'How many potential winners do you want to add to the drawing? Please enter a whole number'
#number = raw_input()

#while (number!=0):
##	respList.append(resp)
#	number = int(number)-1
#	resp = raw_input('[+] Please type another name and press <ENTER>: \n')

#print respList	

print '[+] Thanks for playing - please wait while the results are computed...'
print '[+] We are working with some BIG DATA right now, over 10,000,000 votes are being cast...'

potentialWinner = ['Mike Bills','Jim Ellis','Jeff Pinkham','Michiel Bugher','Steve Short','Brad Wight' ]

Responder0 = 0
Responder1 = 0
Responder2 = 0
Responder3 = 0
Responder4 = 0
Responder5 = 0

import random
while (x<10000002):
        x=x+1         
        y = random.choice(potentialWinner)
        
        if ('Jim Ellis' in y):
            Responder1 = Responder1 + 1
        elif ('Jeff Pinkham' in y):
            Responder2 = Responder2 + 1
        elif ('Michiel Bugher' in y):
            Responder3 = Responder3 + 1
        elif ('Steve Short' in y):
            Responder4 = Responder4 + 1
        elif ('Mike Bills' in y):
            Responder0 = Responder0 + 1    
        elif ('Brad Wight' in y):
            Responder5 = Responder5 + 1   
potentialWinners = potentialWinner


responderValues = [Responder0,Responder1,Responder2, Responder3, Responder4, Responder5]
#print responderValues
#print sorted(responderValues)
theWinners = sorted(responderValues)
#print theWinners
theWinners = theWinners[-3:]
#print theWinners

#potentialWinners = sorted(potentialWinners)



#threeWinners = potentialWinners[-4:]
#print threeWinners and the runner up

print '\n'



for p in theWinners: 
    if p == Responder0:
        print '[+] Mike Bills = '+ str(p)
    elif p == Responder1: 
        print '[+] Jim Ellis = '+ str(p)
    elif p == Responder2: 
        print '[+] Jeff Pinkham = '+ str(p)
    elif p == Responder3:
        print '[+] Michiel Bugher = '+ str(p)
    elif p == Responder4:
        print '[+] Steve Short = '+ str(p)
    elif p == Responder5:
        print '[+] Brad Wight = '+ str(p)
    else: 
        print 'end of the list'
        