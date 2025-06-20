import time
import cv2
from eye_detection import detect_eyes
from output_video import cargar_video, mostrar_video, mostrar_password, cerrar_video, mostrar_mensaje_final,mostrar_mensaje_inicial,mostrar_fps
from decoder import procesar_binario

cap = cargar_video("./input/video.mp4")
#cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = 1 / fps 

last_detection_time_eyes = None
last_detection_time_no_eyes = None
last_successful_detection_time = None 
binario = ""
password = ""
real_password = "8372"
valid_binario = True
tolerance_interval = 0.5  
time_threshold = 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    mostrar_mensaje_inicial(frame)
    mostrar_video(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        print("STARTING...")
        break

prev_time = time.time()  
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame, eyes_detected_now = detect_eyes(frame)  
    current_time = time.time()

    if eyes_detected_now:
        last_successful_detection_time = current_time  
        eyes_detected_now = True
    else:
        if last_successful_detection_time and (current_time - last_successful_detection_time <= tolerance_interval):
            eyes_detected_now = True
        else:
            eyes_detected_now = False

    if eyes_detected_now:
        if last_detection_time_eyes is None or current_time - last_detection_time_eyes > time_threshold:
            binario += "1"
            last_detection_time_eyes = current_time
            print(1)
    else:
        if last_detection_time_no_eyes is None or current_time - last_detection_time_no_eyes > time_threshold:
            binario += "0"
            last_detection_time_no_eyes = current_time
            print(0)

    numero, binario, valid_binario = procesar_binario(binario, valid_binario)
    
    if numero: 
        password += numero 

    mostrar_password(frame, password)

    fps_display = 1 / (current_time - prev_time)  
    prev_time = current_time  
    mostrar_fps(frame, fps_display)  

    mostrar_video(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if len(password) == 4:
        break

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    es_correcto = password == real_password
    mensaje = "PASSWORD CORRECT: COMPUTER UNLOCKED" if es_correcto else "PASSWORD INCORRECT: TRY AGAIN"
    mostrar_mensaje_final(frame,mensaje,es_correcto)
    mostrar_video(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cerrar_video(cap)