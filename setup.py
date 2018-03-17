"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='aide_document',
    version='0.1.4',
    description='Provides templating engine for use within the AguaClara AIDE.',
    url='https://github.com/AguaClara/aide_document',
    author='Cornell University AguaClara',
    author_email='aguaclara@cornell.edu',
    license = 'MIT',
    packages=find_packages(),
    install_requires=['jinja2','aide_document'],
    include_package_data=True,
    test_suite="tests",
    zip_safe=False
)