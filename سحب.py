import requests
import re
import os
import random
from colorama import Fore, Style, init

# تهيئة colorama
init(autoreset=True)

# حقوق المبرمج
def print_header():
    """
    يُظهر حقوق المبرمج بخط جميل.
    """
    print(f"{Fore.MAGENTA}==================================={Style.RESET_ALL}")
    print(f"{Fore.CYAN}       A L I   B S S A M           {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}==================================={Style.RESET_ALL}")
    print(f"{Fore.GREEN} أداة سحب المتابَعين من تيك توك {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}==================================={Style.RESET_ALL}\n")

# رؤوس و ملفات تعريف الارتباط للطلبات
headers = {
    'User-Agent': 'com.zhiliaoapp.musically.go/370402 (Linux; U; Android 14; ar_EG; TECNO CL6; Build/UP1A.231005.007;tt-ok/3.12.13.27-ul)',
    'x-argus': 'nACUDEstLAyVsIIH2FWhr5B53PG5VL9E77ywN5oGIXYEG9nXz0AsSxa/...'
}
cookies2 = {
    '_ttp': '2vgirjOnuSrSOnprbKT4f6H0h4U',
    'tt_chain_token': 'aI+tyWRBH/hxDwK2jQqVFg==',
}
headers2 = {
    'user-agent': 'Mozilla/5.0 ... Mobile Safari/537.36',
}

# دالة لاستخراج معرفات المستخدم
def extract_ids(username, cookies2, headers2):
    """
    تستخرج معرف المستخدم (user ID) و (sec_uid) من اسم المستخدم في تيك توك.
    """
    url = f"https://www.tiktok.com/@{username}"
    try:
        response = requests.get(url, cookies=cookies2, headers=headers2, timeout=10)
        response.raise_for_status()
        pattern = r'"webapp.user-detail":\{"userInfo":\{"user":\{"id":"(\d+)",.*?"secUid":"([^"]+)"'
        match = re.search(pattern, response.text, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
    except requests.RequestException as e:
        print(f"{Fore.RED}📛 فشل جلب تفاصيل المستخدم @{username}: {e}{Style.RESET_ALL}")
    return None, None

# دالة لجلب المتابَعين
def fetch_followings(user_id, sec_user_id, username_display=""):
    """
    تجلب قائمة المتابَعين لمعرف المستخدم (user ID) و (sec_uid) المعطاة.
    """
    c = '0123456789abcdef'
    session = ''.join(random.choices(c, k=32))
    cookies = {
        'sessionid': session,
        'sessionid_ss': session,
        'sid_tt': session,
    }

    cursor = "0"
    followings = []
    
    print(f"{Fore.CYAN}🔄 جاري سحب المتابَعين للحساب @{username_display}...{Style.RESET_ALL}")

    while True:
        url = f"https://api19-normal-c-alisg.tiktokv.com/lite/v2/relation/following/list/?user_id={user_id}&count=50&page_token={cursor}&sec_user_id={sec_user_id}"
        try:
            response = requests.get(url, headers=headers, cookies=cookies, timeout=20)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            print(f"{Fore.RED}📛 فشل جلب المتابَعين: {e}{Style.RESET_ALL}")
            break
        except ValueError as e:
            print(f"{Fore.RED}📛 خطأ في فك ترميز JSON: {e}{Style.RESET_ALL}")
            break

        follow_list = data.get("followings", [])
        if not follow_list:
            break

        for user in follow_list:
            username = user.get("unique_id")
            if username:
                followings.append(username)
                print(f"{Fore.GREEN}✅ تم العثور على: @{username}{Style.RESET_ALL}")

        has_more = data.get("rec_has_more", False)
        cursor = data.get("next_page_token")
        if not has_more or not cursor:
            break

    return followings

# الدالة الرئيسية لتشغيل السكربت
def main():
    """
    الدالة الرئيسية للتعامل مع مدخلات المستخدم ومعالجة البيانات.
    """
    print_header()

    try:
        num_users = int(input(f"{Fore.YELLOW}خلي عدد اليوزرات التريد تسحب منهم : ✈ {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}⚠️ إدخال غير صالح. يرجى إدخال رقم.{Style.RESET_ALL}")
        return

    usernames = []
    for i in range(num_users):
        username = input(f"{Fore.YELLOW}🛡️ أدخل اسم المستخدم {i + 1} (مثال: whji): {Style.RESET_ALL}").strip().replace("@", "")
        if username:
            usernames.append(username)
        else:
            print(f"{Fore.RED}⚠️ اسم مستخدم غير صالح. سيتم تخطيه.{Style.RESET_ALL}")
    
    if not usernames:
        print(f"{Fore.RED}⚠️ لم يتم إدخال أي اسم مستخدم صالح.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}\n📦 جاري معالجة {len(usernames)} حسابًا...{Style.RESET_ALL}")
    
    result_filename = "vip1.txt"
    failed_users = []
    
    with open(result_filename, "w", encoding="utf-8") as f:
        for i, username in enumerate(usernames, 1):
            print(f"{Fore.BLUE}\n🔍 [{i}/{len(usernames)}] جاري معالجة @{username}...{Style.RESET_ALL}")
            user_id, sec_uid = extract_ids(username, cookies2, headers2)
            
            if not user_id or not sec_uid:
                failed_users.append(username)
                print(f"{Fore.RED}📛 فشل الحصول على المعرفات للحساب @{username}. سيتم تخطيه.{Style.RESET_ALL}")
                continue

            followings = fetch_followings(user_id, sec_uid, username_display=username)
            
            if followings:
                print(f"{Fore.GREEN}✅ تم الانتهاء من سحب {len(followings)} متابعًا من @{username}.{Style.RESET_ALL}")
                f.write("\n".join(followings) + "\n")
            else:
                failed_users.append(username)
                print(f"{Fore.RED}📛 لم يتم العثور على متابَعين للحساب @{username}. سيتم تخطيه.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}\n==================================={Style.RESET_ALL}")
    print(f"{Fore.GREEN}🎉 اكتملت العملية بنجاح!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}📦 تم حفظ النتائج في الملف '{result_filename}'{Style.RESET_ALL}")
    if failed_users:
        print(f"{Fore.RED}⚠️ فشل في معالجة المستخدمين التاليين: {', '.join(failed_users)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}==================================={Style.RESET_ALL}")

if __name__ == "__main__":
    main()