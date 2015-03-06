from PyQt4 import uic

with open('livescope_ui.py','w') as f:
    uic.compileUi('livescope_ui.ui',f)
