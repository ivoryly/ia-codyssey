import time
import json
from mars_mission_computer import DummySensor

class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,      
            'mars_base_external_temperature': None,      
            'mars_base_internal_humidity': None,         
            'mars_base_external_illuminance': None,      
            'mars_base_internal_co2': None,              
            'mars_base_internal_oxygen': None            
        }
        
        self.ds = DummySensor()
        self.data_buffer = {key: [] for key in self.env_values}

    def get_sensor_data(self):
        start_time = time.time()

        while True:
            user_input = input("계속하려면 엔터, 중지하려면 q 입력: ").strip().lower()
            if user_input == "q":
                print("System stopped...")
                break

            self.ds.set_env()
            self.env_values = self.ds.get_env()

           
            for key, value in self.env_values.items():
                self.data_buffer[key].append(value)
    
            print(json.dumps(self.env_values, ensure_ascii=False, indent=4))

            # 5분 경과 시 평균 출력
            if time.time() - start_time >= 300:  
                avg_values = {k: round(sum(v) / len(v), 2) for k, v in self.data_buffer.items()}
                print("\n===== 5분 평균 값 =====")
                print(json.dumps(avg_values, ensure_ascii=False, indent=4))
                print("=======================\n")

                self.data_buffer = {key: [] for key in self.env_values}
                start_time = time.time()

            time.sleep(5)


if __name__ == "__main__":
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()