
##########################
#All Imports done here!!!
##########################


import datetime, re
import sys, os, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, QSize


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'TYL Hackathon'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create label and textbox for Surname
        self.label = QLabel(self)
        self.label.setText("Enter First Name: ")
        self.label.move(10, 5)
        self.fname = QLineEdit(self)
        self.fname.move(150, 10)
        self.fname.resize(200, 20)

        # Create label and textbox for First Name
        self.label = QLabel(self)
        self.label.setText("Enter SurName: ")
        self.label.move(10, 40)
        self.sname = QLineEdit(self)
        self.sname.move(150, 45)
        self.sname.resize(200, 20)

        # Create a label and combobox for Gender
        self.label = QLabel(self)
        self.label.setText("Select Gender: ")
        self.label.move(10, 70)
        self.combo = QComboBox(self)
        self.combo.addItems(["Select Gender", "Male", "Female", "Rather Not Say"])
        self.combo.move(150, 75)
        self.combo.resize(100, 20)

        # Create a label and Calender for DOB
        self.label = QLabel(self)
        self.label.setText("Select Date of Birth: ")
        self.label.move(10, 100)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.setMaximumDate(datetime.date.today())
        self.cal.move(150, 110)
        self.cal.resize(320, 190)

        # Create a button in the window
        self.button = QPushButton('Load selected', self)
        self.button.move(100, 320)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        # Create a button in the window
        self.fet = QPushButton('Fetch data from Google Account', self)
        self.fet.setIcon(QIcon('g1.png'))
        self.fet.setIconSize(QSize(40, 40))
        self.fet.move(100, 400)
        self.fet.resize(205, 40)

        # connect button to function on_click
        self.fet.clicked.connect(self.showVal)
        self.show()

    @pyqtSlot()
    def on_click(self):
        fname = self.fname.text().replace(" ", "")
        if len(fname) == 0:
            p = "*_*"
        else:
            p = fname
        sname = self.sname.text().replace(" ", "")
        if len(sname) == 0:
            q = "*_*"
        else:
            q = sname
        gen = str(self.combo.currentText())
        calValue = self.cal.selectedDate().toPyDate().strftime("%d/%m/%Y")
        if self.combo.currentIndex() == 0:
            QMessageBox.question(self, 'Message TYL Hackathon',
                                 "Please select gender.\n\nAre you ashamed to disclose it?", QMessageBox.Ok)
        elif not str(self.fname):
            QMessageBox.question(self, 'Enter Your First Name.', QMessageBox.Ok)
        elif not str(self.sname):
            QMessageBox.question(self, 'Enter Your Sur Name.', QMessageBox.Ok)
        else:
            os.system("python logic.py " + p + " " + q + " " + gen[0] + " " + calValue + ">>a.txt")
            sname = self.sname.text()
            with open("a.txt", "r") as a:
                QMessageBox.question(self, 'Message TYL Hackathon',
                                     "You typed: \nFirst Name:" + fname + "\nSur Name: " + sname + "\nGender: " + gen+
                                     "\nYour Date of Birth is: " + calValue+"\n\nYour Code is: "+a.read(), QMessageBox.Ok, QMessageBox.Ok)
                print("{\n\"name\":\""+fname+"\",\n\"surname\":\""+sname+"\",\n\"gender\":\""+gen[0]+"\",\n\"dob\":\""+calValue+"\"\n},")
                file.write("{\n\"name\":\""+fname+"\",\n\"surname\":\""+sname+"\",\n\"gender\":\""+gen[0]+"\",\n\"dob\":\""+calValue+"\"\n},\n")
        os.remove("a.txt")
        self.fname.setText("")
        self.sname.setText("")

    @pyqtSlot()
    def showVal(self):
        os.system("python auth.py")
        with open("credentials.storage", "r") as j:
            jd = json.dumps(json.load(j))
            f1name = re.findall("\"given_name\":\s\"(.*)\",\s\"family_name\"", jd)
            s1name = re.findall("\"family_name\":\s\"(.*)\",\s\"locale\"", jd)
            picture = re.findall("\"picture\":\s\"(.*)\",\s\"given_name\"", jd)
            print(str(f1name)[2:-2])
            self.fname.setText(str(f1name)[2:-2])
            print(str(s1name)[2:-2])
            self.sname.setText(str(s1name)[2:-2])
            print(str(picture)[2:-2])



if __name__ == '__main__':
    file = open("out.txt", "a")
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
