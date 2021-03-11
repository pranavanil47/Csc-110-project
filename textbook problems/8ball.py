import random 
def ball():
    ball_list = ['Yes, of course!','Without a doubt, yes.','You can count on it.',\
        'For sure!','Ask me later.','I’m not sure.','I can’t tell you right now.',\
            'I’ll tell you after my nap.','No way!','I don’t think so.','Without a doubt, no.' \
            ,'The answer is clearly NO.']
    
    return ball_list


def rgen():
    ball_8 = ball()
    print('---------------------')
    print('welcome to 8ball ©')
    i = 0
    while True:
        number = random.randint(0,11)
        input('Think of your problem and press Enter..........')
        print()
        print(ball_8[number])
        
        

rgen()
















