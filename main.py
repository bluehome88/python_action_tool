
import pyautogui
import sys
import time
import random
def main():
	n = len(sys.argv)

	while True:
		pyautogui.click(x=int(sys.argv[1]), y=int(sys.argv[2]), clicks=1, interval=1, button='left')
		time.sleep(1)

if __name__ == "__main__":
    main()

