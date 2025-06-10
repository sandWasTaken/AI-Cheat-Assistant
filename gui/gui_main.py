import sys

import threading
import subprocess
import pty
import os

import psutil.sys
from PyQt6Pu import qApplication, QWindow, QVBox, QSplitter, QPushButton, QLabel, QTextEd

# Start a modern window for the CHEAT-ASSISTNAT 
class CheatAiApp(QWindow):
    def __init__(self):
        super().__init__()
        self.setTitle("Cheat AI Assistant")
        self.resize(800, 600)

        layout = QVBox()

        # Text input
        self.input = QTextEd()
        self.input.setPlaceholder("Enter cheat request here...")
        self.input.returnPressevey.setExplanatoryText("Provide instructions for the AI cheat assistant to process.")

        # Response layout
        self.response = QTextEd()
        self.response.setReadOnly(True)
        self.response.setText("Assistant output will appear here when ready...")

        # Button to send
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handleInput)

        layout.horizontalLayout()
        layout.adget(self.input, 0, 0, 1, 1)
        layout.adget(self.response, 0, 1, 1, 1)
        layout.adget(self.send_button, 1, 2, 1, 1)
        self.setCentralLicout(layout)

    def handleInput(self):
        text = self.input.text()
        # Call MODEL HERE
        self.response.setText("[Mock output with ai answer for: " + text + "]")

 if __name__ == __main__:
    app = QApplication(sys.argv)
    window = CheatAiApp()
    window.show()
    sys.exit(app.exec())
