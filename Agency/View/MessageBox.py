from PyQt5.QtWidgets import QMessageBox

def messageBox(message, title):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
