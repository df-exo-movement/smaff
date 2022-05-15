from random import randrange
from random import choice
import json
import os
import numpy as np

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
# import tensorflow as tf
from keras.models import load_model


class StartPage(Screen):
    pass


class MaFF(Image):
    def __init__(self, **kwargs):
        super(MaFF, self).__init__(**kwargs)
        self.feed = None
        self.face = None
        self.label = None
        self.img_model = None
        self.clock = Clock
        self.ans = 'Start'

    def unloadcamera(self):
        self.feed.release()
        self.clock.unschedule(self.update)

    def loadcamera(self):
        self.feed = cv2.VideoCapture(0)
        self.face = cv2.CascadeClassifier('faceclassifier\haarcascade_frontalface_alt.xml')
        self.label = ['Happy', 'Sad', 'Angry', 'Disgust', 'Fear', 'Surpise', 'Neutral']
        self.img_model = load_model("./faceclassifier/emotion.h5")
        self.clock.schedule_interval(self.update, 1.0 / 33.0)

    def update(self, *args):
        ret, frame = self.feed.read()
        height, width = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(frame, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED)
        faces = self.face.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 2)
            facex = frame[y:y + h, x:x + w]
            facex = cv2.cvtColor(facex, cv2.COLOR_BGR2GRAY)
            facex = cv2.resize(facex, (200, 200))
            facex = facex / 255
            facex = facex.reshape(200, 200, -1)
            facex = np.expand_dims(facex, axis=0)
            prepred_face = self.img_model.predict(facex)
            prediction = np.argmax(prepred_face, axis=1)
            lbl = None
            if prediction[0] == 0:
                lbl = 'Angry'
                self.ans = 'Angry'

            if prediction[0] == 1:
                lbl = 'Happy'
                self.ans = 'Happy'

            if prediction[0] == 2:
                lbl = 'Sad'
                self.ans = 'Sad'

            if prediction[0] == 3:
                lbl = 'Surprised'
                self.ans = 'Surprised'

            cv2.putText(frame, lbl, (10, height - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        bufImg = cv2.flip(frame, 0).tobytes()
        img_txtur = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_txtur.blit_buffer(bufImg, colorfmt='bgr', bufferfmt='ubyte')
        self.texture = img_txtur


class Login(Screen):
    user_name = StringProperty("")
    password = StringProperty("")
    authenticated = BooleanProperty(False)

    def verify(self, user, passwd):
        p_file = open("./userdata/profiles.json")
        profiles = json.load(p_file)
        pass_lookup = None
        u = str(user)
        p = str(passwd)
        try:
            pass_lookup = profiles[u]["password"]
        except:
            pass
        if p == pass_lookup:
            self.authenticated = True
        else:
            self.authenticated = False
        p_file.close()


class CreateProfile(Screen):
    def createUser(self, user, password):
        p_file = open("./userdata/profiles.json", 'r+')
        profiles = json.load(p_file)

        u = str(user)
        p = str(password)

        profiles[u] = {"password": p}
        try:
            p_file.seek(0)
            json.dump(profiles, p_file)
            p_file.close()
        except:
            print(profiles)


class MainMenu(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CameraPage(Screen):
    pass
    # def switch_click(self, switchObject, switchValue):
    #     print(switchValue)


class SelectDiff(Screen):
    difficulty = "Easy"


class HardQuestionPage(Screen):
    q_file = open("./Questions/Hard/questions.json")
    q = json.load(q_file)

    count = 1
    chosen = []
    initQuestion = randrange(1, 12)
    chosen.append(initQuestion)
    text = StringProperty(q[str(initQuestion)]['text'])
    answer = StringProperty(q[str(initQuestion)]['answer'])
    img_path = StringProperty(q[str(initQuestion)]['img_path'])
    win = BooleanProperty(False)
    print("x")

    def verify(self, ans, cor_ans):
        print(ans)
        print(cor_ans)
        if ans == cor_ans:
            print(ans)

    def refresh(self):
        try:
            pick = choice([i for i in range(1, 13) if i not in self.chosen])
            self.chosen.append(pick)
            self.text = self.q[str(pick)]['text']
            self.answer = self.q[str(pick)]['answer']
            self.img_path = self.q[str(pick)]['img_path']
            self.count += 1
            print(self.chosen, self.count)
            # if len(self.chosen) == 12:
        except:
            if self.count == 12:
                self.win = True

class QuestionPage(Screen):
    q_file = open("./Questions/Hard/questions.json")
    q = json.load(q_file)


    count = 1
    chosen = []
    initQuestion = randrange(1, 12)
    chosen.append(initQuestion)
    text = StringProperty(q[str(initQuestion)]['text'])
    answer = StringProperty(q[str(initQuestion)]['answer'])
    img_path = StringProperty(q[str(initQuestion)]['img_path'])
    win = BooleanProperty(False)
    print("x")

    def refresh(self):
        try:
            pick = choice([i for i in range(1, 13) if i not in self.chosen])
            self.chosen.append(pick)
            self.text = self.q[str(pick)]['text']
            self.answer = self.q[str(pick)]['answer']
            self.img_path = self.q[str(pick)]['img_path']
            self.count += 1
            print(self.chosen, self.count)
            # if len(self.chosen) == 12:
        except:
            if self.count == 12:
                self.win = True

class Win(Screen):
    def reload(self):
        print('[RELOADING QUESTIONS PAGE]')
        HardQuestionPage.count = 1
        HardQuestionPage.chosen.clear()
        print(HardQuestionPage.chosen)


class Correct(Screen):
    # def refresh(self):
    #     QuestionPage.choice = randrange(1, 12)
    #     QuestionPage.text = QuestionPage.q[str(QuestionPage.choice)]['text']
    #     QuestionPage.answer = QuestionPage.q[str(QuestionPage.choice)]['answer']
    pass


class Incorrect(Screen):
    # def refresh(self):
    #     QuestionPage.choice = randrange(1, 12)
    #     QuestionPage.text = QuestionPage.q[str(QuestionPage.choice)]['text']
    #     QuestionPage.answer = QuestionPage.q[str(QuestionPage.choice)]['answer']
    pass


class Smaff(App):
    manager = WindowManager()
    manager.add_widget(Win())



Smaff().run()
