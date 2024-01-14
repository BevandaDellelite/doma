from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QListWidget,QComboBox
from PyQt5.QtCore import Qt 


app = QApplication([])
window = QWidget()

window.resize(250,250)

sym = QLabel('syma:')
text = QLabel('Y valyty:')
text1 = QLabel('Rezultat:')
text2 = QPushButton("Konvertuvaty")
line = QLineEdit()
text3 = QLabel('')

combo = QComboBox()
list1 = ['eur','usd','logik']
combo.addItems(list1)

def add_task():
    t = line.text()
    c = combo.currentText()
    if c == 'eur':
        res = int(t) * 42
        text3.setText(str(res))
    elif c == 'usd':
        res = int(t) * 38
        text3.setText(str(res))
    elif c == 'logik':
        res = int(t) * 100
        text3.setText(str(res))
text2.clicked.connect(add_task)

v = QVBoxLayout()
v.addWidget(sym)
v.addWidget(line)
v.addWidget(text)
v.addWidget(text1)
v.addWidget(text2)
v.addWidget(combo)
v.addWidget(text3)


window.setLayout(v)
window.show()
app.exec()