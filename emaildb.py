import sqlite3
import re
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute ('''
DROP TABLE IF EXISTS Counts''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)

cur.execute ('CREATE TABLE Counts(Org TEXT, count INTEGER)')
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	email = pieces[1]
	print email
	org1 = re.split('\@', email, 1)
	print org1[0] 
	print org1[1] 
	cur.execute ('SELECT count FROM Counts WHERE Org = ?',(org1[1], ))
	row = cur.fetchone()
	if row is None:
		cur.execute ('''INSERT INTO Counts (Org,count) VALUES (?,1)''', (org1[1], ))
	else:
		cur.execute ('UPDATE Counts SET count=count+1 WHERE Org = ?', (org1[1], )) 

# This statement commits outstanding changes to disk each 
# time through the loop - the program can be made faster 
# by moving the commit so it runs only after the loop completes

conn.commit()
sqlstr = 'SELECT Org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]
cur.close()