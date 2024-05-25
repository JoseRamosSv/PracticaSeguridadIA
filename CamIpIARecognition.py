import cv2
import mediapipe as mp

# Dirección IP de la cámara
camera_ip = "192.168.1.100"
# Puerto de la cámara
camera_port = 8080
# URL de la transmisión de la cámara
camera_url = f"http://{camera_ip}:{camera_port}/video"

# Inicializar el objeto VideoCapture
cap = cv2.VideoCapture(camera_url)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Inicializar el objeto Face Detection de MediaPipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Ciclo para capturar y mostrar los fotogramas de la cámara
while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()

    # Verificar si se capturó correctamente el fotograma
    if not ret:
        print("No se pudo capturar el fotograma.")
        break

    # Convertir la imagen a RGB (MediaPipe usa imágenes en RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar rostros en la imagen
    results = face_detection.process(rgb_frame)

    # Dibujar recuadros alrededor de los rostros detectados
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el fotograma en una ventana
    cv2.imshow('Camera Feed', frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
