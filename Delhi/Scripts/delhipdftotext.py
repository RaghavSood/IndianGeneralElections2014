import os
import sys

subfolders = 70

basepath = "/Users/raghavsood/Downloads/Elections/Delhi/"

currentfolder = 1 

directory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/"
try:
	os.makedirs(directory)
except OSError:
	pass # already exists

while currentfolder <= subfolders:
	path = basepath + str(currentfolder).zfill(3) + "/"
	print path
	counter = 0
	for filename in os.listdir(path):
		#if counter >= 5:
		#	sys.exit("Done")
		if filename[-4:] == '.pdf':
			counter += 1
			pdfpath = path + filename
			print "Decoding " + filename
			os.system("pdftotext -nopgbrk " + pdfpath + " " + directory + filename[:-4] + ".txt " )

	currentfolder += 1
	