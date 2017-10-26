import time
import msvcrt
def countdown(mins,secs):
    print("Press 'esc' to continue with your mission:\n")
    print("Time remaining:")
    while True:
        if(secs == -1):
            secs = 59
            mins -= 1
        if(secs > 9):  
            print(str(0) + str(mins) + ":" + str(secs), end = "\r")
        else:
            print(str(0) + str(mins) + ":" + str(0) + str(secs), end = "\r")
        time.sleep(1)
        secs -= 1
        if(mins == 0 and secs == -1):
            break
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if(key == b'\x1b'):
                break