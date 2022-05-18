
# **S**how **M**e **A** **F**unny **F**ace

---
## Introduction
Welcome to Smaff! For the NYIT Computer Science B.S. Capstone project of Spring 2022, students: [Dylan Finn](), [Jennifer Gulmohamad](), [Loyal Greene](), and [Annie Zeng]()
came together under the guidance of [Prof. Houwei Cao](https://www.nyit.edu/bio/hcao02) to create an educational game with the goal of teaching children emotional recognition and response through
the practical application of real time image classification using a Convulutional Neural Network within our game.

---

## To Run Application:

1. Install required dependencies:

```
pip install kivy opencv-python tensorflow
```

2. Run application:
```
cd ./application/smaff

python main.py
```
---

## To Train Model:

1. Install required dependencies:
```
pip install tensorflow
```

2. Run model

```
cd ./application/CNN

python model.py
```
> If you would like to use the model you trained rather than the one pre-included. Make sure that the line loading the .h5 in the main.py (located within the MaFF Object) file is aimed at the path of whatever model you choose to use
