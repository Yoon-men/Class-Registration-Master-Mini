'''
======================================================================================
                        < Class_Registration_Master_Mini_v1.0 >

'수강신청 마스터'를 사용해 나머지 99%의 사람들에게 당신과의 격차를 확실히 느끼게 해주십시오.

                                 * Made by Yoonmen *

                               - 23.?.?? (???) ??:?? -
======================================================================================
'''

import sys
from PySide2.QtWidgets import QApplication, QTreeWidgetItem
from PySide2.QtCore import QThread, QObject, QEvent
from collections import deque

from CRMM_mainUI import MainUI

class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI
        mainUI = MainUI()

        global thread_basicFn
        thread_basicFn = QThread()
        thread_basicFn.start()
        global basicFn
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)

        global subjectData
        subjectData = deque()

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())



    def signal(self) : 
        # << mainUI (1/1) >> --------------------
        mainUI.subjectCode_le.returnPressed.connect(basicFn.addSubject)
        mainUI.addSubject_bt.clicked.connect(basicFn.addSubject)

        mainUI.subjectSave_bt.clicked.connect(BasicFn.setSubjectData)               # Test code / please delete the contents of this line.
        mainUI.subjectBin_bt.clicked.connect(BasicFn.delSubject)




class BasicFn(QObject) : 
    def setSubjectBox(self) : 
        tmp = [QTreeWidgetItem(data) for data in subjectData]
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



    def setSubjectData(self) : 
        global subjectData
        N = mainUI.subjectBox_tw.topLevelItemCount()
        subjectData = [0 for _ in range(N)]
        for i in range(N) : 
            item = mainUI.subjectBox_tw.topLevelItem(i)
            subjectData[i] = [item.text(0), item.text(1), item.text(2)]



    def delSubject(self) : 
        if mainUI.subjectBox_tw.currentItem() : 
            item = mainUI.subjectBox_tw.currentItem()
            mainUI.subjectBox_tw.takeTopLevelItem(mainUI.subjectBox_tw.indexOfTopLevelItem(item))
        
        basicFn.setSubjectData()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
