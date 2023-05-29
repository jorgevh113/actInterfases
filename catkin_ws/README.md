# Workspace de los nodos de ROS

## Paquete green_object_detection
En este paquete se encuentran todos nodos de ROS para la transmisión de coordenadas de objetos dentro de la carpeta `src`

### Carpeta msgs_proto
En esta carpeta se encuentra el archivo proto donde se definen los mensajes y servicios gRPC. Además, se encuentran el código `coordServer.py` que pone en servicio el servidor gRPC encargado de transmitir las coordenadas del tópico de */gren_object_coordinates*. 

### Carpeta systemObject
En esta carpeta se encuentran archivos necesarios para poner a disposición de uso la librería de sistema, tanto el código de c++ donde se declara la función, como los archivos compilados para generarla. 

### Carpeta src
*green_object_detection.py* es el nodo encargado de analizar la imagen con la librería opencv y encontrar objetos verdes. *publish_image.py* es un nodo que se utiliza para publicar la imagen en el tópico */camera/image_raw*