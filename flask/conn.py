from flask import Flask, render_template
import json
import grpc
import coord_pb2
import coord_pb2_grpc
from google.protobuf.json_format import MessageToJson

app = Flask(__name__,template_folder='templates')

def get_coords():
    channel = grpc.insecure_channel('localhost:50052/coords')
    stub = coord_pb2_grpc.CoordsCommStub(channel)
    
    # Realizar la llamada al servidor gRPC
    response = stub.GetCoords(coord_pb2.Empty())
    
    # Procesar la respuesta
    # ...
    return response

# Flask route para realizar la llamada al servidor gRPC
@app.route('/call-go-api')
def call_go_api():
    coords = json.loads(MessageToJson(get_coords()))
    return render_template('home.html', coords=coords)
    # Resto del código Flask
    # ...
    

if __name__ == '__main__':
    app.run()
