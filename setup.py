# - Standard installation script
# - Installs your package using Python distribution utils (distutils)
from distutils.core import setup

setup(
    name='ikram.learn',
    version='0.1dev',
    packages=['learn',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
