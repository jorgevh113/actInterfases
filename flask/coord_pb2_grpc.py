# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import coord_pb2 as coord__pb2


class CoordsCommStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCoords = channel.unary_unary(
                '/RpcDemo.CoordsComm/GetCoords',
                request_serializer=coord__pb2.Empty.SerializeToString,
                response_deserializer=coord__pb2.PointStamped.FromString,
                )


class CoordsCommServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCoords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoordsCommServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCoords': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoords,
                    request_deserializer=coord__pb2.Empty.FromString,
                    response_serializer=coord__pb2.PointStamped.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RpcDemo.CoordsComm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CoordsComm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCoords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RpcDemo.CoordsComm/GetCoords',
            coord__pb2.Empty.SerializeToString,
            coord__pb2.PointStamped.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)