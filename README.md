Proyecto: Detección de Cuerpos en Tiempo Real
Descripción
Este proyecto utiliza OpenCV y Python para detectar cuerpos humanos en tiempo real a través de la cámara web. Utiliza un clasificador Haar para detectar cuerpos, dibujar un rectángulo alrededor de cada cuerpo detectado y mostrar el video en vivo con las detecciones. Además, imprime las coordenadas de los cuerpos detectados en la consola.

Requisitos
Python 3.x

OpenCV

Instalación
Clonar el repositorio o descarga el código:
Si estás trabajando con un repositorio, puedes clonarlo usando Git:

bash
Copiar
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
Instalar las dependencias:

Asegúrate de tener Python instalado y luego instala las bibliotecas necesarias usando pip:

bash
Copiar
pip install opencv-python
Uso
Asegúrate de que tu cámara esté conectada y funcione correctamente.

Ejecuta el script para iniciar la detección de cuerpos:

bash
Copiar
python deteccion_cuerpos.py
El programa abrirá la cámara, y en tiempo real mostrará las personas detectadas, dibujando un rectángulo alrededor de cada uno. También imprimirá las coordenadas de los cuerpos detectados en la consola.

Para cerrar la ventana y detener el script, presiona la tecla q.

Ejemplo de salida
Cuerpos detectados: El video en tiempo real con los cuerpos humanos detectados y los rectángulos dibujados alrededor de ellos.

Coordenadas: Las coordenadas de los cuerpos detectados se imprimirán en la consola, en el formato x={x}, y={y}, w={w}, h={h}.

Código
python
Copiar
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
Autor
Gerson Mera
