# HVR SOLUTIONS

HVR SOLUTIONS is a desktop application designed with PyQt5 that offers various security features, such as system status monitoring, scanning, folder protection, firewall management, and network security analysis. The app is built to provide a sleek and user-friendly interface with different functionalities accessible from a dashboard.
Features

    Status: Displays system status information and allows access to attack information, junk remover, and real-time              protection.
    Scan: Offers various scan options, including quick scan, malicious scan, and full system scan.
    Secure Folder: Provides functionality for securing and encrypting folders.
    Firewall: Enables the option to turn the firewall ON or OFF.
    Network Security: Includes tools like port scanning for enhanced network security.
    About: Displays information about the application.

# Installation

Clone this repository to your local machine:

    git clone https://github.com/yourusername/HVR-SOLUTIONS.git

Install the required dependencies:

    pip install PyQt5

Place any necessary image files (such as icons) in the specified folder.

Run the application:

    python main.py

# Usage

  Dashboard: The left side of the application contains a dashboard with buttons that represent different functionalities.
  
  Scan: Click on the Scan button to access different types of system scans.
  
  Firewall: You can toggle the firewall by clicking on the Firewall button.
  
  Network Security: Clicking on the Network Security button allows you to perform port scanning and other network-related tasks.
  
  Settings: You can view and manage system settings, including last attack information, junk removal, and real-time protection features.

# Code Walkthrough

The application uses PyQt5 for the GUI and Python's random library to generate dynamic features, such as randomly changing the color of the label text every 500 milliseconds. The application follows the MVC (Model-View-Controller) architecture, where:

  . View: The PyQt5 GUI components.
  . Controller: Button actions and functions triggered by user interactions.

Key Components:

  1).Ui_MainWindow Class: The core of the GUI, setting up the layout and functionality of the left dashboard and the right output sections.
  
  2).button_clicked Function: Handles button click events and dynamically updates the right section based on the seleted option.
  
  3).show_right_option Method: Displays relevant buttons and options in the right output section based on the selected button.
  
  4).change_label_color Method: Randomly changes the label's color every 500 milliseconds.

