package main

import (
	"context"
	"log"
	"net"

	pb "grpc_yt/gen/proto"

	"google.golang.org/grpc"
)

type CoordsCommServer struct {
	pb.UnimplementedCoordsCommServer
}

func (s *CoordsCommServer) GetCoords(ctx context.Context, req *pb.Empty) (*pb.PointStamped, error) {
	// Establecer conexión gRPC como cliente
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Println(err)
		return nil, err
	}
	defer conn.Close()

	// Crear cliente gRPC para el servidor externo
	coordsCommClient := pb.NewCoordsCommClient(conn)

	// Solicitar los valores de PointStamped al servidor externo
	resp, err := coordsCommClient.GetCoords(context.Background(), &pb.Empty{})
	if err != nil {
		log.Println(err)
		return nil, err
	}

	return resp, nil
}

func main() {
	listener, err := net.Listen("tcp", ":50052")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()

	pb.RegisterCoordsCommServer(grpcServer, &CoordsCommServer{})

	log.Println("Server started, listening on :50052")

	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
