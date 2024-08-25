import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingersCoordinate=[(8,6),(12,10),(16,14),(20,18)]
thumbCoordinate=(4,3)
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    upcount=0
    success , img = cap.read() # reading Frame 
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # converting BGR to RGB
    results = Hands.process(converted_image) # Processing Image for Tracking 
    handNo=0
    lmList=[]

    if results.multi_hand_landmarks: # Getting Landmark(location) of Hands if Exists 
        for id,lm in enumerate(results.multi_hand_landmarks[handNo].landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            lmList.append((cx,cy))