import pyautogui
import time
import sys

# sys.path.insert(0,'../');

from firefox_auto import firefox_auto_api


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
def logMessage(fileName = "insta.log",msg = ""):
    if(logMessageFileObj == None):
        logMessageFileObj = open(fileName);
        pass;

    logMessageFileObj.write(msg);
        


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
            return False;

        # go two pages down
        ret_val = firefox_auto_api.goPageDown(noOfPages = noOfPagesDownsForLatestPic);
        if(ret_val == None or ret_val == False):
            return False;
        
        # click on possible first image
        pyautogui.click(firstLatestImageLocationX, firstLatestImageLocationY);
        
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
            return False;
        
    except Exception as e:
        return None;
    
    return True;





nextIMG_positionCache = None;
def isNextImage():
    global nextIMG_positionCache;
    try:
        nextIMG_position = pyautogui.locateOnScreen(nextImage_ICON);
    except Exception as e:
        return None;
    return nextIMG_position;




prevIMG_positionCache = None;
def isPrevImage():
    global prevIMG_positionCache;
    
    try:
        prevIMG_position = pyautogui.locateOnScreen(prevImage_ICON);
    except Exception as e:
        return None;
    return prevIMG_position;
    




like_positionCache = None;
def likeImage():
    global like_positionCache;
    
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




liked_positionCache = None;
def isLiked():
    global liked_positionCache;
    
    try:
        liked_position = pyautogui.locateOnScreen(likedImage_ICON);
        if(liked_position == None):
            return False;
    except Exception as e:
        return None;
    
    return True;




nextIMG_positionCache = None;
def nextImage():
    global nextIMG_positionCache;
    
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

