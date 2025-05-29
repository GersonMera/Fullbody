import cv2 # importamos del opencv-python

imagen = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
# capturar video desde la camara
camara = cv2.VideoCapture(0) # defecto de camara
if not camara.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()
    print("oe baboso presione 'q' para salir del video")

while True:
    reat, frame = camara.read() # leer el video
    if not reat:
        print("Error: No se pudo leer la ventana.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir a escala de grises
    cuerpo = imagen.detectMultiScale(gray, 1.1, 4) # Detectar cuerpos
    for (x, y, w, h) in cuerpo: # Dibujar rectángulos alrededor de los cuerpos detectados
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(f"Cuerpo detectado en coordenadas: x={x}, y={y}, w={w}, h={h}") # Imprimir coordenadas de los cuerpos
    cv2.imshow('Cuerpos detectados', frame) # Mostrar el video con los cuerpos detectados
    if cv2.waitKey(1) & 0xFF == ord('q'): # salir del video si se presiona 'q'
        break
# Liberar la cámara y cerrar todas las ventanas
camara.release()
cv2.destroyAllWindows()
print("Cámara liberada y ventanas cerradas. Fin del script.") # Mensaje de éxito
# Fin del script























