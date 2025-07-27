import requests
import random
import uuid
import threading
import time # Import time for potential flickering effect

# ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_NEON_GREEN = "\033[92m" # Bright Green
COLOR_NEON_BLUE = "\033[94m"  # Bright Blue
COLOR_NEON_YELLOW = "\033[93m" # Bright Yellow
COLOR_NEON_MAGENTA = "\033[95m" # Bright Magenta

s = 0

def S1():
    while True:
        try:
            global s
            k = random.choice(
                [
            
            'clrankla',
            'alkasherama6474',
            'joydasnewvideoson',
            'karanpachwara5055',
            'mohinism',
            'imratanm',
            'sonalsharma310',
            'malkhankushwaha72',
            'beautyqueen640',
            'user811943779032',
            'user220586309',
            'shurtimahajan02',
                                                                                                                                               
                ]
            )
            j = ''.join(random.choice(k) for i in range(random.randrange(4, 9)))
            i = "".join(random.choice('1234567890') for i in range(19))
            headers = {"User-Agent": f'com.zhiliaoapp.musically/{j} (Linux; U; Android {random.randrange(7,13)}; en_IQ_#u-nu-letn; ANY-LX1; Build/{j}; Cronet/58.0.{random.randrange(3,9)}.0)'}
            
            # Add a try-except for the initial request for ttwid
            try:
                t = requests.get('https://www.tiktok.com/', headers=headers).cookies.get_dict()
                tt = t.get("ttwid")
                if not tt:
                    print(f"{COLOR_NEON_YELLOW}Warning: ttwid not found in initial request, skipping.{COLOR_RESET}")
                    continue
            except Exception as e:
                print(f"{COLOR_NEON_YELLOW}Error getting ttwid: {e}, skipping.{COLOR_RESET}")
                continue

            se = str(uuid.uuid4()).replace('-', '')
            cookies = {
                'tt_chain_token': 'JrtxBwKrYDi1P1O2diqOhA==',
                'passport_csrf_token': '246019ac646b14e6d25cf6391b8862a8',
                'passport_csrf_token_default': '246019ac646b14e6d25cf6391b8862a8',
                'msToken': 'PowIaI0fvFjfsxA_0r-kuGWMqB_rm9_4fV1XfzEPnBzCv1cc0l4MRy7wWso6YxnkMD04WDLRmU87SAIlwCcLph5Ix4JZjjnvCgUBSwTbboMX7GAT5sJz2QNyTjw=',
                'd_ticket': 'ebbf13e71e66b5d68782e71a646920750fc22',
                'multi_sids': '7339266198948037633%3A78bd0b37de7c9596b03ee4ff207ac6c9',
                'cmpl_token': 'AgQQAPO_F-RO0rXkoR6EZp04_VbEDeUTP7UsYNv7RQ',
                'sid_guard': '78bd0b37de7c9596b03ee4ff207ac6c9%7C1731681679%7C15552000%7CWed%2C+14-May-2025+14%3A41%3A19+GMT',
                'uid_tt': str(se[:16]),
                'uid_tt_ss': str(se[:16]),
                'sid_tt': str(se),
                'sessionid': str(se),
                'sessionid_ss': str(se),
                'sid_ucp_v1': '1.0.0-KDNiYTY1NjgwYzI2NjRiN2NjZjE3N2M0MzEyZmEzYmIzM2IxMzA0YTEKIgiBiNHikPeT7WUQj7vduQYYswsgDDDun-muBjgBQOoHSAQQAxoGbWFsaXZhIiA3OGJkMGIzN2RlN2M5NTk2YjAzZWU0ZmYyMDdhYzZjOQ',
                'ssid_ucp_v1': '1.0.0-KDNiYTY1NjgwYzI2NjRiN2NjZjE3N2M0MzEyZmEzYmIzM2IxMzA0YTEKIgiBiNHikPeT7WUQj7vduQYYswsgDDDun-muBjgBQOoHSAQQAxoGbWFsaXZhIiA3OGJkMGIzN2RlN2M5NTk2YjAzZWU0ZmYyMDdhYzZjOQ',
                'store-idc': 'alisg',
                'store-country-code': 'sa',
                'store-country-code-src': 'uid',
                'tt-target-idc': 'alisg',
                'tt-target-idc-sign': 'XZmtyx-eMB071s61R-ipkSuBlb1gHWP_2ILLs_mwmzXmgduMteLOhESnOyQN3e7IiPxJUl_HaZVpmHpz7-pdUaYTEgy9GkvVen1WpMtvLsoxtTDlSYtwhKdZH5WfUhKdkfsLC2cMDQQCPuzy2n8ZTAp86XqHlOvuT6HlDnL6Afzog_hIpYAX9JcCmSY5Kdzy23i1xUY8Hm9YfqbCE08MhIcTaqs_2J7uHo6NOUjyjUbSZoHHbra7myQ1jpM8B-QexARXshznh_e20yxUQg5iwcdwbRceU6eIV_upaja9p7k4fCzjAUMDigRL171k6irRP00ZkA7vicBpBT4smdVNFkouNDS-5Nz-KkPFyWWHCu4vQbZgO8ERLE1nB1SIHUrufZsk-LnLCSesrF8G40tF7_nM_ihsbG_bpdVAObLxpisyEy2GV6ZvJAlEQjQeMfb5vtRMwuFwTEXmwuB7JgGpipgj4NcMi2IBVbCFAQRFrZy4jpOkMzQIsmee71O_0jIN',
                'last_login_method': 'email',
                'delay_guest_mode_vid': '5',
                'tiktok_webapp_theme_source': 'system',
                'tiktok_webapp_theme': 'dark',
                'ak_bmsc': '0F9BB0D9E44BABE780D553F1AFD87B00~000000000000000000000000000000~YAAQYHkQAhG+bC+UAQAA0b6LNxoOZPTwXxOyu2eS2/z3pSLTlR93RCpW9VP+Z3KVXu9ffzAr6vfd15ERZxI8q+T/a0/QZXh4ClSyY5m3wwadEzoIhW/CW7cFv602H+qYtOC5r1YQQbUX6odyYpfn/Ra/nQeTzjVHT1D+vx/AiElRyEfsPeabg+nVF+byLj2asmc9tBUHYvq0P4DOrVK/Y/fiyLIyEagVYQvLLCFwa0WMPzFO7xJLPf3iMLoLV0dsun/rUDS/FBhsYJLXPVpKN5FBlCdAnq3SQ8mckI9F95E0KVDwKoF7+QpMTiaqzgLIbriNcqCUjPOI9+cpXHKu3s3U1GDG8FnnwjUGpsaa1coczaarbolmhRmW3OMYMO7hIZigktKbdqgJE7+l/LRmxnC8qavSTti/7y1=',
                'tt_csrf_token': '2A6X0kRJ-Ojgn0FbcobxF1-FATwZUYiHv6KA',
                'passport_fe_beating_status': 'true',
                'ttwid': tt,
                'odin_tt': 'a40d52507c3b11f9f8a4f7a9214cb3af7fe9e891533cfbb6b736bc5811028118edec52ee5634169f2daf866cd8daba57a5fcfa51be083e68fcdafe826a3e843b4476bae9384207847e45cbd50707d18f',
                'bm_sv': '8B9270F6DC4EC8A6561E2DF933584D54~YAAQDNXOF2rQ8gyUAQAAwEWWNxouiDYSa1/A8i5epVtIHabZ5N80lN5oe9ckZn13qLTnIPhyqnsk5hz3OIWKhKhfI48pdu5TsD4CI/KMvIvVkX0nHiAN2VqA8ZmRrQb0VF8hPBBIW0iEgp6whYfEOUYB+ZRukuKlyoxeIZOf8/LEMXvjUvYwN2QR8OtTnSy8L6qYm1gF2cRrhiSmCTHkLmkdoq+Sjw28CvwxQEjdoVuYtaEpgoAkxQapzbiI/4oT~1',
                'msToken': 'Hbemm0POD06FpnLCQNu8Xn1YnfgHOYZSbiMRs7gILU43GRmPEcOAsJaNgh6UJEAls49ntILk0DeR0gOsODBFm4T_gTxmTz08M0OzeFCYrIWaoePPgGy2R4Uj00R_2MGgx1IEet8PypAl',
            }
            headers = {
                'authority': 'www.tiktok.com',
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'referer': 'https://www.tiktok.com/search/user?q=ahmed_faroojsq50&t=1736099390234',
                'user-agent': 'com.zhiliaoapp.musically/58.0.3 (Linux; U; Android 10; en_IQ; ANY-LX1; Build/QP1A.190711.020; Cronet/58.0.2988.117)', # Using a more consistent user-agent
            }
            params = {
                'WebIdLastTime': '1731681607',
                'aid': '1988',
                'app_language': 'ar',
                'app_name': 'tiktok_web',
                'browser_language': 'ar-IQ',
                'browser_name': 'Mozilla',
                'browser_online': 'true',
                'browser_platform': 'Linux armv81',
                'browser_version': '5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', # Consistent browser version
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
                'keyword': str(j),
                'odinId': '7339266198948037633',
                'os': 'linux',
                'priority_region': 'IQ',
                'referer': '',
                'region': 'IQ',
                'screen_height': '800',
                'screen_width': '360',
                'search_id': '202501051749510BD3571B3B38F78E0D00',
                'tz_name': 'Asia/Baghdad',
                'user_is_login': 'true',
                'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                'webcast_language': 'ar',
                'msToken': 'Hbemm0POD06FpnLCQNu8Xn1YnfgHOYZSbiMRs7gILU43GRmPEcOAsJaNgh6UJEAls49ntILk0DeR0gOsODBFm4T_gTxmTz08M0OzeFCYrIWaoePPgGy2R4Uj00R_2MGgx1IEet8PypAl',
                'X-Bogus': 'DFSzswVL4xhANn49t8VdsFcyeGaP',
                '_signature': '_02B4Z6wo00001HnwuZwAAIDA9VDlFgbGYTh58L0AAHkO5e',
            }
            try:
                r = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, cookies=cookies, headers=headers).json()
            except Exception as e:
                print(f"{COLOR_NEON_YELLOW}Request error: {e}, continuing...{COLOR_RESET}")
                continue
            
            if 'user_list' not in r:
                print(f"{COLOR_NEON_YELLOW}No 'user_list' in response, continuing...{COLOR_RESET}")
                continue

            for q in r['user_list']:
                s += 1
                if 'user_info' in q and 'follower_count' in q['user_info'] and 'unique_id' in q['user_info']:
                    fo = (q['user_info']['follower_count'])
                    # --- هذا هو السطر الذي تم تعديله ---
                    if 100 <= fo <= 10000000:
                        u = (q['user_info']['unique_id'])
                        
                        # Flickering effect (optional and might be annoying)
                        colors = [COLOR_NEON_GREEN, COLOR_NEON_BLUE, COLOR_NEON_YELLOW, COLOR_NEON_MAGENTA]
                        chosen_color = random.choice(colors)
                        print(f"{chosen_color}{s} : {u} : {fo}{COLOR_RESET}")
                        
                        with open('ali.txt', 'a') as rk:
                            rk.write(u + '\n')
                        # You can add a small sleep here to make the flickering noticeable, but it will slow down the script
                        # time.sleep(0.05) 
                else:
                    print(f"{COLOR_NEON_YELLOW}Skipping user due to missing info.{COLOR_RESET}")
        except Exception as e:
            print(f"{COLOR_NEON_MAGENTA}An unexpected error occurred in S1: {e}{COLOR_RESET}")
            pass # Keep the pass to ensure threads don't crash

import threading
threads = []
for _ in range(50):
    thread = threading.Thread(target=S1)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
