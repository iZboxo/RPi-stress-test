# RPi-stress-test

This repository contains a Python script designed to stress the CPU of a Raspberry Pi and simultaneously monitor its temperature.

## How it Works

The `stress_and_monitor.py` script combines two main functionalities:

1.  **CPU Stress:** It utilizes the `multiprocessing` module to create as many processes as there are CPU cores on your Raspberry Pi. Each process runs an infinite `busy_wait` loop, consuming CPU cycles and generating heat.

2.  **Temperature Monitoring & Graphing:** It continuously reads the CPU temperature using the `vcgencmd measure_temp` command (specific to Raspberry Pi OS). The temperature is then displayed in the terminal along with a simple text-based bar graph, providing a visual representation of the temperature increase.

## Usage

To run the script, navigate to the `temp_monitor` directory in your Raspberry Pi's terminal and execute the following command:

```bash
python3 stress_and_monitor.py
```

The script will immediately start stressing the CPU and displaying the temperature updates. To stop the script, press `Ctrl+C`.

## Important Notes

*   This script is intended for testing and monitoring purposes. Prolonged high temperatures can potentially reduce the lifespan of your hardware. Use responsibly.
*   The `vcgencmd` command is specific to Raspberry Pi OS. This script may not work on other Linux distributions without modifications to the `get_cpu_temperature` function.

---

This project was created with the assistance of the Gemini CLI.