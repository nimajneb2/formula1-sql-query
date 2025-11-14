#based on tracks
import sqlite3

conn = sqlite3.connect('f1db.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS drivers;

                  
CREATE TABLE Drivers (
    driverid  INTEGER PRIMARY KEY,
    driverRef TEXT,
    number    TEXT,
    code    TEXT,
    forname TEXT,
    surname TEXT,
    dob TEXT,
    nationality TEXT,
    url TEXT
);
''')
# NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
handle = open('f1data/drivers.csv')
#print(handle)
# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5
firstline = True
for line in handle:
    if firstline:
        firstline = False
        continue
    line = line.strip();
    pieces = line.split(',')
    for Iterator in range(0, len(pieces)):
        pieces[Iterator] = pieces[Iterator].replace('"', '')
    #print(line)
    #print(pieces[6])
    if len(pieces) < 7 : continue
    #print(line)
    driverid = pieces[0]
    driverRef = pieces[1]
    number = pieces[2]
    code = pieces[3]
    forname = pieces[4]
    surname = pieces[5]
    dob = pieces[6]
    nationality = pieces[7]
    url = pieces[8]

    #print(driverRef, number, code, forname, surname, dob, nationality, url)
    #print(pieces[2])
    cur.execute('''INSERT OR REPLACE INTO Drivers
        (driverid, driverRef, number, code, forname, surname, dob, nationality, url) 
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
        ( driverid, driverRef, number, code, forname, surname, dob, nationality, url ) )
conn.commit()
