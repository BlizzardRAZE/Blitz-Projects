import pyautogui
import datetime
import threading
import os

userCancel = False
threadActive = True

def textGUI():
    print("Hello User!\nPlease Enter a time to run mouse")
    seconds = input("Enter number of seconds: ")
    minutes = input("EntFer number of minutes: ")
    hours = input("Enter number of hours: ")
    while True:
        if(seconds.isnumeric() and int(seconds) <= 59):
            if(minutes.isnumeric() and int(minutes) <= 59):
                if(hours.isnumeric() and int(hours) <= 99):
                    os.system('cls')
                    print(f"Time Set!")
                    print(f"Setting Mouse...")
                    return seconds, minutes, hours
                else:
                    os.system('cls')
                    print("Warning! Please enter a valid integer number for hours")
                    hours = input("Enter number of hours: ")
            else:
                os.system('cls')
                print("Warning! Please enter a valid integer number for minutes")
                minutes = input("Enter number of minutes: ")
        else:
            os.system('cls')
            print("Warning! Please enter a valid integer number for seconds")
            seconds = input("Enter number of seconds: ")

def quitMouse():
    while True and threadActive:
        userInput = input()
        if (userInput.upper() == "Q"):
            global userCancel 
            userCancel = True
            break

def moveMouse(seconds, minutes, hours):   
    timeIsUp = False 
    mouseTime = int(0)
    mouseTime += int(seconds)
    mouseTime += int(minutes) * 60
    mouseTime += int(hours) * 3600
    input_thread = threading.Thread(target=quitMouse)
    input_thread.start()
    while not timeIsUp:
        pyautogui.moveTo(250, 250, duration= 1)
        os.system('cls')
        print(f"Time Remaining: {datetime.timedelta(seconds=mouseTime)}\nPress Q to Quit")
        mouseTime -= 1
        pyautogui.moveTo(1595, 250, duration= 1)
        os.system('cls')
        print(f"Time Remaining: {datetime.timedelta(seconds=mouseTime)}\nPress Q to Quit")
        mouseTime -= 1
        if userCancel == True:
            os.system('cls')
            print("Time Canceled!")
            exit()
        if mouseTime == 0:
            timeIsUp = True
    os.system('cls')
    print("Time's Up!\nPress enter to quit program")
    global threadActive
    threadActive = False
        
    
def main():
    os.system('cls')
    s, m, h= textGUI()
    moveMouse(s, m, h)

if __name__ == "__main__":
    main()