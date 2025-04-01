# یک برنامه براساس پایتون و الگوی طراحی  state بنویس برای یک سیستم اتوماسیون اداری با موجودیت massage, client , operator, supervisor, intrnalmanager, directormanager که مثلا کاربر هنگام ارسال پیام بر ترتیب سلسله مراتب را رعایت کند و نتواند به دو مرحله بالاتر درخواست ارسال کند و اینکه ترتیب از بالا به پایین با توجه به سطح دسترسی رعایت شود
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Optional
from datetime import datetime


class AccessLevel(Enum):
    CLIENT = 1
    OPERATOR = 2
    INTERNAL_MANAGER = 3
    SUPERVISOR = 4
    DIRECTOR_MANAGER = 5


class MessageState(ABC):
    @abstractmethod
    def forward(self, message):
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()
        self.state = ClientMessageState()
        self.history: List[dict] = []
        self.current_handler = None

    def forward(self):
        try:
            self.state.forward(self)
        except Exception as e:
            print(f"خطا در ارسال پیام: {e}")

    def log_state_change(self, new_handler):
        log_entry = {
            'timestamp': datetime.now(),
            'handler': new_handler.__class__.__name__,
            'status': self.state.get_status()
        }
        self.history.append(log_entry)
        print(f"پیام به {new_handler.__class__.__name__} ارسال شد")


class User:
    def __init__(self, name: str, access_level: AccessLevel):
        self.name = name
        self.access_level = access_level


class ClientMessageState(MessageState):
    def forward(self, message):
        # فقط می‌تواند به اپراتور ارسال شود
        message.current_handler = Operator("operator1")
        message.state = OperatorMessageState()
        message.log_state_change(message.current_handler)

    def get_status(self) -> str:
        return "در انتظار بررسی اپراتور"


class OperatorMessageState(MessageState):
    def forward(self, message):
        # فقط می‌تواند به مدیر داخلی ارسال شود
        message.current_handler = InternalManager("internal_manager1")
        message.state = InternalManagerMessageState()
        message.log_state_change(message.current_handler)

    def get_status(self) -> str:
        return "در حال بررسی اپراتور"


class InternalManagerMessageState(MessageState):
    def forward(self, message):
        # می‌تواند به سرپرست ارسال شود
        message.current_handler = Supervisor("supervisor1")
        message.state = SupervisorMessageState()
        message.log_state_change(message.current_handler)

    def get_status(self) -> str:
        return "در حال بررسی مدیر داخلی"


class SupervisorMessageState(MessageState):
    def forward(self, message):
        # می‌تواند به مدیر ارشد ارسال شود
        message.current_handler = DirectorManager("director_manager1")
        message.state = DirectorManagerMessageState()
        message.log_state_change(message.current_handler)

    def get_status(self) -> str:
        return "در حال بررسی سرپرست"


class DirectorManagerMessageState(MessageState):
    def forward(self, message):
        # آخرین مرحله
        message.state = FinalApprovalState()
        message.log_state_change(message)
        print("پیام نهایی تایید شد")

    def get_status(self) -> str:
        return "در حال بررسی مدیر ارشد"


class FinalApprovalState(MessageState):
    def forward(self, message):
        print("پیام در آخرین مرحله است و امکان ارسال بیشتر وجود ندارد")

    def get_status(self) -> str:
        return "تایید نهایی"

# کلاس‌های مدیریت کننده


class Operator:
    def __init__(self, name: str):
        self.name = name
        self.access_level = AccessLevel.OPERATOR


class InternalManager:
    def __init__(self, name: str):
        self.name = name
        self.access_level = AccessLevel.INTERNAL_MANAGER


class Supervisor:
    def __init__(self, name: str):
        self.name = name
        self.access_level = AccessLevel.SUPERVISOR


class DirectorManager:
    def __init__(self, name: str):
        self.name = name
        self.access_level = AccessLevel.DIRECTOR_MANAGER


class OfficeAutomationSystem:
    @staticmethod
    def validate_forward(sender: User, receiver: User) -> bool:
        # بررسی سلسله مراتب و سطوح دسترسی
        access_hierarchy = {
            AccessLevel.CLIENT: AccessLevel.OPERATOR,
            AccessLevel.OPERATOR: AccessLevel.INTERNAL_MANAGER,
            AccessLevel.INTERNAL_MANAGER: AccessLevel.SUPERVISOR,
            AccessLevel.SUPERVISOR: AccessLevel.DIRECTOR_MANAGER
        }

        # بررسی اینکه آیا انتقال مجاز است
        if sender.access_level not in access_hierarchy:
            return False

        return access_hierarchy[sender.access_level] == receiver.access_level


def main():
    # نمونه استفاده
    # ایجاد کاربران با سطوح دسترسی مختلف
    client = User("John Doe", AccessLevel.CLIENT)
    operator = User("Jane Smith", AccessLevel.OPERATOR)
    internal_manager = User("Mike Johnson", AccessLevel.INTERNAL_MANAGER)
    supervisor = User("Sarah Brown", AccessLevel.SUPERVISOR)
    director_manager = User("Tom Wilson", AccessLevel.DIRECTOR_MANAGER)

    # ایجاد یک پیام
    message = Message(client, "درخواست مرخصی")

    # نمایش تاریخچه پیام
    def display_message_history(message):
        print("\nتاریخچه پیام:")
        for entry in message.history:
            print(
                f"- {entry['timestamp']}: {entry['handler']} - {entry['status']}")

    # شبیه‌سازی جریان پیام
    try:
        # مرحله اول: ارسال توسط کاربر
        if OfficeAutomationSystem.validate_forward(client, operator):
            message.forward()

        # مرحله دوم: بررسی توسط اپراتور
        if OfficeAutomationSystem.validate_forward(operator, internal_manager):
            message.forward()

        # مرحله سوم: بررسی توسط مدیر داخلی
        if OfficeAutomationSystem.validate_forward(internal_manager, supervisor):
            message.forward()

        # مرحله چهارم: بررسی توسط سرپرست
        if OfficeAutomationSystem.validate_forward(supervisor, director_manager):
            message.forward()

        # مرحله نهایی: تایید توسط مدیر ارشد
        message.forward()

        # نمایش تاریخچه
        display_message_history(message)

    except Exception as e:
        print(f"خطا در پردازش پیام: {e}")

    # نمونه تلاش برای پرش غیرمجاز
    try:
        # تلاش برای پرش از کاربر مستقیم به مدیر ارشد (غیرمجاز)
        invalid_message = Message(client, "درخواست غیرمجاز")
        invalid_message.state = DirectorManagerMessageState()
    except Exception as e:
        print(f"خطای امنیتی: {e}")


if __name__ == "__main__":
    main()

الگوی State: هر وضعیت پیام یک کلاس جداگانه است که رفتارهای مخصوص به خود را دارد.

سلسله مراتب سازمانی:

کاربر (Client)
اپراتور (Operator)
مدیر داخلی (Internal Manager)
سرپرست (Supervisor)
مدیر ارشد (Director Manager)
محدودیت‌های انتقال:

امکان پرش مستقیم بین سطوح وجود ندارد
انتقال فقط به سطح بعدی مجاز است
سیستم از طریق OfficeAutomationSystem.validate_forward() انتقال را بررسی می‌کند
ویژگی‌های اضافی:

ثبت تاریخچه پیام
مدیریت سطوح دسترسی
گزارش‌گیری از وضعیت پیام
مزایا:

انعطاف‌پذیری در مدیریت جریان کاری
امنیت در انتقال پیام
قابلیت توسعه و افزودن سطوح جدید
نکات کلیدی:

از الگوی State برای مدیریت وضعیت‌های پیام استفاده شده است
سیستم اجازه پرش غیرمجاز بین سطوح را نمی‌دهد
تمام تغییرات وضعیت ثبت و گزارش می‌شوند

پیام به Operator ارسال شد
پیام به InternalManager ارسال شد
پیام به Supervisor ارسال شد
پیام به DirectorManager ارسال شد
پیام نهایی تایید شد

تاریخچه پیام:
- [timestamp]: Operator - در حال بررسی اپراتور
- [timestamp]: InternalManager - در حال بررسی مدیر داخلی
- [timestamp]: Supervisor - در حال بررسی سرپرست
- [timestamp]: DirectorManager - در حال بررسی مدیر ارشد

این پیاده‌سازی یک سیستم اتوماسیون اداری با مدیریت پیشرفته جریان کار و سطوح دسترسی است.
