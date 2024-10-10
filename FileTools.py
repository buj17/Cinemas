import xlsxwriter
from cinemas import CinemaNet, Cinema, Hall, Session


def create_schedule(cinema_net: CinemaNet, start_date, end_date):
    workbook = xlsxwriter.Workbook('schedule.xlsx')
    worksheet = workbook.add_worksheet()
    header = ('Кинотеатр', 'Сеанс', 'Дата проведения', 'Время начала', 'Время окончания')
    for index, element in enumerate(header):
        worksheet.write(0, index, element)

    data = []

    for cinema_name in cinema_net.get_cinemas():
        cinema: Cinema = cinema_net.get_cinema(cinema_name)

        for hall_name in cinema.get_halls():
            hall: Hall = cinema.get_hall(hall_name)

            for session_name in hall.get_sessions():
                session: Session = hall.get_session(session_name)

                session_date = session.get_day()

                if start_date <= session_date <= end_date:
                    data.append((cinema.get_name(),
                                 session.get_name(),
                                 session.get_day(),
                                 session.get_start_time(),
                                 session.get_end_time()))

    data.sort(key=lambda x: (x[2], x[3], x[0], x[1]))

    for index, (cinema_name, session_name, day, start_time, end_time) in enumerate(data, 1):
        day_text = day.strftime('%d.%m.%Y')
        start_time_text = start_time.strftime('%H:%M')
        end_time_text = end_time.strftime('%H:%M')

        worksheet.write(index, 0, cinema_name)
        worksheet.write(index, 1, session_name)
        worksheet.write(index, 2, day_text)
        worksheet.write(index, 3, start_time_text)
        worksheet.write(index, 4, end_time_text)

    workbook.close()
