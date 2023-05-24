from __future__ import print_function

import logging

import grpc
import coord_pb2
import coord_pb2_grpc
import serial 


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = coord_pb2_grpc.CoordsCommStub(channel)
        response = stub.getCoords(coord_pb2.Empty())
        print("Coords received: " + str(response))
        ser.write(str("Hola").encode())
        
        print("Coords sent to Arduino")
        ardResponse = ser.readline().decode().strip()
        print(ardResponse)



if __name__ == '__main__':
    logging.basicConfig()
    ser = serial.Serial('/dev/ttyACM0', 9600)
    run()
    ser.close()