import grpc
from concurrent import futures
from protocols import meu_qoelho_mq_pb2_grpc
from controller import MeuQoelhoMqServicer

def serve():
    node = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meu_qoelho_mq_pb2_grpc.add_MeuQoelhoMqServicer_to_server(MeuQoelhoMqServicer(), node)
    node.add_insecure_port("[::]:50051")
    node.start()
    print("node is running")
    node.wait_for_termination()

serve()
