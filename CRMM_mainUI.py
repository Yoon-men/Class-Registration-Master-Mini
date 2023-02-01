from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QRadioButton, QLabel, QButtonGroup, QLineEdit, QLCDNumber, QCheckBox, QTreeWidget, QAbstractItemView, QComboBox
from PySide2.QtGui import QFont, QIntValidator, QMovie, QIcon
from PySide2.QtCore import Qt, QEvent, QByteArray

import webbrowser


class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()
        self.signal()
    
    def mainUI(self) : 
        # basic_part
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(836, 611)
        self.setWindowTitle("Class_Registration_Master_Mini_v1.0")
        self.setWindowIcon(QIcon("CRM.ico"))                 # Test code / please modify the contents of this line.


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(5, 5, 826, 601)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #131514;\n"
                                        "border : 4px solid #8a2c2c;\n"
                                    "}")

        self.addSubject_lb = QLabel(self.body_frm)
        self.addSubject_lb.setGeometry(142, 131, 540, 50)
        self.addSubject_lb.setStyleSheet("QLabel{\n"
                                            "border : 3px solid #8a2c2c;\n"
                                            "background-color : #131514;\n"
                                        "}")

        le_styleSheet = ("QLineEdit{\n"
                            "color : #dddddd;\n"
                            "background-color : #232323;\n"
                            "border : 2px solid #8a2c2c;\n"
                            "selection-color : #000000;\n"
                            "selection-background-color : #ffffff;\n"
                        "}\n"
                        "QLineEdit:focus{\n"
                            "border-color : #e14f50;\n"
                        "}")

        self.subjectName_le = QLineEdit(self.body_frm)
        self.subjectName_le.setGeometry(151, 141, 239, 30)
        self.subjectName_le.setFont(QFont("굴림", 12))
        self.subjectName_le.setStyleSheet(le_styleSheet)
        self.subjectName_le.setPlaceholderText("(교과목명)")

        self.subjectCode_le = QLineEdit(self.body_frm)
        self.subjectCode_le.setGeometry(396, 141, 180, 30)
        self.subjectCode_le.setFont(QFont("굴림", 12))
        self.subjectCode_le.setStyleSheet(le_styleSheet)
        self.subjectCode_le.setPlaceholderText("(교과목코드)")

        self.addSubject_bt = QPushButton(self.body_frm)
        self.addSubject_bt.setGeometry(582, 141, 91, 30)
        self.addSubject_bt.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.addSubject_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #8a2c2c;\n"
                                            "background-color : #131514;\n"
                                            "color : #ffffff;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                            "background-color : #e14f50;\n"
                                            "color : #000000;\n"
                                        "}")
        self.addSubject_bt.setText("추가")
        self.addSubject_bt.setFocusPolicy(Qt.NoFocus)

        self.subjectBox_tw = QTreeWidget(self.body_frm)
        self.subjectBox_tw.setGeometry(142, 189, 541, 301)
        self.subjectBox_tw.setFont(QFont("나눔고딕OTF", 13, QFont.Bold))
        self.subjectBox_tw.setStyleSheet("QTreeWidget{\n"
                                                "border : 3px solid #8a2c2c;\n"
                                                "background-color : #131514;\n"
                                                "color : #ffffff;\n"
                                            "}\n"

                                            "QHeaderView{\n"
                                                "border : 0px;\n"
                                            "}\n"
                                            "QHeaderView::section{\n"
                                                "border : 1px solid #8a2c2c;\n"
                                                "background-color : #642223;\n"
                                                "font-family : 나눔고딕OTF;\n"
                                                "font-weight : bold;\n"
                                                "font-size : 13pt;\n"
                                                "color : #ffffff;\n"
                                            "}\n"

                                            "QTreeWidget::item::selected{\n"
                                                "background-color : #434343;\n"
                                                "color : #ffffff;\n"
                                            "}\n"
                                            "QTreeWidget::item::hover{\n"
                                                "background-color : #434343;\n"
                                            "}\n"

                                            "QTreeView::branch:has-children:!has-siblings:closed,\n"
                                            "QTreeView::branch:closed:has-children:has-siblings{\n"
                                                "border-image : none;\n"
                                                "image : url(:/img/branch_closed.png);\n"
                                            "}\n"
                                            "QTreeView::branch:open:has-children:!has-siblings,\n"
                                            "QTreeView::branch:open:has-children:has-siblings{\n"
                                                "border-image : none;\n"
                                                "image : url(:/img/branch_open.png);\n"
                                            "}")
        self.subjectBox_tw.setHeaderLabels(["교과목명", "교과목코드", "단축키"])
        self.subjectBox_tw.header().resizeSection(0, 200)
        self.subjectBox_tw.header().resizeSection(1, 190)
        self.subjectBox_tw.header().resizeSection(2, 100)
        self.subjectBox_tw.setFocusPolicy(Qt.NoFocus)




    def signal(self) : 
        pass                # Test code / please delete the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())