# actInterfases
Actividad de interfases

## Ejecutar el launch file para detección del objeto verde

```
cd catkin_ws
source devel/setup.bash
roslaunch green_object_detection object_detection.launch
```

### Este launch file inicializa tres nodos:
**1. publish_image.py:** Inicializa el nodo para publicar imagen de la cámara en el tópico */camera/image\_raw*

**2. green\_object_detection.py:** Inicializa el nodo para la detección de objetos verdes en la imagen, usa una librería .so para multiplicar las coordenadas y publica el resultado en el tópico */green\_object\_coordinates*

**3. coordServer.py:** Inicializa un nodo para levantar un servidor gRPC que recibe un mensaje vacío y devuelve las coordenadas obtenidas del tópico de las coordenadas del objeto

### Ejecutar el cliente en CSharp para obtener las coordenadas del objeto

```
cd ../csharp/csGrpc/csGrpc/bin/Debug/
mono csGrpc.exe
```
