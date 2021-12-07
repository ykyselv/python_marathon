from multiprocessing import Process
from datetime import datetime
import time


def start_processes(info):
    for item in info:
        proc = Process(target=task_process, args = (item['name'], item['year'], item['delay']))
        proc.start()


def task_process(name, year, delay):
    age = datetime.now().year - year
    time.sleep(delay)
    print(f"{name},{age} years old")


# if __name__ == '__main__':
#     jobs = [
#         {'name': 'John', 'year': 1990, 'delay': 10},
#         {'name': 'Chris', 'year': 1993, 'delay': 5},
#         {'name': 'Matthew', 'year': 2010, 'delay': 3},
#     ]

#     start_processes(jobs)
