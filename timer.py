import time
import msvcrt
def countdown(mins,secs):
    print("Press 'esc' to continue with your mission:\n")
    print("Time remaining:")
    while True:
        if(secs == -1): # Resets the seconds and minutes when the seconds reaches -1
            secs = 59
            mins -= 1
        if(secs > 9):  
            print(str(0) + str(mins) + ":" + str(secs), end = "\r")
        else:
            print(str(0) + str(mins) + ":" + str(0) + str(secs), end = "\r")    # Adds a zero ahead of the seconds when the seconds reaches less than 9
        time.sleep(1)   # Wait 1 second
        secs -= 1
        if(mins == 0 and secs == -1):
            break
        if msvcrt.kbhit():          # Detects when a keys is pressed
            key = msvcrt.getch()    # Returns the ASCII value of the key that was pressed
            if(key == b'\x1b'):     # Breaks if the key's value is equal to the ACII value of the escape key
                break