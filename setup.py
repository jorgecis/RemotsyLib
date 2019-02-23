# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='remotsylib',
    version='0.0.1',
    description='A Remotsy lib for use the Restfull API',
    long_description=long_description,
    url='https://github.com/jorgecis/remotsylib',
    author='Jorge Cisneros',
    author_email='jorge@remotsy.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Remotsy infrared remote control smarthome',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    #install_requires=['peppercorn'],  # Optional
    #extras_require={  # Optional
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},
)
