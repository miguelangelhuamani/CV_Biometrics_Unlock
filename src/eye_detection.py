import cv2
import numpy as np

def detect_eyes(frame):

    fs = cv2.FileStorage("src/calibration_params.xml", cv2.FILE_STORAGE_READ)
    dist = fs.getNode("dist").mat()
    mtx = fs.getNode("mtx").mat()
    fs.release()
    undistorted_frame = cv2.undistort(frame, mtx, dist, None, mtx)

    gray = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    eyes_detected_now = False

    for (fx, fy, fw, fh) in faces:
        roi_top = fy + fh // 4
        roi_bottom = fy + fh // 2
        roi_width = fw // 2
        roi_x = fx + fw // 4
        roi_gray = gray[roi_top:roi_bottom, roi_x:roi_x + roi_width]

        blurred = cv2.GaussianBlur(roi_gray, (7, 7), 2)
        edges = cv2.Canny(blurred, 50, 150)
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, param1=100, param2=15, minRadius=8, maxRadius=20)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (cx, cy, r) in circles:
                area = np.pi * (r ** 2)
                if area < 50 or area > 1500:
                    continue

                mask = np.zeros(roi_gray.shape, dtype=np.uint8)
                cv2.circle(mask, (cx, cy), r, 255, -1)
                mean_intensity = cv2.mean(roi_gray, mask=mask)[0]

                if mean_intensity > 60:
                    continue

                global_x = roi_x + cx
                global_y = roi_top + cy
                cv2.circle(frame, (global_x, global_y), r, (0, 255, 0), 2)
                cv2.circle(frame, (global_x, global_y), 2, (0, 0, 255), 3)
                eyes_detected_now = True

    return frame, eyes_detected_now