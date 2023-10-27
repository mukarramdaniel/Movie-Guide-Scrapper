# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\3rd semester\DSA MID project\cs261f22pid22\advance_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 357)
        Dialog.setStyleSheet("background-color:#d1d1d1;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblTitle = QtWidgets.QLabel(self.frame)
        self.lblTitle.setGeometry(QtCore.QRect(10, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.txtTitle = QtWidgets.QLineEdit(self.frame)
        self.txtTitle.setGeometry(QtCore.QRect(10, 30, 161, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(9)
        self.txtTitle.setFont(font)
        self.txtTitle.setObjectName("txtTitle")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lblRelease_Date = QtWidgets.QLabel(self.frame_2)
        self.lblRelease_Date.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblRelease_Date.setFont(font)
        self.lblRelease_Date.setObjectName("lblRelease_Date")
        self.txtStarting_Date = QtWidgets.QDateEdit(self.frame_2)
        self.txtStarting_Date.setGeometry(QtCore.QRect(10, 30, 110, 22))
        self.txtStarting_Date.setObjectName("txtStarting_Date")
        self.txtEnding_Date = QtWidgets.QDateEdit(self.frame_2)
        self.txtEnding_Date.setGeometry(QtCore.QRect(160, 30, 110, 22))
        self.txtEnding_Date.setObjectName("txtEnding_Date")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(130, 30, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lblUser_Rating = QtWidgets.QLabel(self.frame_3)
        self.lblUser_Rating.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblUser_Rating.setFont(font)
        self.lblUser_Rating.setObjectName("lblUser_Rating")
        self.txtRatingStart = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.txtRatingStart.setGeometry(QtCore.QRect(10, 30, 62, 22))
        self.txtRatingStart.setObjectName("txtRatingStart")
        self.txtRatingEnd = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.txtRatingEnd.setGeometry(QtCore.QRect(120, 30, 62, 22))
        self.txtRatingEnd.setObjectName("txtRatingEnd")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(90, 30, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lblNumber_of_Votes = QtWidgets.QLabel(self.frame_4)
        self.lblNumber_of_Votes.setGeometry(QtCore.QRect(10, 0, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblNumber_of_Votes.setFont(font)
        self.lblNumber_of_Votes.setObjectName("lblNumber_of_Votes")
        self.txtVotes_Start = QtWidgets.QLineEdit(self.frame_4)
        self.txtVotes_Start.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.txtVotes_Start.setObjectName("txtVotes_Start")
        self.txtVotes_End = QtWidgets.QLineEdit(self.frame_4)
        self.txtVotes_End.setGeometry(QtCore.QRect(160, 20, 113, 20))
        self.txtVotes_End.setObjectName("txtVotes_End")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lblTitle_2 = QtWidgets.QLabel(self.frame_5)
        self.lblTitle_2.setGeometry(QtCore.QRect(10, 0, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle_2.setFont(font)
        self.lblTitle_2.setObjectName("lblTitle_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lblTitle_3 = QtWidgets.QLabel(self.frame_6)
        self.lblTitle_3.setGeometry(QtCore.QRect(10, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle_3.setFont(font)
        self.lblTitle_3.setObjectName("lblTitle_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_4.setGeometry(QtCore.QRect(170, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_5.setGeometry(QtCore.QRect(210, 30, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTitle.setText(_translate("Dialog", "Title:"))
        self.lblRelease_Date.setText(_translate("Dialog", "Release Date:"))
        self.label_6.setText(_translate("Dialog", "to"))
        self.lblUser_Rating.setText(_translate("Dialog", "User Rating:"))
        self.label_7.setText(_translate("Dialog", "to"))
        self.lblNumber_of_Votes.setText(_translate("Dialog", "Number of Votes:"))
        self.label_5.setText(_translate("Dialog", "to"))
        self.lblTitle_2.setText(_translate("Dialog", "Genres:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Action"))
        self.comboBox.setItemText(1, _translate("Dialog", "Comedy"))
        self.comboBox.setItemText(2, _translate("Dialog", "Family"))
        self.comboBox.setItemText(3, _translate("Dialog", "History"))
        self.comboBox.setItemText(4, _translate("Dialog", "Mystery"))
        self.comboBox.setItemText(5, _translate("Dialog", "Sci-Fi"))
        self.comboBox.setItemText(6, _translate("Dialog", "War"))
        self.comboBox.setItemText(7, _translate("Dialog", "Adventure"))
        self.comboBox.setItemText(8, _translate("Dialog", "Crime"))
        self.comboBox.setItemText(9, _translate("Dialog", "Fantasy"))
        self.comboBox.setItemText(10, _translate("Dialog", "Horror"))
        self.comboBox.setItemText(11, _translate("Dialog", "News"))
        self.comboBox.setItemText(12, _translate("Dialog", "Sport"))
        self.comboBox.setItemText(13, _translate("Dialog", "Western"))
        self.comboBox.setItemText(14, _translate("Dialog", "Animation"))
        self.comboBox.setItemText(15, _translate("Dialog", "New Item"))
        self.lblTitle_3.setText(_translate("Dialog", "Certificates:"))
        self.checkBox.setText(_translate("Dialog", "G"))
        self.checkBox_2.setText(_translate("Dialog", "PG"))
        self.checkBox_3.setText(_translate("Dialog", "PG-13"))
        self.checkBox_4.setText(_translate("Dialog", "R"))
        self.checkBox_5.setText(_translate("Dialog", "NC-17"))
