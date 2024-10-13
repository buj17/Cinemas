from CinemasUi import Ui_MainWindow
from FileTools import create_schedule
from PyQt6.QtCore import QDate
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget, QTreeWidgetItem, QPushButton, QLabel
from cinemas import CinemaNet, Cinema, Hall, Session, IncorrectTimeRangeError, TimeRangeIntersectionError


class Cinemas(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.date = self.date_edit.setDate(QDate.currentDate())
        self.schedule_start_date.setDate(QDate.currentDate())
        self.schedule_end_date.setDate(QDate.currentDate())
        self.warning_session_label.setStyleSheet('color: red')
        self.warning_schedule_label.setStyleSheet('color: red')

        self.cinema_net = CinemaNet('Кинотеатры')

        self.cinema_edit.textChanged.connect(self.toggle_add_cinema_button)
        self.add_cinema_button.clicked.connect(self.add_cinema)

        self.hall_form_cinema_combo_box.currentTextChanged.connect(self.toggle_hall_edit)
        self.hall_edit.textChanged.connect(self.toggle_hall_params)
        self.add_hall_button.clicked.connect(self.add_hall)

        self.session_form_cinema_combo_box.currentTextChanged.connect(self._update_session_form_hall_combo_box)
        self.session_form_hall_combo_box.currentTextChanged.connect(self.toggle_session_edit)
        self.session_edit.textChanged.connect(self.toggle_session_params)
        self.add_session_button.clicked.connect(self.add_session)

        # self.create_button.clicked.connect(self.add_items)

        self.cinema_combo_box.currentIndexChanged.connect(self._update_hall_combo_box)
        self.hall_combo_box.currentIndexChanged.connect(self.update_session_combo_box)
        self.delete_cinema_button.clicked.connect(self.delete_cinema)
        self.delete_hall_button.clicked.connect(self.delete_hall)
        self.delete_session_button.clicked.connect(self.delete_session)
        self.go_to_session_button.clicked.connect(self.show_session_config_window)

        self.create_schedule_button.clicked.connect(self.create_schedule)

    def toggle_add_cinema_button(self):
        text = self.cinema_edit.text()
        if text and ' '.join(('Кинотеатр', text)) not in self.cinema_net.get_cinemas():
            self.add_cinema_button.setEnabled(True)
        else:
            self.add_cinema_button.setDisabled(True)

    def clear_cinema_form(self):
        self.cinema_edit.clear()

    def add_cinema(self):
        text = self.cinema_edit.text()
        if text and ' '.join(('Кинотеатр', text)) not in self.cinema_net.get_cinemas():
            cinema = Cinema(' '.join(('Кинотеатр', text)))
            self.cinema_net.add_cinema(cinema)
            self.clear_cinema_form()
            self.update_tree()
            self.update_cinema_combo_boxes()

    def toggle_hall_edit(self):
        text = self.hall_form_cinema_combo_box.currentText()
        if text:
            self.hall_edit.setEnabled(True)
        else:
            self.hall_edit.setDisabled(True)

    def toggle_hall_params(self):
        text = self.hall_edit.text()
        current_cinema: Cinema = self.cinema_net.get_cinema(self.hall_form_cinema_combo_box.currentText())

        if text and ' '.join(('Зал', text)) not in current_cinema.get_halls():
            self.length_spin_box.setEnabled(True)
            self.width_spin_box.setEnabled(True)
            self.add_hall_button.setEnabled(True)
        else:
            self.length_spin_box.setDisabled(True)
            self.width_spin_box.setDisabled(True)
            self.add_hall_button.setDisabled(True)

    def clear_hall_form(self):
        self.hall_edit.clear()

    def add_hall(self):
        text = self.hall_edit.text()
        current_cinema: Cinema = self.cinema_net.get_cinema(self.hall_form_cinema_combo_box.currentText())
        if text and ' '.join(('Зал', text)) not in current_cinema.get_halls():
            hall_length = self.length_spin_box.value()
            hall_width = self.width_spin_box.value()
            hall = Hall(' '.join(('Зал', text)), hall_length, hall_width)
            current_cinema.add_hall(hall)
            self.clear_hall_form()
            self.update_tree()
            self.update_hall_combo_boxes()

    def toggle_session_edit(self):
        text = self.session_form_hall_combo_box.currentText()
        if text:
            self.session_edit.setEnabled(True)
        else:
            self.session_edit.setDisabled(True)

    def toggle_session_params(self):
        text = self.session_edit.text()
        current_cinema: Cinema = self.cinema_net.get_cinema(self.session_form_cinema_combo_box.currentText())
        current_hall: Hall = current_cinema.get_hall(self.session_form_hall_combo_box.currentText())

        if text and ' '.join(('Сеанс', text)) not in current_hall.get_sessions():
            self.date_edit.setEnabled(True)
            self.start_time_edit.setEnabled(True)
            self.end_time_edit.setEnabled(True)
            self.add_session_button.setEnabled(True)
        else:
            self.date_edit.setDisabled(True)
            self.start_time_edit.setDisabled(True)
            self.end_time_edit.setDisabled(True)
            self.add_session_button.setDisabled(True)

    def add_session(self):
        text = self.session_edit.text()
        current_cinema: Cinema = self.cinema_net.get_cinema(self.session_form_cinema_combo_box.currentText())
        current_hall: Hall = current_cinema.get_hall(self.session_form_hall_combo_box.currentText())

        if text and ' '.join(('Сеанс', text)) not in current_hall.get_sessions():
            session_day = self.date_edit.date().toPyDate()
            session_start_time = self.start_time_edit.time().toPyTime()
            session_end_time = self.end_time_edit.time().toPyTime()
            try:
                current_hall.add_session(' '.join(('Сеанс', text)), session_start_time, session_end_time, session_day)
            except IncorrectTimeRangeError:
                self.show_warning_add_message('Время начала должно быть меньше времени конца')
                return None
            except TimeRangeIntersectionError:
                self.show_warning_add_message('Время данного сеанса пересекается с другим')
                return None
            else:
                self.hide_warning_add_message()
                self.clear_session_form()
                self.update_tree()
                self.update_session_combo_box()

    def clear_session_form(self):
        self.session_edit.clear()

    def update_tree(self):
        self.cinemas_tree.clear()

        for cinema_name in self.cinema_net.get_cinemas():
            cinema: Cinema = self.cinema_net.get_cinema(cinema_name)
            cinema_tree_item = QTreeWidgetItem(self.cinemas_tree)
            cinema_text = cinema.get_name()
            cinema_tree_item.setText(0, cinema_text)

            for hall_name in cinema.get_halls():
                hall: Hall = cinema.get_hall(hall_name)
                hall_tree_item = QTreeWidgetItem(cinema_tree_item)
                hall_text = hall.get_name()
                hall_tree_item.setText(0, hall_text)

                for session_name in hall.get_sessions():
                    session = hall.get_session(session_name)
                    session_tree_item = QTreeWidgetItem(hall_tree_item)
                    session_text = session.get_name()
                    session_tree_item.setText(0, session_text)

    def show_warning_add_message(self, text):
        self.warning_session_label.setText(text)

    def hide_warning_add_message(self):
        self.warning_session_label.setText('')

    def update_cinema_combo_boxes(self):
        self._update_cinema_combo_box()
        self._update_hall_form_cinema_combo_box()
        self._update_session_form_cinema_combo_box()

    def _update_cinema_combo_box(self):
        self.cinema_combo_box.clear()
        for cinema_name in self.cinema_net.get_cinemas():
            self.cinema_combo_box.addItem(cinema_name)

    def _update_hall_form_cinema_combo_box(self):
        self.hall_form_cinema_combo_box.clear()
        for cinema_name in self.cinema_net.get_cinemas():
            self.hall_form_cinema_combo_box.addItem(cinema_name)

    def _update_session_form_cinema_combo_box(self):
        self.session_form_cinema_combo_box.clear()
        for cinema_name in self.cinema_net.get_cinemas():
            self.session_form_cinema_combo_box.addItem(cinema_name)

    def update_hall_combo_boxes(self):
        self._update_hall_combo_box()
        self._update_session_form_hall_combo_box()

    def _update_hall_combo_box(self):
        self.hall_combo_box.clear()
        try:
            cinema = self.cinema_net.get_cinema(self.cinema_combo_box.currentText())
        except KeyError:
            self.hall_combo_box.setDisabled(True)
            self.delete_hall_button.setDisabled(True)
            return None

        halls = cinema.get_halls()
        for hall_name in halls:
            self.hall_combo_box.addItem(hall_name)

        if self.hall_combo_box.currentText():
            self.hall_combo_box.setEnabled(True)
            self.delete_hall_button.setEnabled(True)
        else:
            self.hall_combo_box.setDisabled(True)
            self.delete_hall_button.setDisabled(True)

    def _update_session_form_hall_combo_box(self):
        self.session_form_hall_combo_box.clear()
        try:
            cinema = self.cinema_net.get_cinema(self.session_form_cinema_combo_box.currentText())
        except KeyError:
            self.session_form_hall_combo_box.setDisabled(True)
            return None

        halls = cinema.get_halls()
        for hall_name in halls:
            self.session_form_hall_combo_box.addItem(hall_name)

        if self.session_form_hall_combo_box.currentText():
            self.session_form_hall_combo_box.setEnabled(True)
        else:
            self.session_form_hall_combo_box.setDisabled(True)

    def update_session_combo_box(self):
        self.session_combo_box.clear()
        try:
            cinema = self.cinema_net.get_cinema(self.cinema_combo_box.currentText())
            hall = cinema.get_hall(self.hall_combo_box.currentText())
        except KeyError:
            self.session_combo_box.setDisabled(True)
            self.go_to_session_button.setDisabled(True)
            self.delete_session_button.setDisabled(True)
            return None

        sessions = hall.get_sessions()
        for session_name in sessions:
            self.session_combo_box.addItem(session_name)

        if self.session_combo_box.currentText():
            self.session_combo_box.setEnabled(True)
            self.go_to_session_button.setEnabled(True)
            self.delete_session_button.setEnabled(True)
        else:
            self.session_combo_box.setDisabled(True)
            self.go_to_session_button.setDisabled(True)
            self.delete_session_button.setDefault(True)

    def update_all_combo_boxes(self):
        self.update_cinema_combo_boxes()
        self._update_hall_combo_box()
        self.update_session_combo_box()

    def delete_cinema(self):
        cinema_name = self.cinema_combo_box.currentText()
        if cinema_name:
            self.cinema_net.del_cinema(cinema_name)
            self.update_tree()
            self.update_all_combo_boxes()

    def delete_hall(self):
        hall_name = self.hall_combo_box.currentText()
        if hall_name:
            cinema = self.cinema_net.get_cinema(self.cinema_combo_box.currentText())
            cinema.del_hall(hall_name)
            self.update_tree()
            self.update_all_combo_boxes()

    def delete_session(self):
        session_name = self.session_combo_box.currentText()
        if session_name:
            cinema = self.cinema_net.get_cinema(self.cinema_combo_box.currentText())
            hall = cinema.get_hall(self.hall_combo_box.currentText())
            hall.del_session(session_name)
            self.update_tree()
            self.update_all_combo_boxes()

    def show_session_config_window(self):
        cinema = self.cinema_net.get_cinema(self.cinema_combo_box.currentText())
        hall = cinema.get_hall(self.hall_combo_box.currentText())
        session_to_config = hall.get_session(self.session_combo_box.currentText())

        self.session_config_window = SessionConfigWindow(self, session_to_config)
        self.session_config_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.session_config_window.show()

    def show_warning_schedule_message(self, text):
        self.warning_schedule_label.setText(text)

    def hide_warning_schedule_message(self):
        self.warning_schedule_label.setText('')

    def create_schedule(self):
        start_date = self.schedule_start_date.date().toPyDate()
        end_date = self.schedule_end_date.date().toPyDate()

        if start_date > end_date:
            self.show_warning_schedule_message("Начальная дата больше конечной")
        else:
            self.hide_warning_schedule_message()

        create_schedule(self.cinema_net, start_date, end_date)


class SessionConfigWindow(QWidget):
    def __init__(self, parent, session):
        super().__init__()
        self.parent = parent
        self.session: Session = session
        self.button_matrix = []
        self.initUI()

    def initUI(self):
        self.resize(500, 500)

        rows, cols = self.session.hall_width, self.session.hall_length

        for row in range(rows):
            self.button_matrix.append([])
            for col in range(cols):
                seat = self.session.get_seat(row, col)
                if seat.is_taken():
                    text = '*'
                else:
                    text = ''

                btn = QPushButton(text, self)
                btn.resize(30, 30)
                btn.move(10 + 30 * col, 10 + 30 * row)
                btn.clicked.connect(self.seat_config)
                self.button_matrix[-1].append(btn)

        self.info_label = QLabel('* - место занято, пустая строка - место свободно', self)
        self.info_label.move(10, 15 + 30 * rows)

        self.save_and_quit_button = QPushButton('Сохранить и выйти', self)
        self.save_and_quit_button.move(10, 45 + 30 * rows)
        self.save_and_quit_button.clicked.connect(self.save_and_quit)

    def seat_config(self):
        if self.sender().text() == '*':
            self.sender().setText('')
        else:
            self.sender().setText('*')

    def save_and_quit(self):
        rows, cols = self.session.hall_width, self.session.hall_length

        for row in range(rows):
            for col in range(cols):
                seat = self.session.get_seat(row, col)
                text = self.button_matrix[row][col].text()
                if text == '*':
                    seat.take()
                else:
                    seat.release()

        self.close()
