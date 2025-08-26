import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

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
        self.display.setStyleSheet("""
            font-size: 48px;
            padding-right: 10px;
            padding-top: 50px;
            background: #000000;
            color: white;
            border: none;
        """)

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
                        border-top-left-radius: 30px;
                        border-bottom-left-radius: 30px;
                        border-top-right-radius: 30px;
                        border-bottom-right-radius: 30px;
                    """)
                    self.buttons[button_text] = button
                    col += 2
                    continue  # 다음 반복으로 넘어감

                # 나머지 버튼
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

        for key, button in self.buttons.items():
            if key in {'0','1','2','3','4','5','6','7','8','9'}:
                button.clicked.connect(lambda checked, k=key: self.input_value(k))
   

    def input_value(self, value):
        self.display.setText(self.display.text() + value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())