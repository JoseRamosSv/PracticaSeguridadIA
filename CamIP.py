import cv2

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

# Ciclo para capturar y mostrar los fotogramas de la cámara
while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()

    # Verificar si se capturó correctamente el fotograma
    if not ret:
        print("No se pudo capturar el fotograma.")
        break

    # Mostrar el fotograma en una ventana
    cv2.imshow('Camera Feed', frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
