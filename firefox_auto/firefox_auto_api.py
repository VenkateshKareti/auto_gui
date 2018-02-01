import pyautogui

pyautogui.FAILSAFE = True;
pyautogui.PAUSE = 2;


def openLink(link = None):
    if(link == None):
        return None;

    try:
        pyautogui.hotkey('ctrl','l');
        pyautogui.typewrite(link,interval = 0.01);
        pyautogui.press('enter');
    except Exception as e:
        print(e);
        return None;
    
    return True;


def refreshPage():
    try:
        pyautogui.hotkey('ctrl','r');
    except Exception as e:
        return None;
    
    return True;

def goToTopOfPage():
    try:
        pyautogui.press('home');
    except Exception as e:
        return None;

    return True;

def goPageDown(noOfPages = 1):
    if(noOfPages == None or noOfPages == 0):
        return False;
    
    try:
        for i in range(noOfPages):
            pyautogui.press('pagedown');
    except Exception as e:
        return None;

    return True;
