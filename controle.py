from PyQt5 import uic,QtWidgets
import mysql.connector

def funcao_principal():
    linha1 = formulario.lineEdit_1.text()
    linha2 = formulario.lineEdit_2.text()
    linha3= formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked():
        print("Categoria informática foi selecionada")
    elif formulario.radioButton_2.isChecked():
        print("Categoria alimentos foi selecionada")
    else:
        
        print("Categoria eletronicos foi selecionada")

    print("Codigo:", linha1)
    print("Descricao:", linha2)
    print("Valor:",linha3)


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.botao_1.clicked.connect(funcao_principal)

formulario.show()
app.exec()