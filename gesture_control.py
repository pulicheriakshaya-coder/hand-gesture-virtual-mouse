import time
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Disable PyAutoGUI's fail-safe to prevent accidental crashes if mouse hits a corner
pyautogui.FAILSAFE = False

# 1. Initialize Webcam & Get Screen Size
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

screen_w, screen_h = pyautogui.size()

# 2. Smoothing Variables (Higher = smoother movement, but slightly more delay)
smoothening = 5
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# 3. Initialize Modern MediaPipe Hand Landmarker
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
)
detector = vision.HandLandmarker.create_from_options(options)

pTime = 0
click_cooldown = 0  # Prevents rapid-fire clicking

while cap.isOpened():
  success, img = cap.read()
  if not success:
    break

  # Flip the image horizontally for a natural mirror view
  img = cv2.flip(img, 1)

  rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

  recognition_result = detector.detect(mp_image)

  if recognition_result.hand_landmarks:
    for hand_landmarks in recognition_result.hand_landmarks:
      h, w, c = img.shape

      # Landmark 4: Thumb tip, Landmark 8: Index finger tip
      x_thumb = int(hand_landmarks[4].x * w)
      y_thumb = int(hand_landmarks[4].y * h)
      x_index = int(hand_landmarks[8].x * w)
      y_index = int(hand_landmarks[8].y * h)

      # --- MOUSE MOVEMENT (Index Finger with Smoothing) ---
      # Map camera frame boundaries to screen resolution (with a 75px border padding)
      screen_x = np.interp(x_index, (75, w - 75), (0, screen_w))
      screen_y = np.interp(y_index, (75, h - 75), (0, screen_h))

      # Smooth values to eliminate jitter
      clocX = plocX + (screen_x - plocX) / smoothening
      clocY = plocY + (screen_y - plocY) / smoothening

      # Move mouse cursor
      pyautogui.moveTo(clocX, clocY)
      plocX, plocY = clocX, clocY

      # Draw visual indicators on webcam window
      cv2.circle(img, (x_index, y_index), 10, (255, 0, 255), cv2.FILLED)
      cv2.circle(img, (x_thumb, y_thumb), 10, (0, 255, 255), cv2.FILLED)
      cv2.line(img, (x_thumb, y_thumb), (x_index, y_index), (0, 255, 0), 2)

      # --- MOUSE CLICK (Thumb & Index Pinch) ---
      distance = np.hypot(x_index - x_thumb, y_index - y_thumb)
      if distance < 35 and time.time() - click_cooldown > 0.5:
        pyautogui.click()
        click_cooldown = time.time()
        cv2.circle(img, (x_index, y_index), 15, (0, 255, 0), cv2.FILLED)
        cv2.putText(
            img,
            "CLICK",
            (x_index - 25, y_index - 20),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

  # FPS calculation
  cTime = time.time()
  fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
  pTime = cTime
  cv2.putText(
      img,
      f"FPS: {int(fps)}",
      (40, 50),
      cv2.FONT_HERSHEY_COMPLEX,
      1,
      (255, 0, 0),
      3,
  )

  cv2.imshow("Virtual Mouse", img)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()