from datetime import time, date


class IncorrectTimeRangeError(Exception):
    """Время начала сеанса больше чем время конца сеанса"""


class TimeRangeIntersectionError(Exception):
    """Сеансы в данном зале пересекаются по времени"""


class Seat:
    def __init__(self):
        self.taken = False

    def take(self):
        self.taken = True

    def release(self):
        self.taken = False

    def is_taken(self):
        return self.taken


class Session:
    def __init__(self, name: str, hall_length: int, hall_width: int, start_time: time, end_time: time, day: date):
        """Будем считать что для каждой сессии зал, в котором эта сессия проходит, будет отдельной сущностью,
        т.е сам зал хранит только информацию о своем размере, а матрица с местами у каждой сессии отдельная"""
        if start_time >= end_time:
            raise IncorrectTimeRangeError('End time must be more than start time')
        self.seat_matrix = [[Seat() for __ in range(hall_length)] for _ in range(hall_width)]
        self.hall_length = hall_length
        self.hall_width = hall_width
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def get_seat(self, row, col):
        return self.seat_matrix[row - 1][col - 1]

    def is_taken(self, row, col):
        return self.get_seat(row, col).is_taken()

    def take(self, row, col):
        self.get_seat(row, col).take()

    def release(self, row, col):
        self.get_seat(row, col).release()

    def get_name(self):
        return self.name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def __str__(self):
        res = '   '
        cols_s = ''.join(map(lambda x: str(x).rjust(3), range(1, self.hall_length + 1)))
        res += cols_s + '\n'
        for i in range(1, self.hall_width + 1):
            res += str(i).rjust(3)
            res += ''.join(map(lambda x: '  1' if x.is_taken() else '  0', self.seat_matrix[i - 1]))
            res += '\n'
        return res

    def __repr__(self):
        s = f'Session("{self.name}", {self.hall_width}, {self.hall_width}, \
{repr(self.start_time)}, {repr(self.end_time)})'

        return s


class Hall:
    def __init__(self, hall_name: str, length: int, width: int):
        """Места в зале представлены прямоугольной матрицей размером width строк и length столбцов"""
        self.seat_matrix = [[Seat() for __ in range(length)] for _ in range(width)]
        self.length = length
        self.width = width
        self.hall_name = hall_name
        self.sessions = {}

    def add_session(self, session_name: str, start_time: time, end_time: time, day: date):
        for session in self.sessions.values():
            session: Session
            if (session.get_start_time() <= start_time <= session.get_end_time() or
                    session.get_start_time() <= end_time <= session.get_end_time()):
                raise TimeRangeIntersectionError

        self.sessions.setdefault(session_name,
                                 Session(session_name, self.length, self.width, start_time, end_time, day))

    def del_session(self, session_name: str):
        del self.sessions[session_name]

    def get_name(self):
        return self.hall_name

    def get_session(self, session_name: str) -> Session:
        return self.sessions[session_name]

    def get_sessions(self):
        return list(self.sessions)

    def __repr__(self):
        return f'Hall("{self.hall_name}", {self.length}, {self.width})'


class Cinema:
    def __init__(self, name: str):
        self.name = name
        self.halls = {}

    def add_hall(self, hall: Hall):
        self.halls.setdefault(hall.get_name(), hall)

    def del_hall(self, hall_name: str):
        del self.halls[hall_name]

    def get_hall(self, hall_name: str):
        return self.halls[hall_name]

    def get_name(self):
        return self.name

    def get_halls(self):
        return list(self.halls)

    def __repr__(self):
        return f'Cinema("{self.name}")'


class CinemaNet:
    def __init__(self, name: str):
        self.name = name
        self.cinemas = {}

    def add_cinema(self, cinema: Cinema):
        self.cinemas.setdefault(cinema.get_name(), cinema)

    def del_cinema(self, cinema: str):
        del self.cinemas[cinema]

    def get_cinema(self, cinema_name: str):
        return self.cinemas[cinema_name]

    def get_name(self):
        return self.name

    def get_cinemas(self):
        return list(self.cinemas)

    def __repr__(self):
        return f'CinemaNet("{self.name}")'


if __name__ == '__main__':
    hall = Hall('A', 10, 10)
    hall.del_session('1')
    hall.add_session('1', time(14), time(16))
    print(repr(hall.get_session('1')))
    # hall.add_session('1', time(14), time(16))
