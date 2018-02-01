import pyautogui

pyautogui.FAILSAFE = True;
pyautogui.PAUSE = 2;


def minimizeWindow():
    try:
        pyautogui.hotkey('winleft','h');
    except Exception as e:
        raise Exception("Error: while hiding window :: "+str(e));

    return True;




def unMaximizeWindow():
    try:
        pyautogui.hotkey('winleft','up');
    except Exception as e:
        raise Exception("Error: while un-Minimizing window :: "+str(e));

    return True;



def maximizeWindow():
    try:
        pyautogui.hotkey('winleft','down');
    except Exception as e:
        raise Exception("Error: while Minimizing window :: "+str(e));

    return True;

        
