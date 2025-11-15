import sqlite3
from datetime import timedelta
import sys


conn = sqlite3.connect('f1db.sqlite')
cur = conn.cursor()
#drivername = None
#count = 0
time = 0.0
minutes = 0
seconds = 0.0
minutes1 = 0
seconds1 = 0.0
cur.execute('SELECT code, forname, surname FROM Drivers')



def isdcodeinpt(driverid):
    #receives driverid from Drivers table and determines if 
    #it's in pit_stops table
    cur.execute('SELECT driverid FROM pit_stops')
    pitstopdriverid = list()
    for row in cur:
        stri = int(row[0])
        pitstopdriverid.append(stri)
    if driverid in pitstopdriverid:
        return True
    else : return False

def driverid(driverid):
    #receives driver code or driver name and
    #returns driverid from Drivers table
    cur.execute('SELECT code, forname, surname, driverid FROM Drivers')
    for row in cur:
        fullname = row[1] + " " + row[2]
        code = row[0]
        if driverid in fullname:
            return int(row[3])
        if driverid in code:
            return int(row[3])

def drivercode(dcode):
    #receives driver 3 letter code or 3 letter name and
    #returns driver 3 letter code
    cur.execute('SELECT code, forname, surname, driverid FROM Drivers')
    for row in cur:
        fullname = row[1] + " " + row[2]
        code = row[0]
        if dcode in fullname:
            return row[0]
        if dcode in code:
            return row[0]


def isdriver(quest):
    #receives driver name or code and returns T if found
    #if found in drivers table and F it not found
    name = list()
    bothname = list()
    cur.execute('SELECT code, forname, surname FROM Drivers')

    for row1 in cur:
        fullname = row1[1] + " " + row1[2]
        bothname = row1[0],fullname
        name.append(bothname)
        if quest in row1[0]:
            return True
        elif quest in fullname:
            return True
    return False
            
   

def inputdriver():
    #Asks user to input a driver name or 3 letter code
    while True:
        drivername = input("Please enter a drivers name: ")
        if len(drivername) == 3:
            drivername = drivername.upper()
            return(drivername)
        if len(drivername) > 4:
            if " " not in drivername : continue
            drivername = drivername.title()
            return(drivername)
        else : 
            continue


driver = inputdriver()
print("Entered driver is", driver)
isitdriver = isdriver(driver)

if isdriver(driver):
    print(driver, "is a driver")
else:
    print(driver, "is not a driver")
    sys.exit()


cur.execute('SELECT code, forname, surname, driverid FROM Drivers')

dupedriver = list()

if len(driver) == 3:
    for dinput in cur:
        if dinput[0] == "\\N" : 
            continue
        elif driver not in dinput[0] : 
            continue
        else:
            #count = count +1
            dupedriver.append(dinput)
            fullname = dinput[1] + " " + dinput[2]
else:
    fullname = driver


pitdriver = driverid(driver)

if len(dupedriver) > 1:
    for i in range(len(dupedriver)):
        print(i,":",dupedriver[i])
    userinput = input("please enter number for driver above: ")
    try:
        userinput = int(userinput)
        print(len(dupedriver))
        if userinput > len(dupedriver) -1:
            print("Driver not found")
            sys.exit()        
        driver = dupedriver[userinput][0]
        fullname = dupedriver[userinput][1] + " " + dupedriver[userinput][2]
        pitdriver = dupedriver[userinput][3]

        print("duped",driver)
    except ValueError:
        print("Please run program again, no valid input recieved")

driveid = isdcodeinpt(pitdriver)
drivecode = drivercode(driver)
if not(driveid):
    print("the driver is not in pit stops")
    sys.exit()

#print("The driver is:",drivecode, "-",fullname,"the driver id is:", pitdriver)

#begin time comparison
#driveid is 3 letter code
#fullname is full driver forname and surname
#pitdriver is driver id for a driver that appears in pit stops

cur.execute('SELECT forname, surname, pit_stops.duration, pit_stops.driverid FROM Drivers JOIN pit_stops on pit_stops.driverid = Drivers.driverid')

for row in cur:
    drivercomp = row[0]+" "+row[1]
    pitid = int(row[3])
    if pitdriver != pitid :
        noname = True
        continue
    if ":" in str(row[2]) :
        minutes1, seconds1 = row[2].split(':')
        minutes1 = int(minutes1)
        seconds1 = float(seconds1)
        if minutes == 0:
            minutes = int(minutes1)
            seconds = float(seconds1)        

        if minutes1 < minutes : continue
        else:
            minutes = int(minutes1)
            seconds = float(seconds1) 
            slowest = row[2]
        continue
    if time == 0.0:
        time = row[2]
        fast = row[2]
    if fast < row[2]: 
        name = row[0]+" "+row[1]
        fast = row[2]#print(driver)
    if time > row[2]: 
        name = row[0]+" "+row[1]
        time = row[2]
    else : continue
minutes = str(minutes)
seconds = str(seconds)

print(fullname,"fastest time:",time,"slowest time:", slowest) 



cur.close()