import psutil, time, os

def beginMonitor():
    proc = psutil.Process(os.getpid())
    while True:
        cpu_usage = proc.cpu_percent(interval=1.0)
        memory_usage = proc.memory_percent()
        print(f"CPU %: {cpu_usage}")
        print(f"Memory %: {memory_usage}")