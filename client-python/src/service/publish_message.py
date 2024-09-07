import grpc

from protocols import meu_qoelho_mq_pb2

def perform(stub, name, messages, isBytes):
    msg_list = []
    for message in messages:
        if isBytes:
            msg = meu_qoelho_mq_pb2.MessageType(
                bytes_message=message.encode('utf-8')
            )
        else:
            msg = meu_qoelho_mq_pb2.MessageType(
                text_message=message
            )
        msg_list.append(msg)

    req = meu_qoelho_mq_pb2.PublishMessagesRequest(
        queueName=name,
        messages=msg_list
    )
    try:
        stub.publishMessages(req)
        returnMsg = 'Messages published as bytes' if isBytes else 'Messages published'
        print(returnMsg)
    except grpc.RpcError as e:
        print('Error publishing message:', e)
