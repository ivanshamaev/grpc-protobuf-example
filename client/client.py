import grpc
import logging
import hello_pb2
import hello_pb2_grpc
import sys

logging.basicConfig(level=logging.INFO, format='[CLIENT] %(message)s')

def run(host="server", port=50051):
    target = f"{host}:{port}"
    logging.info(f"Создаём канал к {target}...")
    with grpc.insecure_channel(target) as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        logging.info("Stub создан. Отправляем запрос...")
        response = stub.SayHello(hello_pb2.HelloRequest(name="Python Junior"))
        logging.info(f"Получен ответ: {response.message}")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "server"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 50051
    run(host, port)