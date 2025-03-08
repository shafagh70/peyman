class Cineam:
    pass


class Movie:
    pass


class Time:
    pass 
     

class Hall:
    def __init__(self, name, cineam, capacity):
        self.name = name
        self.cineam = cineam
        self.capacity = capacity

class Seat:
    def __init__(self,number):
        self.number = number
        self.status = None
        self.customer = None

class Sens:
    def __init__(self, cineam, movie, time, hall):
        self.cineam = cineam
        self.movie = movie
        self.time = time
        self.hall = hall
        self.Seat = []
        self.prototype_seats()

        def prototype_seat(self):
            for i in range(self.hall.capacity):
                self.Seat.append(Seat(i))

if '__name__' = '__main__':
    cinema = cinema()
    movie = movie()
    time = time()
    hall = hall('shafagh',cinema, 90)

    print(len(sens.seats))



    import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def clone(self):
        # متد برای ایجاد کپی عمیق از نمونه فعلی
        return copy.deepcopy(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# استفاده از کلاس
if __name__ == "__main__":
    # ایجاد یک نمونه اصلی
    original_person = Person("Alice", 30)

    # کپی کردن نمونه
    cloned_person = original_person.clone()
    cloned_person.name = "Bob"  # تغییر نام در کپی
    cloned_person.age = 25       # تغییر سن در کپی

    # نمایش اطلاعات
    print(original_person)  # خروجی: Name: Alice, Age: 30
    print(cloned_person)     # خروجی: Name: Bob, Age: 25
