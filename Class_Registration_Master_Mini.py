'''
======================================================================================
                       < Class_Registration_Master_Mini_v1.0.1 >

'수강신청 마스터'를 사용해 나머지 99%의 사람들에게 당신과의 격차를 확실히 느끼게 해주십시오.

                                 * Made by Yoonmen *

                                - 23.2.8 (WED) 03:51 -
======================================================================================
'''

import sys
from PySide2.QtWidgets import QApplication, QTreeWidgetItem
from PySide2.QtCore import QThread, QObject, QEvent, Qt
from collections import deque
from keyboard import is_pressed
from pyperclip import copy
from pyautogui import hotkey

from CRMM_mainUI import MainUI


class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI
        mainUI = MainUI()

        global thread_basicFn, basicFn
        thread_basicFn = QThread()
        thread_basicFn.start()
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)
        
        global thread_keyFn, keyFn
        thread_keyFn = QThread()
        thread_keyFn.start()
        keyFn = KeyFn()
        keyFn.moveToThread(thread_keyFn)

        global subjectData
        subjectData = deque()

        global power
        power = False

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())



    def signal(self) : 
        # << mainUI (1/1) >> --------------------
        # mainUI.subjectCode_le.returnPressed.connect(BasicFn.addSubject)
        mainUI.addSubject_bt.clicked.connect(BasicFn.addSubject)

        mainUI.subjectBox_tw.viewport().installEventFilter(self)

        mainUI.subjectSave_bt.clicked.connect(BasicFn.setSubjectData)
        mainUI.subjectBin_bt.clicked.connect(BasicFn.delSubject)

        mainUI.activate_bt.clicked.connect(keyFn.activate)
        mainUI.deactivate_bt.clicked.connect(basicFn.deactivate)



    def eventFilter(self, object, event) : 
        if object == mainUI.subjectBox_tw.viewport() : 
            if event.type() == QEvent.Drop : 
                mainUI.savePoint_lb.show()
        
        return False




class BasicFn(QObject) : 
    def setSubjectBox(self) : 
        tmp = []
        for data in subjectData : 
            item = QTreeWidgetItem(data)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsEnabled)
            tmp.append(item)
        mainUI.subjectBox_tw.clear()
        mainUI.subjectBox_tw.insertTopLevelItems(0, tmp)



    def addSubject(self) : 
        subjectName, subjectCode = mainUI.subjectName_le.text(), mainUI.subjectCode_le.text()
        if (subjectName == "") or (subjectCode == "") : 
            mainUI.body_frm.hide()
            mainUI.subjectError_lb.show()
            mainUI.subjectError_bt.show()
        else : 
            global subjectData
            if len(subjectData) < 9 : 
                subjectData.append([subjectName, subjectCode, f"ctrl+{len(subjectData)+1}"])
                basicFn.setSubjectBox()
            elif len(subjectData) == 9 : 
                subjectData.append([subjectName, subjectCode, "ctrl+0"])
                basicFn.setSubjectBox()
            else : 
                mainUI.body_frm.hide()
                mainUI.maxedOutError_lb.show()
                mainUI.maxedOutError_bt.show()

            mainUI.subjectName_le.setText(""); mainUI.subjectCode_le.setText("")
            mainUI.savePoint_lb.hide()



    def setSubjectData(self) : 
        global subjectData
        N = mainUI.subjectBox_tw.topLevelItemCount()
        subjectData = [None] * N
        for i in range(N) : 
            item = mainUI.subjectBox_tw.topLevelItem(i)
            subjectData[i] = [item.text(0), item.text(1), f"ctrl+{i+1 if i < 9 else 0}"]

        basicFn.setSubjectBox()
        mainUI.savePoint_lb.hide()



    def delSubject(self) : 
        if mainUI.subjectBox_tw.currentItem() : 
            item = mainUI.subjectBox_tw.currentItem()
            mainUI.subjectBox_tw.takeTopLevelItem(mainUI.subjectBox_tw.indexOfTopLevelItem(item))
        
        basicFn.setSubjectData()



    def deactivate(self) : 
        global power
        power = False




class KeyFn(QObject) : 
    def activate(self) : 
        global power
        power = True
        while power : 
            if   is_pressed("ctrl+1") : copy(subjectData[0][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+2") : copy(subjectData[1][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+3") : copy(subjectData[2][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+4") : copy(subjectData[3][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+5") : copy(subjectData[4][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+6") : copy(subjectData[5][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+7") : copy(subjectData[6][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+8") : copy(subjectData[7][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+9") : copy(subjectData[8][1]); hotkey("ctrl", "v")
            elif is_pressed("ctrl+0") : copy(subjectData[9][1]); hotkey("ctrl", "v")





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
