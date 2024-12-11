from ultralytics import YOLO
import cv2
import numpy as np
import mss
from pynput.keyboard import Controller as KeyboardController
import win32gui


def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def triggerbot():

    model = YOLO("train9/weights/best.pt")


    sct = mss.mss()
    monitor = sct.monitors[1]


    screen_width = monitor["width"]
    screen_height = monitor["height"]


    region_width = 320
    region_height = 240
    region = {
        "top": (screen_height - region_height) // 2,
        "left": (screen_width - region_width) // 2,
        "width": region_width,
        "height": region_height,
    }

    print(f"Capturing region: {region}")


    keyboard = KeyboardController()


    screen_mid_x = screen_width / 2
    screen_mid_y = screen_height / 2
    threshold = 10

    while True:

        active_window = get_active_window_title()
        if "VALORANT" in active_window.upper():
            print(f"Active window: {active_window}")
            screenshot = np.array(sct.grab(region))
            frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
            results = model.predict(frame, imgsz=640, conf=0.35,device=0)
            for result in results:
                for box in result.boxes:

                    x1, y1, x2, y2 = box.xyxy[0].tolist()


                    bbox_center_x = (x1 + x2) / 2
                    bbox_center_y = (y1 + y2) / 2


                    screen_x = region["left"] + bbox_center_x
                    screen_y = region["top"] + bbox_center_y

                    print(f"Detected object at: ({screen_x}, {screen_y})")


                    if (
                        abs(screen_x - screen_mid_x) <= threshold
                        and abs(screen_y - screen_mid_y) <= threshold
                    ):
                        keyboard.press("p")
                        keyboard.release("p")

        else:
            print(f"Active window: {active_window} - valorant not detected")


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cv2.destroyAllWindows()

if __name__ == "__main__":
    triggerbot()
