# -*- coding: utf-8 -*-
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='totalvoice-python',
    version='0.0.6',
    url='https://github.com/totalvoice/totalvoice-python',
    license='MIT License',
    author='Carlos Henrique dos Santos',
    author_email='carlos@totalvoice.com.br',
    keywords='totalvoice biblioteca python',
    description=u'Biblioteca para utilização da API da Totalvoice em Python',
    packages=find_packages(),
    )