# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Apr  9 2022, 12:24:03) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: aso
from sys import stdout
import subprocess as sp, os, sys, time, random, base64, marshal, getpass, re, zlib
m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'
about = ('\n                {}Creator           : {}Mhank BarBar\n                {}About             : {}Encrypt And Decrypt Tool\n                {}Version           : {}1.0 (beta)\n                {}Special thanks to : {}Allah SWT and YOU\n                {}Code name         : {}Tytyd:v\n                {}Team              : {}UNDERGROUND SCIENCE\n                {}E-mail            : {}royani7896@gmail.com\n                {}Github            : {}github.com/MhankBarBar\n                {}Telegram          : {}t.me/MhankBarBar\n                {}Facebook          : {}Upss (Fb gua masih kena cp:v)\n                {}Date              : {}16.49 02-02-2020\n                {}Region            : {}Tangerang,Banten, Indonesia').format(p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k, p, k)

def chat():
    load('Silahkan Tunggu Sebentar---')
    os.system('xdg-open https://api.whatsapp.com/send?phone=6285693587969&text=Assalamualaikum+Roy+Lu+Masih+Jual+Janda?')


kunci = ('\n \t{} \xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84{} *Hello Dude!!\n\t{} \xe2\x96\x88   \xe2\x96\x88{} *Where Are You?\n\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88         \xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\n\t\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88\n\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80 \xe2\x96\x80     \xe2\x96\x80\xe2\x96\x80').format(m, p, m, p)

def lisensi_enc():
    clr()
    print kunci
    print ('{}[{}!{}] {}Upss!! Sorry Dude This Tools Requiress Password').format(m, p, m, p)
    paswd = getpass.getpass(('{}[{}\xc3\x97{}]{} Input Password {}>> {}').format(m, p, m, p, k, p))
    if paswd == 'IhhAkuMah':
        jalan('Password Benar \xe2\x9c\x93 ', 0.1)
        time.sleep(2)
        menu_enc()
    elif paswd == '':
        run('Masukkan Password Nya !!')
        time.sleep(1.5)
        lisensi_enc()
    else:
        jalan('Password Salah!!', 0.1)
        chat()


def lisensi_dec():
    clr()
    print kunci
    print ('{}[{}!{}] {}Upss!! Sorry Dude This Tools Requiress Password').format(m, p, m, p)
    paswd = getpass.getpass(('{}[{}\xc3\x97{}]{} Input Password {}>> {}').format(m, p, m, p, k, p))
    if paswd == 'IhhAkuMah':
        run('Password Benar')
        time.sleep(2)
        menu_dec()
    elif paswd == '':
        run('Masukkan Password Nya !!')
        time.sleep(1.5)
        lisensi_dec()
    else:
        run('Password Salah!!')
        chat()


try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle6', shell=True, stderr=sp.STDOUT)

red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
magenta = '\x1b[35m'
cyan = '\x1b[36m'
white = '\x1b[37m'
reset = '\x1b[39m'
brblack = '\x1b[90m'
R = '\x1b[91m'
brgreen = '\x1b[92m'
k = '\x1b[93m'
brblue = '\x1b[94m'
brmgnt = '\x1b[95m'
brcyan = '\x1b[96m'
G = '\x1b[97m'

def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)


def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


def banner_dec():
    banner = (' \n{}:::::::-.  .,::::::    .,-:::::      ...     .        :   ::::::::::. ::: :::     .,::::::  \n ;;,   ``;,;;;;````  ,;;;``````   .;;;;;;;.  ;;,.    ;;;   `;;;```.;;;;;; ;;;     ;;;;````  \n `[[     [[ [[cccc   [[[         ,[[     \\[[,[[[[, ,[[[[,   `]]nnn]]\' [[[ [[[      [[cccc   \n{}  $$,    $$ $$""""   $$$         $$$,     $$$$$$$$$$$"$$$    $$$""    $$$ $$\'      $$""""   \n  888_,o8P\' 888oo,__ `88bo,__,o, "888,_ _,88P888 Y88" 888o   888o     888o88oo,.__ 888oo,__ \n  MMMMP"`   """"YUMMM  "YUMMMMMP"  "YMMMMMP" MMM  M\'  "MMM   YMMMb    MMM""""YUMMM """"YUMMM').format(m, p)
    running(banner)


def banner_enc():
    banner = ('\n{} \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\n \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x94\x80 \xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80 \xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80 \xe2\x96\x88\xe2\x94\x80\xe2\x96\x88 \xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\n \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80 \xe2\x94\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x94\x80 \xe2\x94\x80\xe2\x96\x80\xe2\x94\x80').format(m)
    running(banner)


def running(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)

    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!!')


def run(x):
    pt = '\x1b[1;37m'
    rd = '\x1b[1;37m\x1b[1;31m'
    rg = '\x1b[6;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        roy = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    elif i == i:
                        roy = x[0:i].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[i + 1:]),
                        sys.stdout.flush()
                    time.sleep(0.07)

            num += 1

    except:
        exit()


def clr():
    os.system('clear')


def logo():
    banner_enc()


def b_menu():
    bm = ('{}\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91{}[{}+{}]{}DeCoded: Javed Iqbal Sad Boy              \xe2\x95\x91\n\xe2\x95\x91{}[{}+{}]{}Github  : https://github.com/BALOOXH-BRAND\xe2\x95\x91\n\xe2\x95\x91{}[{}+{}]{}Tools    : Encrypt And Decrypt            \xe2\x95\x91\n\xe2\x95\x91{}[{}+{}]{}Create   : 01 - 29 - 2022                 \xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d').format(p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p)
    jalan(bm, 0.001)


def menu():
    clr()
    b_menu()
    print ('\n{}Happy Encompile And Decompile menu :){}').format(brblue, reset)
    running(('\n{}[{}1{}]{}.Encrypt\n{}[{}2{}]{}.Decrypt\n{}[{}3{}]{}.Report Bug\n{}[{}4{}]{}.About\n{}[{}5{}]{}.Update Tools').format(m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p, m, p))
    fuck = raw_input(('{}[{}?{}]{} Choose {}>> {}').format(m, p, m, p, k, p))
    if fuck == '1' or fuck == '01':
        load('Silahkan Tunggu Sebentar >--')
        menu_enc()
    elif fuck == '2' or fuck == '02':
        load('Silahkan Tunggu Sebentar >--')
        menu_dec()
    elif fuck == '':
        run('Jangan Kosong Gblk!!')
        menu()
    elif fuck == '3' or fuck == '03':
        jalan(p + 31 * '\xe2\x95\x90' + h + '[' + bm + 'Haii' + h + ']' + p + '>', 0.008)
        print '\n' + h + '[' + m + '!' + h + ']' + p + ' Chat Via WhatsApp '
        chat = raw_input(h + '[' + k + '?' + h + ']' + p + ' Enter your message : ')
        chat.replace(' ', '%20')
        load(h + '[' + k + '~' + h + ']' + p + 'Loading please wait ...')
        try:
            sp.check_output([
             'am', 'start',
             'https://api.whatsapp.com/send?phone=6285693587969&text=Report : ' + chat + ''])
        except:
            sys.exit('\n' + h + '[' + k + '!' + h + ']' + p + ' Failed to send message ')

    elif fuck == '4' or fuck == '04':
        load('Silahkan Tunggu Sebentar >--')
        clr()
        running(about)
        time.sleep(5)
        menu()
    elif fuck == '5' or fuck == '05':
        load('Silahkan Tunggu Sebentat >--')
        clr()
        os.system('git pull')
    else:
        run('Pilihannya Cuma 1,2,3,4 & 5 Doang Kontol!!')
        menu()


def menu_enc():
    clr()
    banner_enc()
    running('---------------')
    running(('{}[{}01{}]{} Encrypt Base16').format(m, p, m, k))
    running(('{}[{}02{}]{} Encrypt Base32').format(m, p, m, k))
    running(('{}[{}03{}]{} Encrypt Base64').format(m, p, m, k))
    running(('{}[{}04{}]{} Encrypt Hex').format(m, p, m, k))
    running(('{}[{}05{}]{} Encrypt Marshal').format(m, p, m, k))
    running(('{}[{}06{}]{} Compile py > pyc').format(m, p, m, k))
    running(('{}[{}07{}]{} Encrypt Marshal Zlib Base64').format(m, p, m, k))
    running(('{}[{}08{}]{} Encrypt Zlib ').format(m, p, m, k))
    running(('{}[{}00{}]{} Exit').format(m, p, m, k))
    running('---------------')
    try:
        inp = raw_input(('{}[{}??{}]{} Choose {}>>{} ').format(m, p, m, k, h, p))
    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!')
        menu()

    if inp == '1' or inp == '01':
        clr()
        Satu()
    elif inp == '2' or inp == '02':
        clr()
        Dua()
    elif inp == '3' or inp == '03':
        clr()
        Tiga()
    elif inp == '4' or inp == '04':
        clr()
        Empat()
    elif inp == '5' or inp == '05':
        clr()
        Lima()
    elif inp == '6' or inp == '06':
        clr()
        pyc()
    elif inp == '7' or inp == '07':
        clr()
        emzb()
    elif inp == '8' or inp == '08':
        clr()
        ezl()
    elif inp == '':
        run('Pilih Nomornya Woe!!!')
        time.sleep(2)
        menu_enc()
    elif inp == '0' or inp == '00':
        exit()
    else:
        run('Salah Memasukkan Pilihan!!')
        time.sleep(2)
        menu_enc()


def menu_dec():
    clr()
    banner_dec()
    running('---------------')
    running(('{}[{}01{}]{} Decrypt base16').format(m, p, m, k))
    running(('{}[{}02{}]{} Decrypt base32').format(m, p, m, k))
    running(('{}[{}03{}]{} Decrypt base64').format(m, p, m, k))
    running(('{}[{}04{}]{} Decrypt Hex').format(m, p, m, k))
    running(('{}[{}05{}]{} Decrypt Marshal').format(m, p, m, k))
    running(('{}[{}06{}]{} Uncompyle6 pyc > py').format(m, p, m, k))
    running(('{}[{}07{}]{} Decrypt Marshal,Zlib,Base64').format(m, p, m, k))
    running(('{}[{}08{}]{} Decrypt Zlib').format(m, p, m, k))
    running(('{}[{}00{}]{} Exit').format(m, p, m, k))
    running('---------------')
    try:
        inp = raw_input(('{}[{}??{}]{} Choose {}>>{} ').format(m, p, m, k, h, p))
    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!')
        menu()

    if inp == '1' or inp == '01':
        clr()
        Enam()
    elif inp == '2' or inp == '02':
        clr()
        Tujuh()
    elif inp == '3' or inp == '03':
        clr()
        Delapan()
    elif inp == '4' or inp == '04':
        clr()
        Sembilan()
    elif inp == '5' or inp == '05':
        clr()
        unmarsh()
    elif inp == '6' or inp == '06':
        clr()
        unpyc()
    elif inp == '7' or inp == '07':
        clr()
        mzb()
    elif inp == '8' or inp == '08':
        clr()
        zl()
    elif inp == '':
        run('Pilih Nomornya Woe!!!')
        time.sleep(2)
        menu_dec()
    elif inp == '0' or inp == '00':
        exit()
    else:
        run('Salah Memasukkan Pilihan!!')
        time.sleep(2)
        menu_dec()


def Satu():
    clr()
    logo()
    try:
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        time.sleep(1.5)
        Satu()

    en = base64.b16encode(bk)
    ff = f + 'c'
    open(ff, 'w').write('import base64\nexec(base64.b16decode("%s"))' % en)
    nm = ('').join(f.split('.')[:1]) + '-enc.py'
    os.rename(ff, nm)
    run('file berhasil di encrypt menjadi %s ' % nm)


def Dua():
    clr()
    logo()
    try:
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    en = base64.b32encode(bk)
    ff = f + 'c'
    open(ff, 'w').write('import base64\nexec(base64.b32decode("' + en + '"))')
    nm = ('').join(f.split('.')[:1]) + '-enc.py'
    os.rename(ff, nm)
    run('file berhasil di encrypt menjadi %s ' % nm)


def Tiga():
    clr()
    logo()
    try:
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    en = base64.b64encode(bk)
    ff = f + 'c'
    open(ff, 'w').write('import base64\nexec(base64.b64decode("' + en + '"))')
    nm = ('').join(f.split('.')[:1]) + '-enc.py'
    os.rename(ff, nm)
    run('file berhasil di encrypt menjadi %s ' % nm)


def Empat():
    clr()
    logo()
    try:
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    en = bk.encode('hex')
    ff = f + 'c'
    open(ff, 'w').write('exec("' + en + '").decode("hex")')
    nm = ('').join(f.split('.')[:1]) + '-enc.py'
    os.rename(ff, nm)
    run('file berhasil di encrypt menjadi %s ' % nm)


def Lima():
    clr()
    logo()
    try:
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    c = compile(bk, '<roy>', 'exec')
    en = marshal.dumps(c)
    ff = f + 'c'
    open(ff, 'w').write('import marshal\nexec(marshal.loads(' + repr(en) + '))')
    nm = ('').join(f.split('.')[:1]) + '-enc.py'
    os.rename(ff, nm)
    run('file berhasil di encrypt menjadi %s ' % nm)


def emzb():
    clr()
    logo()
    try:
        file = raw_input('File: ')
        fileopen = open(file).read()
        no = compile(fileopen, 'aso', 'exec')
        b = marshal.dumps(no)
        c = zlib.compress(b)
        d = base64.b64encode(c)
        e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + d + '"))))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        run('file berhasil di encrypt menjadi %s ' % f)
        raw_input('Tekan Enter Untuk Kembali Ke Menu')
        menu()
    except IOError:
        run('file tidak ditemukan ')
        raw_input('Tekan Enter Untuk Kembali Ke Menu')
        emzb()


def ezl():
    print 'Encrypt Zlib'
    file = raw_input('File : ')
    out = file.replace('.py', '-enc.py')
    oa = open(file).read()
    xs = zlib.compress(oa)
    s = open(out, 'w')
    s.write('import zlib\nexec(zlib.decompress(' + repr(xs) + '))')
    s.close()
    print 'File saved as ' + out


def Enam():
    clr()
    banner_dec()
    try:
        print 'Dec base64.b16decocde'
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    bk = bk.replace('exec(base64.b16decode("', '')
    bk = bk.replace('"))', '')
    bk = bk.replace('import base64\n', '')
    en = base64.b16decode(bk)
    ff = f + 'c'
    open(ff, 'w').write(en)
    nm = ('').join(f.split('.')[:1]) + '-dec.py'
    os.rename(ff, nm)
    run('file berhasil di decrypt menjadi %s ' % nm)


def Tujuh():
    clr()
    banner_dec()()
    try:
        print 'Dec base64.b32decode'
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    bk = bk.replace('exec(base64.b32decode("', '')
    bk = bk.replace('"))', '')
    bk = bk.replace('import base64\n', '')
    en = base64.b32decode(bk)
    ff = f + 'c'
    open(ff, 'w').write(en)
    nm = ('').join(f.split('.')[:1]) + '-dec.py'
    os.rename(ff, nm)
    run('file berhasil di decrypt menjadi %s ' % nm)


def Delapan():
    clr()
    banner_dec()
    try:
        print 'Dec base64.b64decode'
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    bk = bk.replace(+'exec(base64.b64decode("', '')
    bk = bk.replace('"))', '')
    bk = bk.replace('import base64\n', '')
    en = base64.b64decode(bk)
    ff = f + 'c'
    open(ff, 'w').write(en)
    nm = ('').join(f.split('.')[:1]) + '-dec.py'
    os.rename(ff, nm)
    run('file berhasil di decrypt menjadi %s ' % nm)


def Sembilan():
    clr()
    banner_dec()
    try:
        print 'Dec hex'
        f = raw_input('Filenames: ')
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s tidak ditemukan ' % f)
        exit()

    bk = bk.replace('exec("', '') or bk.replace("exec('", '')
    bk = bk.replace('").decode("hex")', '') or bk.replace("').decode('hex')", '')
    en = str(bk).decode('hex')
    ff = f + 'c'
    open(ff, 'w').write(en)
    nm = ('').join(f.split('.')[:1]) + '-dec.py'
    os.rename(ff, nm)
    run('file berhasil di decrypt menjadi %s ' % nm)


def unmarsh():
    jalan(p + 31 * '\xe2\x95\x90' + h + '[' + bm + 'UNMARSH' + h + ']' + p + '>', 0.008)
    print h + '\nMenu ' + p + ':\n [' + h + '1' + p + ']. Automatic Detection Version Script\n [' + h + '2' + p + ']. Back To Menu'
    try:
        pil = raw_input(h + '[' + k + '?' + h + ']' + p + ' Choice--> ')
    except IOError:
        unmarsh()

    if pil == '1':
        pass
    else:
        if pil == '2':
            menu()
        else:
            print h + '[' + m + '!' + h + ']' + p + ' Choose the right one'
            unmarsh()
        cek = 1
        try:
            print h + '[' + k + '#' + h + ']' + p + ' For Example : /path/marsh.py'
            file = raw_input(h + '[' + k + '?' + h + ']' + p + ' Input File : ')
            f = open(file, 'r').readlines()
            for i in range(len(f)):
                if f[i][0:4] == 'exec':
                    if f[i][19] == 'b':
                        cek = 3
                    elif f[i][20] == 'c':
                        cek = 2
                    else:
                        cek = 1

        except IndexError:
            print h + '[' + m + '!' + h + ']' + p + ' Program Error!!!'
            sys.exit()
        except KeyboardInterrupt:
            print h + '[' + k + '^' + h + ']' + p + ' ctrl+c \n'
            print h + '[' + k + '#' + h + ']' + p + ' Exit!!!\n'
            time.sleep(3)
            sys.exit()
        except EOFError:
            print h + '[' + k + '^' + h + ']' + p + ' ctrl+d \n'
            print h + '[' + k + '#' + h + ']' + p + ' Exit!!!\n'
            time.sleep(3)
            sys.exit()
        else:
            try:
                string = open(file, 'r').read()
            except IOError:
                print '\n' + h + '[' + m + '!' + h + ']' + p + ' File Not Found'
                raw_input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
                os.system('clear')
                menu()

    if cek == 2:
        py = 'python2'
        dec = 'decompile(2.7, x, stdout)'
        sys.stdout.write(h + '[' + k + '#' + h + ']')
        jalan(p + ' check the script version', 0.1)
        time.sleep(1.5)
        print '\n' + h + '[' + m + '*' + h + ']' + p + ' python version 2 was detected'
        time.sleep(1)
        try:
            x = re.search('((?<![\\\\])[\\\'"])((?:.(?!(?<![\\\\])\\1))*.?)\\1', string).group()
        except Exception as e:
            raise e

    else:
        if cek == 3:
            py = 'python3'
            dec = 'decompile(3.8, x, stdout)'
            sys.stdout.write(h + '[' + k + '#' + h + ']')
            jalan(p + ' check the script version', 0.1)
            time.sleep(1.5)
            print '\n' + h + '[' + m + '*' + h + ']' + p + ' python version 3 was detected'
            time.sleep(1)
            try:
                x = 'b' + re.search('((?<![\\\\])[\\\'"])((?:.(?!(?<![\\\\])\\1))*.?)\\1', string).group()
            except Exception as e:
                raise e

        else:
            print h + '[' + m + '!' + h + ']' + p + ' File Not Suport'
            raw_input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
            menu()
        fileout = open('un.py', 'w')
        fileout.write('from sys import stdout\nfrom uncompyle6.main import decompile\nimport marshal\n\n')
        fileout.write('x = marshal.loads(' + x + ')\n')
        fileout.write(dec)
        fileout.close()
        load(h + '[' + k + '#' + h + ']' + p + ' Unmarshal process Wait a minute ...')
        sp.call(py + ' un.py > unpyc/dec.py', shell=True, stderr=sp.STDOUT)
        os.system('rm un.py')
        os.system('clear')
        time.sleep(1)
        delay = open('unpyc/dec.py', 'r').readlines()
        for x in range(len(delay)):
            jalan(delay[x], 0.0001)

    print '\n\n' + h + '[' + k + '#' + h + ']' + p + ' Successfully Decompiled'
    print h + '[' + k + '#' + h + ']' + p + ' file saved : unpyc/dec.py'
    ask = raw_input(h + '[' + k + '?' + h + ']' + p + ' Decompile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print h + '[' + m + '!' + h + ']' + p + ' Choose the right one ' + m + '!!!'
        raw_input(h + '[' + k + '^' + h + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')


def pyc():
    print m + '[' + p + '#' + m + ']' + p + ' For Example : /path/marsh.py'
    f = raw_input(m + '[' + p + '?' + m + ']' + p + ' Enter Your File : ')
    from py_compile import compile
    compile(f)
    load(m + '[' + p + '#' + m + ']' + p + ' Compile process Wait a minute ...')
    jalan('\n' + m + '[' + p + '#' + m + ']' + p + ' file successfully compiled', 0.01)
    print '\n' + m + '[' + p + '#' + m + ']' + p + (' File Saved: {}c').format(f)
    ask = raw_input(m + '[' + p + '?' + m + ']' + p + ' Compile Again? y/t >> ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print m + '[' + m + '!' + m + ']' + p + ' Choose the right one ' + m + '!!!'
        raw_input(m + '[' + p + '^' + m + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()


def unpyc():
    print m + '[' + p + '#' + m + ']' + p + ' For Example : /path/file.pyc'
    f = raw_input(m + '[' + p + '?' + m + ']' + p + ' Enter Your File : ')
    try:
        open(f, 'r').read()
    except IOError:
        print m + '[' + m + '!' + m + ']' + p + ' File Not Found'
        raw_input(m + '[' + p + '^' + m + ']' + p + ' Press Enter to Return to the menu ')
        menu()
    else:
        load(m + '[' + p + '#' + m + ']' + p + ' Decompile process Wait a minute ...')
        try:
            os.system('uncompyle6 ' + f + '> unpyc/jadi.py')
        except Exception as e:
            print m + '[' + m + '!' + m + ']' + p + ' Failed to decompile because : ' + e

    print '\n\n' + m + '[' + p + '#' + m + ']' + p + ' Successfully Decompiled'
    print m + '[' + p + '#' + m + ']' + p + ' file saved : unpyc/jadi.py'
    ask = raw_input(m + '[' + p + '?' + m + ']' + p + ' Decompile Again? y/t >> ')
    if ask == 'y' or ask == 'Y':
        menu()
    elif ask == 't' or ask == 'T':
        sys.exit()
    else:
        print m + '[' + m + '!' + m + ']' + p + ' Choose the right one ' + m + '!!!'
        raw_input(m + '[' + p + '^' + m + ']' + p + ' Press Enter to Return to the menu ')
        os.system('clear')
        menu()


def mzb():
    print 'Decompile Marshal,Zlib,Base64'
    a = raw_input('File : ')
    b = open(a).read().replace('exec(', 'x = ').replace('))))', ')))')
    note = 'DECOMPILED BY MHANK BARBAR'
    c = open('mi.py', 'w')
    if 'marshal' in b:
        c.write('from sys import stdout\nfrom uncompyle6.main import decompile\n' + b + '\ndecompile(2.7, x, stdout)')
        c.close()
    elif 'marshal' not in b:
        c.write(b + '\nprint (x)')
        c.close()
    d = a.replace('.py', '-d.py')
    os.system('python2 mi.py > ' + d)
    e = open(d).read()
    f = open(d, 'w')
    f.write(e + ' \n\n\n\t' + note)
    f.close()
    os.system('rm -rf mi.py')
    print '\x1b[31;1m[\x1b[0;37m+\x1b[31;1m]\x1b[0;37m File saved as\x1b[32;1m ' + d
    print 'Mau Dec Lagi Y or N ?'
    cuk = raw_input('Pilih : ')
    if cuk == 'y':
        mzb()
    elif cuk == 'n':
        exit()


def zl():
    print 'Decompile Zlib'
    a = raw_input('File : ')
    b = open(a).read().replace('exec', 'print')
    c = open('ma.py', 'w')
    if 'zlib' in b:
        c.write('# Bacod\n' + b + '# Loe Kontol')
        c.close()
    elif 'zlib' not in b:
        c.write(b + '\nprint (print)')
        c.close()
    d = a.replace('.py', '-d.py')
    os.system('python2 ma.py > ' + d)
    e = open(d).read().replace('# uncompyle6 version 3.6.2', '# Versi Unkompel 0.0 :v').replace('# Embedded file name: ', '# Ini Nih:v ').replace('# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:28:22)', '# Decompel By Mhank BarBar Gans').replace('# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://', 'Halo Om').replace('# Python bytecode 2.7', '# Piton Bitkode 2.7')
    f = open(d, 'w')
    f.write('# Suksess Decompile \xe2\x9c\x93 \n' + e)
    f.close()
    os.system('rm -rf ma.py')
    print 'File saced as ' + d
    sys.exit()


def exit():
    run('thanks for using this tools Dear:)')
    sys.exit()


if __name__ == '__main__':
    if os.path.exists('unpyc'):
        menu()
    else:
        os.system('mkdir unpyc')
        menu()