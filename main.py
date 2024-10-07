import sys
from datetime import date

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QTreeWidgetItem
from cinemas import CinemaNet, Cinema, Hall
from ex import Ui_MainWindow


class Cinemas(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cinema_net = CinemaNet('Кинотеатры')

        self.cinema_edit.textChanged.connect(self.block_unblock_hall_edit)

        self.hall_edit.textChanged.connect(self.block_unblock_session_line)

        self.session_edit.textChanged.connect(self.block_unblock_session_params)

        self.create_button.clicked.connect(self.add_items)

    def block_unblock_hall_edit(self):
        if self.cinema_edit.text():
            self._unblock_hall_edit()
            if self.hall_edit.text():
                self._unblock_session_edit()
        else:
            self._block_hall_edit()
            self._block_session_edit()

    def block_unblock_session_line(self):
        if self.hall_edit.text():
            self._unblock_session_line()
            if self.session_edit.text():
                self._unblock_session_params()
        else:
            self._block_session_line()
            self._block_session_params()

    def block_unblock_session_params(self):
        if self.session_edit.text():
            self._unblock_session_params()
        else:
            self._block_session_params()

    def _block_hall_line(self):
        self.hall_edit.setDisabled(True)

    def _block_hall_params(self):
        self.length_spin_box.setDisabled(True)
        self.width_spin_box.setDisabled(True)

    def _block_hall_edit(self):
        self._block_hall_line()
        self._block_hall_params()

    def _unblock_hall_line(self):
        self.hall_edit.setEnabled(True)

    def _unblock_hall_params(self):
        self.length_spin_box.setEnabled(True)
        self.width_spin_box.setEnabled(True)

    def _unblock_hall_edit(self):
        self._unblock_hall_line()
        self._unblock_hall_params()

    def _block_session_line(self):
        self.session_edit.setDisabled(True)

    def _block_session_params(self):
        self.date_edit.setDisabled(True)
        self.start_time_edit.setDisabled(True)
        self.end_time_edit.setDisabled(True)

    def _block_session_edit(self):
        self._block_session_line()
        self._block_session_params()

    def _unblock_session_line(self):
        self.session_edit.setEnabled(True)

    def _unblock_session_params(self):
        self.date_edit.setEnabled(True)
        self.start_time_edit.setEnabled(True)
        self.end_time_edit.setEnabled(True)

    def _unblock_session_edit(self):
        self._unblock_session_line()
        self._unblock_session_params()

    def add_items(self):
        if self.cinema_edit.text():
            cinema_name = ' '.join(('Кинотеатр', self.cinema_edit.text()))
        else:
            cinema_name = None

        if self.hall_edit.isEnabled() and self.hall_edit.text():
            hall_name = ' '.join(('Зал', self.hall_edit.text()))
            hall_length = self.length_spin_box.value()
            hall_width = self.width_spin_box.value()
        else:
            hall_name = hall_length = hall_width = None

        if self.session_edit.isEnabled() and self.session_edit.text():
            session_name = ' '.join(('Сеанс', self.session_edit.text()))
            session_date = date(*self.date_edit.date().getDate())
            session_start_time = self.start_time_edit.time().toPyTime()
            session_end_time = self.end_time_edit.time().toPyTime()
        else:
            session_name = session_date = session_start_time = session_end_time = None

        if cinema_name:
            if cinema_name in self.cinema_net.get_cinemas():
                cinema = self.cinema_net.get_cinema(cinema_name)
            else:
                cinema = Cinema(cinema_name)
                self.cinema_net.add_cinema(cinema)
        else:
            cinema = None

        if hall_name:
            if hall_name in cinema.get_halls():
                hall = cinema.get_hall(hall_name)
            else:
                hall = Hall(hall_name, hall_length, hall_width)
                cinema.add_hall(hall)
        else:
            hall = None

        if session_name:
            if session_name not in hall.get_sessions():
                try:
                    hall.add_session(session_name, session_start_time, session_end_time)
                except Exception as err:
                    print(type(err))

        self.update_tree()

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

    def show_warning_message(self, text):
        pass

    def hide_warning_message(self):
        self.warning_session_label.setText('')
        self.warning_session_label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cinemas()
    ex.show()
    sys.exit(app.exec())
