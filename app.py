import sys
from dataclasses import replace
import random

from PyQt5.QtWidgets import QApplication, QMainWindow

import design

class GeraJogo(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


        self.btnGeraMega.clicked.connect(self.sorteio_mega)
        self.btnGeraFacil.clicked.connect(self.sorteio_facil)

    def sorteio_mega(self):
        self.volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
        random.shuffle(self.volante)
        numeros = str(self.volante[0:15])
        self.labelRetornoMega.setText(
            numeros.replace("'", "").replace(',', ' -').replace('[', '').replace(']', '')
        )

    def sorteio_facil(self):
        self.volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
        random.shuffle(self.volante)
        numeros = str(self.volante[0:20])
        self.labelRetornoFacil.setText(
            numeros.replace("'", "").replace(',', ' -').replace('[', '').replace(']', '')
        )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_jogo = GeraJogo()
    gera_jogo.show()
    qt.exec_()