from setuptools import setup, find_packages

setup(
    name='mirorr',
    description='Python tools for Mirorr',
    author='CSIRO AEHRC',
    version='0.0.1',
    license='CSIRO-OSSL',
    packages=find_packages(),
    install_requires=['nipype'],
)
