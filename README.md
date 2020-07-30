# Phantom_Automation_App
Phantom List is a desktop Application for automating a sequence of instruction for mouse and keyboard using Python, PyAutoGui module and PyQt5 GUI framework. The initial idea was inspired by ghost mouse where a user can record mouse information and play it back. Having used PyAutoGui to automate tasks, I wanted to create a program using the PyAutoGui module and create a user interface with PyQt5 so that someone without knowledge of python would be able to use it. During the development I have tried to minimize the amount of button and windows to create a more simpler and minimalistic look.
<img src= "https://github.com/karlduggan/Phantom_Automation_App/blob/master/screenshot.png">

## Capture
	To capture the position of your mouse, using the shortcut key "Ctrl + A" input the position data 
	along with mouse button option into the list which will appear in the list window.

## Mouse Buttons 
	There are currently three boxes to choose through when selection mouse button action.
		1. Double click: To open folders / shortcut " Ctrl + Q "
		2. Left click: For selecting / shortcut " Ctrl + W "
		3. Right click: Options / shortcut " Ctrl + E "
	It is important to note that if you intend on actioning a mouse button,
	please make sure that the selection is checked before pressing Capture. 

## Play
	Once your sequence of automated instruction is complete,
	pressing Play will run through and action chronologically.

## Delete
	To delete, select item from list and press Delete. 
	The selection will be removed and the index order will be adjusted.
## Add
	Pressing Add will initiate a pop-up to appear where the user will be able to manually 
	write the input to be added to the list.
	It is important that the input written correctly with comas separating each section.
	Example: int,int,str,str,str = 100,150,True,False,False
	
	The five section correlate as follows x position, y position, Double Click, Left Click, Right Click.
## Clear
	Pressing Clear will erase all inputs that appear in the list and on memory.

## Save Files
	The Save function will allow you to save your project where ever you like via pop-up window.

## Load Files
	The Load function will allow you to open and load previous automation list so that it can be run again or edited.

## Text Input
	The text line edit appears at the bottom of the programs window, If kept blank, text automation will not be activated, 
	if text has been entered it will be written when Capture is selected.

