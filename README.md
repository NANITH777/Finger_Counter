### **Hand Gesture Recognition Using OpenCV and MediaPipe**

#### **Overview**

This project utilizes OpenCV and MediaPipe to perform real-time hand gesture recognition using a webcam. It detects hands and counts the number of fingers raised, supporting up to two hands. The application displays individual finger counts for each hand and aggregates the total. A specific message appears if both hands have all fingers raised.

---

#### **Features**

- Real-time hand tracking with finger counting.
- Supports two-hand detection.
- Visual feedback for each hand’s raised finger count.
- Gesture recognition with a special message if both hands have all fingers up.

---

#### **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NANITH777/Finger_Counter.git
   cd Finger_Counter

   ```

2. **Install Required Packages**
   Ensure Python is installed, then use `pip` to install the required libraries:
   ```bash
   pip install opencv-python mediapipe
   ```

#### **Code Explanation**

1. **Initialization**: Initializes MediaPipe Hands to track hand landmarks with `max_num_hands=2` to enable two-hand tracking.
2. **Landmark Processing**: For each hand detected, it calculates coordinates and recognizes gestures by comparing joint positions.
3. **Gesture Recognition Logic**: Counts fingers raised for each hand and displays a message when both hands have all fingers up.
4. **Display**: Shows the current count for each hand, the total count, and the specific message when both hands are fully extended.

#### **Usage Guide**

- **Start Video Feed**: The program will begin capturing from your webcam.
- **Display Information**: Each detected hand's raised fingers will be counted, shown on the screen, and aggregated. If both hands are fully extended, a special message appears.

#### **Sample Output**

- _Hand 1_: 3 fingers raised
- _Hand 2_: 2 fingers raised
- _Total Fingers_: 5 fingers
