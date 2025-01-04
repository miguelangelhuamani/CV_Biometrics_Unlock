import cv2

def cargar_video(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap

def mostrar_video(frame):
    cv2.imshow('Eyes Detected', frame)

def mostrar_mensaje_inicial(frame): 
    cv2.putText(frame, "Press 's' to start introducing the password...", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def mostrar_password(frame, password):
    cv2.putText(frame, f'Password: {password}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

def mostrar_fps(frame, fps):
    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

def mostrar_mensaje_final(frame, mensaje, es_correcto):
    color = (0, 255, 0) if es_correcto else (0, 0, 255) 
    cv2.putText(frame, mensaje, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

def cerrar_video(cap):
    cap.release()
    cv2.destroyAllWindows()