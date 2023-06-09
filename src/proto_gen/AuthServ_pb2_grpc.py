# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import AuthServ_pb2 as AuthServ__pb2


class AuthAndRegistServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TryRegistr = channel.unary_unary(
                '/CAS.AuthAndRegistService/TryRegistr',
                request_serializer=AuthServ__pb2.RegistrationInput.SerializeToString,
                response_deserializer=AuthServ__pb2.RegistrationResult.FromString,
                )
        self.TryVerifRegistr = channel.unary_unary(
                '/CAS.AuthAndRegistService/TryVerifRegistr',
                request_serializer=AuthServ__pb2.RegistrationVerificationInput.SerializeToString,
                response_deserializer=AuthServ__pb2.RegistrationVerificationResult.FromString,
                )
        self.Authenticate = channel.unary_unary(
                '/CAS.AuthAndRegistService/Authenticate',
                request_serializer=AuthServ__pb2.AuthInput.SerializeToString,
                response_deserializer=AuthServ__pb2.AuthResult.FromString,
                )
        self.AuthFromPassword = channel.unary_unary(
                '/CAS.AuthAndRegistService/AuthFromPassword',
                request_serializer=AuthServ__pb2.PasswordAuthInput.SerializeToString,
                response_deserializer=AuthServ__pb2.PasswordAuthResult.FromString,
                )


class AuthAndRegistServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TryRegistr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TryVerifRegistr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthFromPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthAndRegistServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TryRegistr': grpc.unary_unary_rpc_method_handler(
                    servicer.TryRegistr,
                    request_deserializer=AuthServ__pb2.RegistrationInput.FromString,
                    response_serializer=AuthServ__pb2.RegistrationResult.SerializeToString,
            ),
            'TryVerifRegistr': grpc.unary_unary_rpc_method_handler(
                    servicer.TryVerifRegistr,
                    request_deserializer=AuthServ__pb2.RegistrationVerificationInput.FromString,
                    response_serializer=AuthServ__pb2.RegistrationVerificationResult.SerializeToString,
            ),
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=AuthServ__pb2.AuthInput.FromString,
                    response_serializer=AuthServ__pb2.AuthResult.SerializeToString,
            ),
            'AuthFromPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthFromPassword,
                    request_deserializer=AuthServ__pb2.PasswordAuthInput.FromString,
                    response_serializer=AuthServ__pb2.PasswordAuthResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CAS.AuthAndRegistService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthAndRegistService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TryRegistr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CAS.AuthAndRegistService/TryRegistr',
            AuthServ__pb2.RegistrationInput.SerializeToString,
            AuthServ__pb2.RegistrationResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TryVerifRegistr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CAS.AuthAndRegistService/TryVerifRegistr',
            AuthServ__pb2.RegistrationVerificationInput.SerializeToString,
            AuthServ__pb2.RegistrationVerificationResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CAS.AuthAndRegistService/Authenticate',
            AuthServ__pb2.AuthInput.SerializeToString,
            AuthServ__pb2.AuthResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthFromPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CAS.AuthAndRegistService/AuthFromPassword',
            AuthServ__pb2.PasswordAuthInput.SerializeToString,
            AuthServ__pb2.PasswordAuthResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
