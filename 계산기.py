import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Style Calculator")
        self.setFixedSize(300, 500)
        self.setStyleSheet("background-color: black;")

        # 디스플레이
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(90)
        self.display.setAlignment(Qt.AlignRight)
        # 스타일시트에서 font-size 속성을 제거하여 코드에서 폰트 크기를 제어할 수 있도록 합니다.
        self.display.setStyleSheet("""
            padding-right: 10px;
            padding-top: 50px;
            background: #000000;
            color: white;
            border: none;
        """)
        # 초기 폰트 크기를 코드로 설정합니다.
        font = self.display.font()
        font.setPointSize(30)
        self.display.setFont(font)


        # 버튼 레이아웃
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = [
            ['AC', '+/-', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for row, button_row in enumerate(buttons):
            col = 0
            for button_text in button_row:
                if button_text == '0':
                    button = QPushButton(button_text)
                    button.setFixedSize(130, 60) 
                    buttons_layout.addWidget(button, row+1, col, 1, 2)
                    button.setStyleSheet("""
                        background-color: #333333;
                        color: white;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 30px;
                    """)
                    self.buttons[button_text] = button
                    col += 2
                    continue

                button = QPushButton(button_text)
                button.setFixedSize(60, 60)
                buttons_layout.addWidget(button, row+1, col)
                self.buttons[button_text] = button
                col += 1

                # 버튼 스타일링
                if button_text in {'÷', '×', '-', '+', '='}:
                    button.setStyleSheet("""
                        background-color: #FF9500;
                        color: white;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 30px;
                    """)
                elif button_text in {'AC', '+/-', '%'}:
                    button.setStyleSheet("""
                        background-color: #A5A5A5;
                        color: black;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 30px;
                    """)
                else:
                    button.setStyleSheet("""
                        background-color: #333333;
                        color: white;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 30px;
                    """)

        # 전체 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        # 버튼 이벤트 연결
        for key, button in self.buttons.items():
            if key not in {'=', 'AC', '+/-', '%'}:
                button.clicked.connect(lambda checked, k=key: self.input_value(k))
        self.buttons['AC'].clicked.connect(self.clear)
        self.buttons['='].clicked.connect(self.calculate)
        self.buttons['+/-'].clicked.connect(self.plus_minus)
        self.buttons['%'].clicked.connect(self.percent)

        self.current_expression = ""

    def input_value(self, value):
        # 계산용으로 변환
        calc_value = value
        if value == '×':
            calc_value = '*'
        elif value == '÷':
            calc_value = '/'
        
        if value == '.':
            # 현재 입력된 마지막 숫자 부분 확인
            # 연산자를 기준으로 분리하여 마지막 부분을 확인합니다.
            parts = self.current_expression.replace('*', ' ').replace('/', ' ').replace('+', ' ').replace('-', ' ').split()
            if parts and '.' in parts[-1]:
                return

        # 내부 수식 저장 (계산용)
        self.current_expression += calc_value

        # 화면 표시용 텍스트는 내부 수식을 기반으로 생성하여 일관성을 유지합니다.
        display_text = self.current_expression.replace('*', '×').replace('/', '÷')
        self.display_result(display_text)


    def clear(self):
        self.current_expression = ""
        self.display_result("")

    def calculate(self):
        try:
            # 마지막이 연산자로 끝나면 계산하지 않음
            if self.current_expression and self.current_expression[-1] in "*/+-":
                return

            result = eval(self.current_expression)

            if isinstance(result, float):
                # 소수점 이하 불필요한 0 제거 및 반올림
                result = round(result, 6)
                if result == int(result):
                    result = int(result)

            self.display_result(result)
            self.current_expression = str(result)
        
        except ZeroDivisionError:
            self.display_result("오류")
            self.current_expression = ""
        except Exception: # 더 넓은 범위의 에러를 처리
            self.display_result("오류")
            self.current_expression = ""

    def plus_minus(self):
        if self.current_expression:
            if self.current_expression.startswith('-'):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = '-' + self.current_expression
            self.display_result(self.current_expression)

    def percent(self):
        try:
            if self.current_expression:
                result = eval(self.current_expression) / 100
                if isinstance(result, float):
                    result = round(result, 8) # 백분율은 더 정밀하게
                self.current_expression = str(result)
                self.display_result(self.current_expression)
        except Exception:
            self.display_result("오류")
            self.current_expression = ""


    def display_result(self, result):
        """결과를 디스플레이에 표시하고 텍스트 길이에 따라 폰트 크기를 조절합니다."""
        result_str = str(result)
        self.display.setText(result_str)

        # 최대/최소 폰트 크기
        max_font_size = 30
        min_font_size = 10

        font = self.display.font()
        font_size = max_font_size

        # QLineEdit의 실제 너비를 기준으로 폰트 크기를 계산합니다.
        max_width = self.display.width() - 20  # 양쪽 여백 고려

        # 폰트 크기를 설정하고, 해당 크기일 때의 텍스트 너비를 측정합니다.
        while font_size > min_font_size:
            font.setPointSize(font_size)
            fm = QFontMetrics(font)
            # 텍스트 너비가 디스플레이 너비보다 작으면 루프를 종료합니다.
            if fm.horizontalAdvance(result_str) < max_width:
                break
            font_size -= 1
        
        font.setPointSize(font_size)
        self.display.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())