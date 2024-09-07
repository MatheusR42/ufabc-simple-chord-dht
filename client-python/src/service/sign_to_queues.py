import grpc

from protocols import meu_qoelho_mq_pb2

def perform(stub, queue_names):
    try:
        req = meu_qoelho_mq_pb2.SignToQueuesRequest(queuesNames=queue_names)
        for response in stub.signToQueues(req):
            print('Signed to queues:', response.queueName)
            print('Sign response message:', response.message)
    except grpc.RpcError as e:
        print('Error signing to queues:', e)
