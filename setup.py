from setuptools import setup, find_packages

setup(
    name='qncmbe',
    version='0.2',
    description='Python tools for the QNC-MBE lab at the University of Waterloo',
    url='https://github.com/cdeimert/multipass',
    author='Chris Deimert',
    author_email='cdeimert@uwaterloo.ca',
    license='MIT',
    packages=find_packages(exclude=['tests','tests.*','examples','examples.*']),
    install_requires=[
        'cycler',
        'matplotlib',
        'numpy',
        'openpyxl',
        'pywin32',
        'PyQt5',
        'scipy'
    ],
    include_package_data = True,
    zip_safe = False
)