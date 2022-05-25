from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel

from PyQt5.QtGui import QStandardItem, QStandardItemModel

Boygroups = ('BTS', 'EXO', 'GOT7', 'Seventeen', 'TXT', 'Stray Kids', 'MCND','Boy Story', 'Enhypen', 'VIXX', 'BigBang', 'iKON', '4MIX', 'The Boyz')
modelo = QStandardItemModel(len(Boygroups),1)
modelo.setHorizontalHeaderLabels(['Boygroups'])

for linha, Boygroups in enumerate(Boygroups):      # [(1, 'BTS'), (2, 'EXO') ]
    elemento = QStandardItem(Boygroups)
    modelo.setItem(linha, 0, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)    
filtro.setFilterKeyColumn(0)
#filtro.setFilterCaseSensivity(Qt.CaseInsensitive)

app=QtWidgets.QApplication([])
tela=uic.loadUi("layout.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size: 20px;color: rgb(203, 203, 234);")
tela.lineEdit.textChanged.connect(filtro.setFilterRegExp)

tela.show()
app.exec()