from PyQt4 import uic

with open('my_ui.py','w') as f:
    uic.compileUi('my_ui.ui',f)
