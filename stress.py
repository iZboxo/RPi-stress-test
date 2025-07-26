
import multiprocessing
import time

def busy_wait():
    while True:
        pass

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=busy_wait)
        process.start()
        processes.append(process)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            for process in processes:
                process.terminate()
            break
