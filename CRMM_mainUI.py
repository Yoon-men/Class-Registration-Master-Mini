from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QLabel, QLineEdit, QTreeWidget, QAbstractItemView
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt

from webbrowser import open as webBrowserOpen


class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()
        self.signal()
    
    def mainUI(self) : 
        # basic_part
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(837, 612)
        self.setWindowTitle("Class_Registration_Master_Mini_v1.0")
        self.setWindowIcon(QIcon("CRMM.ico"))

        self.superBody_frm = QFrame(self)
        self.superBody_frm.setGeometry(0, 0, 837, 612)
        self.superBody_frm.setStyleSheet("QFrame{\n"
                                            "background-color : #131514;\n"
                                        "}")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(6, 6, 826, 601)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #131514;\n"
                                        "border : 4px solid #8a2c2c;\n"
                                    "}")

        self.github_bt = QPushButton(self.body_frm)
        self.github_bt.setGeometry(14, 13, 40, 40)
        self.github_bt.setStyleSheet("QPushButton{\n"
                                        "border-radius : 10px;\n"
                                        "image : url(:/img/github_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/github_bt_hover.png);\n"
                                    "}")

        self.addSubject_lb = QLabel(self.body_frm)
        self.addSubject_lb.setGeometry(142, 121, 540, 50)
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
        self.subjectName_le.setGeometry(151, 131, 239, 30)
        self.subjectName_le.setFont(QFont("굴림", 12))
        self.subjectName_le.setStyleSheet(le_styleSheet)
        self.subjectName_le.setPlaceholderText("(교과목명)")

        self.subjectCode_le = QLineEdit(self.body_frm)
        self.subjectCode_le.setGeometry(396, 131, 180, 30)
        self.subjectCode_le.setFont(QFont("굴림", 12))
        self.subjectCode_le.setStyleSheet(le_styleSheet)
        self.subjectCode_le.setPlaceholderText("(교과목코드)")

        self.addSubject_bt = QPushButton(self.body_frm)
        self.addSubject_bt.setGeometry(582, 131, 91, 30)
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
        self.subjectBox_tw.setGeometry(142, 179, 541, 301)
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
        self.subjectBox_tw.setDragDropMode(QAbstractItemView.DragDrop)
        self.subjectBox_tw.setDefaultDropAction(Qt.MoveAction)

        self.subjectBin_bt = QPushButton(self.body_frm)
        self.subjectBin_bt.setGeometry(688, 440, 41, 41)
        self.subjectBin_bt.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/subjectBin_bt_normal.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/subjectBin_bt_hover.png);\n"
                                        "}")

        self.subjectSave_bt = QPushButton(self.body_frm)
        self.subjectSave_bt.setGeometry(688, 394, 41, 41)
        self.subjectSave_bt.setStyleSheet("QPushButton{\n"
                                                "image : url(:/img/subjectSave_bt_normal.png);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "image : url(:/img/subjectSave_bt_hover.png);\n"
                                            "}")

        self.savePoint_lb = QLabel(self.body_frm)
        self.savePoint_lb.setGeometry(735, 410, 8, 8)
        self.savePoint_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/savePoint.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.savePoint_lb.hide()

        self.activate_bt = QPushButton(self.body_frm)
        self.activate_bt.setGeometry(471, 536, 341, 51)
        self.activate_bt.setStyleSheet("QPushButton{"
                                            "image : url(:/img/activate_bt_normal.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/activate_bt_hover.png);\n"
                                        "}")
        global activeFlag
        activeFlag = 0

        self.deactivate_bt = QPushButton(self.body_frm)
        self.deactivate_bt.setGeometry(471, 536, 341, 51)
        self.deactivate_bt.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/deactivate_bt_normal.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/deactivate_bt_hover.png);\n"
                                        "}")
        self.deactivate_bt.hide()

        error_bt_styleSheet = ("QPushButton{\n"
                                    "image : url(:/img/finale_notPrepared_bt_normal.png);\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                    "image : url(:/img/finale_notPrepared_bt_hover.png);\n"
                                "}")

        self.subjectError_lb = QLabel(self.superBody_frm)
        self.subjectError_lb.setGeometry(138, 106, 561, 401)
        self.subjectError_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/subjectError_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.subjectError_lb.hide()

        self.subjectError_bt = QPushButton(self.superBody_frm)
        self.subjectError_bt.setGeometry(154, 441, 529, 53)
        self.subjectError_bt.setStyleSheet(error_bt_styleSheet)
        self.subjectError_bt.hide()

        self.maxedOutError_lb = QLabel(self.superBody_frm)
        self.maxedOutError_lb.setGeometry(138, 106, 561, 401)
        self.maxedOutError_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/maxedOutError_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.maxedOutError_lb.hide()

        self.maxedOutError_bt = QPushButton(self.superBody_frm)
        self.maxedOutError_bt.setGeometry(154, 441, 529, 53)
        self.maxedOutError_bt.setStyleSheet(error_bt_styleSheet)
        self.maxedOutError_bt.hide()



    def signal(self) : 
        self.github_bt.clicked.connect(self.openGithub)

        self.activate_bt.clicked.connect(self.buttonSwap)
        self.deactivate_bt.clicked.connect(self.buttonSwap)

        self.subjectError_bt.clicked.connect(self.returnToMain_subjectError)
        self.maxedOutError_bt.clicked.connect(self.returnToMain_maxedOutError)



    def openGithub(self) : 
        webBrowserOpen("https://github.com/Yoon-men/Class_Registration_Master_Mini")



    def buttonSwap(self) : 
        global activeFlag
        if not activeFlag : 
            activeFlag = 1
            self.activate_bt.hide()
            self.deactivate_bt.show()
        else : 
            activeFlag = 0
            self.deactivate_bt.hide()
            self.activate_bt.show()



    def returnToMain_subjectError(self) : 
        self.subjectError_lb.hide()
        self.subjectError_bt.hide()
        self.body_frm.show()



    def returnToMain_maxedOutError(self) : 
        self.maxedOutError_lb.hide()
        self.maxedOutError_bt.hide()
        self.body_frm.show()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())
