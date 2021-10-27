# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# http://www.flint.jp/misc/?q=dik&lang=en


import ctypes
import time
import pyautogui
from PIL import Image, ImageGrab
import pytesseract
import keyboard
import cv2
import numpy

pytesseract.pytesseract.tesseract_cmd = r'E:\\New Folder\\tesseract.exe'
SendInput = ctypes.windll.user32.SendInput
2
One = 0x02
Two = 0x03
SpaceBar = 0x39
SAFETY = 1
TAB = 0x0F
two = 0x03
esc = 0x01

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def Click():
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def Tab():
    PressKey(TAB)
    ReleaseKey(TAB)


def Start():
    PressKey(SpaceBar)
    ReleaseKey(SpaceBar)
    time.sleep(0.1)
    PressKey(SpaceBar)
    ReleaseKey(SpaceBar)


def Bramble(i):
    for s in range(i):
        time.sleep(0.25)
        PressKey(One)
        ReleaseKey(One)
        time.sleep(0.25)
        PressKey(Two)
        ReleaseKey(Two)
        time.sleep(0.25)
        PressKey(One)
        ReleaseKey(One)
        time.sleep(0.25)
        PressKey(Two)
        ReleaseKey(Two)




def BrambleYer(i):
    y = 1
    for s in range(i):
        time.sleep(0.25)
        PressKey(One)
        ReleaseKey(One)
        time.sleep(0.25)
        PressKey(Two)
        ReleaseKey(Two)
        time.sleep(0.25)
        PressKey(One)
        ReleaseKey(One)
        time.sleep(0.25)
        PressKey(Two)
        ReleaseKey(Two)
        print(y)
        y = y + 1


def Village():
    pyautogui.moveTo(1800, 900, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(1800, 100, 0.4)
    pyautogui.mouseUp()
    pyautogui.moveTo(1800, 750, 0.1)
    Click()
    pyautogui.moveTo(1550, 560, 0.1)
    Click()
    pyautogui.moveTo(1800, 250, 0.4)
    pyautogui.mouseDown()
    pyautogui.moveTo(1800, 1000, 0.4)
    pyautogui.mouseUp()


def VillageLoc():
    pyautogui.moveTo(1550, 560, 0.1)
    Click()


def Obyn():
    pyautogui.moveTo(1700, 200, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1000, 448, 0.1)
    Click()


def Dart():
    pyautogui.moveTo(1800, 200, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(550, 475, 0.1)
    Click()


def Sniper1():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 530, 0.1)
    Click()
    time.sleep(0.3)


def Sniper1Loc():
    pyautogui.moveTo(1460, 530, 0.1)
    Click()


def Sniper2():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 590, 0.1)
    Click()
    time.sleep(0.3)


def Sniper2Loc():
    pyautogui.moveTo(1460, 590, 0.1)
    Click()


def Sniper3():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 470, 0.1)
    Click()
    time.sleep(0.3)


def Sniper3Loc():
    pyautogui.moveTo(1460, 470, 0.1)
    Click()


def Sniper4():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 410, 0.1)
    Click()
    time.sleep(0.3)


def Sniper5():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 650, 0.1)
    Click()
    time.sleep(0.3)


def Sniper6():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 710, 0.1)
    Click()
    time.sleep(0.3)


def Sniper7():
    pyautogui.moveTo(1800, 630, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1460, 350, 0.1)
    Click()
    time.sleep(0.3)


def Path1():
    pyautogui.moveTo(350, 480, 0.1)
    Click()


def Path2():
    pyautogui.moveTo(350, 630, 0.1)
    Click()


def Path3():
    pyautogui.moveTo(350, 780, 0.1)
    Click()


while SAFETY != 2:
    time.sleep(2)
    pyautogui.moveTo(790, 990, 0.1)
    Click()
    pyautogui.moveTo(1300, 990, 0.1)
    Click()
    time.sleep(0.3)
    Click()
    pyautogui.moveTo(700, 350, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(1250, 500, 0.1)
    Click()
    time.sleep(0.3)
    pyautogui.moveTo(600, 600, 0.1)
    Click()
    time.sleep(3)
    Obyn()
    Dart()
    time.sleep(0.5)
    Start()
    Bramble(15)
    Sniper1()
    Bramble(10)
    Sniper1Loc()
    Path3()  # upgrade to faster shooting, sniper 1
    Bramble(25)
    Path3()  # upgrade to even faster, sniper 1
    Bramble(15)
    Path2()  # upgrade to camo, sniper 1
    Bramble(15)
    Path2()  # upgrade to shrapnel, sniper 1
    Bramble(20)
    Sniper2()  # maim moab sniper
    Sniper2Loc()
    Bramble(20)
    Path3()  # faster moab sniper 2
    Bramble(10)
    Path3()  # even faster moab sniper 2
    Bramble(10)
    Path1()  # fmj moab sniper 2
    Tab()
    Bramble(17)
    Path1()  # large caliber moab sniper 2
    Bramble(65)
    Sniper1Loc()
    Path3()  # semi auto sniper 1
    Bramble(40)
    Sniper2Loc()
    Path1()  # deadly moab sniper 2
    Bramble(2)
    Sniper3()
    Click()
    Bramble(5)
    Path3()
    Bramble(2)
    Path3()
    Bramble(2)
    Path2()
    Bramble(2)
    Path2()
    Bramble(25)
    Path3()  # semi auto sniper 3
    Bramble(25)
    Path3()  # full auto sniper 3
    Sniper2Loc()
    Bramble(40)
    Path1()  # cripple moab sniper 2
    Sniper1Loc()
    Bramble(19)
    Path3()  # full auto sniper 1
    Bramble(7)
    Village()
    VillageLoc()
    Path1()
    Path1()
    Bramble(4)
    Sniper4()
    Click()
    Path3()
    Path3()
    Bramble(3)
    Path2()
    Path2()
    Bramble(20)
    Path3()
    Bramble(25)
    Path3()
    time.sleep(3)
    Sniper5()  # 8:30
    Click()
    Path3()
    Path3()
    time.sleep(5)
    Path2()
    Path2()
    time.sleep(10)
    Path3()  # 17:23
    time.sleep(41)
    Bramble(7)
    Path3()
    Bramble(10)
    Sniper6()
    Click()
    Path3()
    Path3()
    Bramble(5)
    Path2()
    Path2()
    Bramble(15)
    Path3()
    Bramble(55)
    Path3()
    Sniper7()
    Click()
    Path3()
    Path3()
    Bramble(5)
    Path2()
    Path2()
    Bramble(10)
    Path3()
    Bramble(55)
    Path3()
    Bramble(60)
    VillageLoc()
    Path2()
    Path2()
    Bramble(73)  # 63 ish seconds
    im = ImageGrab.grab(bbox=(700, 400, 800 + 480, 500 + 80))
    im.save("defeat.png")
    image = cv2.imread('defeat.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text2 = pytesseract.image_to_string(gray)
    if text2 == "DEFCAT,\n":
        pyautogui.moveTo(750, 750, 0.1)
        Click()
        print("yes")
        time.sleep(1)
    time.sleep(1)
    pyautogui.moveTo(950, 900, 0.1)
    Click()
    time.sleep(1)
    pyautogui.moveTo(820, 830, 0.1)
    Click()
    time.sleep(1)
    pyautogui.moveTo(900, 660, 0.1)
    Click()
    time.sleep(1)
    pyautogui.moveTo(850, 560, 0.1)
    Click()
    time.sleep(1)
    Click()
    pyautogui.moveTo(1150, 560, 0.1)
    Click()
    time.sleep(1)
    Click()
    time.sleep(1)
    PressKey(esc)
    ReleaseKey(esc)
    time.sleep(1)
    pyautogui.moveTo(850, 700, 0.1)
    Click()

# im1 = Image.open('level.PNG')
# im = ImageGrab.grab(bbox=(840, 550, 840 + 255, 550 + 57))  # (x, moves top left corner of photo vertically, length, lower value decreases vertical seen) first 2 values have to be less than last 2 values?
# im.save("level2.PNG")
# i = 1

# a = cv2.imread("level.PNG")
# b = cv2.imread("level2.PNG")
# difference = cv2.subtract(a, b)
# result = not np.any(difference)
# if result is True:
#     print("Pictures are the same")
# else:
#     cv2.imwrite("ed.jpg", difference)
#     print("Pictures are different, the difference is stored as ed.jpg")

# while i != 2:
#     time.sleep(2)
#     # im1.show()
#     i = i + 1
# #     if im1 == im:
# #         print("yes")
# #         exit()
#
#     else:
#         print("no")
#         exit()
