from setuptools import setup

setup(
    name='handcontrol',
    version='1.0.0',
    author='3D-Bionics',
    packages=['handcontrol'],
    license='LICENSE',
    description='Software to control the 3D-Bionics Hand',
    long_description=open('README.md').read(),
    install_requires=[
        "npyscreen",
        "pyserial"
    ],
)