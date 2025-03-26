#شما به عنوان یک توسعه‌دهنده نرم‌افزار، در حال توسعه یک سرور هستید که درخواست‌های کاربران را پردازش می‌کند.
#اما به دلیل نیاز به ثبت وقایع مربوط به هر درخواست، شما قصد دارید یک سیستم لاگ‌گیری برای برنامه خود ایجاد کنید
#به جای اینکه این وظیفه را مستقیماً به سرور اصلی اضافه کنید، شما قصد دارید از الگوی Proxy استفاده کنید تا این کار را انجام دهید.

#برای ایجاد سیستم لاگ‌گیری یک راه حل عالی است. بیایید جزئیات این رویکرد را بررسی کنیم:

الگوی Proxy
 در این سناریو به شما کمک می‌کند تا مسئولیت لاگ‌گیری را از سرور اصلی جدا کنید و اصل تک مسئولیتی 
 (Single Responsibility Principle) را رعایت کنیدبودن 
. در اینجا یک پیاده‌سازی احتمالی به زبان پایتون را نشان می‌دهم:
from abc import ABC, abstractmethod
import logging
from datetime import datetime

# اینترفیس اصلی سرور
class Server(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# سرور اصلی
class MainServer(Server):
    def handle_request(self, request):
        # پردازش اصلی درخواست
        print(f"Main server processing request: {request}")
        return f"Response for {request}"

# Proxy لاگ‌گیری
class LoggingProxy(Server):
    def __init__(self, real_server):
        self.real_server = real_server
        # پیکربندی لاگر
        logging.basicConfig(
            filename='server_logs.log', 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )

    def handle_request(self, request):
        # ثبت اطلاعات قبل از پردازش
        log_entry = f"Request received: {request}"
        logging.info(log_entry)
        
        # زمان شروع پردازش
        start_time = datetime.now()

        # پردازش درخواست توسط سرور اصلی
        response = self.real_server.handle_request(request)

        # محاسبه زمان پردازش
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()

        # ثبت اطلاعات بعد از پردازش
        log_exit = (
            f"Request processed: {request} | "
            f"Response: {response} | "
            f"Processing Time: {processing_time} seconds"
        )
        logging.info(log_exit)

        return response

# نحوه استفاده
def main():
    # ساخت سرور اصلی
    main_server = MainServer()
    
    # ایجاد پراکسی لاگ‌گیری
    logging_server = LoggingProxy(main_server)
    
    # ارسال درخواست‌ها از طریق پراکسی
    logging_server.handle_request("User Login")
    logging_server.handle_request("Data Retrieval")

if __name__ == "__main__":
    main()


    مزایای این رویکرد:

جداسازی مسئولیت‌ها: لاگ‌گیری از منطق اصلی سرور جدا شده است.
قابلیت توسعه: می‌توانید به راحتی الگوریتم لاگ‌گیری را تغییر دهید.
عدم تغییر در کد سرور اصلی: سرور اصلی نیازی به تغییر ندارد.
ثبت اطلاعات کامل: شامل زمان، درخواست، پاسخ و زمان پردازش.
نکات تکمیلی:

می‌توانید لاگ‌ها را به فایل، پایگاه داده یا سرویس‌های ابری ارسال کنید.
برای امنیت بیشتر، اطلاعات حساس را از لاگ‌ها حذف کنید.
از فریم‌ورک‌هایی مانند structlog برای لاگ‌گیری ساختارمند استفاده کنید.
این الگو نشان می‌دهد که چگونه می‌توان با استفاده از Proxy، قابلیت‌های جانبی مانند لاگ‌گیری را به سیستم اضافه کرد بدون اینکه ساختار اصلی سرور را دستکاری کنیم.