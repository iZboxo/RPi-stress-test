

import time
import os

def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=","").replace("'C\n",""))

def draw_graph(temp):
    bar = ''
    for i in range(0, int(temp)):
        bar += '#'
    print(f'{temp:.1f}°C {bar}')

if __name__ == "__main__":
    while True:
        try:
            cpu_temp = get_cpu_temperature()
            draw_graph(cpu_temp)
            time.sleep(1)
        except KeyboardInterrupt:
            break

