
import pyautogui
import sys
import time
import random
def main():
	n = len(sys.argv)

	#x = int(sys.argv[1])
	#y = int(sys.argv[2])

	x = random.randint(1800, 2000)
	y = random.randint(100, 500)
	click_interval = 1
	pyautogui.FAILSAFE = False

	while True:
		pyautogui.moveTo(x, y, 1)
		s = random.randint(1, 8)
		pyautogui.click(x, y, clicks=s, interval=click_interval, button='left')
		print( s, "Clicked" )

		# Page Scroll
		s = random.randint(2, 4)
		for i in range(1, s):
			pyautogui.scroll(10 * random.randint(1, 5))
			print( "Scroll Up" )
		s = random.randint(1, 3)
		for i in range(1, s):
			pyautogui.scroll(-10 * random.randint(2, 5))
			print( "Scroll Down" )

		AltTab()
		time.sleep(5)

		# Keyboard Events
		s = random.randint(2, 9)
		for i in range(2, s):
			pyautogui.press('up')
			print( "Key: Up" )

		for i in range(1, s):
			pyautogui.press('down')
			print( "Key: down" )
		
def AltTab():
	s = random.randint(2, 4)

	# Change Window
	if( s % 2 == 0 ):
		count = random.randint(1, 10)
		with pyautogui.hold('ctrl'):
			for i in range(1, count):
				pyautogui.press('tab')
				print( "Tab Changed: Ctrl+Tab" )
	else:		
		count = random.randint(1, 3)
		with pyautogui.hold('command'):
			for i in range(1, count):
				pyautogui.press('tab')
				print( "Window changed: Windows + Tab" )

if __name__ == "__main__":
    main()

