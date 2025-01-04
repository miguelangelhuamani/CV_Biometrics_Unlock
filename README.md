# Sistema de detección de patrón ocular para acceso informático
Este proyecto implementa un sistema de detección y seguimiento de iris basado en OpenCV, diseñado para interpretar el parpadeo como una entrada binaria y descodificarlo en una contraseña númerica para desbloquear desbloquear el ordenador. La detección de iris se ha realizado mediante trasnformación de imagen, detección de bordes y transformada de Hough, para luego ser mostrada por cámara la visualización en tiempo real de la detección y contraseña.

### Funcionalidades
	•	Transformación de la imagen: Escala de grises, detección de caras, reducción de ROI y filtro Gaussiano
    •	Detección de iris: Detección de bordes y Transformada de Hough
	•	Seguimiento de iris: Dibuja círculos verdes para pupilas válidas y rojos para destacar el centro.
	•	Entrada binaria: Interpreta el parpadeo como una secuencia binaria.
	•	Validación de contraseña: Permite verificar si la secuencia ingresada coincide con la contraseña predefinida.
	•	Visualización en tiempo real: Muestra el video con las detecciones y mensajes de estado.
