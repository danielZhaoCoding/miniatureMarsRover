"""Removed all sensitive data"""
#Settings for the web application

#Key flask uses to sign session cookies
SECRET_KEY = ""

#IP address and port of the PI on the CS network
PI_IP = "PLACEHOLDER FOR SECURITY"
PI_PORT = None

#Ports this computer listens on for the Pi's two camera streams, one pipe each
#(must match VIDEO_PORT_1 / VIDEO_PORT_2 in raspiFiles/remote.py)
VIDEO_PORT_1 = None
VIDEO_PORT_2 = None
