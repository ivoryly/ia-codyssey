filename = 'C:/Users/SangAh/Desktop/python/mission_computer_main.log'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print('\n=== 로그 파일 내용 ===')
        for line in lines:
            print(line.strip())
    
except FileNotFoundError:
    print(f"[오류] 파일이 존재하지 않습니다: {filename}")
except PermissionError:
    print(f"[오류] 파일에 접근할 권한이 없습니다: {filename}")
except Exception as e:
    print(f"[오류] 알 수 없는 문제가 발생했습니다: {e}")
    
    
log_list = []
for line in lines[1:]:  
    parts = line.strip().split(',')
    timestamp = parts[0]
    event = parts[1]
    message = ','.join(parts[2:])  
    log_list.append([timestamp, event, message])

print('\n로그 리스트:')
for item in log_list:
    print(item)

log_list.sort(reverse=True, key=lambda x: x[0])

print('\n시간 역순으로 정렬된 로그 리스트:')
for item in log_list:
    print(item)

log_list.sort(reverse=False, key=lambda x: x[0])

log_dict = {}
for i, entry in enumerate(log_list):
    log_dict[str(i)] = {
        'timestamp' : entry[0],
        'event': entry[1],
        'message': entry[2]}
print('\n사전 형태:')
print(log_dict)

search_keyword = 'Oxygen'

print(f"\n[검색 결과] '{search_keyword}'이(가) 포함된 로그:")
found = False
for key, value in log_dict.items():
    if search_keyword in value['message']:
        print(f"키: {key}, 시간: {value['timestamp']}, 이벤트: {value['event']}, 메시지: {value['message']}")
        found = True

if not found:
    print("해당 문자열이 포함된 로그가 없습니다.")

json_filename = 'C:/Users/SangAh/Desktop/python/mission_computer_main.json'
try:
    with open(json_filename, 'w', encoding='utf-8') as json_file:     #json.dump(log_dict, json_file, indent=2)
        json_file.write('{\n')
        items = list(log_dict.items())    #인덱스를 사용하여 반복하려면 리스트로 바꿔줘야함(딕셔너리 자체는 인덱스 접근 안된다. 정렬위해 튜플로) .items() (키, 값) 형식으로 튜플로 묶어서 반환
        for i, (key, value) in enumerate(items):       
            json_file.write(f' "{key}": {{"timestamp" : "{value["timestamp"]}", "event" : "{value["event"]}", "message" : "{value["message"]}"}}')
            if i < len(items) -1:
                json_file.write(',\n')    #마지막 ,때문에 인덱스를 붙여 리스트로 바꾼거임
            else:
                json_file.write('\n')
        json_file.write('}\n')
    print(f'\n JSON 파일로 저장 완료: {json_filename}')
except Exception as e:
    print(f'[오류] JSON 파일 저장 중 문제 발생: {e}')