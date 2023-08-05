from PyQt5.QtWidgets import QApplication,QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

app = QApplication([])

win_main = QWidget()
win_main.setWindowTitle("Калькулятор")
win_main.resize(500,500)

main_layout = QVBoxLayout()
input_layout = QHBoxLayout()
first_layout = QHBoxLayout()
second_layout = QHBoxLayout()
third_layout = QHBoxLayout()
last_layout = QHBoxLayout()
result_layout=QHBoxLayout()

result1=QLabel("0")
result1.setStyleSheet("font-size: 60px;")


num1 = QPushButton('1')
num2 = QPushButton('2')
num3 = QPushButton('3')
num4 = QPushButton('4')
num5 = QPushButton('5')
num6 = QPushButton('6')
num7 = QPushButton('7')
num8 = QPushButton('8')
num9 = QPushButton('9')
num0 = QPushButton('0')
num0.setStyleSheet("background-color: red;")
num1.setStyleSheet("background-color: red;")
num2.setStyleSheet("background-color: red;")
num3.setStyleSheet("background-color: red;")
num4.setStyleSheet("background-color: red;")
num5.setStyleSheet("background-color: red;")
num6.setStyleSheet("background-color: red;")
num7.setStyleSheet("background-color: red;")
num8.setStyleSheet("background-color: red;")
num9.setStyleSheet("background-color: red;")
add_btn = QPushButton('+')
sub_btn = QPushButton('-')
mul_btn = QPushButton('*')
div_btn = QPushButton('/')
equals_btn = QPushButton('=')
clear_btn = QPushButton('C')
backspace_btn = QPushButton('⌫')
add_btn.setStyleSheet("background-color: lime;")
sub_btn.setStyleSheet("background-color: lime;")
mul_btn.setStyleSheet("background-color: lime;")
div_btn.setStyleSheet("background-color: lime;")
equals_btn.setStyleSheet("background-color: lime;")
clear_btn.setStyleSheet("background-color: lime;")
backspace_btn.setStyleSheet("background-color: lime;")

input_numbers = QLineEdit('')
input_numbers.setReadOnly(True)  # Make the input field read-only

input_layout.addWidget(input_numbers)
result_layout.addWidget(result1)
first_layout.addWidget(num1)
first_layout.addWidget(num2)
first_layout.addWidget(num3)
second_layout.addWidget(num4)
second_layout.addWidget(num5)
second_layout.addWidget(num6)
third_layout.addWidget(num7)
third_layout.addWidget(num8)
third_layout.addWidget(num9)
last_layout.addWidget(num0)
last_layout.addWidget(add_btn)
last_layout.addWidget(sub_btn)
last_layout.addWidget(mul_btn)
last_layout.addWidget(div_btn)
last_layout.addWidget(equals_btn)
last_layout.addWidget(clear_btn)
last_layout.addWidget(backspace_btn)

main_layout.addLayout(result_layout)
main_layout.addLayout(input_layout)
main_layout.addLayout(first_layout)
main_layout.addLayout(second_layout)
main_layout.addLayout(third_layout)
main_layout.addLayout(last_layout)

win_main.setLayout(main_layout)
win_main.show()

current_operation = None
current_result = None

def handle_button_click():
    global current_operation, current_result
    button = app.sender()
    text = button.text()
    if text.isdigit():
        input_numbers.setText(input_numbers.text() + text)
    elif text in ['+', '-', '*', '/']:
        if input_numbers.text():
            current_operation = text
            current_result = int(input_numbers.text())
            input_numbers.setText('')
    elif text == "=":
        if current_operation and input_numbers.text():
            second_number = int(input_numbers.text())
            if current_operation == "+":
                result = current_result + second_number
                result1.setText(str(result))
            elif current_operation == "-":
                result = current_result - second_number
                result1.setText(str(result))
            elif current_operation == "*":
                result = current_result * second_number
                result1.setText(str(result))
            elif current_operation == "/":
                if second_number != 0:
                    result = current_result / second_number
                    result1.setText(str(result))
                else:
                    result = "Error: Division by zero"
                    result1.setText(str(result))
                
            else:
                result = 0
            input_numbers.setText(str(result))
            current_operation = None
            current_result = result  # Save the current result for possible further calculations
            result1.setText(str(current_result))
def handle_clear():
    global current_operation, current_result
    current_operation = None
    current_result = None
    input_numbers.setText('')
    
def handle_backspace():
    text = input_numbers.text()
    input_numbers.setText(text[:-1])
    result1.setText("0")


equals_btn.clicked.connect(handle_button_click)

num1.clicked.connect(handle_button_click)
num2.clicked.connect(handle_button_click)
num3.clicked.connect(handle_button_click)
num4.clicked.connect(handle_button_click)
num5.clicked.connect(handle_button_click)
num6.clicked.connect(handle_button_click)
num7.clicked.connect(handle_button_click)
num8.clicked.connect(handle_button_click)
num9.clicked.connect(handle_button_click)
num0.clicked.connect(handle_button_click)

add_btn.clicked.connect(handle_button_click)
sub_btn.clicked.connect(handle_button_click)
mul_btn.clicked.connect(handle_button_click)
div_btn.clicked.connect(handle_button_click)

clear_btn.clicked.connect(handle_clear)
backspace_btn.clicked.connect(handle_backspace)

app.exec_()
