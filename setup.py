from setuptools import setup, find_packages
from os import path
from codecs import open as openf

here = path.abspath(path.dirname(__file__))

with openf(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='remotsylib',
    version='0.0.2',
    description='A Remotsy python lib for use the Restfull API',
    long_description=long_description,
    url='https://github.com/jorgecis/remotsylib',
    author='Jorge Cisneros',
    author_email='jorge@remotsy.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='Remotsy infrared remote control smarthome',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
