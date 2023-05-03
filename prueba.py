import ctypes

mylibrary = ctypes.CDLL('./libmylibrary.so')


x = ctypes.c_float(1.0)
y = ctypes.c_float(2.0)
z = ctypes.c_float(3.0)
mylibrary.calculateCoords(ctypes.pointer(x),ctypes.pointer(y),ctypes.pointer(z))

print('x: '+str(x.value)+' y: '+str(y.value)+' z: '+str(z.value))