import random

def userchoice():
    while True:
        options=['Rock','Paper','Scissors']
        user=input("Please select your input")
        if(user in options):
            return user
        else:
           print("Please enter a valid input") 


def compchoice():
    options=['Rock','Paper','Scissors']   
    comp=random.choice(options)         
    return comp
    
user=userchoice()
comp=compchoice()

if((user=='Scissor'and comp=='Rock')or(user=='Paper'and comp=='Scissor')or(user=='Rock'and comp=='Paper')):
    print("User Lost")    
elif((user=='Rock'and comp=='Scissor')or(user=='Scissor'and comp=='paper')or(user=='paper'and comp=='Rock')):
    print("User Wins!!!")        
else:
    print("Its a Tie")    