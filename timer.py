import time

seconds=input("Enter the time in number of seconds: ")

# define the countdown timer function
def countdowm_timer(seconds) :
    while seconds>0:
        min=int(seconds/60)
        sec=int(seconds%60)
    
        timer=f'{min}:{sec}'
        print(timer,end='\r')
        time.sleep(1)

        seconds=seconds-1
    print("Time up!")



countdowm_timer(int(seconds))
