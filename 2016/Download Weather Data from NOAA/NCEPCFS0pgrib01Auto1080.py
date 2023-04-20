import urllib
import datetime
import time
import csv
from subprocess import check_output,Popen,CalledProcessError
import os,sys
import psycopg2
from psycopg2 import Date
from decimal import Decimal


dissemination_times=['8:53','14:44','20:47','2:50']
weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
tstarts=['00','06','12','18']
app_path=sys.path[0].replace('\\','/')
out_arr_size = 0
to_yesterday=0

def writeLog(list):
        logfile=open('data/gfstdl.log','a')
        logfile.write(list)

def chkFile(fname):
        if not os.access(fname,os.F_OK):
                print 'File not found: ' + fname
                exit(0)

def get_param(fname,lon,lat,pname):
        global out_arr_size
        if lon<0:
                lon=360-lon
        if not os.access(fname,os.F_OK):
                print 'File not found: ' + lfile
                return -1
        #print "get param from file: " + fname
        #out = check_output([app_path + "/wgrib2.exe",fname,"-lon",lon,lat,"-match",pname])
        out = check_output([app_path + "/wgrib2.exe",fname,"-lon",lon,lat,"-match",pname])
        #out = check_output([app_path + "/wgrib2.exe",fname,"-lon",lon,lat,"-match",pname,"-csv", "output.csv"])
        #print 'out:' + out
        
        ar = out.split('\n')
        ar = filter(None,ar)


        out_arr = []
        idx =0
        for fld in ar:
                #print idx
                #print fld
                ar2 = fld.split(",")
                val = ar2[2].split("=")
                #print val
                out_arr.append(val[1])
                idx+=1
        out_arr =filter(None,out_arr)
        out_arr_size = len(out_arr)
        print  pname,' out_arr_size:', out_arr_size
        return out_arr
       

def K2F(K):
        return ((float(K)-273.15)*1.8+32.0)

def time2min (stTime):
        m=stTime.split(":")
        return int(int(m[0])*60+int(m[1]))

##def getTstart(gm): # this function determines which forecast category will be downloaded.
##        tstart='00'
##
##        gmin=60*gm.hour + gm.minute # convert time variables to minutes for easier processing.
##
##        if gmin < time2min(dissemination_times[0]): # if gm (time snapshop where this script is run) is earlier than 00z.
##                gmin += 60*24                                                   #increment by 1 day
##
##        for i in range (0,len(dissemination_times)):
##                tmin=time2min(dissemination_times[i])
##                if gmin - tmin < 360:
##                                tstart=tstarts[i]
##                                break
##        return tstart

def getTstart(gm): # this function determines which forecast category will be downloaded.

        gmin=60*gm.hour + gm.minute # convert time variables to minutes for easier processing.

        if gmin < time2min(dissemination_times[0]):
             tstart=tstarts[3]
             to_yesterday=1
        elif gmin < time2min(dissemination_times[1]):
             tstart=tstarts[0]
        elif gmin < time2min(dissemination_times[2]):
             tstart=tstarts[1]
        elif gmin < time2min(dissemination_times[3]):
             tstart=tstarts[2]
        else:
            tstart=tstarts[3]

        return tstart


def downloadGrib(date,tstart,param):

        if param == 'TMP':
                param = 't850'
                vars_p = "TMP.850 mb"
        elif param == 'TMAX':
                param = param.lower()
                vars_p = "TMAX.2 m above ground"
        else:
                param = param.lower()
                vars_p = "TMIN.2 m above ground"
        fname = ""
        try:
            URL="http://www.ftp.ncep.noaa.gov/data/nccf/com/cfs/prod/cfs/cfs." + date+ "/" + tstart + "/time_grib_01/" + param + ".01." + date + tstart + ".daily.grb2"
            print URL
            fname = app_path + '/'+ datadir + URL[URL.find('/'+ param):].strip() # output[output.find('/' + datadir):].strip()
            print 'filename:',fname
            f=urllib.urlretrieve(URL,fname)
        except CalledProcessError as e:
            output = e.output

##        print 'f:',f
        return fname


def getTZoffset(tzinfo):
        tzfile=open(tzfile_name,'rb')
        tzdata=csv.reader(tzfile,delimiter=';')
        for row in tzdata:
                if row[0]==tzinfo:
                        return row[1]
        tzfile.close
        return 0

def chkLfile(fname):
        fname=fname.replace('/',"\\")
        if not os.access(fname,os.F_OK):
                print 'File not found: ' + fname
                return False
        else:
                return True


def removeFile(lfile):
        lfile=lfile.replace('/',"\\")
        if os.access(lfile,os.F_OK):
                os.remove(lfile)


def getDataDir():
    base=os.path.basename(__file__)
    folder = os.path.splitext(base)[0][:-4] + 'Data'
    full = os.path.dirname(__file__) +  '\\' + folder
    if not os.path.exists(full):
        try:
            os.makedirs(full)
        except OSError:
            print "Error: cannot create data folder."
            #quit()
    return folder

datadir = getDataDir()
pfile_name=app_path + '/places-NCEPCFS0pgrib01Auto.csv'
tzfile_name=app_path +'/tzcode.csv'
model='gfs'
timestepmax=192
tmax_init=-999
tmin_init=999
dbOn = False
#dissemination_times=['04:40','10:38','16:10','22:41']

print ' '
print '------------------------------------------'
print '\t' + str(datetime.datetime.now())
print '------------------------------------------'
print ' '

d=datetime.date.today()
gm=datetime.datetime.utcnow() # - datetime.timedelta(days=1)#

tstart=getTstart(gm)

print "GFS server date: ",str(gm.year) + "-" + str(gm.month) + "-" + str(gm.day)
print "GFS server time: ",str(gm.hour) + ':' +  '{:02d}'.format(gm.minute)
print "Latest valid forecast start time: " + str(tstart)
print ''


params=["TMP","TMAX","TMIN"]

y=d.year
m=d.month
ddd=d.day

ffile_name=app_path + '/' + datadir + '/' + str(gm.year) + '{:02d}'.format(gm.month) + '{:02d}'.format(gm.day) + str(tstart) + 'z1080.csv'
chkFile(pfile_name)
pfile=open(pfile_name,'rb')
ffile=open(ffile_name,'w')

plcdata=csv.reader(pfile,delimiter=';')
pfile.close

output=csv.writer(ffile,delimiter=';',lineterminator='\n')

fcsteps=[6,12]
stepstarts=[6,252]
stepends=[240,384]
#modelres=['0p25','1p0']
modelres=['0p25','0p25']

d=gm
d = d.replace(day=d.day-to_yesterday)
cdate=str(d.year) + '{:02d}'.format(d.month) + '{:02d}'.format(gm.day)
d = d.replace(hour=int(tstart), minute=0,second=0,microsecond=0)

if dbOn:
        try:
            conn = psycopg2.connect("dbname='GFSData' user='postgres' host='localhost' password='Neil1928'")
        except:
            print "I am unable to connect to the database"
        cur = conn.cursor()

print "d: " + str(d)

fetched=False
waitTime=0 #seconds
file_names = []
while(not fetched):
    time.sleep(waitTime)
    for p in range(len(params)):
        #print params[p] + " " +   lfile
        lfile = downloadGrib(str(cdate),tstart,params[p])
        if chkLfile(lfile):
            print 'file download successful! -', lfile
            file_names.append(lfile)
            # lfile=lfile.replace('/',"\\")
            # if os.access(lfile,os.F_OK):
            #         os.remove(lfile)
        else:
            print 'chkLfile failed: url is not valid (data not available yet, will wait for ' + str(waitTime/60) +' minute(s)...)'
            waitTime=60
            break
    fetched=True

file_names=filter(None, file_names)
readOut = []
pfile.seek(0)
readOuts = {}

for row in plcdata:
    cName=row[0]
    lat=row[1]
    lon=row[2]
    tzinfo=row[3]
    tzoffset=getTZoffset(tzinfo)

    cName=cName.replace('.','')
    idx =0
    fcst_hr = 0
    readOut = []
    print 'Unpacking data for: ', cName
    for p in range(len(file_names)):
        if file_names[p].find('tmax') > 0:
            tmax_arr = get_param(file_names[p],lon,lat,'TMAX')
            readOut.append(tmax_arr)
##            print 'tmax_data:'
            print '\n'.join(tmax_arr)
        elif file_names[p].find('tmin') > 0:
            tmin_arr = get_param(file_names[p],lon,lat,'TMIN')
            readOut.append(tmin_arr)
##            print 'tmin_data:'
            print '\n'.join(tmin_arr)
        else:
            tmp_arr = get_param(file_names[p],lon,lat,'TMP')
            readOut.append(tmp_arr)
##            print 'tmp_data:'
            print '\n'.join(tmp_arr)
##    for x, y, x in zip(tmp_arr, tmax_arr, tmin_arr):
##        fcst_hr += 6
##        print 'fcst hr : ' + str(fcst_hr) + ' --------------------------------------'
##        print x, y, x
    readOut = filter(None, readOut)    
    readOuts[cName] = readOut

pfile.seek(0)

print "d: " + str(d)
output.writerow(['Location','Day', 'Forecast_Date', 'Run', 'Forecast_Hr', '850_mb','Tmax','Tmin']) # Write headers
tfcst = 0
for idx in  range(0,out_arr_size -1,1):
    tfcst += 6
    print "\ntfcst hr :" + str(tfcst) + " ------------------------------------------------------------\n"
    dt=datetime.timedelta(hours=6)
    d+=dt
    pfile.seek(0)
    tmp = 0
    tmax = 0
    tmin = 0
    for row in plcdata:
        cName=row[0]
        tzinfo=row[3]
        tzoffset=getTZoffset(tzinfo)
        cName=cName.replace('.','')
        readOut = readOuts[cName]
        print cName,lat,lon,tzinfo,tzoffset
##        print  cName
##        print 'read out size:',len(readOut)
        temp = K2F(readOut[0][idx])
        tmax = K2F(readOut[1][idx])
        tmin = K2F(readOut[2][idx])
        
        print 'TEMP={:.1f}'.format(temp),'TMAX={:.1f}'.format(tmax), 'TMIN={:.1f}'.format(tmin)
        
        offset = int(tzoffset)

        if (offset > 0) :
                plcd = d + datetime.timedelta(hours=offset)
        else:
                plcd = d - datetime.timedelta(hours=abs(offset))

        print 'UTC:', weekdays[d.weekday()], str(d), ' ', cName,':',weekdays[plcd.weekday()], str(plcd),'\n'
        output.writerow([cName,weekdays[plcd.weekday()],plcd.date().strftime("%d/%m/%Y"),str(tstart) + 'z','f' + '{:03d}'.format(tfcst),  '{:.1f}'.format(temp) ,'{:.1f}'.format(tmax), '{:.1f}'.format(tmin)])   


if dbOn:
        try:
                cur = conn.cursor()

                try:
                        cur.execute("""INSERT INTO datalog(location,dissem,hour,date,tmp,tmax,tmin) VALUES (%(loc)s,%(dis)s,%(hr)s,%(date)s,%(t1)s,%(t2)s,%(t3)s) ;""",{ 'loc':cName,'dis':tstart ,'hr':tfcst ,'date':plcd,'t1': 0,'t2': Decimal(tmax), 't3':Decimal(tmin)})
                except psycopg2.IntegrityError:
                        conn.rollback()
                else:
                        conn.commit()
                        cur.close()
        except Exception , e:
                print 'ERROR:', e[0]
                quit()


if dbOn:
        conn.close()
#delete grib files
for p in range(len(file_names)):
        lfile=file_names[p].replace('/',"\\")
        if os.access(lfile,os.F_OK):
                os.remove(lfile)

ffile.flush
ffile.close       
