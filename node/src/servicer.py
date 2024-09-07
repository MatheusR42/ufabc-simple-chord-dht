from protocols import meu_qoelho_mq_pb2_grpc
from protocols import meu_qoelho_mq_pb2
from db import DB
from queueservice import QueueService
import grpc

class MeuQoelhoMqServicer(meu_qoelho_mq_pb2_grpc.MeuQoelhoMqServicer):
  service: QueueService

  def __init__(self):
    self.service = QueueService(DB())

  def join(self, request, context):
    ip = context.peer()
    print("join!")
    print("ip:", ip)
    print("request:", request)
    return self.service.join()

