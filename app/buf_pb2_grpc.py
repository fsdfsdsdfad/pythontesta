# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buf_pb2 as buf__pb2


class SolverServicerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Solve = channel.unary_unary(
                '/buf.SolverServicer/Solve',
                request_serializer=buf__pb2.SolveRequest.SerializeToString,
                response_deserializer=buf__pb2.SolveResponse.FromString,
                )
        self.Hi = channel.unary_unary(
                '/buf.SolverServicer/Hi',
                request_serializer=buf__pb2.HiRequest.SerializeToString,
                response_deserializer=buf__pb2.HiResponse.FromString,
                )


class SolverServicerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Solve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Hi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SolverServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Solve': grpc.unary_unary_rpc_method_handler(
                    servicer.Solve,
                    request_deserializer=buf__pb2.SolveRequest.FromString,
                    response_serializer=buf__pb2.SolveResponse.SerializeToString,
            ),
            'Hi': grpc.unary_unary_rpc_method_handler(
                    servicer.Hi,
                    request_deserializer=buf__pb2.HiRequest.FromString,
                    response_serializer=buf__pb2.HiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'buf.SolverServicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SolverServicer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Solve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buf.SolverServicer/Solve',
            buf__pb2.SolveRequest.SerializeToString,
            buf__pb2.SolveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Hi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buf.SolverServicer/Hi',
            buf__pb2.HiRequest.SerializeToString,
            buf__pb2.HiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
