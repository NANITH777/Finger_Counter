import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingersCoordinate=[(8,6),(12,10),(16,14),(20,18)]
thumbCoordinate=(4,3)
cap = cv2.VideoCapture(0)