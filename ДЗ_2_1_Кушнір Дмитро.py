import queue
import time
import random

request_queue = queue.Queue()
request_id = 1

def generate_request():
    global request_id
    request = f"Request_{request_id}"
    request_queue.put(request)
    print(f"Створено нову заявку: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Оброблено заявку: {request}")
    else:
        print("Черга пуста")

print("Програма починає роботу. Для завершення натисніть Ctrl+C")

try:
    while True:
        generate_request()
        time.sleep(random.uniform(1, 2))
        process_request()
        time.sleep(random.uniform(1, 2))
except KeyboardInterrupt:
    print("Програма завершена користувачем")
