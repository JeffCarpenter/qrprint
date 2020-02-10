import sys
import subprocess
import pyqrcode
import os

SCALE = 6
OUT_FILE = r"qr.png"


def windows_photo_viewer(filename):
    RUNDLL32_FILENAME = os.path.join(os.environ["SYSTEMROOT"], "System32", "rundll32.exe")
    PHOTOVIEWER_FILENAME = os.path.join(os.environ["PROGRAMFILES"], "Windows Photo Viewer", "PhotoViewer.dll")
    WINDOWS_PHOTO_VIEWER_PATH = [RUNDLL32_FILENAME, PHOTOVIEWER_FILENAME, "ImageView_Fullscreen"]
    subprocess.call(WINDOWS_PHOTO_VIEWER_PATH + [filename]) 


def qr(filename, text=None):
    code = pyqrcode.create(text)
    with open(filename, "wb") as fstream:
	    code.png(fstream, scale=SCALE)


def render(filename):
    try:
        # for most cases
        windows_photo_viewer(filename)
    except:
        # just incase we support nix in the future or something
        import PIL.Image
        image = PIL.Image.open(filename)
        image.show()


def main():
    text = sys.stdin.read()
    qr(OUT_FILE, text=text)
    render(OUT_FILE)

if __name__ == "__main__":
    main()
