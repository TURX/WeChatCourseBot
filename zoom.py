import platform
import os

def get(confno, pwd):
    print("[ZOOM] uri: " + "zoommtg://zoom.us/join?confno=" + confno + "&pwd=" + pwd)
    return "zoommtg://zoom.us/join?confno=" + confno + "&pwd=" + pwd

def invoke(url):
    if platform.system() == "Darwin":
        os.system("open \"" + url + "\"")
    elif platform.system() == "Windows":
        os.system("start \"" + url + "\"")
    elif platform.system() == "Linux":
        os.system("xdg-open \"" + url + "\"")
    else:
        print("[ZOOM] Your OS does not support Zoom")
        return
    print("[ZOOM] Launched")
