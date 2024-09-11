import grpc
from concurrent import futures
from protocols import meu_qoelho_mq_pb2_grpc
from servicer import MeuQoelhoMqServicer
from signal import signal, SIGTERM, SIGINT, pause
import threading
import os
import time

# Interactive terminal function
def interactive_terminal():
    time.sleep(5)
    while True:
        command = input("Enter command (type 'exit' to quit): \n")
        if command == 'exit':
            print("Exiting interactive terminal...  \n")
            break
        else:
            print(f"Received command: {command}  \n")

# gRPC server function
def serve(server, port):
    server.start()
    print(f"gRPC server started on IP 0.0.0.0 and port {port}")
    server.wait_for_termination()

# Thread to run both server and terminal
if __name__ == "__main__":
    # Create the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = MeuQoelhoMqServicer()
    meu_qoelho_mq_pb2_grpc.add_MeuQoelhoMqServicer_to_server(servicer, server)
    port = server.add_insecure_port("[::]:50051")

    # Create thread for the gRPC server
    server_thread = threading.Thread(target=serve, args=(server,port))
    server_thread.start()

    # Handle termination signals in the main thread
    def handle_termination(*_: any) -> None:
        print("Shutting down server...")
        server.stop(0)
        servicer.service.clear_subs()
        print('Cleared subs')
        os._exit(0)

    signal(SIGINT, handle_termination)
    signal(SIGTERM, handle_termination)

    # Run the interactive terminal in the main thread
    interactive_terminal()

    # Wait for the server thread to finish (this will happen when the server is terminated)
    server_thread.join()
