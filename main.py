# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *
from threading import Thread
import cv2
from db import Database


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")

        self.ui.btn_insert_emploees.clicked.connect(self.new_employees)
        self.ui.btn_list_emploees.clicked.connect(self.show_employees)
        self.ui.btn_edit_emploees.clicked.connect(self.edit_employees)

        self.ui.show()

    def show_employees(self):
        window.hide()
        show_employees.ui.show()

    def new_employees(self):
        window.hide()
        new_employees.ui.show()

    def edit_employees(self):
        window.hide()
        edit_employees.ui.show()


class Edit_employees(Main):
    def __init__(self):
        super(Edit_employees, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form_edit.ui')

        self.ui.btn_confirm.clicked.connect(self.confirm)

    def confirm(self):
        name_choice = self.ui.btn_choice_name.text()
        name = self.ui.lbl_name.text()
        family = self.ui.lbl_family.text()
        code = self.ui.lbl_code.text()
        date = self.ui.lbl_date.text()

        Database.update(code, name, family, date, name_choice)

        msg = QMessageBox()
        msg.setText('Done')
        msg.exec_()

        name_choice = self.ui.btn_choice_name.setText('')
        name = self.ui.lbl_name.setText('')
        family = self.ui.lbl_family.setText('')
        code = self.ui.lbl_code.setText('')
        date = self.ui.lbl_date.setText('')


class Show_employees(Main):
    def __init__(self):
        super(Show_employees, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form_show.ui')
        self.db_select = Database.select()

        for db in self.db_select:
            self.read_from_db(db[0], db[1], db[2], db[3], 'detect_face.jpg', )

    def read_from_db(self, code, name, family, date, pic):
        label_code = QLabel()
        label_code.setStyleSheet(
            'background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 75 12pt "MS Shell Dlg 2";')
        label_code.setText(f'{code}')

        label_name = QLabel()
        label_name.setStyleSheet(
            'background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 75 12pt "MS Shell Dlg 2";')
        label_name.setText(f'{name}')

        label_family = QLabel()
        label_family.setStyleSheet(
            'background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 75 12pt "MS Shell Dlg 2";')
        label_family.setText(f'{family}')

        label_date = QLabel()
        label_date.setStyleSheet(
            'background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 75 12pt "MS Shell Dlg 2";')
        label_date.setText(f'{date}')

        label_pic = QLabel()
        label_pic.setStyleSheet(
            'background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 75 12pt "MS Shell Dlg 2";')
        label_pic.setPixmap(QPixmap(f'{pic}'))

        self.ui.hl_code.addWidget(label_code)
        self.ui.hl_name.addWidget(label_name)
        self.ui.hl_family.addWidget(label_family)
        self.ui.hl_date.addWidget(label_date)
        self.ui.hl_pictures_.addWidget(label_pic)


class New_employees(Main):
    def __init__(self):
        super(New_employees, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form_new.ui')

        self.ui.btn_send.clicked.connect(self.new_employee)

        self.ui.btn_camera.clicked.connect(self.webcam)

        self.ui.btn_faces.clicked.connect(self.face)

        self.ui.btn_face_color.clicked.connect(self.face_color)

        self.ui.face_black_white.clicked.connect(self.face_black_white)

        self.ui.btn_blur.clicked.connect(self.btn_blur)

        self.ui.btn_purple.clicked.connect(self.btn_purple)

        self.ui.btn_gray.clicked.connect(self.btn_gray)

    def btn_gray(self):
        thread = Thread(target=self.btn_grays)
        thread.start()

    def btn_grays(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)
        while True:
            validation, frame = video_cap.read(0)
            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)

            for (x, y, w, h) in faces:
                detect_face = frame_gray[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

            cv2.imwrite('face_gray.jpg', frame_gray)
            self.ui.lbl_camera.setPixmap(QPixmap('face_gray.jpg'))
        video_cap.release()

    def btn_purple(self):
        thread = Thread(target=self.btn_purples)
        thread.start()

    def btn_purples(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)
        while True:
            validation, frame = video_cap.read(0)
            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)

            for (x, y, w, h) in faces:
                frame = 255 - frame
                detect_face = frame[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

            cv2.imwrite('face_purple.jpg', frame)
            self.ui.lbl_camera.setPixmap(QPixmap('face_purple.jpg'))
        video_cap.release()

    def btn_blur(self):
        thread = Thread(target=self.btn_blurs)
        thread.start()

    def btn_blurs(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)
        while True:
            validation, frame = video_cap.read(0)
            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)
            for (x, y, w, h) in faces:
                frame_gray = 255 - frame_gray

                frame_gray = cv2.GaussianBlur(frame_gray, (21, 21), 0)

                detect_face = frame_gray[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

            cv2.imwrite('face_blur.jpg', frame_gray)
            self.ui.lbl_camera.setPixmap(QPixmap('face_blur.jpg'))
        video_cap.release()

    def face_black_white(self):
        thread = Thread(target=self.face_black_whites)
        thread.start()

    def face_black_whites(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)
        while True:
            validation, frame = video_cap.read(0)
            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)
            for (x, y, w, h) in faces:
                frame_gray_2 = 255 - frame_gray

                frame_gray_2 = cv2.GaussianBlur(frame_gray_2, (21, 21), 0)

                output = cv2.divide(frame_gray, 255 - frame_gray_2, scale=256.0)

                detect_face = output[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

                cv2.imwrite('face_black_white.jpg', output)
            self.ui.lbl_camera.setPixmap(QPixmap('face_black_white.jpg'))
        video_cap.release()

    def face_color(self):
        thread = Thread(target=self.face_colors)
        thread.start()

    def face_colors(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)
        while True:
            validation, frame = video_cap.read(0)
            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)

            for (x, y, w, h) in faces:
                frame_gray = 255 - frame_gray
                detect_face = frame_gray[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

            cv2.imwrite('face_color.jpg', frame_gray)
            self.ui.lbl_camera.setPixmap(QPixmap('face_color.jpg'))
        video_cap.release()

    def face(self):
        thread = Thread(target=self.faces)
        thread.start()

    def faces(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)

        while True:
            validation, frame = video_cap.read()

            if validation is not True:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(frame_gray, 1.3)

            for (x, y, w, h) in faces:
                rows, columns = frame_gray.shape

                half_frame = frame_gray[0:rows, 0:columns // 2]
                flip_frame = cv2.flip(half_frame, 1)
                frame_gray[:, columns // 2:] = flip_frame

                detect_face = frame_gray[y:y + h, x:x + w]
                cv2.imwrite('detect_face.jpg', detect_face)

            cv2.imwrite('faces.jpg', frame_gray)
            self.ui.lbl_camera.setPixmap(QPixmap('faces'))
        video_cap.release()

    def webcam(self):
        thread = Thread(target=self.start_webcam)
        thread.start()

    def start_webcam(self):
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_cap = cv2.VideoCapture(0)

        while True:
            validation, frame = video_cap.read()

            if validation is not True:
                break

            frame_gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(frame_gary, 1.3)
            for i, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
                self.detect_face = frame[y:y + h, x:x + w]
                cv2.imwrite(f'detect_face.jpg', self.detect_face)

            cv2.imwrite('face.jpg', frame)
            self.ui.lbl_camera.setPixmap(QPixmap('face.jpg'))
        video_cap.release()

    def new_employee(self):
        code = self.ui.txt_code.text()
        name = self.ui.txt_name.text()
        family = self.ui.txt_family.text()
        date = self.ui.txt_birth.text()
        if name != '' and family != '' and date != '':
            response = Database.insert(code, name, family, date)
            if response == True:
                show_employees.read_from_db(code, name, family, date, 'detect_face.jpg')

                code = self.ui.txt_code.setText('')
                name = self.ui.txt_name.setText('')
                family = self.ui.txt_family.setText('')
                date = self.ui.txt_birth.setText('')

                msg = QMessageBox()
                msg.setText('Done')
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText('Error: Fill In All The Fields')
            msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    show_employees = Show_employees()
    new_employees = New_employees()
    edit_employees = Edit_employees()
    sys.exit(app.exec_())
