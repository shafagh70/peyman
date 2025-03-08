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
