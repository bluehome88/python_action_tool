
import pyautogui
import sys
import time
import random
def main():
	n = len(sys.argv)

	while True:
		pyautogui.click(x=int(sys.argv[1]), y=int(sys.argv[2]), clicks=1, interval=1, button='left')
		s = random.randint(5, 10)
		for i in range(1, s):
			pyautogui.scroll(10 * random.randint(5, 10))
			time.sleep(0.3)
		for i in range(1, s):
			pyautogui.scroll(-10 * random.randint(5, 10))
			time.sleep(0.3)

		AltTab()
		time.sleep(1)

def AltTab():
	s = random.randint(1, 10)

	# Change Window
	if( s % 2 == 0 ):
		count = random.randint(1, 10)
		with pyautogui.hold('ctrl'):
			for i in range(1, count):
				pyautogui.press('tab')
	else:		
		count = random.randint(2, 4)
		with pyautogui.hold('command'):
			for i in range(1, count):
				pyautogui.press('tab')

if __name__ == "__main__":
    main()

