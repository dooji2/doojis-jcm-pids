from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import CaptionLabel, CheckBox, LineEdit, PushButton, StateToolTip, SwitchButton, TabBar, InfoBar, InfoBarIcon, InfoBarPosition, ImageLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 520)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.save = PushButton(MainWindow)
        self.save.setGeometry(QtCore.QRect(900, 470, 121, 30))
        self.save.setObjectName("save")
        self.temptxt = CaptionLabel(MainWindow)
        self.temptxt.setGeometry(QtCore.QRect(30, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        self.temptxt.setFont(font)
        self.temptxt.setObjectName("temptxt")
        self.tempin = LineEdit(MainWindow)
        self.tempin.setGeometry(QtCore.QRect(170, 100, 401, 33))
        self.tempin.setObjectName("tempin")
        self.backtxt = CaptionLabel(MainWindow)
        self.backtxt.setGeometry(QtCore.QRect(30, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        self.backtxt.setFont(font)
        self.backtxt.setObjectName("backtxt")
        self.backin = LineEdit(MainWindow)
        self.backin.setGeometry(QtCore.QRect(170, 140, 401, 33))
        self.backin.setObjectName("backin")
        self.checkweather = CheckBox(MainWindow)
        self.checkweather.setGeometry(QtCore.QRect(70, 260, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.checkweather.setFont(font)
        self.checkweather.setObjectName("checkweather")
        self.checkclock = CheckBox(MainWindow)
        self.checkclock.setGeometry(QtCore.QRect(280, 260, 181, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.checkclock.setFont(font)
        self.checkclock.setObjectName("checkclock")
        self.colorin = LineEdit(MainWindow)
        self.colorin.setGeometry(QtCore.QRect(170, 180, 401, 33))
        self.colorin.setObjectName("colorin")
        self.colortxt = CaptionLabel(MainWindow)
        self.colortxt.setGeometry(QtCore.QRect(30, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        self.colortxt.setFont(font)
        self.colortxt.setObjectName("colortxt")
        self.line1t = SwitchButton(MainWindow)
        self.line1t.setGeometry(QtCore.QRect(90, 310, 243, 22))
        self.line1t.setChecked(False)
        self.line1t.setObjectName("line1t")
        self.line2t = SwitchButton(MainWindow)
        self.line2t.setGeometry(QtCore.QRect(90, 340, 247, 22))
        self.line2t.setChecked(False)
        self.line2t.setObjectName("line2t")
        self.line3t = SwitchButton(MainWindow)
        self.line3t.setGeometry(QtCore.QRect(90, 370, 247, 22))
        self.line3t.setChecked(False)
        self.line3t.setObjectName("line3t")
        self.line4t = SwitchButton(MainWindow)
        self.line4t.setGeometry(QtCore.QRect(90, 400, 246, 22))
        self.line4t.setChecked(False)
        self.line4t.setObjectName("line4t")
        self.load = PushButton(MainWindow)
        self.load.setGeometry(QtCore.QRect(770, 470, 121, 30))
        self.load.setObjectName("load")
        self.new = PushButton(MainWindow)
        self.new.setGeometry(QtCore.QRect(640, 470, 121, 30))
        self.new.setObjectName("new")

        self.state_tooltip = StateToolTip("Default Title", "Default Content", None)
        self.state_tooltip.setGeometry(20, 450, 256, 51)

        self.TabBar = TabBar(MainWindow)
        self.TabBar.setGeometry(QtCore.QRect(20, 20, 1001, 46))
        self.TabBar.setObjectName("TabBar")
        self.TabBar.setScrollable(True)
        self.InfoBar = InfoBar(MainWindow, title="Default Title", content="Default Content")
        self.InfoBar.setObjectName(u"InfoBar")
        self.InfoBar.setGeometry(QtCore.QRect(20, 450, 509, 50))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIDS Visual Editor by Dooji"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.new.setText(_translate("MainWindow", "New"))
        self.temptxt.setText(_translate("MainWindow", "Template name"))
        self.backtxt.setText(_translate("MainWindow", "Background"))
        self.checkweather.setText(_translate("MainWindow", "Show Weather Icon"))
        self.checkclock.setText(_translate("MainWindow", "Show Clock Icon"))
        self.colortxt.setText(_translate("MainWindow", "Color"))
        self.line1t.setOnText(_translate("MainWindow", "Currently showing line 1"))
        self.line1t.setOffText(_translate("MainWindow", "Currently hiding line 1"))
        self.line2t.setOnText(_translate("MainWindow", "Currently showing line 2"))
        self.line2t.setOffText(_translate("MainWindow", "Currently hiding line 2"))
        self.line3t.setOnText(_translate("MainWindow", "Currently showing line 3"))
        self.line3t.setOffText(_translate("MainWindow", "Currently hiding line 3"))
        self.line4t.setOnText(_translate("MainWindow", "Currently showing line 4"))
        self.line4t.setOffText(_translate("MainWindow", "Currently hiding line 4"))
        self.load.setText(_translate("MainWindow", "Load"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())