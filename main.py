from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from phantomClass import Phantom
from threading import Thread
import pickle


class Ui_Form(object):
    def __init__(self):
        # Phantom Automation class
        self.phantom = Phantom()
        self.trackSwitch = False
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 393)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 7, 2, 1, 1)
        self.pushButton_add.clicked.connect(self.getText)
        
        self.pushButton_delete = QtWidgets.QPushButton(self.widget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 6, 2, 1, 1)
        self.pushButton_delete.clicked.connect(self.deleteAtion)
        
        self.lineEdit_typeText = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_typeText.setText("")
        self.lineEdit_typeText.setObjectName("lineEdit_typeText")
        self.gridLayout.addWidget(self.lineEdit_typeText, 9, 1, 1, 1)
        
        self.label_text = QtWidgets.QLabel(self.widget)
        self.label_text.setObjectName("label_text")
        self.gridLayout.addWidget(self.label_text, 9, 0, 1, 1)
        
        self.pushButton_capture = QtWidgets.QPushButton(self.widget)
        self.pushButton_capture.setObjectName("pushButton_capture")
        self.gridLayout.addWidget(self.pushButton_capture, 0, 2, 1, 1)
        self.pushButton_capture.clicked.connect(self.captureAction)
        
        self.checkBox_doubleClick = QtWidgets.QCheckBox(self.widget)
        self.checkBox_doubleClick.setObjectName("checkBox_doubleClick")
        self.gridLayout.addWidget(self.checkBox_doubleClick, 1, 2, 1, 1)
        
        self.checkBox_leftClick = QtWidgets.QCheckBox(self.widget)
        self.checkBox_leftClick.setObjectName("checkBox_leftClick")
        self.gridLayout.addWidget(self.checkBox_leftClick, 2, 2, 1, 1)
        
        self.checkBox_rightClick = QtWidgets.QCheckBox(self.widget)
        self.checkBox_rightClick.setObjectName("checkBox_rightClick")
        self.gridLayout.addWidget(self.checkBox_rightClick, 3, 2, 1, 1)
        
        self.widget_saveload = QtWidgets.QWidget(self.widget)
        self.widget_saveload.setObjectName("widget_saveload")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_saveload)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButton_save = QtWidgets.QPushButton(self.widget_saveload)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_save.clicked.connect(self.saveFunc)
        
        self.pushButton_load = QtWidgets.QPushButton(self.widget_saveload)
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.pushButton_load.clicked.connect(self.loadFunc)
        
        self.gridLayout.addWidget(self.widget_saveload, 9, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 9, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
    #
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 8, 2, 1, 1)
        self.pushButton_clear.clicked.connect(self.clearAction)
        
        self.pushButton_play = QtWidgets.QPushButton(self.widget)
        self.pushButton_play.setObjectName("pushButton_play")
        self.gridLayout.addWidget(self.pushButton_play, 5, 2, 1, 1)
        self.pushButton_play.clicked.connect(self.playAction)
        
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Phantom List v1.0"))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.pushButton_delete.setText(_translate("Form", "Delete"))
        self.label_text.setText(_translate("Form", "Text :"))
        self.pushButton_capture.setText(_translate("Form", "Capture / Ctrl + A"))
        self.pushButton_capture.setShortcut(_translate("Form", "Meta+A"))
        self.checkBox_doubleClick.setText(_translate("Form", "Double Click / Ctrl + Q"))
        self.checkBox_doubleClick.setShortcut(_translate("Form", "Meta+Q"))
        self.checkBox_leftClick.setText(_translate("Form", "Left Click / Ctrl + W"))
        self.checkBox_leftClick.setShortcut(_translate("Form", "Meta+W"))
        self.checkBox_rightClick.setText(_translate("Form", "Right Click / Ctrl + E"))
        self.checkBox_rightClick.setShortcut(_translate("Form", "Meta+E"))

        self.pushButton_save.setText(_translate("Form", "Save"))
        self.pushButton_load.setText(_translate("Form", "Load"))
        self.pushButton_clear.setText(_translate("Form", "Clear"))
        self.pushButton_play.setText(_translate("Form", "Play"))
        
# Button Functions

    # Update ListWidget with data
    def update_listWidget(self):
        # Clear the listWidget
        
        self.listWidget.clear()
        data = self.phantom.get_dataList()
        for i in data:
            self.listWidget.addItem(str(i))
           
    # Capture and submit data 
    def captureAction(self):
        # return true or false with isChecked()
        
        double_clk = self.checkBox_doubleClick.isChecked()
        left_clk = self.checkBox_leftClick.isChecked()
        right_clk = self.checkBox_rightClick.isChecked()
        
        # Check Text type is check, if yes then collect text
        text = None
        if self.lineEdit_typeText.text() != '':
            text = self.lineEdit_typeText.text()

        
        self.phantom.capture(double_clk,left_clk,right_clk,text)
        # Update the view with new data
        self.update_listWidget()
        # After Submit the checkboxes must be unchecked for the next submission 
        self.checkBox_doubleClick.setChecked(False)
        self.checkBox_leftClick.setChecked(False)
        self.checkBox_rightClick.setChecked(False)
        self.lineEdit_typeText.clear()
    
    # Play Button  play and stop
    def playAction(self):
        # Check that data list is not empty
        if self.phantom.get_dataList() != []:
            self._play()
            
        else:
            print('Data List Empty')
        
    def _play(self):
        # Run automation through Threading
        t = Thread(target=self.phantom.runAuto)
        t.start()
        
    # Save Function 
    def saveFunc(self):
        name = QtWidgets.QFileDialog.getSaveFileName(Form,'Save File')
        filename = name[0]
        with open(filename + '.pkl', 'wb') as file:
            data = self.phantom.get_dataList()
            pickle.dump(data, file)


    # Load Function 
    def loadFunc(self):
        try: 
            name = QtWidgets.QFileDialog.getOpenFileName(Form, 'Open File')
            filename = name[0]
            with open(filename, 'rb') as file:
                
                data = pickle.load(file)
                self.phantom.set_datalist(data)
            
                # Update the list with loaded data
                self.update_listWidget()    
        except:
            return
    
    # Clear data function
    def clearAction(self):
        self.phantom.clear_datalist()
        # Update list widget
        self.update_listWidget()    
    
            
    # Delete selected function
    def deleteAtion(self):
        # Get selected item from list widget
        item = self.listWidget.currentItem().text()
        # Remove the selected item from data list
        self.phantom.delete_datalist(item)
        
        # Update list
        self.update_listWidget()
    
    def getText(self):
        text, okPressed = QInputDialog.getText(Form, "Input Entry","Enter Input: \n\nX postion,\nY position,\nDouble click (True Or False),\nLeft Click (True Or False),\nRight Click (True Or False),\n", QLineEdit.Normal, "")
        if okPressed and text != '':
            try:
                self.phantom.addConvert(text)
            except:
                print('Incorrect input')
        # Update the list
        self.update_listWidget()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
