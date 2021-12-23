from setuptools import setup, find_packages

from distutils.util import convert_path

long_description ="""
# Virtual Pi

The easiest way to use this package is to install using pip3 for python 3

```bash
$ sudo pip3 install VPi
```

To use the mock or virtual pi just type the following at the beginning of your script.

```python
try:
      from RPi.GPIO import GPIO
      import board
      import busio
      import spidev
except:
      from VPi.GPIO import GPIO
      import VPi.board as board
      import VPi.busio as busio
      import VPi.spidev as spidev
```

## Works with

- [python 3.6.8](https://www.python.org/downloads/release/3.6.8)

"""

pkg_ns = {}

ver_path = convert_path('VPi/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), pkg_ns)

setup(
      name='VPi',
      version=pkg_ns['__version__'],
      description='Virtual Pi Library for Raspberry Pi',
      url='https://github.com/codenio/',
      author='Aananth K',
      author_email='aananthraj1995@gmail.com',
      license='GPL-3.0',
      packages=find_packages(exclude=[]),
      install_requires=["numpy==1.19.5"],
      zip_safe=False,
      long_description_content_type="text/markdown",
      long_description=long_description,
)
