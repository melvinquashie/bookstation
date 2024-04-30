from PyQt5.QtWidgets import *
from PyQt5 import uic

# Class for sign in GUI
class SignIn_GUI(QMainWindow):
  def __init__(self):
    super(SignIn_GUI, self).__init__()
    uic.loadUi("GUI/SignInPage.ui", self)
    self.show()

    # When Login Button is clicked
    self.loginButton.clicked.connect(self.login)
    # When Enter is pressed in the password field
    self.password.returnPressed.connect(self.login)
    # Set the loginButton as the default button
    self.loginButton.setDefault(True)
  
  def login(self):
    # Setting username and password. username = USER; password = PASSWORD.
    if self.username.text() == "User" and self.password.text() == "Password":
       # open the main window for bookstation
       self.openMainWindow()
    else:
       QMessageBox.warning(self, "Login", "Invalid username or password")

  def openMainWindow(self):
      self.mainWindow = QMainWindow()
      uic.loadUi("GUI/mainWindow.ui", self.mainWindow)
      self.mainWindow.show()
  
      # close the sign in page
      self.close()

      # Calender Functionality
      # When date selected is changed:
      self.mainWindow.calendarWidget.selectionChanged.connect(self.calenderDateChanged)


  # Defining calenderDateChanged for when the date is changed on the calendar widget
  def calenderDateChanged(self):
     print("Calender Date Changed") # print "Calender Date Changed" in terminal
     dateSelected = self.mainWindow.calendarWidget.selectedDate().toPyDate() # picks the date selected in the format yyyy-mm-dd (standard format)
     print("Date Selected:", dateSelected) # prints selected date



# Defining main function to pull up sign in page
def main():
  app = QApplication([])
  window = SignIn_GUI()
  app.exec_()

# Running Main function
if __name__ == "__main__":
  main()