import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['LEIA-ME.txt']

# Saida de arquivos
configuracao = Executable(
    script='app.py', # definir arquivo principal da aplicação
    icon='icone.ico'
)
# Configurar o executável
setup(
    name='Automatizador do Instagram',
    version='1.0',
    description='Este programa automatiza as curtidas do Instagram',
    author='Alexsandro Passos',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)