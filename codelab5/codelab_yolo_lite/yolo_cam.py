import cv2
import time
from ultralytics import YOLO

# Cargar modelo nano
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se puede abrir la cámara")
    exit()

prev_time = time.time()
fps = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se recibió frame")
        break

    # Reducir tamaño para CPU
    frame = cv2.resize(frame, (640, 480))

    # Inferencia en CPU
    results = model(frame, device='cpu')

    # Dibujar detecciones
    annotated_frame = results[0].plot()

    # Calcular FPS
    curr_time = time.time()
    fps = 0.9 * fps + 0.1 * (1 / (curr_time - prev_time))  # suavizado
    prev_time = curr_time

    # Mostrar FPS en pantalla
    cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 CPU Optimizado", annotated_frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


