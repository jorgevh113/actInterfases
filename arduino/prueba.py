
from __future__ import print_function
import logging
import grpc
import coord_pb2
import coord_pb2_grpc
import serial,time

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = coord_pb2_grpc.CoordsCommStub(channel)
        response = stub.getCoords(coord_pb2.Empty())


arduino = serial.Serial('/dev/ttyACM0', 9600)
while True:
    run()
    time.sleep(1)
    arduino.write(str("Hola").encode())
    while True:
        if arduino.inWaiting() > 0:
            
            response = arduino.readline().decode().strip()
            print(response)
            break
arduino.close()