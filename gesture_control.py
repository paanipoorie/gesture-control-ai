import cv2
from cvzone.HandTrackingModule import HandDetector
import subprocess
import time

# Initialize the webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Cooldown timer tracking
last_action_time = {"calculator": 0, "calendar": 0, "brave": 0, "vscode": 0}
cooldown = 4  # seconds

# Define action functions
def open_calculator():
    subprocess.Popen(["gnome-calculator"])
    print("🧮 Calculator opened")

def open_calendar():
    subprocess.Popen(["gnome-calendar"])
    print("📅 Calendar opened")

def open_brave():
    subprocess.Popen(["brave-browser"])
    print("🌐 Brave Browser opened")

def open_vscode():
    subprocess.Popen(["code"])
    print("💻 VS Code opened")

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)

        cv2.putText(img, f"Fingers: {totalFingers}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        current_time = time.time()

        # Fist gesture: open Calculator
        if fingers == [0, 0, 0, 0, 0] and current_time - last_action_time["calculator"] > cooldown:
            open_calculator()
            last_action_time["calculator"] = current_time
            cv2.putText(img, "Calculator", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # 1 finger: open Calendar
        elif fingers == [0, 1, 0, 0, 0] and current_time - last_action_time["calendar"] > cooldown:
            open_calendar()
            last_action_time["calendar"] = current_time
            cv2.putText(img, "Calendar", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # 3 fingers: open Brave browser
        elif fingers == [0, 1, 1, 1, 0] and current_time - last_action_time["brave"] > cooldown:
            open_brave()
            last_action_time["brave"] = current_time
            cv2.putText(img, "Brave", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # 4 fingers: open VS Code
        elif fingers == [0, 1, 1, 1, 1] and current_time - last_action_time["vscode"] > cooldown:
            open_vscode()
            last_action_time["vscode"] = current_time
            cv2.putText(img, "VS Code", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
