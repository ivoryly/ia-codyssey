import threading
import time
from multiprocessing import Process
from mars_mission_computer3 import ExtendedMissionComputer
from mars_mission_computer2 import MissionComputer
import json

class MissionComputer2(MissionComputer):
    def get_sensor_data_once(self):
        self.ds.set_env()
        self.env_values = self.ds.get_env()
        for key, value in self.env_values.items():
            self.data_buffer[key].append(value)
        print(json.dumps(self.env_values, ensure_ascii=False, indent=4))


def repeat_every_20s(func):
    while True:
        func()
        time.sleep(20)

def run_multithread():
    RunComputer = ExtendedMissionComputer()
    RunComputer2 = MissionComputer2()

    threads = [
    threading.Thread(target=repeat_every_20s, args=(RunComputer.get_mission_computer_info,)),
    threading.Thread(target=repeat_every_20s, args=(RunComputer.get_mission_computer_load,)),
    threading.Thread(target=repeat_every_20s, args=(RunComputer2.get_sensor_data_once,)),
    ]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def run_multiprocess():
    runComputer1 = ExtendedMissionComputer()
    runComputer2 = ExtendedMissionComputer()
    runComputer3 = MissionComputer2()

    processes = [
        Process(target=repeat_every_20s, args=(runComputer1.get_mission_computer_info,)),
        Process(target=repeat_every_20s, args=(runComputer2.get_mission_computer_load,)),
        Process(target=repeat_every_20s, args=(runComputer3.get_sensor_data_once,)),
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

if __name__ == "__main__":    #multiprocessing.Process 는 새 프로세스를 만들 때 부모 스크립트를 다시 실행
    choice = input("1: Thread 실행, 2: Process 실행 선택: ").strip()
    if choice == "1":
        run_multithread()
    elif choice == "2":
        run_multiprocess()