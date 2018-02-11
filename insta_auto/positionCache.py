import pyautogui

class positionCache():

    def __init__(self,img = None):
        self.img = img;
        
        self.minX = 960;
        self.maxX = 960;          
        self.minY = 540;
        self.maxY = 540;

        
    # return cache position
    def getCacheRange(self):
        return (self.minX,self.minY,
                self.maxX,self.maxY);

    def __str__(self):
        return self.img+" :: ("+str(self.minX)+","+str(self.minY)+") :: ("+str(self.maxX)+","+str(self.maxY)+")";
        

    # update cache position
    def update(self,topLeftX = 0, topLeftY = 0, rangeX = 0, rangeY = 0):
        if(self.minX > topLeftX):
            self.minX = topLeftX;
        if(self.minY > topLeftY):
            self.minY = topLeftY;
            
        if(self.maxX < (topLeftX + rangeX)):
            self.maxX = topLeftX + rangeX;
        if(self.maxY < (topLeftY + rangeY)):
            self.maxY = topLeftY + rangeY;



    # locate the img on screen
    def locateOnScreen(self, img = None):

        # init position 
        position = None;

        # param check
        if(img != None and img):
            self.img = img;
        elif((img == None or img) and
             (self.img == None or self.img)):
            raise Exception("Error: No image provided in positionCache to locate on screen");
        
        # search img with cache region
        try:
            position = pyautogui.locateOnScreen(self.img,
                                                region = (self.minX, self.minY,
                                                          self.maxX, self.maxY));
        except Exception as e:
            raise Exception("Error: locating img :"+str(e));

        
        # search complete screeen if cache reguib did not work
        if(position == None):
            try:
                position = pyautogui.locateOnScreen(self.img);
            except Exception as e:
                raise Exception("Error: locating img :"+str(e));
            
        # if position found, update cache
        if(position != None):
            self.update(topLeftX = position[0], topLeftY = position[1],
                        rangeX = position[2], rangeY = position[3]);

        # return position
        return position;
        
