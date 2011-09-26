#!/bin/sh

pyuic4 main_form.ui > main_form_ui.py
perl -p -i -e 's/PyQt4/PySide/g' main_form_ui.py
pyside-lupdate gui.pro
