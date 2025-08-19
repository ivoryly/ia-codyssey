filename = 'C:/Users/SangAh/Desktop/python/Mars_Base_Inventory_List.csv'

inventory = []

def to_float(value):
    try:
        return float(value)
    except:
        return None

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        header = lines[0].strip().split(",")  
        for line in lines[1:]:  
            fields = line.strip().split(",")

            item = {
                "substance": fields[0],
                "weight": to_float(fields[1]),
                "Specific Gravity": to_float(fields[2]),
                "Strength": fields[3],
                "Flammability": to_float(fields[4])
            }
            inventory.append(item)

except FileNotFoundError:
    print(f'[오류] 파일이 존재하지 않습니다: {filename}')
except PermissionError:
    print(f'[오류] 파일에 접근할 권한이 없습니다: {filename}')
except Exception as e:
    print(f'[오류] 알 수 없는 문제가 발생했습니다: {e}')         
        
      

inventory.sort(key=lambda x: (x["Flammability"] is not None, x["Flammability"]), reverse=True)

dangerous_items = [item for item in inventory if item["Flammability"] is not None and item["Flammability"] >= 0.7]

print("=== 인화성 순 정렬 목록 ===")
for item in inventory:
    print(item)

print("\n=== 인화성 0.7 이상 위험 물질 목록 ===")
for item in dangerous_items:
    print(item)


report_file = 'C:/Users/SangAh/Desktop/python/Mars_Base_Inventory_danger.csv'
try:
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('substance,weight,Specific Gravity,Strength,Flammability\n')
        for item in dangerous_items:
        # None 값은 빈칸으로 처리
            weight = "" if item["weight"] is None else item["weight"]
            sg = "" if item["Specific Gravity"] is None else item["Specific Gravity"]
            flam = "" if item["Flammability"] is None else item["Flammability"]
            line = f"{item['substance']},{weight},{sg},{item['Strength']},{flam}\n"
            f.write(line)
    print(f'\n CSV 파일로 저장 완료: {report_file}')        
except Exception as e:
    print(f'[오류] 파일 저장 중 문제 발생: {e}')

import pickle  
binary_file = 'C:/Users/SangAh/Desktop/python/Mars_Base_Inventory_List.bin'

try:
    with open(binary_file, 'wb') as bf:
        pickle.dump(inventory, bf)
    print(f'\n이진 파일로 저장 완료: {binary_file}')
except Exception as e:
    print(f'[오류] 이진 파일 저장 중 문제 발생: {e}')

try:
    with open(binary_file, 'rb') as bf:
        loaded_inventory = pickle.load(bf)
    print("\n=== 이진 파일에서 불러온 인화성 정렬 목록 ===")
    for item in loaded_inventory:
        print(item)
except Exception as e:
    print(f'[오류] 이진 파일 읽기 중 문제 발생: {e}')