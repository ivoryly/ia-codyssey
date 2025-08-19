import numpy as np

file1 = r'C:\Users\SangAh\Desktop\python\mars_base_main_parts-001.csv'
file2 = r'C:\Users\SangAh\Desktop\python\mars_base_main_parts-002.csv'
file3 = r'C:\Users\SangAh\Desktop\python\mars_base_main_parts-003.csv'
arr1 = np.genfromtxt(file1, delimiter=',', names=True, dtype=None, encoding='utf-8-sig')
arr2 = np.genfromtxt(file2, delimiter=',', names=True, dtype=None, encoding='utf-8-sig')
arr3 = np.genfromtxt(file3, delimiter=',', names=True, dtype=None, encoding='utf-8-sig')

print(arr1.dtype.names)   #('\ufeffparts', 'strength') 
print(arr2.dtype.names)
print(arr3.dtype.names)

parts = np.column_stack((arr1['parts'], arr1['strength'], arr2['strength'], arr3['strength']))
print(parts)

mean_strengths = np.round(np.mean(parts[:, 1:].astype(float), axis=1), 2)

parts_avg = np.column_stack((parts[:, 0:], mean_strengths))
print('\n======== 각 항목 평균값 ========')
print(parts_avg)


filtered_parts = parts_avg[mean_strengths < 50]

output_file = r'C:\Users\SangAh\Desktop\python\parts_to_work_on.csv'
header = 'parts, strength_1, strength_2, strength_3, average'

try:
    np.savetxt(output_file, filtered_parts, delimiter=',', fmt='%s', header=header, comments='')
    print('파일 저장 완료:', output_file)
except Exception as e:
    print('파일 저장 중 오류 발생:', e)    


parts2 = np.genfromtxt(output_file, delimiter=',', dtype=str, skip_header=1)
print('\n======== parts2 (필터링된 데이터) ========')
print(parts2)


parts3 = parts2.T
print('\n======== parts3 (전치 행렬) ========')
print(parts3)