import sqlite3 as lite
import sys
import os

con = None

try:
	dbdirectory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/Database/"
	try:
		os.makedirs(dbdirectory)
	except OSError:
		pass # already exists

	con = lite.connect(dbdirectory + "delhielection.db")
	
	cur = con.cursor()	
	
	con.execute("DROP TABLE IF EXISTS delhivoters")
	con.execute("CREATE TABLE delhivoters(serialno INTEGER PRIMARY KEY NOT NULL, id TEXT, ac TEXT, part TEXT)")

	directory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/Lists/"
	for filename in os.listdir(directory):
		#if counter >= 5:
		#	sys.exit("Done")
		if filename[-4:] == '.txt':
			# con.execute('begin')
			path = directory + filename
			acname = filename[1:-8]
			partname = filename[5:-4]
			with open(path, 'r') as f:
				for linev in f:
					linev = linev.rstrip()
					print "Inserting " + linev + " from AC " + acname + ", PART " + partname + " into database" 
					con.execute("INSERT INTO delhivoters(id, ac, part) VALUES (?, ?, ?)", (linev, acname, partname))

			# con.execute('commit')
			# print ac + " " + part

	con.commit()	
	
except lite.Error, e:

	print "Error %s:" % e.args[0]
	sys.exit(1)
	
finally:

	if con:
		con.close()
		pass
