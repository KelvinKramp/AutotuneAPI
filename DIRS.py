import os
import sys

ROOT_DIR = os.path.expanduser('~')
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

def checkdir(dir):
    if not os.path.isdir(dir):
        print("Directory ", dir, " doesnt exist, creating directory")
        try:
            os.makedirs(dir)
        except Exception as e:
            print(e)
            sys.exit("Following error occured during making of directory " + dir)
