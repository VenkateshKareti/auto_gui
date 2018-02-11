import pyautogui
import time
import sys
import datetime

# sys.path.insert(0,'../');

from firefox_auto import firefox_auto_api;
from insta_auto import positionCache;

pyautogui.FAILSAFE = True;
pyautogui.PAUSE = 2;


# insta_auto config data
logMessageFileObj = None;

displayResolution = 1080;       # 1920x1080x32

nextImage_ICON = "";
prevImage_ICON = "";
likeImage_ICON = "";
likedImage_ICON = "";

noOfPagesDownsForLatestPic = 0;
firstLatestImageLocationX = 0;
firstLatestImageLocationY = 0;
pixelRangeForFirstLatestImage = 0;

retryLimit = 7;
retryDelay = 1;


# log screenshot to file
def logScreenshot(fileName = "a.jpg"):
    pyautogui.screenshot(fileName);


# log message to log file
def logMessage(fileName = "insta_auto_api.log",msg = ""):
    global logMessageFileObj;
    
    T = str(datetime.datetime.now());
    
    if(logMessageFileObj == None):
        logMessageFileObj = open(fileName,"a");
    logMessageFileObj.write(T+"::"+msg+"\n");
        


# initialize insta config data
def init_InstaAutoConfigData(display_resolution = 1080,
                             retry_limit = 7,
                             retry_delay = 2):
    
    global displayResolution;

    global nextImage_ICON;
    global prevImage_ICON;
    global likeImage_ICON;
    global likedImage_ICON;

    global noOfPagesDownsForLatestPic;
    global firstLatestImageLocationX;
    global firstLatestImageLocationY;
    global pixelRangeForFirstLatestImage;

    global retryLimit;
    global retryDelay;


    retryLimit = retry_limit;
    retryDelay = retry_delay;

    
    if(displayResolution == 600):
        displayResolution = 600;

        nextImage_ICON = 'data/images/insta_NextImage_disp800x600_2122017.png';
        prevImage_ICON = 'data/images/insta_PrevImage_disp800x600_2122017.png';
        likeImage_ICON = 'data/images/insta_Like_disp800x600_2122017.png';
        likedImage_ICON = 'data/images/insta_Liked_disp800x600_2122017.png';

        noOfPagesDownsForLatestPic = 2;
        firstLatestImageLocationX = 127;
        firstLatestImageLocationY = 531;
        pixelRangeForFirstLatestImage = 20;

    elif(displayResolution == 720):
        displayResolution = 720;

        nextImage_ICON = './data/images/insta_NextImage_disp1280x720_15012018.png';
        prevImage_ICON = './data/images/insta_PrevImage_disp1280x720_15012018.png';
        likeImage_ICON = './data/images/insta_Like_disp1280x720_15012018.png';
        likedImage_ICON = './data/images/insta_Liked_disp1280x720_15012018.png';

        noOfPagesDownsForLatestPic = 2;
        firstLatestImageLocationX = 289;
        firstLatestImageLocationY = 646;
        pixelRangeForFirstLatestImage = 50;

    elif(displayResolution == 1080):
        displayResolution = 1080;

        nextImage_ICON = './data/images/insta_NextImage_disp1280x720_15012018.png';
        prevImage_ICON = './data/images/insta_PrevImage_disp1280x720_15012018.png';
        likeImage_ICON = './data/images/insta_Like_disp1280x720_15012018.png';
        likedImage_ICON = './data/images/insta_Liked_disp1280x720_15012018.png';

        noOfPagesDownsForLatestPic = 1;
        firstLatestImageLocationX = 560;
        firstLatestImageLocationY = 750;
        pixelRangeForFirstLatestImage = 100;

    return True;







def clickLatestPic():
    try:
        # go to home/start of page
        ret_val = firefox_auto_api.goToTopOfPage();
        if(ret_val == None or ret_val == False):
            logMessage(msg = "Error: firefox api failed to go top of the page");
            return False;

        # go two pages down
        ret_val = firefox_auto_api.goPageDown(noOfPages = noOfPagesDownsForLatestPic);
        if(ret_val == None or ret_val == False):
            logMessage(msg = "Error: firefox api failed to go down page for No.of pages :"+str(noOfPagesDownsForLatestPic));
            return False;
        
        # click on possible first image
        try:
            pyautogui.click(firstLatestImageLocationX, firstLatestImageLocationY);
        except Exception as e:
            logMessage(msg = "Error: pyautogui failed to click on first image, err:"+str(e));
            return False;
            
        # wait till the image loads
        count = 0;
        while(count < retryLimit):
            xy = isNextImage();
            if(xy == None):        
                time.sleep(retryDelay);
            else:
                break;
            count += 1;
            
        if(count >= retryLimit):
            logMessage(msg = "Error: Latest Image is not loaded after multiple tries");
            return False;
        
    except Exception as e:
        logMessage(msg = "Error: unknown cause: "+str(e));
        return None;
    
    return True;





nextIMG_positionCache = positionCache.positionCache(img = nextImage_ICON);
def isNextImage():
    global nextIMG_positionCache;
    try:
        # nextIMG_position = pyautogui.locateOnScreen(nextImage_ICON);
        nextIMG_position = nextIMG_positionCache.locateOnScreen(img = nextImage_ICON);
    except Exception as e:
        logMessage(msg = "Error: pyautogui failed to locate next icon to confirm next Image; with err :"+str(e));
        return None;
    return nextIMG_position;




prevIMG_positionCache = positionCache.positionCache(img = prevImage_ICON);
def isPrevImage():
    global prevIMG_positionCache;
    
    try:
        # prevIMG_position = pyautogui.locateOnScreen(prevImage_ICON);
        prevIMG_position = prevIMG_positionCache.locateOnScreen(img = prevImage_ICON);
    except Exception as e:
        logMessage(msg = "Error: pyautogui failed to locate prev-icon to confirm prev image; with err :"+str(e));
        return None;
    return prevIMG_position;
    




like_positionCache = positionCache.positionCache(img = likeImage_ICON);
def likeImage():
    global like_positionCache;
    
    try:
        # get like icon position
        # like_position = pyautogui.locateOnScreen(likeImage_ICON);
        like_position = like_positionCache.locateOnScreen(img = likeImage_ICON);
        if(like_position == None):
            logMessage(msg = "Error: pyautogui failed to locate like icon");
            return False;
        else:
            # click like
            try:
                pyautogui.click(like_position[0]+10, like_position[1]+10);
            except Exception as e:
                logMessage(msg = "Error: pyautogui failed to click like; with err :"+str(e));
                return False;
            # confirm liked
            if(isLiked() == None or isLiked() == False):
                logMessage(msg = "Error: clicking like did not work. like icon did not turn liked!");
                return False;
    except Exception as e:
        logMessage(msg = "Error: unknown error while liking image; with err :"+str(e));
        return None;

    return True;




liked_positionCache = positionCache.positionCache(img = likedImage_ICON);
def isLiked():
    global liked_positionCache;
    
    try:
        # liked_position = pyautogui.locateOnScreen(likedImage_ICON);
        liked_position = liked_positionCache.locateOnScreen(img = likedImage_ICON);
        if(liked_position == None):
            return False;
    except Exception as e:
        logMessage(msg = "Error: pyautogui failed to locate liked icon with err :"+str(e));
        return None;
    
    return True;





def nextImage():
    global nextIMG_positionCache;
    
    try:
        # nextIMG_position = pyautogui.locateOnScreen(nextImage_ICON);
        nextIMG_position = nextIMG_positionCache.locateOnScreen(img = nextImage_ICON);
        if(nextIMG_position == None):
            logMessage(msg = "Error: pyautogui failed to locate next icon");
            return False;
        else:
            pyautogui.click(nextIMG_position[0]+5,nextIMG_position[1]+5);
    except Exception as e:
        logMessage(msg = "Error: unknown error while locating next icon with err :"+str(e));
        return None;
    
    return True;







def getHashTagLink(tag = None):
    if(tag == None):
        logMessage(msg = "Error: no tag passed to generate instagram hash-tag link");
        return None;
    
    link = "https://www.instagram.com/explore/tags/"+tag+"/";
    
    return link;

