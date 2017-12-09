import pyautogui
import time
import sys

# sys.path.insert(0,'../');

from firefox_auto import firefox_auto_api


pyautogui.FAILSAFE = True;
pyautogui.PAUSE = 0.01;


nextImage_ICON = 'data/images/insta_NextImage_disp800x600_2122017.png';
prevImage_ICON = 'data/images/insta_PrevImage_disp800x600_2122017.png';
likeImage_ICON = 'data/images/insta_Like_disp800x600_2122017.png';
likedImage_ICON = 'data/images/insta_Liked_disp800x600_2122017.png';
topPosts_ICON = 'insta_TopPosts_disp800x600_2122017.png';

retry_limit = 7;
retry_delay = 1;

def clickLatestPic():  
    try:
        # go to home/start of page
        ret_val = firefox_auto_api.goToTopOfPage();
        if(ret_val == None or ret_val == False):
            return False;

        # go two pages down
        ret_val = firefox_auto_api.goPageDown(noOfPages = 2);
        if(ret_val == None or ret_val == False):
            return False;
        
        # click on possible first image
        # pyautogui.click(127, 531); # 800x600 
        pyautogui.click(333, 543); # 1366x768 (16:9)
        
        # wait till the image loads
        count = 0;
        while(count < retry_limit):
            xy = isNextImage();
            if(xy == None):        
                time.sleep(retry_delay);
            else:
                break;
            count += 1;
        
    except Exception as e:
        return None;
    
    return True;






def isNextImage():
    try:
        nextIMG_position = pyautogui.locateOnScreen(nextImage_ICON);
    except Exception as e:
        return None;
    return nextIMG_position;





def isPrevImage():
    try:
        prevIMG_position = pyautogui.locateOnScreen(prevImage_ICON);
    except Exception as e:
        return None;
    return prevIMG_position;
    





def likeImage():
    try:
        # get like icon position
        like_position = pyautogui.locateOnScreen(likeImage_ICON);
        if(like_position == None):
            # no like icon found
            return False;
        else:
            # click like
            pyautogui.click(like_position[0]+10, like_position[1]+10);
            # confirm liked
            if(isLiked() == None or isLiked() == False):
                return False;
    except Exception as e:
        return None;

    return True;





def isLiked():
    try:
        liked_position = pyautogui.locateOnScreen(likedImage_ICON);
        if(liked_position == None):
            return False;
    except Exception as e:
        return None;
    
    return True;




def nextImage():
    try:
        nextIMG_position = pyautogui.locateOnScreen(nextImage_ICON);
        if(nextIMG_position == None):
            return False;
        else:
            pyautogui.click(nextIMG_position[0]+5,nextIMG_position[1]+5);
    except Exception as e:
        return None;
    return True;







def getHashTagLink(tag = None):
    if(tag == None):
        return None;
    
    link = "https://www.instagram.com/explore/tags/"+tag+"/";
    
    return link;

