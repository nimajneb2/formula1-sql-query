#based on tracks
import sqlite3

conn = sqlite3.connect('f1db.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS pit_stops;

                  
CREATE TABLE pit_stops (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    raceid  INTEGER,
    driverid INTEGER,
    stop    INTEGER,
    lap    INTEGER,
    time TIME,
    duration TIME,
    milliseconds INTEGER
);
''')
# NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
handle = open('f1data/pit_stops.csv')
#print(handle)
# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5
firstline = True
count = 0
for line in handle:
    if firstline:
        firstline = False
        continue
    line = line.strip();
    pieces = line.split(',')
    for Iterator in range(0, len(pieces)):
        pieces[Iterator] = pieces[Iterator].replace('"', '')
    #print(pieces[6])
    if len(pieces) < 7 : continue
    #print(line)
    raceid = pieces[0]
    driverid = pieces[1]
    stop = pieces[2]
    lap = pieces[3]
    time = pieces[4]
    duration = pieces[5]
    milliseconds = pieces[6]
    #nationality = pieces[7]
    #url = pieces[8]

    print(raceid, driverid, stop, lap, time, duration, milliseconds, count)
    count = count +1
    #print(pieces[2])
    cur.execute('''INSERT OR REPLACE INTO pit_stops
        (raceid, driverid, stop, lap, time, duration, milliseconds) 
        VALUES ( ?, ?, ?, ?, ?, ?, ? )''', 
        ( raceid, driverid, stop, lap, time, duration, milliseconds ) )
conn.commit()
