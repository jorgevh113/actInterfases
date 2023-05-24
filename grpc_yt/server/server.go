package main

import (
	"context"
	pb "grpc_yt/gen/proto"
	"log"

	"net"

	"net/http"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
)

type TestApiServer struct {
	pb.UnimplementedTestApiServer
}

func (s *TestApiServer) Echo(ctx context.Context, req *pb.ResponseRequest) (*pb.ResponseRequest, error) {
	return req, nil
}

func (s *TestApiServer) GetUser(ctx context.Context, req *pb.UserRequest) (*pb.UserResponse, error) {
	return &pb.UserResponse{
		Age:   20,
		Name:  "John",
		Email: "jorgevh0310@gmail.com"}, nil
}

func main() {

	go func() {

		mux := runtime.NewServeMux()

		pb.RegisterTestApiHandlerServer(context.Background(), mux, &TestApiServer{})

		log.Fatalln(http.ListenAndServe(":8081", mux))
	}()

	listener, err := net.Listen("tcp", ":8082")
	if err != nil {
		log.Fatalln(err)
	}

	grpcServer := grpc.NewServer()

	pb.RegisterTestApiServer(grpcServer, &TestApiServer{})

	err = grpcServer.Serve(listener)
	if err != nil {
		log.Println(err)
	}

}
