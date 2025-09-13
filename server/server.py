import grpc
from concurrent import futures
import logging
import hello_pb2
import hello_pb2_grpc

logging.basicConfig(level=logging.INFO, format='[SERVER] %(message)s')

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"Получен запрос: name={request.name}")
        response = hello_pb2.HelloReply(message=f"Привет, {request.name}!")
        logging.info(f"Отправляем ответ: {response.message}")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    logging.info("gRPC сервер запущен на порту 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()