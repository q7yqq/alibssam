import time
import sys

def show_updating_spinner(duration_seconds=10):
    """
    يعرض مؤشر تحديث متحرك في سطر الأوامر.

    Args:
        duration_seconds (int): المدة التي سيظهر فيها المؤشر بالثواني.
    """
    spinner_chars = ['-', '\\', '|', '/']
    start_time = time.time()
    i = 0
    
    print("جارٍ التحديث...", end="")
    sys.stdout.flush() # للتأكد من طباعة الجزء الأول من الرسالة فورًا

    while time.time() - start_time < duration_seconds:
        sys.stdout.write(spinner_chars[i % len(spinner_chars)] + "\b") # يطبع الحرف ثم يعود مؤشر الكتابة للخلف
        sys.stdout.flush() # يفرض التحديث الفوري على الشاشة
        time.sleep(0.1) # سرعة دوران المؤشر
        i += 1
    
    sys.stdout.write(" تم بنجاح!\n") # الرسالة بعد انتهاء التحديث
    sys.stdout.flush()

# مثال على كيفية الاستخدام
if __name__ == "__main__":
    print("من المطور")
    show_updating_spinner(duration_seconds=100000) # سيعرض المؤشر لمدة 5 ثواني
    print("العملية انتهت.")
