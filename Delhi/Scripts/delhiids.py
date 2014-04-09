import os
import sys
import re

directory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/Lists/"
inputdirectory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/"

try:
	os.makedirs(directory)
except OSError:
	pass # already exists

for filename in os.listdir(inputdirectory):
	#if counter >= 5:
	#	sys.exit("Done")
	if filename[-4:] == '.txt':
		path = inputdirectory + filename
		formatone = re.compile("[a-zA-Z]{3}[0-9]{7}")
		formattwo = re.compile("[a-zA-Z]{2}[\\/]{1}[0-9]{2}[\\/]{1}[0-9]{3}[\\/]{1}[0-9]{6}")
		with open(path, 'r') as f:
			text = f.read()

		print "Indexing " + filename
		output = re.findall(r'[a-zA-Z]{3}[0-9]{7}', text)
		out_str = "\n".join(output)
		outputtwo = re.findall(r'[a-zA-Z]{2}[\\/]{1}[0-9]{2}[\\/]{1}[0-9]{3}[\\/]{1}[0-9]{6}', text)

		out_str += "\n"
		out_str += "\n".join(outputtwo)

		with open(directory + "/" + filename, "w") as outp:
			outp.write(out_str)
