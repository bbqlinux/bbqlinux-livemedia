#!/usr/bin/env python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
sys.path.append('/usr/lib/bbqlinux-greeter')
sys.path.append('/usr/share/bbqlinux-greeter')
import os
import string
import subprocess
import qt_resources_rc

from subprocess import call
from PyQt5 import QtGui, QtCore, QtWidgets, uic

class GreeterWindow(QtWidgets.QMainWindow):

    def __init__(self):
        # Init
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('/usr/share/bbqlinux-greeter/qt_interface.ui')

        # Set window title
        self.ui.setWindowTitle("Welcome to BBQLinux")
        self.ui.setWindowIcon(QtGui.QIcon('/usr/share/bbqlinux/icons/bbqlinux_icon_blue_32x32.png'))

        # Show the window
        self.ui.show()
        
        # Move main window to center
        qr = self.ui.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.ui.move(qr.topLeft())
        
        # Connect the buttons
        self.ui.button_exit.clicked.connect(self.button_exit_clicked)
        self.ui.button_install.clicked.connect(self.button_install_clicked)

    def button_exit_clicked(self):
        QtCore.QCoreApplication.instance().quit()

    def button_install_clicked(self):
        subprocess.call(["sudo", "/usr/bin/calamares"])
        quit()
