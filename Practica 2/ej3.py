import string

jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""

letter  = input("Ingrese una letra: ")

if letter.isalpha():
    print([char for char in jupyter_info.split() if char.lower().startswith(letter)])
else:
    print("Te dije que tenias que poner una letra capo")


letter  = input("Ingrese una letra: ")

if letter in string.ascii_letters:
    print([char for char in jupyter_info.split() if char.lower().startswith(letter)])
else:
    print("Te dije que tenias que poner una letra capo")