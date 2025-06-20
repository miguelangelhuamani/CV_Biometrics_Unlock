import os
import cv2
import numpy as np

pattern_size = (6, 9)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((np.prod(pattern_size), 3), dtype=np.float32)
objp[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)

obj_points = []  # Puntos en el espacio 3D (del tablero)
img_points = []  # Puntos 2D (en la imagen)

image_dir = "calibration_images"
image_files = sorted(os.listdir(image_dir))

for i in range(1,len(image_files)):
    image_file = image_files[i]
    image_path = os.path.join(image_dir, image_file)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    if ret:
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        obj_points.append(objp)
        img_points.append(corners)

        cv2.drawChessboardCorners(img, pattern_size, corners, ret)

    cv2.imshow('Calibration Image', img)
    cv2.waitKey(500)  

cv2.destroyAllWindows()

rms_error, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

print("Matriz intrínseca:\n", mtx)
print("Coeficientes de distorsión:", dist)
print("Error RMS de calibración:", rms_error)

#Guardamos los parámetros en un fichero: calibration_params.xml
fs = cv2.FileStorage("calibration_params.xml", cv2.FILE_STORAGE_WRITE)
fs.write("mtx", mtx)
fs.write("dist", dist)
fs.release()