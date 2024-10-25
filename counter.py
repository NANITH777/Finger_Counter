import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Coordinate mappings
fingersCoordinate = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinate = (4, 3)

# Start video capture
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    upcount = 0
    success, img = cap.read()
    if not success:
        break  # Break if frame not read correctly
    
    # Convert color from BGR to RGB
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(converted_image)
    
    if results.multi_hand_landmarks:  # If hands are detected
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            lmList = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

            for point in lmList:
                cv2.circle(img, point, 5, (0, 255, 0), cv2.FILLED)

            # Count fingers
            for coordinate in fingersCoordinate:
                if lmList[coordinate[0]][1] < lmList[coordinate[1]][1]:
                    upcount += 1
            if lmList[thumbCoordinate[0]][0] > lmList[thumbCoordinate[1]][0]:
                upcount += 1

            # Display count
            cv2.putText(img, str(upcount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (0, 0, 255), 12)

            # Gesture Recognition
            if upcount == 5:
                cv2.putText(img, "All Fingers Up!", (50, 300), cv2.FONT_HERSHEY_PLAIN, 12, (255, 0, 0), 12)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) == 113: # 113 - Q : press on Q : Close Video 
        break

cap.release()
cv2.destroyAllWindows()