import threading
import time
from multiprocessing import Process
from mars_mission_computer3 import ExtendedMissionComputer

def repeat_every_20s(func):
    while True:
        func()
        time.sleep(20)

def run_multithread():
    RunComputer = ExtendedMissionComputer()

    t1 = threading.Thread(target=repeat_every_20s, args=(RunComputer.get_mission_computer_info,))
    t2 = threading.Thread(target=repeat_every_20s, args=(RunComputer.get_mission_computer_load,))
    t3 = threading.Thread(target=RunComputer.get_sensor_data)  

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def run_multiprocess():
    runComputer1 = ExtendedMissionComputer()
    runComputer2 = ExtendedMissionComputer()
    runComputer3 = ExtendedMissionComputer()

    processes = []

    for mc in [runComputer1, runComputer2, runComputer3]:
        processes.append(Process(target=repeat_every_20s, args=(mc.get_mission_computer_info,)))
        processes.append(Process(target=repeat_every_20s, args=(mc.get_mission_computer_load,)))
        processes.append(Process(target=mc.get_sensor_data))

    for p in processes:
        p.start()
    for p in processes:
        p.join()

if __name__ == "__main__":
    choice = input("1: Thread 실행, 2: Process 실행 선택: ").strip()
    if choice == "1":
        run_multithread()
    elif choice == "2":
        run_multiprocess()