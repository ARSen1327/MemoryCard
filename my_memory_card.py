#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup, QMessageBox )
from random import shuffle

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q_list = []
q_list.append(Question('Какого цвета нет на флаге РФ', 'Зелёный',
        'Красный', 'Синий', 'Белый'))
q_list.append(Question('Национальная хижина якутов', 'Ураса',
        'Юрта', 'Иглу', 'Хата'))
q_list.append(Question('При каком правителе Россия стала империей', 'Пётр I',
        'Екатерина II', 'Александр I', 'Алексей Михайлович'))
#создание окна приложения
app = QApplication([]) 
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(420, 240) # размер окна

text = QLabel('Вопрос') # вопрос
btext = 'Ответить'
button = QPushButton(btext) # главная кнопка

# форма вопросов
radiogroup = QGroupBox('Ответы:')
rbt1 = QRadioButton('Ответ 1')
rbt2 = QRadioButton('Ответ 2')
rbt3 = QRadioButton('Ответ 3')
rbt4 = QRadioButton('Ответ 4')
rlh = QHBoxLayout()
rlv1 = QVBoxLayout()
rlv2 = QVBoxLayout()
rlv1.addWidget(rbt1, alignment = Qt.AlignCenter)
rlv1.addWidget(rbt2, alignment = Qt.AlignCenter)
rlv2.addWidget(rbt3, alignment = Qt.AlignCenter)
rlv2.addWidget(rbt4, alignment = Qt.AlignCenter)
rlh.addLayout(rlv1)
rlh.addLayout(rlv2)
radiogroup.setLayout(rlh)
rg = QButtonGroup()
rg.addButton(rbt1)
rg.addButton(rbt2)
rg.addButton(rbt3)
rg.addButton(rbt4)

# форма ответа
ansgroup = QGroupBox('Правильно/неправильно')
answer = QLabel('Правильно')
right = QLabel('Правильный ответ')
alv = QVBoxLayout()
alv.addWidget(answer, alignment = Qt.AlignVCenter)
alv.addWidget(right, alignment = Qt.AlignVCenter)
ansgroup.setLayout(alv)

# направляющие окна
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h1.addWidget(text, alignment = Qt.AlignCenter)
h2.addWidget(radiogroup, alignment = Qt.AlignCenter)
h2.addWidget(radiogroup, alignment = Qt.AlignCenter)
h3.addWidget(button, stretch = 2)
v_main = QVBoxLayout()
v_main.addLayout(h1)
v_main.addLayout(h2)
v_main.addLayout(h3)
main_win.setLayout(v_main)

def show_result():
    radiogroup.hide()
    ansgroup.show()
    btext = ("Следующий вопрос")
    button.setText(btext)
def show_question():
    rg.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    rg.setExclusive(True)
    radiogroup.show()
    ansgroup.hide()
    btext = 'Ответить'
    button.setText(btext)

answers = [rbt1, rbt2, rbt3, rbt4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    right.setText(q.right_ans)
    show_question()

def show_correct(res):
    answer.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Наверное')

def next_q():
    main_win.cur_q += 1
    main_win.total += 1
    if main_win.cur_q >= len(q_list):
        result = QMessageBox()
        rating = round(main_win.score / main_win.total * 100, 2)
        if rating >= 50:
            result.setText('Молодец!\nТы прошел тест!\n'+str(rating)+'%')
        else:
            result.setText('Молодец!\nТы прошел тест!\n'+str(rating)+'%')
        result.exec_()
        main_win.close()
    else:
        q = q_list[main_win.cur_q]
        ask(q)

def click_ok():
    if button.text()== 'Ответить':
        check_answer()
    else:
        next_q()

#запус программы
main_win.cur_q = -1
main_win.total = -1
main_win.score = 0
next_q() 
button.clicked.connect(click_ok)

radiogroup.show()
ansgroup.hide()

main_win.show()
app.exec_()
