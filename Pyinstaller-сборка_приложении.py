https://pypi.org/project/pyinstaller/

#сборка приложения с настройками по умолчанию
pyinstaller notepad.py

#сборка приложения в виде одного файла
pyinstaller -F notepad.py

# noconsole запрещает запускать консоль
pyinstaller -w notepad.py

# icon компилирования файла сос своей иконкой
pyinstaller -w -i "путь до иконки" notepad.py