# grpc-protobuf-example
Полный гайд: gRPC + ProtoBuf + Python + Docker

# venv
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
```

# Генерация Python-кода из .proto
Запускаем команду (можно внутри контейнера или на своей машине):
```
python -m grpc_tools.protoc -I=./proto --python_out=./server --grpc_python_out=./server ./proto/hello.proto
python -m grpc_tools.protoc -I=./proto --python_out=./client --grpc_python_out=./client ./proto/hello.proto
```

# Запускаем локально (без Docker) сервер и клиент на разных портах

## Запускаем сервер
```
python server/server.py
```
В консоли получим результат:
```
[SERVER] gRPC сервер запущен на порту 50051
```

## Запускаем клиент (уйдет запрос к серверу)
Для клиента в файле `client/client.py` нужно в переменной `host` установить:
```
host='localhost'
```

Запускаем клиент командой:
```
python client/client.py
```

## Лог сервера и клиента
Сервер даст ответ на каждый запуск клиента:
```
[SERVER] Получен запрос: name=Python Junior
[SERVER] Отправляем ответ: Привет, Python Junior!
```

Клиент выведет в консоль при каждом запуске:
```
[CLIENT] Создаём канал к серверу...
[CLIENT] Stub создан. Отправляем запрос...
[CLIENT] Получен ответ: Привет, Python Junior!
```

# Запуск с докером
Собираем контейнеры с помощью команды:
```
docker compose build
```

Результат:
```
[+] Building 2/2
 ✔ client  Built
 ✔ server  Built 
```

Запускаем контейнеры
```
docker compose up
```

# Результат

```
[+] Running 3/3
 ✔ Network grpc-protobuf-example_custom_net  Created                                                                            0.1s 
 ✔ Container grpc_server                     Created                                                                            0.2s 
 ✔ Container grpc_client                     Created                                                                            0.2s 
Attaching to grpc_client, grpc_server
grpc_server  | [SERVER] gRPC сервер запущен на порту 50051
grpc_client  | [CLIENT] Создаём канал к server:50051...
grpc_client  | [CLIENT] Stub создан. Отправляем запрос...
grpc_server  | [SERVER] Получен запрос: name=Python Junior
grpc_server  | [SERVER] Отправляем ответ: Привет, Python Junior!
grpc_client  | [CLIENT] Получен ответ: Привет, Python Junior!
```

## Полезные команды docker compose
### Остановить сервисы и удалить контейнеры
```
docker compose down
```

### Удалить контейнеры + сети + volumes проекта
```
docker compose down -v
```

### Удалить контейнеры + сети + volumes + собранные образы
```
docker compose down --rmi all -v
```
