import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
Hands = mpHands.Hands(static_image_mode=False, max_num_hands=2)  # detection of two hands
mpDraw = mp.solutions.drawing_utils

# Coordinate mappings
fingersCoordinate = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinate = (4, 3)

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break  # Break if frame not read correctly

    # Convert color from BGR to RGB
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(converted_image)
    
    if results.multi_hand_landmarks:  # If hands are detected
        total_fingers = 0  # Count total fingers for both hands
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            lmList = []
            upcount = 0  # Count fingers up for the current hand
            
            # Capture landmarks for the current hand
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            # Draw hand landmarks
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

            # Count fingers
            for coordinate in fingersCoordinate:
                if lmList[coordinate[0]][1] < lmList[coordinate[1]][1]:  # Y-axis comparison
                    upcount += 1
            if lmList[thumbCoordinate[0]][0] > lmList[thumbCoordinate[1]][0]:  # X-axis for thumb
                upcount += 1

            # Display count for the current hand
            total_fingers += upcount  # Aggregate fingers from both hands

            # Draw the finger count for each hand individually
            cv2.putText(img, f"Hand {hand_no + 1}: {upcount} fingers", (10, 50 + hand_no * 50), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Display total fingers count
        cv2.putText(img, f"Total Fingers: {total_fingers}", (10, 150), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        # Recognize gesture based on total fingers up
        if total_fingers == 10:
            cv2.putText(img, "Both Hands: All Fingers Up!", (10, 250), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Hand Tracking - Two Hands", img)

    if cv2.waitKey(1) == 113:  # Press 'Q' to quit
        break

cap.release()
cv2.destroyAllWindows()
