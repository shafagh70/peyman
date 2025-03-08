# طراحی بازی
#تصور کنید که در یک بازی نیاز به ایجاد شخصیت‌ها دارید و هر شخصیت ویژگی‌های خاصی به همراه دارد
#. به جای این که هر بار یک شخصیت جدید از ابتدا ایجاد کنید، می‌توانید شخصیت‌های موجود را کپی کنید.

import copy

class CharacterPrototype:
    def clone(self):
        return copy.deepcopy(self)

class Hero(CharacterPrototype):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"Hero: {self.name}, Power: {self.power}"

# ایجاد شخصیت اصلی
original_hero = Hero("Superman", "Flying")

# کپی کردن شخصیت
cloned_hero = original_hero.clone()
cloned_hero.name = "Batman"

print(original_hero)  # Hero: Superman, Power: Flying
print(cloned_hero)    # Hero: Batman, Power: Flying



# طراحی فرم‌های مختلف
#در مدیریت فرم ها (فرم های وب) می توانید از الگوی پرتوتایپ برای کپی کردن فرم های موجود استفاده کنید.
import copy

class FormPrototype:
    def clone(self):
        return copy.deepcopy(self)

class ContactForm(FormPrototype):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"ContactForm: {self.name}, Email: {self.email}"

# ایجاد فرم اصلی
original_form = ContactForm("Alice", "alice@example.com")

# کپی کردن فرم
cloned_form = original_form.clone()
cloned_form.name = "Bob"

print(original_form)  # ContactForm: Alice, Email: alice@example.com
print(cloned_form)     # ContactForm: Bob, Email: alice@example.com


# مستندات و الگوهای مختلف

# به جای نوشتن مجدد هر یک، می‌توانید از یک الگو استفاده کنید.فرض کنید نیاز دارید مدرک‌ها یا نامه‌های مشابهی بنویسید
import copy

class DocumentPrototype:
    def clone(self):
        return copy.deepcopy(self)

class Document(DocumentPrototype):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Document: {self.title}\nContent: {self.content}"

# ایجاد مدرک اصلی
original_document = Document("Meeting Notes", "Today we discussed...")

# کپی کردن مدرک
cloned_document = original_document.clone()
cloned_document.title = "Meeting Notes - Revision"

print(original_document)  # Document: Meeting Notes
print(cloned_document)     # Document: Meeting Notes - Revision

