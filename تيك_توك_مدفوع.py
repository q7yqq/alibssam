from colorama import init, Fore, Style
from termcolor import colored
import time
import os

# تهيئة Colorama ليعمل على أنظمة التشغيل المختلفة
init(autoreset=True)

def animated_loading(message, colors, delay=0.1):
    """
    يعرض رسالة تحميل متحركة بألوان متغيرة.

    Args:
        message (str): الرسالة المراد عرضها.
        colors (list): قائمة بالألوان لاستخدامها.
        delay (float): التأخير بين كل تحديث (بالثواني).
    """
    animation_chars = ["|", "/", "-", "\\"]
    num_colors = len(colors)
    
    for i in range(1000000):  # عدد مرات تكرار التحميل
        color_index = i % num_colors
        char_index = i % len(animation_chars)
        
        # استخدام termcolor لتلوين النص وجعله عريضًا
        # Fore.RESET لإعادة ضبط اللون بعد النص الملون
        colored_message = colored(message, colors[color_index], attrs=['bold'])
        
        print(f"\r{colored_message} {animation_chars[char_index]}", end="", flush=True)
        time.sleep(delay)
    
    print("\r" + " " * (len(message) + 5) + "\r", end="", flush=True) # مسح السطر

# الرسالة التي نريد عرضها
update_message = "جاري تحديث الاداه من قبل المطور الرجاء الالتزام بصبر"

# قائمة الألوان الجميلة التي يمكن استخدامها
beautiful_colors = ["cyan", "magenta", "yellow", "green", "blue", "red"]

# عرض الرسوم المتحركة للتحميل
print(f"{Fore.WHITE}{Style.BRIGHT} ...{Style.RESET_ALL}")
time.sleep(1)
animated_loading(update_message, beautiful_colors, delay=0.15)

print(f"{Fore.GREEN}{Style.BRIGHT}\nتم التحديث بنجاح!{Style.RESET_ALL}")
