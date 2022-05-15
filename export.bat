@REM Observação: Ao gerar os arquivos EXE por este arquivo bat, o antivirus detecta os EXE como vírus. O que não ocorre digitando os comandos abaixo no console.

del .\dist\*.*
rd .\dist\

pyinstaller -F -w .\pp.py --console -n "pp"
del .\build\pp\*.*
rd .\build\pp\
rd .\build\

pyinstaller -F -w .\pixelPoint.py --icon=icon.ico -n "pixelPoint"
del .\build\pixelPoint\*.*
rd .\build\pixelPoint\
rd .\build\

del *.spec
