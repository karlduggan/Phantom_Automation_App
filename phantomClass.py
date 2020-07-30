import pyautogui as p
from threading import Thread
import time 

class Phantom(object):
    def __init__(self):
        self.active = False
        self.data_list = []
        self.speed = 0.1
        self.sleep = 3
 
        # The atributes will feeds out to the gui framework
        self.xpos = 0
        self.ypos = 0
    
    # Used for saving data
    def get_dataList(self):
        return self.data_list
    
    # Used for loading data
    def set_datalist(self, data):
        self.data_list = data
        
    def get_activeStatus(self):
        return self.active
    
    # Clear data list
    def clear_datalist(self):
        self.data_list = []
    
    # Undo previous entry
    def undo_datalist(self):
        if self.data_list != []:
            index = len(self.data_list) -1
            self.data_list.pop(index)
        else:
            return False
    
    # Entry number / x position / y position / double left click / left click / right click / text
    def insert_data(self, xpos, ypos, dclk=False, lclk=False, rclk=False, text=None):
        entry_num = len(self.data_list)
        self.data_list.append([entry_num,xpos,ypos,dclk,lclk,rclk,text])
    
    def setAuto_speed(self, num):
        self.speed = num
        
    def read_data(self):
        if self.data_list == []:
            return None
        else:
            for i in range(len(self.data_list)):
                print(self.data_list[i])
                
    # Run automation using pyautogui
    def runAuto(self):
        
        time.sleep(0.3)
        if len(self.data_list) > 0:
            self.active = True
            
            index = 0
            while self.active and index < len(self.data_list):
                
                # Position automation check
                xpos = self.data_list[index][1]
                ypos = self.data_list[index][2]
                p.moveTo(xpos,ypos, 0.2)
                
                # Check Double click Boolean 
                if self.data_list[index][3] == True:
                    p.doubleClick()
                    
                # Check Left click Boolean
                if self.data_list[index][4] == True:
                    p.click(button='left')
                
                # Check right click Boolean
                if self.data_list[index][5] == True:
                    p.click(button='right')
                
                # Check Text is not equal to None
                if self.data_list[index][6] != None:
                    p.typewrite(str(self.data_list[index][6]))
                 
                index += 1
         
    # Implemented threading to process separately for multiprocessing 
    def runAutoThread(self):
        x = Thread(target=self.runAuto)
        x.start()
        x.join()
   
    # Need to iterate through the function to get output due to the yield
    def __tracking(self):
            while self.active == True:
                # Gets the position of the mouse in a tuple 
                pos = p.position()
                xpos = pos[0]
                ypos = pos[1]
                # Update time every 0.3 second
                time.sleep(self.speed)
                yield xpos, ypos 

    # Iterate through the yield object 
    def _tracking(self):
        for xpos, ypos in self.__tracking():
            # Update the position attributes
            self.update_XY(xpos,ypos)
            # Print in the terminal for confirmation
            print(xpos, ypos)
            
    # Preparing Threading for multiprocessing, The Threading will be activated on main.py
    # The function below allows a stop / start action
    def startTracking(self):
        if self.active == False:
            self.active = True
            self._tracking()
        else:
            self.active = False
        
    # Gets all required information and the passes to insert_data method
    def capture(self, dclk, lclk, rclk, text):
        # Get position
        pos = p.position()
        xpos = pos[0]
        ypos = pos[1]
        
        self.insert_data(xpos,ypos,dclk,lclk,rclk,text)
    
    def changeActive(self, value):
        self.active = value
    
    def update_XY(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    # Delete item from list function
    def delete_datalist(self, item):
        # Get the index value from the selection
        index = int(item[1])
        # Position within the list
        position = None
        # Iterate through the data list to find matching index
        for i in range(len(self.data_list)):
            itemx = self.data_list[i]
            if itemx[0] == index:
                position = i
        # Using the pop method to remove the item at postion in list
        self.data_list.pop(position)
        
        # Update the list index from 0 till length of list
        num = 0
        for index in self.data_list:
            index[0] = num
            num += 1

    # Convert added input into the data list
    def addConvert(self, input):
        inputSpl = input.split(',')
        # Get X & Y position
        xpos = int(inputSpl[0])
        ypos = int(inputSpl[1])
        # Get boolean input by converting it from string
        dclk = self.getBool(inputSpl[2])
        lclk = self.getBool(inputSpl[3])
        rclk = self.getBool(inputSpl[4])
        # Text input will equal none
        text = None
        # Add these values into the data list
        self.insert_data(xpos,ypos,dclk,lclk,rclk,text)
        
            
    # To convert str to boolean
    def getBool(self, value):
        if value.lower() == 'true':
            return True
        if value.lower() =='false':
            return False

if __name__ == "__main__":
    main = Phantom()
    
