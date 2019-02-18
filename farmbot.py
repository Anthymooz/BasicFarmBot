import time, random, pyautogui

p = pyautogui

time.sleep(5) #Gives you time to prepare the game window

#gotta keep moving so you don't get kicked for going idle

def Move():
    Direction = random.randint(1,4)
    if Direction == 1:
        p.press('w')
        print("Move up")
    if Direction == 2:
        p.press('d')
        print("Move right")
    if Direction == 3:
        p.press('s')
        print("Move down")
    if Direction == 4:
        p.press('a')
        print("Move left")


def Click():
    p.click(x=200,y=200)
    print("Left Mouseclick")


def main():
    Move()
    time.sleep(1)
    Click()
    time.sleep(2)
    main()

main()
