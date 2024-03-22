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




def main():
  app = QApplication([])
  window = SignIn_GUI()
  app.exec_()

if __name__ == "__main__":
  main()