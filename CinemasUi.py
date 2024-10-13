# Form implementation generated from reading ui file 'second_version.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(870, 605)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cinemas_tree = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.cinemas_tree.setGeometry(QtCore.QRect(600, 10, 261, 261))
        self.cinemas_tree.setObjectName("cinemas_tree")
        self.add_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.add_widget.setGeometry(QtCore.QRect(10, 10, 571, 331))
        self.add_widget.setObjectName("add_widget")
        self.add_cinema_widget = QtWidgets.QWidget(parent=self.add_widget)
        self.add_cinema_widget.setGeometry(QtCore.QRect(0, 0, 251, 71))
        self.add_cinema_widget.setObjectName("add_cinema_widget")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.add_cinema_widget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 251, 41))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.add_cinema_layout = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.add_cinema_layout.setContentsMargins(0, 0, 0, 0)
        self.add_cinema_layout.setObjectName("add_cinema_layout")
        self.cinema_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.cinema_label.setObjectName("cinema_label")
        self.add_cinema_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cinema_label)
        self.cinema_edit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.cinema_edit.setObjectName("cinema_edit")
        self.add_cinema_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cinema_edit)
        self.add_cinema_button = QtWidgets.QPushButton(parent=self.add_cinema_widget)
        self.add_cinema_button.setEnabled(False)
        self.add_cinema_button.setGeometry(QtCore.QRect(0, 40, 251, 31))
        self.add_cinema_button.setObjectName("add_cinema_button")
        self.add_hall_widget = QtWidgets.QWidget(parent=self.add_widget)
        self.add_hall_widget.setGeometry(QtCore.QRect(0, 110, 251, 141))
        self.add_hall_widget.setObjectName("add_hall_widget")
        self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.add_hall_widget)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 251, 112))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.add_hall_layout = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.add_hall_layout.setContentsMargins(0, 0, 0, 0)
        self.add_hall_layout.setObjectName("add_hall_layout")
        self.hall_form_cinema_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        self.hall_form_cinema_combo_box.setObjectName("hall_form_cinema_combo_box")
        self.add_hall_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hall_form_cinema_combo_box)
        self.hall_edit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_5)
        self.hall_edit.setEnabled(False)
        self.hall_edit.setObjectName("hall_edit")
        self.add_hall_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hall_edit)
        self.hall_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.hall_label.setObjectName("hall_label")
        self.add_hall_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.hall_label)
        self.length_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.length_label.setObjectName("length_label")
        self.add_hall_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.length_label)
        self.length_spin_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
        self.length_spin_box.setEnabled(False)
        self.length_spin_box.setMinimum(1)
        self.length_spin_box.setMaximum(30)
        self.length_spin_box.setProperty("value", 1)
        self.length_spin_box.setObjectName("length_spin_box")
        self.add_hall_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.length_spin_box)
        self.width_spin_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
        self.width_spin_box.setEnabled(False)
        self.width_spin_box.setMinimum(1)
        self.width_spin_box.setMaximum(30)
        self.width_spin_box.setProperty("value", 1)
        self.width_spin_box.setObjectName("width_spin_box")
        self.add_hall_layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.width_spin_box)
        self.width_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.width_label.setObjectName("width_label")
        self.add_hall_layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.width_label)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.add_hall_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.add_hall_button = QtWidgets.QPushButton(parent=self.add_hall_widget)
        self.add_hall_button.setEnabled(False)
        self.add_hall_button.setGeometry(QtCore.QRect(0, 110, 251, 31))
        self.add_hall_button.setObjectName("add_hall_button")
        self.add_session_widget = QtWidgets.QWidget(parent=self.add_widget)
        self.add_session_widget.setGeometry(QtCore.QRect(270, 0, 301, 251))
        self.add_session_widget.setObjectName("add_session_widget")
        self.formLayoutWidget_6 = QtWidgets.QWidget(parent=self.add_session_widget)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 301, 221))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.add_session_layout = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.add_session_layout.setContentsMargins(0, 0, 0, 0)
        self.add_session_layout.setObjectName("add_session_layout")
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.add_session_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.session_form_cinema_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_6)
        self.session_form_cinema_combo_box.setObjectName("session_form_cinema_combo_box")
        self.add_session_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.session_form_cinema_combo_box)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.label_6.setObjectName("label_6")
        self.add_session_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.session_form_hall_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_6)
        self.session_form_hall_combo_box.setEnabled(False)
        self.session_form_hall_combo_box.setObjectName("session_form_hall_combo_box")
        self.add_session_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.session_form_hall_combo_box)
        self.hall_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.hall_label_3.setObjectName("hall_label_3")
        self.add_session_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.hall_label_3)
        self.session_edit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_6)
        self.session_edit.setEnabled(False)
        self.session_edit.setObjectName("session_edit")
        self.add_session_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.session_edit)
        self.date_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.date_label.setObjectName("date_label")
        self.add_session_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.date_label)
        self.date_edit = QtWidgets.QDateEdit(parent=self.formLayoutWidget_6)
        self.date_edit.setEnabled(False)
        self.date_edit.setObjectName("date_edit")
        self.add_session_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.date_edit)
        self.start_time_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.start_time_label.setObjectName("start_time_label")
        self.add_session_layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.start_time_label)
        self.start_time_edit = QtWidgets.QTimeEdit(parent=self.formLayoutWidget_6)
        self.start_time_edit.setEnabled(False)
        self.start_time_edit.setObjectName("start_time_edit")
        self.add_session_layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.start_time_edit)
        self.end_time_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.end_time_label.setObjectName("end_time_label")
        self.add_session_layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.end_time_label)
        self.end_time_edit = QtWidgets.QTimeEdit(parent=self.formLayoutWidget_6)
        self.end_time_edit.setEnabled(False)
        self.end_time_edit.setObjectName("end_time_edit")
        self.add_session_layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.end_time_edit)
        self.warning_session_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        self.warning_session_label.setObjectName("warning_session_label")
        self.add_session_layout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.warning_session_label)
        self.add_session_button = QtWidgets.QPushButton(parent=self.add_session_widget)
        self.add_session_button.setEnabled(False)
        self.add_session_button.setGeometry(QtCore.QRect(0, 220, 301, 31))
        self.add_session_button.setObjectName("add_session_button")
        self.label_8 = QtWidgets.QLabel(parent=self.add_widget)
        self.label_8.setGeometry(QtCore.QRect(0, 270, 531, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.add_widget)
        self.label_9.setGeometry(QtCore.QRect(0, 290, 531, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.add_widget)
        self.label_10.setGeometry(QtCore.QRect(0, 310, 531, 21))
        self.label_10.setObjectName("label_10")
        self.configure_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.configure_widget.setGeometry(QtCore.QRect(10, 370, 451, 161))
        self.configure_widget.setObjectName("configure_widget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.configure_widget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 451, 93))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.cinema_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.cinema_label_2.setObjectName("cinema_label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cinema_label_2)
        self.cinema_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.cinema_combo_box.setObjectName("cinema_combo_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cinema_combo_box)
        self.hall_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.hall_label_2.setObjectName("hall_label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.hall_label_2)
        self.hall_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.hall_combo_box.setEnabled(False)
        self.hall_combo_box.setObjectName("hall_combo_box")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hall_combo_box)
        self.session_combo_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.session_combo_box.setEnabled(False)
        self.session_combo_box.setObjectName("session_combo_box")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.session_combo_box)
        self.session_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.session_label_2.setObjectName("session_label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.session_label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.configure_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 451, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_cinema_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.delete_cinema_button.setObjectName("delete_cinema_button")
        self.horizontalLayout.addWidget(self.delete_cinema_button)
        self.delete_hall_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.delete_hall_button.setEnabled(False)
        self.delete_hall_button.setObjectName("delete_hall_button")
        self.horizontalLayout.addWidget(self.delete_hall_button)
        self.delete_session_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.delete_session_button.setEnabled(False)
        self.delete_session_button.setObjectName("delete_session_button")
        self.horizontalLayout.addWidget(self.delete_session_button)
        self.go_to_session_button = QtWidgets.QPushButton(parent=self.configure_widget)
        self.go_to_session_button.setEnabled(False)
        self.go_to_session_button.setGeometry(QtCore.QRect(0, 130, 451, 31))
        self.go_to_session_button.setObjectName("go_to_session_button")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(520, 350, 301, 181))
        self.widget.setObjectName("widget")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 30, 301, 67))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.schedule_start_date = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.schedule_start_date.setObjectName("schedule_start_date")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.schedule_start_date)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
        self.schedule_end_date = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.schedule_end_date.setObjectName("schedule_end_date")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.schedule_end_date)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.label.setObjectName("label")
        self.create_schedule_button = QtWidgets.QPushButton(parent=self.widget)
        self.create_schedule_button.setGeometry(QtCore.QRect(0, 100, 301, 31))
        self.create_schedule_button.setObjectName("create_schedule_button")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 130, 301, 21))
        self.label_7.setObjectName("label_7")
        self.warning_schedule_label = QtWidgets.QLabel(parent=self.widget)
        self.warning_schedule_label.setGeometry(QtCore.QRect(0, 160, 301, 21))
        self.warning_schedule_label.setText("")
        self.warning_schedule_label.setObjectName("warning_schedule_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cinemas_tree.headerItem().setText(0, _translate("MainWindow", "Кинотеатры"))
        self.cinema_label.setText(_translate("MainWindow", "Название кинотеатра"))
        self.add_cinema_button.setText(_translate("MainWindow", "Добавить кинотеатр"))
        self.hall_label.setText(_translate("MainWindow", "Название зала"))
        self.length_label.setText(_translate("MainWindow", "Мест в ряду"))
        self.width_label.setText(_translate("MainWindow", "Количество рядов"))
        self.label_4.setText(_translate("MainWindow", "Выберите кинотеатр"))
        self.add_hall_button.setText(_translate("MainWindow", "Добавить зал"))
        self.label_5.setText(_translate("MainWindow", "Выберите кинотеатр"))
        self.label_6.setText(_translate("MainWindow", "Выберите зал"))
        self.hall_label_3.setText(_translate("MainWindow", "Название сеанса"))
        self.date_label.setText(_translate("MainWindow", "Дата сеанса"))
        self.start_time_label.setText(_translate("MainWindow", "Время начала"))
        self.end_time_label.setText(_translate("MainWindow", "Время окончания"))
        self.warning_session_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\"><br/></span></p></body></html>"))
        self.add_session_button.setText(_translate("MainWindow", "Добавить сеанс"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">Названия кинотеатров, залов, сеансов не должны быть пустыми или повторяться, иначе объект не создастся;</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">После заполнения выпадающих списков и названия объекта, форма для заполнения активируется;</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">Добавленные объекты можно увидеть в виджете справа от форм;</span></p></body></html>"))
        self.cinema_label_2.setText(_translate("MainWindow", "Кинотеатр"))
        self.hall_label_2.setText(_translate("MainWindow", "Зал"))
        self.session_label_2.setText(_translate("MainWindow", "Сеанс"))
        self.delete_cinema_button.setText(_translate("MainWindow", "Удалить кинотеатр"))
        self.delete_hall_button.setText(_translate("MainWindow", "Удалить зал"))
        self.delete_session_button.setText(_translate("MainWindow", "Удалить сеанс"))
        self.go_to_session_button.setText(_translate("MainWindow", "Перейти в настройку сеанса"))
        self.label_2.setText(_translate("MainWindow", "Начальная дата"))
        self.label_3.setText(_translate("MainWindow", "Конечная дата"))
        self.label.setText(_translate("MainWindow", "Сформировать расписание сеансов в excel"))
        self.create_schedule_button.setText(_translate("MainWindow", "Создать расписание"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">В папке со скриптом будет создан файл schedule.xlsx</span></p></body></html>"))
