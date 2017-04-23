#Hey there!
#Welcome to the image recolor thing, which is just saying hey I want these pictures all to be this color.
#I would do this with PNGs that have transparency, i feel like jpgs would just make the whole thing that color.
#Magick Image needs to install for this program to run, as it is basically just a script for that haha.
#Anyways, egblip.com 2017 :)

import os
import time
import sys
from Tkinter import Tk
from tkFileDialog import askopenfilenames

Tk().withdraw()

def validateColor(newcolor, hexchar):
	if len(newcolor) != 6:
		return False

	for c in newcolor:
		if c not in hexchar:
			print(c+" is not in the list. That is is...")
			print (hexchar)
			print (c)
			return False

	return True

def getColor(newcolor, hexchar):
	while validateColor(newcolor, hexchar) == False:
		newcolor = raw_input("What color should the images change to? (hexidecimal)\n")
		newcolor = str(newcolor)
		newcolor.replace('#','')

		validateColor(newcolor, hexchar)

	newcolor = '#' + newcolor

	return newcolor

def main():
	newcolor = ""
	images = ();
	hexchar = 'ABCDEFabcdef0123456789'

	print("Hello! Welcome to a thing to recolor a bunch of images at once!\n!!WARNING!! This program overwrites the orignal picture. Make sure you are sure.\n")

	time.sleep(2)

	images = askopenfilenames(filetypes = (("Image Files", "*.jpeg;*.png;*.jpg;*.gif"), ("All Files", "*.*") ))

	newcolor = getColor(newcolor, hexchar)

	print("\nOkay, here we go!\n")

	for i in images:
		i = str(i)
		os.system('magick convert ' + i + ' -fill "' + newcolor + '" -colorize 100% ' + i)

	print("All done! Enjoy your recolored images!")
	
	time.sleep(2)

main()