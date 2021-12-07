import threading
import time

def start_threads(info):
    for item in info:
        thr = threading.Thread(target=task_thread, args=(item['name'], item['path'],item['delay']))
        thr.start()

def task_thread(name, path, delay):
    with open(path, 'r') as file:
        for el in file:
            time.sleep(delay)
            print(f'[{name}]:{el[:-1]}')



# if __name__ == '__main__':
#     jobs = [
#         {'name': 'Thread 1', 'path': 's05t05_threads_file1.txt', 'delay': 3},
#         {'name': 'Thread 2', 'path': 's05t05_threads_file2.txt', 'delay': 1},
#         {'name': 'Thread 3', 'path': 's05t05_threads_file1.txt', 'delay': 5}]
#     start_threads(jobs)