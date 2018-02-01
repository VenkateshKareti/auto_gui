
from insta_auto import insta_auto_api as insta
from firefox_auto import firefox_auto_api as firefox
from auto_gui_utils import auto_gui_utils_api as utils
from gnome_auto import gnome_auto_api as gnome

import time
import pyautogui
import random


pyautogui.FAILSAFE = True;
pyautogui.PAUSE = 2;

instaNextImageDelay = 2;
webPageLoadingDelay = 10;

top_tags =  ['love', 'instagood', 'me', 'cute', 'tbt', 'photooftheday', 'instamood', 'iphonesia', 'tweegram', 'picoftheday', 'igers', 'girl', 'beautiful', 'instadaily', 'summer', 'instagramhub', 'iphoneonly', 'follow', 'igdaily', 'bestoftheday', 'happy', 'picstitch', 'jj', 'sky', 'nofilter', 'fashion', 'followme', 'fun', 'sun'];

top_photo_tags = ['photography', 'photo', 'photos', 'tagsblender', 'pic', 'pics', 'art', 'artist', 'artistic', 'artists', 'arte', 'dibujo', 'myart', 'artwork', 'color', 'all_shots', 'exposure', 'composition', 'focus', 'capture', 'classical', 'clean', 'beautiful', 'perfect', 'shiny', 'amazing', 'best', 'colorful', 'illustration' ];

top_tags_max_index = len(top_photo_tags)-1;


def start_liking(max_images = 50, fail_limit = 10):
    fail_count = 0;
    image_count = 0;
    try:
        while ((fail_count < fail_limit) and
               (image_count < max_images)):
            # like current image
            if(random.choice([True,False])): # like or not to like!
                ret_val = insta.likeImage();
                if(ret_val == None or ret_val == False):
                    fail_count += 1;
                    # continue to next image.
            # go to next Image
            ret_val = insta.nextImage();
            if(ret_val == None or ret_val == False):
                fail_count += 1;
                continue;
            time.sleep(instaNextImageDelay);    # wait for next image
            
            image_count += 1;
            fail_count = 0;
    except Exception as e:
        return None;

    # return status
    if(fail_count >= fail_limit):
        return False;
    else:
        return True;




def start_browsing_images(max_images = 50, fail_limit = 10):
    fail_count = 0;
    image_count = 0;
    try:
        while ((fail_count < fail_limit) and
               (image_count < max_images)):
            
            # go to next Image
            ret_val = insta.nextImage();
            if(ret_val == None or ret_val == False):
                fail_count += 1;
                continue;
            time.sleep(instaNextImageDelay);    # wait for next image and stay on image for a while!
            utils.randomDelay(minSec = 0, maxSec = 5);
            
            image_count += 1;
            fail_count = 0;
    except Exception as e:
        return None;

    # return status
    if(fail_count >= fail_limit):
        return False;
    else:
        return True;

        


def selectRandomTopTag():
    index = random.randint(0,top_tags_max_index);
    return top_photo_tags[index];


def logScreenshot():
    pyautogui.screenshot("a.jpg");
    


# ==========START=========
time.sleep(3);



# initialize insta config data.
try:
    retVal = insta.init_InstaAutoConfigData(display_resolution = 1080,
                                            retry_limit = 7,
                                            retry_delay = 1);
except Exception as e:
    raise Exception("Error: initializing insta config data ::"+
                    str(e));
if(retVal == False):
    raise Exception("Error: initializing insta config data!");

    



# start insta activity
while(True):
    # get hashTag link
    # hashTag = "landscape";
    hashTag = selectRandomTopTag();
    hashTag_link = insta.getHashTagLink(tag = hashTag);
    if(hashTag_link == None or hashTag_link == False):
        print("ERROR: Getting hashTag-link");
        continue;

    # open hashTag link in firefox
    ret_val = firefox.openLink(link = hashTag_link);
    if(ret_val == None or ret_val == False):
        print("ERROR: Opening '"+hashTag_link+"' link in firefox");
        continue;
    time.sleep(webPageLoadingDelay);  # wair for page to load
    
    # open first image
    ret_val = insta.clickLatestPic();
    if(ret_val == None or ret_val == False):
        print("ERROR: Startig exploring lastest image!");
        continue;


    # if(random.choice([True,False])):
    #     # Start Browsing
    #     ret_val = start_browsing_images(max_images = 10, fail_limit = 4);
    #     if(ret_val == None or ret_val == False):
    #         print("Browsing Error! Continuing");
    #         continue;

    # else:
    # Start Liking
    ret_val = start_liking(max_images = 10, fail_limit = 4);
    if(ret_val == None or ret_val == False):
        print("Returned NONE!");
        continue;


    
