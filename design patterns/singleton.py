class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# استفاده از Singleton
singleton1 = Singleton()
singleton2 = Singleton()

# True، به این معنی که هر دو متغیر به یک نمونه اشاره می‌کنند
print(singleton1 is singleton2)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class SingletonClass:
    pass


# استفاده از SingletonClass
singleton1 = SingletonClass()
singleton2 = SingletonClass()

print(singleton1 is singleton2)  # True




class Singleton:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


class DatabaseHandler(Singleton):
    pass


class SSHConnectionHandler(Singleton):
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = DatabaseHandler()
    s3 = SSHConnectionHandler()

    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(id(s1) == id(s2) == id(s3))



   # در این روش، از یک متغیر کلاس برای نگهداری تنها یک نمونه از کلاس استفاده می‌کنیم
   class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# ایجاد یک کلاس فرزند
class ChildSingleton(Singleton):
    pass

# تست خروجی
singleton1 = Singleton()
singleton2 = Singleton()
child1 = ChildSingleton()
child2 = ChildSingleton()

print(singleton1 is singleton2)  # True
print(child1 is child2)           # True
print(singleton1 is child1)       # False، زیرا ChildSingleton از Singleton ارث بری نمی‌کند


# در این روش، می‌توانیم یک متا کلاس تعریف کنیم که به ما اجازه می‌دهد از آن به عنوان 
# Singleton
# استفاده کنیم و کلاس‌ها بتوانند به‌درستی از آن ارث بری کنند
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# استفاده از متا کلاس در کلاس Singleton
class Singleton(metaclass=SingletonMeta):
    pass

# ایجاد یک کلاس فرزند
class ChildSingleton(Singleton):
    pass

# تست خروجی
singleton1 = Singleton()
singleton2 = Singleton()
child1 = ChildSingleton()
child2 = ChildSingleton()

print(singleton1 is singleton2)  # True
print(child1 is child2)           # True
print(singleton1 is child1)       # False، زیرا ChildSingleton از Singleton ارث بری نمی‌کند