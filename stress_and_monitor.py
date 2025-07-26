

import multiprocessing
import time
import os

def busy_wait():
    while True:
        pass

def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=","").replace("'C\n",""))

def draw_graph(temp):
    bar = '█' * int(temp / 2)
    print(f'{temp:.1f}°C |{bar}')

def monitor_and_graph():
    while True:
        try:
            cpu_temp = get_cpu_temperature()
            draw_graph(cpu_temp)
            time.sleep(1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    try:
        monitor_process = multiprocessing.Process(target=monitor_and_graph)
        monitor_process.start()

        num_processes = multiprocessing.cpu_count()
        print(f"Starting {num_processes} stress processes to heat up the CPU.")
        processes = []
        for _ in range(num_processes):
            process = multiprocessing.Process(target=busy_wait)
            process.start()
            processes.append(process)

        monitor_process.join()

    except KeyboardInterrupt:
        print("\nStopping all processes.")
        for p in processes:
            p.terminate()
        if monitor_process.is_alive():
            monitor_process.terminate()
    finally:
        for p in multiprocessing.active_children():
            p.terminate()

