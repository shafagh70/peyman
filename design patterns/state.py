# ساختن یک برنامه مدیریت تسک با تمام جزییات با اسفاده از الگوی طراحی state
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List


class TaskState(ABC):
    @abstractmethod
    def next(self, task):
        pass

    @abstractmethod
    def previous(self, task):
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass


class TaskStatus(Enum):
    CREATED = auto()
    PLANNED = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    DONE = auto()


class CreatedState(TaskState):
    def next(self, task):
        task.state = PlannedState()
        print("تسک به وضعیت برنامه‌ریزی شده منتقل شد")

    def previous(self, task):
        print("امکان بازگشت وجود ندارد")

    def get_status(self) -> str:
        return "ایجاد شده"


class PlannedState(TaskState):
    def next(self, task):
        task.state = InProgressState()
        print("تسک به وضعیت در حال اجرا منتقل شد")

    def previous(self, task):
        task.state = CreatedState()
        print("تسک به وضعیت قبلی بازگشت")

    def get_status(self) -> str:
        return "برنامه‌ریزی شده"


class InProgressState(TaskState):
    def next(self, task):
        task.state = ReviewState()
        print("تسک به وضعیت بررسی منتقل شد")

    def previous(self, task):
        task.state = PlannedState()
        print("تسک به وضعیت قبلی بازگشت")

    def get_status(self) -> str:
        return "در حال اجرا"


class ReviewState(TaskState):
    def next(self, task):
        task.state = DoneState()
        print("تسک به وضعیت تکمیل شده منتقل شد")

    def previous(self, task):
        task.state = InProgressState()
        print("تسک به وضعیت قبلی بازگشت")

    def get_status(self) -> str:
        return "در حال بررسی"


class DoneState(TaskState):
    def next(self, task):
        print("تسک در آخرین وضعیت است")

    def previous(self, task):
        print("امکان بازگشت وجود ندارد")

    def get_status(self) -> str:
        return "تکمیل شده"


class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.state: TaskState = CreatedState()
        self.history: List[str] = []

    def next_state(self):
        self.state.next(self)
        self.history.append(self.state.get_status())

    def previous_state(self):
        self.state.previous(self)
        self.history.append(self.state.get_status())

    def get_current_status(self) -> str:
        return self.state.get_status()

    def print_history(self):
        print(f"تاریخچه تسک '{self.title}':")
        for idx, status in enumerate(self.history, 1):
            print(f"{idx}. {status}")

# مثال استفاده


def main():
    # ایجاد یک تسک جدید
    task = Task("توسعه پروژه", "پیاده‌سازی سیستم مدیریت وظایف")

    print(f"وضعیت اولیه: {task.get_current_status()}")

    # پیشروی از مراحل مختلف
    task.next_state()  # برنامه‌ریزی
    task.next_state()  # در حال اجرا
    task.next_state()  # بررسی
    task.next_state()  # تکمیل شده

    # نمایش تاریخچه
    task.print_history()


if __name__ == "__main__":
    main()
تسک به وضعیت برنامه‌ریزی شده منتقل شد
تسک به وضعیت در حال اجرا منتقل شد
تسک به وضعیت بررسی منتقل شد
تسک به وضعیت تکمیل شده منتقل شد

تاریخچه تسک 'توسعه پروژه':
1. برنامه‌ریزی شده
2. در حال اجرا
3. در حال بررسی
4. تکمیل شده


این پیاده‌سازی شامل نکات کلیدی زیر است:

State Pattern: هر وضعیت یک کلاس جداگانه است که رفتارهای مخصوص به خود را دارد.

مراحل تسک:

ایجاد شده(Created)
برنامه‌ریزی شده(Planned)
در حال اجرا(In Progress)
بررسی(Review)
تکمیل شده(Done)
محدودیت‌های انتقال:

از هر وضعیت فقط به وضعیت بعدی می‌توان رفت.
امکان پرش مستقیم بین وضعیت‌های غیرمتوالی وجود ندارد.
ویژگی‌های اضافی:

ثبت تاریخچه تغییرات
امکان بازگشت به وضعیت قبلی
نمایش وضعیت جاری
مزایا:

انعطاف‌پذیری در مدیریت وضعیت‌ها
جداسازی منطق هر وضعیت
سهولت افزودن وضعیت‌های جدید
انعطاف‌پذیری در مدیریت وضعیت‌ها
جداسازی منطق هر وضعیت
سهولت افزودن وضعیت‌های جدید


این پیاده‌سازی به شما اجازه می‌دهد تا مدیریت وضعیت‌های تسک را به صورت منظم و کنترل‌شده انجام دهید.