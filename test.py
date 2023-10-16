import os
import subprocess
import csv
import ischedule
import threading
import psutil
import datetime
input_file = str(input("Enter your file: "))
input_time = int(input("Enter the time interval  (in seconds): "))
assert os.path.exists(input_file), "I did not find the file  " + str(input_file)
subprocess.Popen(input_file)
with open('resources.csv', 'a+') as rf:
    output = csv.writer(rf)
    output.writerow(['program', 'time', 'working set', 'bytes', 'cpu %', 'open handles'])
    def update_data():
        filename = os.path.basename(input_file)
        for proc in psutil.process_iter():
            if filename in proc.name():
                p_info = proc.pid
                p = psutil.Process(p_info)
                # Записываем время и дату:
                now = datetim  e.datetime.now()
                # Записываем использование памяти: куда 
                p.memory_info()
                ws = p.memory_info().wset / 1024
                pb = p.memory_info().private / 1024
                # Записываем процент использования cpu:
                cpp = p.cpu_percent(interval=input_time) / psutil.cpu_count()
                # Записываем количество открытых потоков:
                open_h = len(p.open_files())
                output.writerow([filename, now, ws, pb, cpp, open_h])
    M_tread = threading.Thread(target=update_data)
    M_tread.start()
    ischedule.schedule(update_data(), interval=input_time)
    ischedule.run_loop()
    rf.close()
это тест 
