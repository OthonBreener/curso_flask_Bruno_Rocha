# informações necessárias para o python tornar a aplicação como um instalavel do pip

'''
setup.py é um arquivo python, que normalmente informa que o módulo / pacote que você está
prestes a instalar foi empacotado e distribuído com o Distutils, que é o padrão para 
a distribuição de módulos Python.
Isso permite que você instale facilmente pacotes Python. Muitas vezes, basta escrever:
    pip install -e .
'''

from setuptools import setup, find_packages

def read(filename):
    return [ req.strip() for req in open(filename).readlines() ]

setup(
    name = 'apilanches',
    version = '0.1.0', #(m.m.p) - major = mudanças grandes, minor = mudanças diarias, patch = correção de bugs
    description = 'Lista de lanches de Ibiá-MG',
    packages = find_packages(),
    include_package_data = True,
    install_requires = read("requirementes.txt"),
    extras_require = {
        "dev": read("requirements-dev.txt")
    }
)