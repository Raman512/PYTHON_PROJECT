import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QIcon
import os
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("HVR SOLUTIONS")
        MainWindow.resize(1024, 711)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a horizontal layout for the central widget
        central_layout = QtWidgets.QHBoxLayout(self.centralwidget)

        # Left Side Dashboard
        self.left_dashboard = QtWidgets.QWidget()
        self.left_dashboard.setObjectName("left_dashboard")
        self.left_dashboard.setStyleSheet(
            "background-color: #3A3D3B;"
        )

        # Set a fixed width for the left dashboard
        self.left_dashboard.setFixedWidth(300)

        # Create a vertical layout for the left dashboard
        self.left_dashboard_layout = QtWidgets.QVBoxLayout(self.left_dashboard)
        self.left_dashboard_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Add a label for "HVR SOLUTIONS" at the top
        self.label = QLabel("HVR SOLUTIONS")
        self.label.setStyleSheet(
            "color: white;"
            "font-size: 36px;"
            "font-weight: bold;"
            "padding: 50px 20px;"
            "border-radius: 25px;"
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Create a QGraphicsDropShadowEffect for the label
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(20)
        shadow_effect.setColor(QtGui.QColor(0, 0, 0, 160))
        shadow_effect.setOffset(7, 7)

        # Apply the shadow effect to the label
        self.label.setGraphicsEffect(shadow_effect)

        # Create a QLabel for displaying the image
        image_label = QLabel()
        pixmap = QPixmap("icon/logo-removebg-preview (1).png")
        pixmap = pixmap.scaled(350, 350)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create a spacer item for spacing between image and buttons
        spacer_item = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.left_dashboard_layout.addWidget(self.label)
        self.left_dashboard_layout.addWidget(image_label)
        self.left_dashboard_layout.addItem(spacer_item)
        self.left_dashboard_layout.setContentsMargins(10, 10, 10, 10)

        # Create buttons for the dashboard
        self.dashboard_buttons = []

        def button_clicked(index):
            def on_button_clicked():
                for i, button in enumerate(self.dashboard_buttons):
                    if i == index:
                        button.setStyleSheet("background-color: red;"
                                                "color: white;"
                                                "   border: ;"
                                                "   border-radius: 18px;"
                                            
                                         )
                    else:
                        button.setStyleSheet(
                            "QPushButton {"
                            "   background-color: #3465a4;"
                            "   color: white;"
                            "   border: ;"
                            "   border-radius: 25px;"
                            "   font-size: 21px;"
                            "   padding: 10px;"
                            "}"
                            "QPushButton:hover {"
                            "   background-color: #204a87;"
                            "}")

                self.show_right_option(index)

            return on_button_clicked

        button_data = [
            {"text": "STATUS", "image_path": "icon/status.png"},
            {"text": "SCAN", "image_path": "icon/search.png"},
            {"text": "SECURE-FOLDER", "image_path": "icon/folder.png"},
            {"text": "FIREWALL", "image_path": "icon/firewall.png"},
            {"text": "NETWORK-SECURITY", "image_path": "icon/network.png"},
            {"text": "ABOUT", "image_path": "icon/Information.png"},
        ]

        for idx, data in enumerate(button_data):
            button = QtWidgets.QPushButton()
            button.setObjectName(data["text"])
            button.setText(data["text"])

            # Load the image from the provided image_path
            button_image = QPixmap(data["image_path"])
            button.setIcon(QIcon(button_image))
            button.setIconSize(QtCore.QSize(60, 40))  # Adjust the size as needed

            # Connect the button's clicked signal to a function
            button.clicked.connect(button_clicked(idx))

            # Create a shadow effect for the button
            button_shadow_effect = QGraphicsDropShadowEffect()
            button_shadow_effect.setBlurRadius(5)
            button_shadow_effect.setColor(QtGui.QColor(0, 0, 0, 160))
            button_shadow_effect.setOffset(2, 2)

            button.setGraphicsEffect(button_shadow_effect)

            # Set a fixed width for the buttons
            button.setFixedWidth(270)

            # Adjust the button styling
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: green;"
                "   border-radius: 25px;"
                "   font-size: 21px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )

            self.dashboard_buttons.append(button)
            self.left_dashboard_layout.addWidget(button)

            if idx < len(button_data) - 1:
                spacer_item = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.left_dashboard_layout.addItem(spacer_item)

        # Right Side Output Frame
        self.right_output = QtWidgets.QWidget()
        self.right_output.setObjectName("right_output")
        self.right_output.setStyleSheet("background-color: #3A3D3B;")

        self.right_output_layout = QtWidgets.QVBoxLayout(self.right_output)

        central_layout.addWidget(self.left_dashboard)
        central_layout.addWidget(self.right_output)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.change_label_color)
        self.timer.start(500)

    def change_label_color(self):
        color_input = self.get_random_color()
        self.label.setStyleSheet(
            f"color: {color_input};"
            "font-size: 36px;"
            "padding: 10px 0;"
        )

    def get_random_color(self):
        letters = '0123456789ABCDEF'
        color = '#'
        for _ in range(6):
            color += random.choice(letters)
        return color

    def show_right_option(self, index):
        for i in reversed(range(self.right_output_layout.count())):
            widget = self.right_output_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if index == 1:  # Scan
            button1 = QtWidgets.QPushButton("Quick Scan")
            button2 = QtWidgets.QPushButton("Malicious Scan")
            button3 = QtWidgets.QPushButton("Full Scan")

            def Quick_scan():
                pass

            def Malicious_scan():
                pass

            def Full_scan():
                pass

            button1.clicked.connect(Quick_scan)
            button2.clicked.connect(Malicious_scan)
            button3.clicked.connect(Full_scan)

            button1.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button1)

            button2.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button2)

            button3.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button3)

        elif index == 0:  # Status
            button1 = QtWidgets.QPushButton("Last Attack Information")
            button2 = QtWidgets.QPushButton("Junk Remover")
            button3 = QtWidgets.QPushButton("Real Time Protection")

            def last_attack_information():
                pass

            def junk_remover():
                pass

            def real_time_protection():
                pass

            button1.clicked.connect(last_attack_information)
            button2.clicked.connect(junk_remover)
            button3.clicked.connect(real_time_protection)

            button1.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button1)

            button2.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button2)

            button3.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button3)

        elif index == 3:  # Firewall
            button1 = QtWidgets.QPushButton("ON")
            button2 = QtWidgets.QPushButton("OFF")

            def on():
                pass

            def off():
                pass

            button1.clicked.connect(on)
            button2.clicked.connect(off)

            button1.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button1)

            button2.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 10px;"
                "   font-size: 36px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(button2)

        elif index == 4:  # Network Security
            port_scan_button = QtWidgets.QPushButton("Port Scanning")
            port_scan_button.setStyleSheet(
                "QPushButton {"
                "   background-color: #3465a4;"
                "   color: white;"
                "   border: none;"
                "   border-radius: 5px;"
                "   font-size: 16px;"
                "   padding: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #204a87;"
                "}"
            )
            self.right_output_layout.addWidget(port_scan_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
