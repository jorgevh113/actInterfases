package main

import (
	"context"
	"log"

	pb "grpc_yt/gen/proto"

	"google.golang.org/grpc"
)

func main() {
	// Establecer conexión gRPC con el servidor
	conn, err := grpc.Dial("localhost:50052", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	// Crear cliente gRPC
	client := pb.NewCoordsCommClient(conn)

	// Realizar la llamada al servidor
	resp, err := client.GetCoords(context.Background(), &pb.Empty{})
	if err != nil {
		log.Fatalf("Failed to get coordinates: %v", err)
	}

	// Manejar la respuesta del servidor
	log.Printf("Received coordinates: %+v", resp)
}
