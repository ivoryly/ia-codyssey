print('Hello Mars')

filename = 'C:/Users/SangAh/Desktop/python/mission_computer_main.log'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print('\n=== 로그 파일 내용 ===')
        print(content)
except FileNotFoundError:
    print(f'[오류] 파일이 존재하지 않습니다: {filename}')
except PermissionError:
    print(f'[오류] 파일에 접근할 권한이 없습니다: {filename}')
except Exception as e:
    print(f'[오류] 알 수 없는 문제가 발생했습니다: {e}')


report_file = 'C:/Users/SangAh/Desktop/python/log_analysis.md'

try:
    with open(report_file, 'w', encoding='utf-8') as report:
        report.write("# 사고 로그 분석 보고서\n\n")
        report.write("## 사고 개요\n")
        report.write("2023년 8월 27일, 산소 탱크의 불안정한 상태로 시작된 일련의 이벤트로 인해 주요 시스템이 셧다운되는 사고가 발생했습니다.\n\n")

        report.write("## 사고 발생 시간 및 단계\n")
        report.write("- 11:35:00 : 산소 탱크 불안정 경고\n")
        report.write("- 11:40:00 : 산소 탱크 폭발\n")
        report.write("- 12:00:00 : 센터 및 미션 제어 시스템 전원 종료\n\n")

        log_entries = [("11:35:00", "산소 탱크 불안정 경고"),
            ("11:40:00", "산소 탱크 폭발"),
            ("12:00:00", "센터 및 미션 제어 시스템 전원 종료")]

        log_entries.sort(reverse=True, key=lambda x: x[0])

        report.write("## 사고 발생 시간 및 단계 (시간 역순)\n")
        for time, event in log_entries:
            report.write(f"- {time} : {event}\n")
        report.write("\n")

        report.write("## 원인 분석\n")
        report.write("산소 탱크의 이상 징후가 탐지된 후 적절한 대응이 이루어지지 않아, 약 5분 후 실제 폭발로 이어졌으며, 20분 후에는 전체 시스템이 종료되었습니다. 조기 경고 신호에 대한 신속한 대응 체계가 부족했던 것이 주요 원인으로 판단됩니다.\n\n")

        report.write("## 결론 및 권고 사항\n")
        report.write("- 산소 탱크 상태 모니터링 시스템 개선\n")
        report.write("- 조기 경고 발생 시 자동 대응 프로토콜 구축\n")
        report.write("- 전원 차단 방지를 위한 이중화 시스템 도입\n")


    print(f"\n[완료] 분석 보고서가 '{report_file}' 파일에 저장되었습니다.")
except Exception as e:
    print(f"[오류] 보고서 작성 중 문제가 발생했습니다: {e}")